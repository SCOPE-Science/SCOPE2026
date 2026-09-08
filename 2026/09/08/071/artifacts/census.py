#!/usr/bin/env python3
"""Committed-slice Hasse-Weil census for small-height genus-2 curves over Fp, p<=37.
Slice S: odd primes <=37 x 12 fixed monic models (coeffs in {-2..2}).
Methods: Fp gcd smoothness; N1 by Euler-criterion sum AND brute y-loop (cross-checked);
orbit tally; N2 by Fp^2 enumeration; Weil poly from N1,N2; Jac order P(1); Serre bound.
Stdlib only. Run: python3 census.py -> census_table.json, census_log.txt
"""
import json, math

PRIMES=[3,5,7,11,13,17,19,23,29,31,37]
# models: name -> coeffs low->high (monic quintic or sextic), coeffs in {-2..2} except leading 1
MODELS={
 "M01": [1,0,0,0,0,1],
 "M02": [1,1,0,0,0,1],
 "M03": [1,-1,2,-2,1,1],
 "M04": [-1,2,0,1,-1,1],
 "M05": [2,-2,-2,2,1,1],
 "M06": [0,1,-1,1,1,1],
 "M07": [1,0,2,-1,0,-1,1],
 "M08": [-1,1,0,2,1,2,1],
 "M09": [2,1,-2,0,-1,1,1],
 "M10": [-2,0,1,1,2,-1,1],
 "M11": [1,-1,-2,2,-2,-1,1],   # p=19 Serre-maximal witness
 "M12": [1,-2,1,1,1,-2,1],     # p=29 Serre-maximal witness
}
def modpoly(poly,p): return [c%p for c in poly]
def strip(poly,p):
    poly=[x%p for x in poly]
    while len(poly)>1 and poly[-1]==0: poly.pop()
    return poly
def pdeg(poly): return len(poly)-1
def pgcd(a,b,p):
    a=strip(list(a),p); b=strip(list(b),p)
    while not (len(b)==1 and b[0]==0):
        while len(a)>1 and a[-1]==0: a.pop()
        while len(b)>1 and b[-1]==0: b.pop()
        if len(b)==1 and b[0]==0: break
        da=len(a)-1; db=len(b)-1
        if da<db: a,b=b,a; da,db=db,da
        inv=pow(b[-1],-1,p)
        c=(a[-1]*inv)%p; s=da-db
        sub=[0]*s+[(c*x)%p for x in b]
        while len(sub)<len(a): sub.append(0)
        a=[(x-y)%p for x,y in zip(a,sub)]
        a=strip(a,p); b=strip(b,p)
        a,b=b,a
    return strip(a,p)
def is_smooth(coeffs,p):
    f=modpoly(coeffs,p)
    fp=[(i*f[i])%p for i in range(1,len(f))]
    fp=strip(fp,p)
    if len(fp)==1 and fp[0]==0: return False
    return pdeg(pgcd(f,fp,p))==0
def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
def evalpoly(coeffs,x,p):
    v=0
    for c in reversed(coeffs): v=(v*x+c)%p
    return v
def count_N1(coeffs,p,deg):
    # method A: Euler sum
    s=sum(legendre(evalpoly(coeffs,x,p),p) for x in range(p))
    ninf=1 if deg==5 else 2
    N1_euler=p+s+ninf
    # method B: brute y loop
    fq={ (y*y)%p for y in range(p)}
    na=sum(1 for x in range(p) if evalpoly(coeffs,x,p) in fq for y in range(p) if (y*y-evalpoly(coeffs,x,p))%p==0)
    # cheaper: count directly
    N1_brute=na+ninf
    assert N1_euler==N1_brute,(p,coeffs,N1_euler,N1_brute)
    # orbit tally
    n0=n1=n2=0
    for x in range(p):
        v=evalpoly(coeffs,x,p)
        L=legendre(v,p)
        if L==-1: n0+=1
        elif L==0: n1+=1
        else: n2+=1
    assert n0+n1+n2==p
    assert n1+2*n2+ninf==N1_euler
    return N1_euler,n0,n1,n2,ninf
def find_irred_quad(p):
    for a in range(p):
        for b in range(p):
            if all(( (x*x+a*x+b)%p)!=0 for x in range(p)): return (a,b)
    raise AssertionError
