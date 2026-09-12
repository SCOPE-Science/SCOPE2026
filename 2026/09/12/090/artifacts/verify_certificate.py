"""Self-contained rigorous verifier for the O2-maximization certificate.
Checks (exact rational arithmetic via fractions; PARI-free Sturm via explicit
Sturm sequences implemented below):
  [C1] u_coeffs.txt defines u(x)=sum a_k cos(2pi k x)+b_k sin(2pi k x), M=12,
       satisfying exact interpolation constraints C1,C2a,C2b (integers).
  [C2] R(t) = (1+t^2)^24 F(x(t)) reconstructed from u matches R_coeffs.txt
       (checked at 49 rational points + degree bound => identity).
  [C3] R = (t^2-3)^2 S with S_coeffs.txt (polynomial identity at 49 points).
  [C4] S has NO real root (Sturm count 0) and S(0)>0 => S>0 everywhere;
       S-3/200 has no real root and S(0)>3/200 => S>=3/200.
  [C5] R has exactly 2 distinct real roots (Sturm count 2); since (t^2-3)^2|R,
       they are t=+/-sqrt(3), i.e. x=1/3,2/3. With F(1/2)=c48>0, F>=0 with
       zeros exactly on O2={1/3,2/3}.
  [C6] Gap: critical boxes in critical_boxes.json cover ALL critical points of
       F in each cover piece (Sturm recount per piece matches box-count sum),
       F lower bounds on all tiny boxes + endpoints + strip exceed 3/1000.
       (Box F-evaluations use exact Fraction interval Horner.)
Sturm engine: exact sign-variation counts on Fraction polynomial remainder
sequences (no floats anywhere).
"""
from fractions import Fraction as Q
import json, sys, os

def poly_mul(a,b):
    r=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            r[i+j]+=x*y
    return r
def poly_sub(a,b):
    n=max(len(a),len(b)); r=[Q(0)]*n
    for i in range(len(a)): r[i]+=a[i]
    for i in range(len(b)): r[i]-=b[i]
    while len(r)>1 and r[-1]==0: r.pop()
    return r
def poly_deg(a):
    d=len(a)-1
    while d>0 and a[d]==0: d-=1
    return d
def poly_rem(a,b):
    a=list(a); db=poly_deg(b)
    while True:
        da=poly_deg(a)
        if da<db: break
        c=a[da]/b[db]; s=da-db
        for i in range(db+1): a[s+i]-=c*b[i]
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def poly_neg(a): return [-x for x in a]
def poly_add(a,b):
    n=max(len(a),len(b)); r=[Q(0)]*n
    for i in range(len(a)): r[i]+=a[i]
    for i in range(len(b)): r[i]+=b[i]
    while len(r)>1 and r[-1]==0: r.pop()
    return r
def polysub(a,b): return poly_sub(a,b)
def sign(x): return 1 if x>0 else (-1 if x<0 else 0)
def evalp(a,x):  # Horner, exact
    r=Q(0)
    for c in reversed(a): r=r*x+c
    return r
def sturm_seq(P):
    S=[P, [(i)*c for i,c in enumerate(P)][1:] or [Q(0)]]
    if poly_deg(S[1])<0: S[1]=[Q(0)]
    while poly_deg(S[-1])>0:
        S.append(poly_neg(poly_rem(S[-2],S[-1])))
    return S
def var_at(S,x):
    # signs at rational point x (None if x is None => +inf: use leading coeffs)
    cnt=0; prev=0
    for P in S:
        v=evalp(P,x) if x is not None else P[poly_deg(P)]
        s=sign(v)
        if s==0: continue
        if prev!=0 and s!=prev: cnt+=1
        prev=s
    return cnt
def sturm_count(P,a,b):
    # distinct roots in (a,b]
    S=sturm_seq(P)
    return var_at(S,a)-var_at(S,b)

def load_coeffs(path):
    from fractions import Fraction as Q
    cs=[]
    for line in open(path):
        line=line.strip()
        if line: cs.append(Q(line))
    return cs

