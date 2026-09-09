#!/usr/bin/env python3
"""Class-resolved Hurwitz (2,3,7) profile for PSL(2,27). Stdlib only.
GF(27) = F3[t]/(t^3+2t+1) (no root mod 3 -> irreducible).
"""
import sys, json
from collections import deque

# ---- GF(27) ----
def fadd(a,b):
    r=0;m=1
    for _ in range(3):
        r+=( ((a%3)+(b%3))%3 )*m; a//=3;b//=3;m*=3
    return r
def fneg(a):
    r=0;m=1
    for _ in range(3):
        r+=((-(a%3))%3)*m; a//=3;m*=3
    return r
def fsub(a,b): return fadd(a,fneg(b))
# mod polynomial: t^3 = t+2 (since t^3+2t+1=0 -> t^3 = t+2). coeffs: t^3 = 0 + 1*t + 2*t^2? No: t^3 = -2t-1 = t+2 mod3. So t^3 = 2 + 1*t + 0*t^2.
def fmul(a,b):
    a0,a1,a2=a%3,(a//3)%3,(a//9)%3
    b0,b1,b2=b%3,(b//3)%3,(b//9)%3
    c0=(a0*b0)%3; c1=(a0*b1+a1*b0)%3; c2=(a0*b2+a1*b1+a2*b0)%3
    c3=(a1*b2+a2*b1)%3; c4=(a2*b2)%3
    # reduce t^3 = 2+t, t^4 = 2t+t^2
    d0=(c0+2*c3)%3; d1=(c1+c3+2*c4)%3; d2=(c2+c4)%3
    return d0+3*d1+9*d2
def fpow(a,k):
    r=1
    for _ in range(k): r=fmul(r,a)
    return r
def finv(a):
    assert a!=0
    for b in range(1,27):
        if fmul(a,b)==1: return b
    raise ValueError
ONE=1; TWO=2; NEGONE=2
PRIM=3  # = t; check order 26
assert fpow(PRIM,26)==1 and fpow(PRIM,13)!=1 and fpow(PRIM,2)!=1

I=(1,0,0,1)
def neg(M): return (fneg(M[0]),fneg(M[1]),fneg(M[2]),fneg(M[3]))
def can(M):
    a,b,c,d=M; N=(fneg(a),fneg(b),fneg(c),fneg(d))
    return tuple(M) if tuple(M)<=N else N
def madd(*a): return a
def mul(A,B):
    a,b,c,d=A; e,f,g,h=B
    return can((fadd(fmul(a,e),fmul(b,g)), fadd(fmul(a,f),fmul(b,h)),
                fadd(fmul(c,e),fmul(d,g)), fadd(fmul(c,f),fmul(d,h))))
def det(M):
    a,b,c,d=M; return fsub(fmul(a,d),fmul(b,c))
def inv(M):
    a,b,c,d=M; assert det(M)==1,(M,det(M))
    return can((d,fneg(b),fneg(c),a))
def pw(M,k):
    R=I
    for _ in range(k): R=mul(R,M)
    return R
def order(M):
    P=M
    for k in range(1,1000):
        if P==I: return k
        P=mul(P,M)
    raise ValueError('order too big')

print('enumerating SL(2,27)...',flush=True)
elts=[]
for a in range(27):
    for b in range(27):
        for c in range(27):
            # d: a*d-b*c=1
            bc=fmul(b,c)
            for d in range(27):
                if fsub(fmul(a,d),bc)==1:
                    elts.append(can((a,b,c,d)))
elts=sorted(set(elts))
print('n=',len(elts),flush=True)
assert len(elts)==27*(27*27-1)//2==9828,(len(elts))
G=len(elts)
# generators
u=can((1,1,0,1)); v=can((1,0,1,1))
w=can((PRIM,0,0,finv(PRIM)))
gens=[u,inv(u),v,inv(v),w,inv(w)]
def conj(g,h): return mul(mul(h,g),inv(h))
seen={}; classes=[]
for g in elts:
    if g in seen: continue
    orb=set([g]); q=deque([g])
    while q:
        x=q.popleft()
        for h in gens:
            y=conj(x,h)
            if y not in orb: orb.add(y); q.append(y)
    for x in orb: seen[x]=len(classes)
    classes.append((g,orb))
assert sum(len(o) for _,o in classes)==G
print('nclasses=',len(classes),flush=True)
# label
def tr(M): return fadd(M[0],M[3])
info=[]
for ci,(rep,orb) in enumerate(classes):
    info.append(dict(ci=ci,order=order(rep),size=len(orb),trace=tr(rep),rep=list(rep)))
from collections import defaultdict
byord=defaultdict(list)
for e in info: byord[e['order']].append(e)
for o in byord: byord[o].sort(key=lambda e:(e['trace'],e['rep']))
name={}
for o,lst in sorted(byord.items()):
    for j,e in enumerate(lst):
        e['name']=f"{o}{chr(65+j)}"; name[e['ci']]=e['name']
def cls_of(g): return name[seen[g]]
members={e['name']:[] for e in info}
for g in elts: members[cls_of(g)].append(g)
for e in sorted(info,key=lambda e:e['name']):
    print(' ',e['name'],'order',e['order'],'size',e['size'],'trace',e['trace'])
c2=[e for e in info if e['order']==2]; c3=[e for e in info if e['order']==3]
c7=sorted([e for e in info if e['order']==7],key=lambda e:e['name'])
print('2-classes:',[(e['name'],e['size']) for e in c2])
print('3-classes:',[(e['name'],e['size']) for e in c3])
print('7-classes:',[(e['name'],e['size']) for e in c7])
C2=c2[0]['name']
x0=members[C2][0]
C=[c for c in elts if mul(c,x0)==mul(x0,c)]
print('|C(x0)|=',len(C))
def suborder(x,y):
    yi=inv(y); got=set([I]); q=deque([I])
    while q:
        z=q.popleft()
        for w_ in (mul(z,x),mul(z,y),mul(z,yi)):
            if w_ not in got: got.add(w_); q.append(w_)
    return len(got)
results=[]
for e3 in c3:
    for e7 in c7:
        T3=e3['name']; T7=e7['name']
        S=[y for y in members[T3] if cls_of(mul(x0,y))==T7]
        N=len(members[C2])*len(S)
        reps=[]; used=set()
        for y in S:
            if y in used: continue
            reps.append(y); q=deque([y]); used.add(y)
            while q:
                z=q.popleft()
                for c in C:
                    w=conj(z,c)
                    if w in S and w not in used: used.add(w); q.append(w)
        assert len(used)==len(S),(T3,T7,len(used),len(S))
        orders=suborder and [(y,suborder(x0,y)) for y in reps]
        gen=[y for y,o in orders if o==G]
        maxo=max(o for _,o in orders)
        results.append(dict(type=f"({C2},{T3},{T7})",N=N,n_reps=len(reps),
            verdict='GENERATES' if gen else 'NON-GENERATING',max_suborder=maxo,
            witness=[list(gen[0])] if gen else None))
        print(f"  ({C2},{T3},{T7}) N={N} reps={len(reps)} verdict={results[-1]['verdict']} maxsub={maxo}",flush=True)
out=dict(p=27,G=G,genus=1+G//84,Gdiv84=(G%84==0),
    classes=[{k:e[k] for k in ('name','order','size','trace')} for e in sorted(info,key=lambda e:e['name'])],
    triples=results)
json.dump(out,open('output/artifacts/hurwitz_psl2_27.json','w'),indent=1)
print('saved. genus=',out['genus'],'div84=',out['Gdiv84'])