def count_N2(coeffs,p,deg):
    # enumerate Fp^2 = Fp[t]/(t^2+a t+b)
    a,b=find_irred_quad(p)
    q2=p*p
    def add(u,v): return ((u[0]+v[0])%p,(u[1]+v[1])%p)
    def mul(u,v):
        # (u0+u1 t)(v0+v1 t), t^2=-a t-b
        r0=(u[0]*v[0]-u[1]*v[1]*b)%p
        r1=(u[0]*v[1]+u[1]*v[0]-u[1]*v[1]*a)%p
        return (r0,r1)
    def pw(u,e):
        r=(1,0); base=u
        while e:
            if e&1: r=mul(r,base)
            base=mul(base,base); e>>=1
        return r
    ninf=1 if deg==5 else 2
    # precompute squares? naive: for each x in Fp^2, count y solutions: 1 if v==0 else (1+chi) where chi=v^((q2-1)/2)
    n=0
    for x0 in range(p):
        for x1 in range(p):
            # eval f at x=(x0,x1)
            vx=(0,0); xp=(1,0); x=(x0,x1)
            for c in coeffs:
                vx=add(vx,mul(((c%p),0),xp)); xp=mul(xp,x)
            if vx==(0,0): n+=1
            else:
                e=pw(vx,(q2-1)//2)
                if e==(1,0): n+=2
                elif e==(p-1,0): n+=0
                else: raise AssertionError(("non-quadratic",p,vx,e))
    return n+ninf
def serre(q,g=2): return q+1+g*math.floor(2*math.sqrt(q))
def weil_from_counts(N1,N2,q):
    a1=N1-q-1
    S1=q+1-N1
    S2=q*q+1-N2
    num=S1*S1-S2
    assert num%2==0,(N1,N2,num)
    a2=num//2
    return a1,a2
rows=[]; log=[]
for pname,coeffs in MODELS.items():
    deg=len(coeffs)-1
    for p in PRIMES:
        sm=is_smooth(coeffs,p)
        if not sm:
            rows.append({"model":pname,"coeffs":coeffs,"deg":deg,"p":p,"smooth":False})
            log.append(f"{pname} p={p}: singular (repeated root mod p), excluded from genus-2 table")
            continue
        N1,n0,n1,n2,ninf=count_N1(coeffs,p,deg)
        N2=count_N2(coeffs,p,deg)
        a1,a2=weil_from_counts(N1,N2,p)
        P1=1+a1+a2+p*a1+p*p
        sb=serre(p); maximal=(N1==sb)
        assert abs(-a1)<=4*math.sqrt(p)+1e-9
        rows.append({"model":pname,"coeffs":coeffs,"deg":deg,"p":p,"smooth":True,
          "N1":N1,"N2":N2,"orbit":[n0,n1,n2],"ninf":ninf,
          "a1":a1,"a2":a2,"P":[1,a1,a2,p*a1,p*p],"Jac":P1,"serre":sb,"maximal":maximal})
        log.append(f"{pname} p={p}: N1={N1} N2={N2} orbit0/1/2={n0}/{n1}/{n2} inf={ninf} P=1+{a1}T+{a2}T^2+{p*a1}T^3+{p*p}T^4 Jac={P1} Serre={sb} maximal={maximal}")
open("census_table.json","w").write(json.dumps({"primes":PRIMES,"serre_g":2,"rows":rows},indent=1))
open("census_log.txt","w").write("\n".join(log)+"\n")
# point lists for witnesses
def point_list(coeffs,p,deg):
    pts=[]
    for x in range(p):
        v=evalpoly(coeffs,x,p)
        for y in range(p):
            if (y*y-v)%p==0: pts.append([x,y])
    ninf=1 if deg==5 else 2
    pts_inf=["inf"]*ninf
    return pts,pts_inf
for pname,p in [("M11",19),("M12",29)]:
    coeffs=MODELS[pname]; deg=len(coeffs)-1
    pts,pi=point_list(coeffs,p,deg)
    open(f"points_{pname}_p{p}.json","w").write(json.dumps({"model":pname,"coeffs":coeffs,"p":p,"affine":pts,"infinity":pi,"N":len(pts)+len(pi)},indent=1))
print(f"done rows={len(rows)} smooth={sum(1 for r in rows if r['smooth'])} maximals={[ (r['model'],r['p'],r['N1']) for r in rows if r.get('maximal')]}")
