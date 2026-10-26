"""Exact finite-field sanity check of the claimed maximal square-zero ideals at rank four."""
from itertools import combinations,product

def inv(x,q):
    return pow(x,-1,q)

def echelon(vectors,q):
    rows=[list(x) for x in vectors if any(x)]
    if not rows:return []
    n=len(rows[0]); p=0
    for j in range(n):
        i=next((i for i in range(p,len(rows)) if rows[i][j]%q),None)
        if i is None:continue
        rows[p],rows[i]=rows[i],rows[p]
        c=inv(rows[p][j]%q,q)
        rows[p]=[(v*c)%q for v in rows[p]]
        for i in range(len(rows)):
            if i==p:continue
            c=rows[i][j]%q
            rows[i]=[(a-c*b)%q for a,b in zip(rows[i],rows[p])]
        p+=1
        if p==len(rows):break
    return tuple(tuple(row) for row in rows[:p])

def basis(r):
    return [(i,) for i in range(r)]+list(combinations(range(r),2))+list(combinations(range(r),3))

def vector(bas,terms,q):
    out=[0]*len(bas)
    for s,c in terms.items():out[bas.index(s)]=c%q
    return tuple(out)

def algebra_product(a,b,bas,q):
    out=[0]*len(bas)
    for i,u in enumerate(bas):
      if not a[i]:continue
      for j,v in enumerate(bas):
       if not b[j] or len(u)+len(v)!=3 and len(u)+len(v)!=2:continue
       if len(u)==2 and len(v)==1:
        both=v+u; sign=-1
       elif len(u)==1 and len(v) in (1,2):
        both=u+v; sign=1
       else:continue
       if len(set(both))!=len(both):continue
       parity=sum(both[x]>both[y] for x in range(len(both)) for y in range(x+1,len(both)))%2
       k=bas.index(tuple(sorted(both)))
       out[k]=(out[k]+a[i]*b[j]*sign*(-1 if parity else 1))%q
    return tuple(out)

def check(r=4,q=3):
    bas=basis(r);d=len(bas)
    z=[vector(bas,{s:1},q) for s in bas if len(s)==3]
    ww=[vector(bas,{s:1},q) for s in bas if len(s)==2]
    lines=[]
    for x in product(range(q),repeat=r):
        if not any(x):continue
        x=tuple((v*inv(next(w for w in x if w),q))%q for v in x)
        if x not in lines:lines.append(x)
    observed=set()
    special=echelon(ww+z,q); observed.add(special)
    for ell in lines:
        a=vector(bas,{(i,):ell[i] for i in range(r)},q)
        ker=[]
        for j in range(r):
            e=vector(bas,{(j,):1},q)
            k=algebra_product(a,e,bas,q)
            if k not in ker and any(k):ker.append(k)
        ker=list(echelon(ker,q))
        comp=[]
        for w in ww:
            if len(echelon(ker+comp+[w],q))>len(ker)+len(comp):comp.append(w)
        assert len(ker)==r-1 and len(comp)==(r-1)*(r-2)//2
        for coeffs in product(range(q),repeat=len(comp)):
            a2=tuple((a[i]+sum(c*w[i] for c,w in zip(coeffs,comp)))%q for i in range(d))
            u=echelon(ker+z+[a2],q)
            assert len(u)==r+len(z)
            for x in u:
                for y in u:
                    assert not any(algebra_product(x,y,bas,q))
                for s in bas:
                    e=vector(bas,{s:1},q)
                    prod=algebra_product(e,x,bas,q)
                    assert len(echelon(list(u)+[prod],q))==len(u)
            observed.add(u)
    expectation=1+((q**r-1)//(q-1))*q**((r-1)*(r-2)//2)
    assert len(observed)==expectation
    print(f'rank={r} q={q} candidate_ideals={len(observed)} expected={expectation} VERIFIED')
if __name__=='__main__':check()
