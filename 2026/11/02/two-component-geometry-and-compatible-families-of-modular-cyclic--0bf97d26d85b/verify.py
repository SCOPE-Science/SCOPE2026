#!/usr/bin/env python3
"""Exact tests of weight-zero Rota--Baxter maps on k[t]/(t^4), characteristic two.

Field elements are encoded using a binary polynomial basis. The defining
operator identity is checked on all 16 ordered pairs of algebra basis vectors.
"""
from itertools import product
from collections import Counter


def finite_field(q):
    degree = {2: 1, 4: 2}[q]
    modulus = {2: 0b11, 4: 0b111}[q]
    def times(a,b):
        out=0
        while b:
            if b & 1: out ^= a
            b >>= 1
            a <<= 1
            if a & q: a ^= modulus
        return out
    mult=[[times(a,b) for b in range(q)] for a in range(q)]
    inverse=[0]*q
    for x in range(1,q):
        inverse[x]=next(y for y in range(1,q) if mult[x][y]==1)
    return degree,mult,inverse


def run(q, full):
    degree, mul, inv = finite_field(q)
    mask=q-1
    def unpack(x):
        return tuple((x>>(degree*i))&mask for i in range(4))
    def pack(v):
        return sum(x<<(degree*i) for i,x in enumerate(v))
    elements=q**4
    entries=[unpack(x) for x in range(elements)]
    basis=[pack(tuple(int(i==j) for i in range(4))) for j in range(4)]
    def algmul(u,v):
        a,b=entries[u],entries[v]
        out=[0]*4
        for i in range(4):
            for j in range(4-i):
                out[i+j]^=mul[a[i]][b[j]]
        return pack(out)
    table=[[algmul(x,y) for y in range(elements)] for x in range(elements)]
    def apply(images,x):
        c=entries[x]
        ans=[0]*4
        for i in range(4):
            if c[i]:
                image=entries[images[i]]
                for j in range(4):
                    ans[j]^=mul[c[i]][image[j]]
        return pack(ans)
    def equations(images):
        for i in range(4):
            for j in range(4):
                left=table[images[i]][images[j]]
                right=apply(images,table[images[i]][basis[j]] ^ table[basis[i]][images[j]])
                if left!=right:
                    return False
        return True
    def rank(images):
        m=[[entries[images[j]][i] for j in range(4)] for i in range(4)]
        row=0
        for col in range(4):
            piv=next((r for r in range(row,4) if m[r][col]),None)
            if piv is None:continue
            m[row],m[piv]=m[piv],m[row]
            scale=inv[m[row][col]]
            m[row]=[mul[scale][x] for x in m[row]]
            for r in range(4):
                if r!=row and m[r][col]:
                    c=m[r][col]
                    m[r]=[m[r][j]^mul[c][m[row][j]] for j in range(4)]
            row+=1
            if row==4:break
        return row
    accepted=Counter()
    accepted_higher=0
    accepted_images=[]
    all_count=0
    if full:
        iterator=product(range(elements),repeat=4)
    else:
        iterator=(tuple(pack((0,0,p[2*i],p[2*i+1])) for i in range(4)) for p in product(range(q),repeat=8))
    for images in iterator:
        all_count+=1
        valid=equations(images)
        if full:
            # This is a completely independent check of the full 4x4 matrix space.
            p=[entries[x] for x in images]
            predicted=all(x[0]==0 and x[1]==0 for x in p) and p[3]==(0,0,0,0) and p[2][2]==0 and mul[p[1][2]][p[2][3]]==0
        else:
            p=[entries[x] for x in images]
            predicted=p[3]==(0,0,0,0) and p[2][2]==0 and mul[p[1][2]][p[2][3]]==0
        assert valid==predicted, (q,images,predicted,valid)
        if not valid: continue
        accepted[rank(images)]+=1
        if q==2: accepted_images.append(tuple(images))
        if any(apply(images,images[i]) for i in range(4)):
            accepted_higher+=1
    ranks={0:1, 1:(q-1)*(2*q*q+2*q+1),2:(q-1)**2*(2*q*q+q)}
    assert accepted==Counter(ranks),(q,accepted,ranks)
    assert sum(accepted.values())==q**3*(2*q-1)
    assert accepted_higher==q*q*(q-1)**2
    if q==2:
        joint=Counter()
        for x in accepted_images:
            for y in accepted_images:
                if equations(tuple(u^v for u,v in zip(x,y))):
                    joint[(rank(x),rank(y))]+=1
        def polynomial_component():
            return [1,q**3+q**2-q-1,q*(q-1)**2*(q+1)]
        def polynomial_intersection():
            return [1,2*q*q-q-1,q*(q-1)**2]
        p0,p1=polynomial_component(),polynomial_intersection()
        predicted={(i,j):2*p0[i]*p0[j]-p1[i]*p1[j] for i in range(3) for j in range(3)}
        assert joint==Counter(predicted),(joint,predicted)
        print(f'q={q} commuting-compatible-pairs={sum(joint.values())} histogram={dict(sorted(joint.items()))} VERIFIED')
        triples=0
        for x in accepted_images:
            for y in accepted_images:
                if not equations(tuple(u^v for u,v in zip(x,y))): continue
                for z in accepted_images:
                    if (equations(tuple(x[i]^z[i] for i in range(4)))
                            and equations(tuple(y[i]^z[i] for i in range(4)))
                            and equations(tuple(x[i]^y[i]^z[i] for i in range(4)))):
                        triples+=1
        assert triples==2*q**12-q**9
        print(f'q={q} compatible-triples={triples} VERIFIED')
    print(f'q={q} full_matrix_space={full} tested={all_count} accepted={sum(accepted.values())} ranks={dict(sorted(accepted.items()))} index_three={accepted_higher} VERIFIED')


if __name__=='__main__':
    run(2,True)
    run(4,False)
    print('MODULAR_C4_ROTA_BAXTER_OK')
