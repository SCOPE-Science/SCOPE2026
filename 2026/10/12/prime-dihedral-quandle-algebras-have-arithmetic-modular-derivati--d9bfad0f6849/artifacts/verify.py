from math import gcd

def ord2(p):
    x=1
    for h in range(1,p):
        x=x*2%p
        if x==1:
            return h
    raise AssertionError

def S(p):
    return [t for t in range(p-1) if t%2 and pow(2,t+1,p)==1]

def pred_dim(p):
    h=ord2(p)
    return 2*(p-1)//((2*h)//gcd(2,h))

def basis_map(p,t,kind):
    C=[[0]*p for _ in range(p)]
    for i in range(p):
        for r in range(1,p):
            c=pow(r,t,p)
            if kind:
                c=c*i%p
            C[i][(i+r)%p]=(C[i][(i+r)%p]+c)%p
    return C

def verify_derivation(p,C):
    inv2=pow(2,-1,p)
    for i in range(p):
        for j in range(p):
            k=(2*j-i)%p
            for u in range(p):
                rhs=(C[i][(2*j-u)%p]+C[j][((u+i)*inv2)%p])%p
                assert C[k][u]==rhs

def full_rank(p):
    n=p*p
    rows=[]
    inv2=pow(2,-1,p)
    def idx(i,u): return i*p+u
    for i in range(p):
        for j in range(p):
            k=(2*j-i)%p
            for u in range(p):
                row={}
                for c,v in [(idx(k,u),1),(idx(i,(2*j-u)%p),-1),
                            (idx(j,((u+i)*inv2)%p),-1)]:
                    row[c]=(row.get(c,0)+v)%p
                    if not row[c]:
                        del row[c]
                rows.append(row)
    piv={}
    rank=0
    for row in rows:
        while row:
            c=min(row)
            if c not in piv:
                z=pow(row[c],-1,p)
                row={j:v*z%p for j,v in row.items()}
                piv[c]=row
                rank+=1
                break
            z=row[c]
            for j,v in piv[c].items():
                nv=(row.get(j,0)-z*v)%p
                if nv: row[j]=nv
                elif j in row: del row[j]
    return rank

for p in (3,5,7,11,13,17,19,23,31):
    ss=S(p)
    assert 2*len(ss)==pred_dim(p)
    for t in ss:
        verify_derivation(p,basis_map(p,t,0))
        verify_derivation(p,basis_map(p,t,1))
    print({"p":p,"ord2":ord2(p),"S":ss,"dimension":pred_dim(p)})

for p in (3,5,7,11):
    nullity=p*p-full_rank(p)
    assert nullity==pred_dim(p)
    print({"p":p,"full_system_nullity":nullity})

print("VERIFY_OK")
