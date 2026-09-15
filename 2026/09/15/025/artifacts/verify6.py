"""Search for a double-divisibility case where some Weyl module has >=3 factors (breaking N_r method).
Rule 15: [Delta(2^m):L(2^j)]=1 iff floor((m-j)/p)≼_p floor((n-2j+1)/p) and (p|m-j or p|n-m-j+1).
Scan p in {3,5}, n=k+j up to 30, j<=m<=6."""
def prec_p(a,b,p):
    def padic(n):
        d=[]
        if n==0: return [0]
        while n>0: d.append(n%p); n//=p
        return d
    if a<0 or b<0: return False
    da,db=padic(a),padic(b); L=max(len(da),len(db)); da+=[0]*(L-len(da)); db+=[0]*(L-len(db))
    return all(x==0 or x==y for x,y in zip(da,db))
def factors(n,m,p,mmax=None):
    out=[]
    for j in range(m+1):
        if m==j: out.append(j); continue
        af=(m-j)//p; bf=(n-2*j+1)//p
        if bf<0: continue
        if prec_p(af,bf,p) and ((m-j)%p==0 or (n-m-j+1)%p==0): out.append(j)
    return out
found=[]
for p in [3,5,7]:
    for n in range(6,31):
        for m in range(0,9):
            if 2*m>n: continue
            f=factors(n,m,p)
            if len(f)>=3:
                # check double-divisibility regime for some k>=j>2 with k+j=n, j>=m
                found.append((p,n,m,f))
for x in found[:20]:
    print(x)
print("total with >=3 factors:", len(found))
# Now check which of these sit in a double-divisibility (k,j):
print()
for (p,n,m,f) in found[:20]:
    js=[j for j in range(3,12) if j>=m and (n-j)>=j and sum(1 for s in range(n-2*j+2,n+1) if s%p==0)>=2]
    print(f"p={p},n={n},m={m},factors={f} relevant-j={js}")
