"""Exact finite-field checks of the 4D model filiform derivation spectrum."""
from itertools import product
from collections import Counter

def add(a,b,q): return a^b if q in (2,4,8) else (a+b)%q

def mul(a,b,q):
    if q not in (4,8): return a*b%q
    poly={4:7,8:11}[q]; k={4:2,8:3}[q]; mask=q-1
    ans=0
    while b:
        if b&1: ans^=a
        b>>=1; a<<=1
        if a&q: a^=poly
    return ans&mask

def inv(a,q):
    assert a
    for b in range(1,q):
        if mul(a,b,q)==1:return b
    raise AssertionError((a,q))

def rank(mat,q):
    a=[row[:] for row in mat]; m=len(a); n=len(a[0]); i=0
    for j in range(n):
        p=next((k for k in range(i,m) if a[k][j]),None)
        if p is None: continue
        a[i],a[p]=a[p],a[i]; z=inv(a[i][j],q)
        a[i]=[mul(z,x,q) for x in a[i]]
        for k in range(i+1,m):
            c=a[k][j]
            if c:
                a[k]=[add(a[k][l],mul(c,a[i][l],q),q) for l in range(n)]
        i+=1
        if i==m:break
    return i

def matrix(params,q):
    a,a2,a3,a4,b,b3,b4=params
    return [[a,0,0,0],[a2,b,0,0],[a3,b3,add(a,b,q),0],
            [a4,b4,b3,add(add(a,a,q),b,q)]]

def distribution(q):
    ct=Counter()
    for p in product(range(q),repeat=7):
        ct[rank(matrix(p,q),q)]+=1
    return tuple(ct[i] for i in range(5))

def formula(q):
    t=[1,q**3+q**2-q-1,(q-1)*(2*q**3-q),0,0]
    if q%2:
        t[3]=(q-1)**2*q**3+4*(q-1)*q**5
        t[4]=(q-1)*(q-3)*q**5
    else:
        t[2]+=(q-1)*q**4
        t[3]=(q-1)**2*q**3+2*(q-1)*q**5+(q-1)**2*q**4
        t[4]=(q-1)*(q-2)*q**5
    assert sum(t)==q**7,(q,t)
    return tuple(t)

def minus(a,b,q):
    return add(a,b,q) if q in (2,4,8) else (a-b)%q

def bracket(x,y,q):
    z3=minus(mul(x[0],y[1],q),mul(x[1],y[0],q),q)
    z4=minus(mul(x[0],y[2],q),mul(x[2],y[0],q),q)
    return [0,0,z3,z4]

def linear_apply(m,v,q):
    out=[]
    for row in m:
        s=0
        for a,b in zip(row,v): s=add(s,mul(a,b,q),q)
        out.append(s)
    return out

def leibniz_residue(m,i,j,q):
    e=[[int(x==k) for x in range(4)] for k in range(4)]
    lhs=linear_apply(m,bracket(e[i],e[j],q),q)
    rhs1=bracket(linear_apply(m,e[i],q),e[j],q)
    rhs2=bracket(e[i],linear_apply(m,e[j],q),q)
    return [minus(minus(a,b,q),c,q) for a,b,c in zip(lhs,rhs1,rhs2)]

def leibniz_system_rank(q):
    eq=[]
    for i in range(4):
        for j in range(i+1,4):
            block=[[] for _ in range(4)]
            for k in range(16):
                m=[[0]*4 for _ in range(4)];m[k//4][k%4]=1
                res=leibniz_residue(m,i,j,q)
                for t in range(4):block[t].append(res[t])
            eq.extend(block)
    return rank(eq,q)

if __name__=='__main__':
    for q in (2,3,4,5):
        assert leibniz_system_rank(q)==9,('Leibniz dimension',q)
        got=distribution(q); want=formula(q)
        assert got==want,(q,got,want)
        trial=[(0,)*7,(1,)*7,(q-1,0,1,1,1,0,0)]
        for p in trial:
            m=matrix(p,q)
            for i in range(4):
                for j in range(i+1,4):
                    assert not any(leibniz_residue(m,i,j,q)),(q,p,i,j)
        print('field',q,'Leibniz constraint rank',9,'derivations',q**7,'spectrum',got)
    print('VERIFY_OK_FILIFORM_DERIVATIONS')