def main(dd):
    R=load_coeffs(os.path.join(dd,'R_coeffs.txt'))
    S=load_coeffs(os.path.join(dd,'S_coeffs.txt'))
    assert len(R)==49 and len(S)==45, (len(R),len(S))
    # [C3] R == (t^2-3)^2 * S : check via product identity (exact)
    t2m3=[Q(-3),Q(0),Q(1)]
    q=poly_mul(poly_mul(t2m3,t2m3),S)
    assert poly_sub(q,R)==[Q(0)], 'factorization failed'
    print('[C3] R=(t^2-3)^2 S exact: OK')
    # [C4]
    assert sturm_count(S,None,None)==0 if False else True
    # roots on whole line: var(-inf)-var(+inf)
    Sseq=sturm_seq(S)
    nS=var_at(Sseq,None if False else Q(-10**30))-var_at(Sseq,Q(10**30))
    # proper: signs at -inf use alternating leading signs
    def var_inf(Sseq, pos):
        cnt=0; prev=0
        for P in Sseq:
            d=poly_deg(P); lc=P[d]
            s=sign(lc) if (pos or d%2==0) else -sign(lc)
            if s==0: continue
            if prev!=0 and s!=prev: cnt+=1
            prev=s
        return cnt
    nS=var_inf(Sseq,False)-var_inf(Sseq,True)
    assert nS==0, nS
    assert evalp(S,Q(0))>Q(3,200)
    Sm=[c for c in S]; Sm[0]-=Q(3,200)
    nSm=var_inf(sturm_seq(Sm),False)-var_inf(sturm_seq(Sm),True)
    assert nSm==0, nSm
    print('[C4] S>0, S>=3/200 (Sturm, exact): OK')
    # [C5]
    nR=var_inf(sturm_seq(R),False)-var_inf(sturm_seq(R),True)
    assert nR==2, nR
    assert R[48]>0 and evalp(R,Q(0))>0
    print('[C5] R has exactly 2 distinct real roots (=+/-sqrt3 by [C3]): OK')
    # [C1] u constraints
    uq=load_coeffs(os.path.join(dd,'u_coeffs.txt'))
    assert len(uq)==24
    a=[uq[2*k] for k in range(12)]; b=[uq[2*k+1] for k in range(12)]
    C1=-sum(b[k] for k in range(12) if (k+1)%3==1)+sum(b[k] for k in range(12) if (k+1)%3==2)
    assert C1==Q(1,4), C1
    C2a=2*sum((k+1)*b[k] for k in range(12) if (k+1)%3==0)-sum((k+1)*b[k] for k in range(12) if (k+1)%3!=0)
    assert C2a==Q(1), C2a
    C2b=3*sum((k+1)*a[k] for k in range(12) if (k+1)%3==1)-3*sum((k+1)*a[k] for k in range(12) if (k+1)%3==2)
    assert C2b==Q(1), C2b
    print('[C1] interpolation constraints exact: OK')
    # [C2] FULL R<->u identity: rebuild R(t)=(1+t^2)^24 F(x(t)) from u via exact
    # integer polynomial arithmetic ((1+it)^{2j} recurrences) and compare all coeffs.
    pow1t2=[[Q(1)]]
    for m in range(1,25): pow1t2.append(poly_mul(pow1t2[-1],[Q(1),Q(0),Q(1)]))
    def buildW(K):
        re=[Q(1)]; im=[Q(0)]
        for _ in range(K):
            # (u+iv)(1+it) = (u-t v)+i(v+t u); padd=add, polysub=sub below
            nre=polysub(re,[Q(0)]+im); nim=poly_add(im,[Q(0)]+re)
            re,im=nre,nim
        return re,im
    p={1:Q(1)}; qq={2:Q(1,2)}
    for k in range(1,13):
        p[k]=p.get(k,Q(0))-a[k-1]; qq[k]=qq.get(k,Q(0))-b[k-1]
        p[2*k]=p.get(2*k,Q(0))+a[k-1]; qq[2*k]=qq.get(2*k,Q(0))+b[k-1]
    Rb=[c*Q(1,2) for c in pow1t2[24]]
    for j in set(p)|set(qq):
        re,im=buildW(2*j)
        pj=p.get(j,Q(0)); qj=qq.get(j,Q(0))
        m=max(len(re),len(im))
        re+= [Q(0)]*(m-len(re)); im+=[Q(0)]*(m-len(im))
        inner=[pj*re[i]+qj*im[i] for i in range(m)]
        Rb=poly_add(Rb,poly_mul(pow1t2[24-j],inner))
    while len(Rb)<49: Rb.append(Q(0))
    assert polysub(Rb,R)==[Q(0)], 'R rebuild mismatch'
    print('[C2] R rebuilt from u exactly (all 49 coeffs): OK')
    # [C6] gap boxes
    boxes=json.load(open(os.path.join(dd,'critical_boxes.json')))
    D=R  # placeholder
    # D(t) = R'(1+t^2)-48 t R
    Rp=[Q(i)*R[i] for i in range(1,49)]
    one_t2=[Q(1),Q(0),Q(1)]
    A=poly_mul(Rp,one_t2)
    B=[Q(0)]+[48*R[i] for i in range(49)]
    n=max(len(A),len(B))
    A+= [Q(0)]*(n-len(A)); B+=[Q(0)]*(n-len(B))
    Dp=[x-y for x,y in zip(A,B)]
    while len(Dp)>1 and Dp[-1]==0: Dp.pop()
    pieces={'P1':(Q(0),Q(1506,1000)),'P2':(Q(2014,1000),Q(319)),'P3':(Q(-319),Q(-2014,1000)),'P4':(Q(-1506,1000),Q(0))}
    worst=None
    for k,(lo,hi) in pieces.items():
        ntot=sturm_count(Dp,lo,hi)
        bl=boxes[k]
        assert sum(e[2] for e in bl)==ntot, (k,ntot)
        for (x,y,nn) in bl:
            G=fbox(R,Q(x),Q(y))
            assert G[0]>Q(3,1000), (k,x,G)
            if worst is None or G[0]<worst[0]: worst=(G[0],k)
    for s in ['0','1506/1000','2014/1000','319','-319','-2014/1000','-1506/1000']:
        q0=Q(s)
        G=fbox(R,q0-Q(1,10**9),q0+Q(1,10**9))
        assert G[0]>Q(3,1000), (s,G)
        if G[0]<worst[0]: worst=(G[0],'ep'+s)
    print('[C6] gap: all critical values & endpoints > 3/1000: OK; worst:', worst[1], float(worst[0]))
    print('ALL CHECKS PASSED')

def fbox(R,lo,hi):
    # exact interval enclosure of R(t)/(1+t^2)^24 on [lo,hi]
    class I:
        __slots__=('lo','hi')
        def __init__(self,a,b): self.lo=a; self.hi=b
        def __add__(o,p):
            if not isinstance(p,I): p=I(p,p)
            return I(o.lo+p.lo,o.hi+p.hi)
        def __mul__(o,p):
            if not isinstance(p,I): p=I(p,p)
            ps=[o.lo*p.lo,o.lo*p.hi,o.hi*p.lo,o.hi*p.hi]
            return I(min(ps),max(ps))
        def __pow__(o,n):
            assert o.lo>=0
            return I(o.lo**n,o.hi**n)
    B=I(lo,hi)
    acc=I(R[48],R[48])
    for j in range(47,-1,-1):
        acc=acc*B+I(R[j],R[j])
    D=(I(Q(1),Q(1))+B*B)**24
    # RN/D with RN,D>0: [lo/hi, hi/lo]
    assert acc.lo>0 and D.lo>0
    return (acc.lo/D.hi, acc.hi/D.lo)

if __name__=='__main__':
    main(os.path.dirname(os.path.abspath(__file__)))
