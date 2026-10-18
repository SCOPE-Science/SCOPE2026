from itertools import product

# Products indexed in a chosen basis [1,u,v,...]
def mult_table(kind,q=2):
    if kind=='non':
        M={(1,1):3,(1,2):4,(2,2):5,(1,3):6}; gens=(1,2); rad_dim=6; cutoff=3
    else:
        M={(1,1):4,(1,2):5,(2,2):6,(1,4):6}; gens=(1,2,3);rad_dim=6;cutoff=4
    def mult(a,b):
        out=[0]*7
        for i,x in enumerate(a):
            if not x:continue
            for j,y in enumerate(b):
                if not y:continue
                k=(0 if i==0 else j if j==0 else M.get(tuple(sorted((i,j))),-1))
                if k>=0:out[k]=(out[k]+x*y)%q
        return tuple(out)
    return mult,gens,cutoff

def rankmod(vecs,q):
    rows=[list(x) for x in vecs]
    p=0
    for c in range(len(rows[0])):
        row=next((i for i in range(p,len(rows)) if rows[i][c]),None)
        if row is None:continue
        rows[p],rows[row]=rows[row],rows[p]
        inv=pow(rows[p][c],-1,q)
        rows[p]=[(v*inv)%q for v in rows[p]]
        for i in range(len(rows)):
            if i==p:continue
            t=rows[i][c]
            if t:rows[i]=[(v-t*w)%q for v,w in zip(rows[i],rows[p])]
        p+=1
        if p==len(rows):break
    return p

def check(kind,q):
    mult,gens,cutoff=mult_table(kind,q)
    z=(0,)*7
    m=[(0,)+t for t in product(range(q),repeat=6)]
    count=0
    for images in product(m,repeat=len(gens)):
        if rankmod([[im[g] for im in images] for g in gens],q)!=len(gens):continue
        u,v=images[:2]
        u2=mult(u,u);v2=mult(v,v);u3=mult(u2,u)
        if u3==z or mult(u2,v)!=z or mult(u,v2)!=z or mult(v2,v)!=z:continue
        if kind=='thin':
            w=images[2]
            if u3!=v2 or any(mult(w,x)!=z for x in images):continue
        count+=1
    expected=((q-1)**2)*q**(9 if kind=='non' else 11)
    assert count==expected,(kind,q,count,expected)
    print(kind,q,count,'expected',expected,'PASS')

if __name__=='__main__':
    for kind in ('non','thin'):
        check(kind,2)

# Independent truncated-power-series witnesses over three prime characteristics.
def trunc_mul(a,b,q):
    out=[0]*14
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:14-i]):
                if y:out[i+j]=(out[i+j]+x*y)%q
    return tuple(out)

def element(*terms):
    out=[0]*14
    for i,c in terms:out[i]=c
    return tuple(out)

def check_trunc(q,thin,extra=False):
    one=element((0,1)); z=(0,)*14
    if thin:
        u=element((4,1));v=element((6,1))
    else:
        u=element((4,1),(5,1));v=element((6,1),(7,1))
    u2=trunc_mul(u,u,q);u3=trunc_mul(u2,u,q)
    v2=trunc_mul(v,v,q);uv=trunc_mul(u,v,q)
    assert trunc_mul(u2,v,q)==z and trunc_mul(u,v2,q)==z
    assert trunc_mul(u3,u,q)==z and trunc_mul(v2,v,q)==z
    if thin:
        assert u3==v2
        w=element((13,1)); assert all(trunc_mul(w,g,q)==z for g in (u,v,w))
        basis=[one,u,v,w,u2,uv,u3]
    else:
        assert tuple((a-b)%q for a,b in zip(u3,v2))==element((13,1))
        basis=[one,u,v,u2,uv,v2,u3]
    if extra:
        h=element((11,1));assert all(trunc_mul(h,g,q)==z for g in (u,v,h))
        basis.append(h)
    assert rankmod(basis,q)==len(basis),(q,thin,extra,'rank')
    for a in basis:
        for b in basis:
            prod=trunc_mul(a,b,q)
            assert rankmod(basis+[prod],q)==len(basis)
    return len(basis)

def check_squarezero(q):
    m,_,_=mult_table('thin',q)
    M={(1,1):4,(1,2):5,(1,4):6}  # v^2 becomes zero in gr.
    def mg(a,b):
        out=[0]*7
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b):
                    if y:
                        k=(0 if i==0 else j if j==0 else M.get(tuple(sorted((i,j))),-1))
                        if k>=0:out[k]=(out[k]+x*y)%q
        return tuple(out)
    old=set();graded=set()
    for t in product(range(q),repeat=6):
        a=(0,)+t
        if not any(m(a,a)):old.add(t[:3])
        if not any(mg(a,a)):graded.add(t[:3])
    assert old=={(0,0,c) for c in range(q)},old
    assert graded=={(0,b,c) for b in range(q) for c in range(q)},graded

if __name__=='__main__':
    for q in (2,3,5):
        for thin in (False,True):
            for extra in (False,True):
                dim=check_trunc(q,thin,extra)
                print('truncated',q,'thin',thin,'extra',extra,'dimension',dim)
    for q in (2,3):
        check_squarezero(q)
        print('square-zero lifting',q,'PASS')
    print('VERIFY_OK')
