from fractions import Fraction as Q

BETA=Q(-3,2); v=(5,-2,Q(-2))
def D(r,k,b=BETA): return 10*Q(k)-10*Q(r)*b
def A(r,k,e,b=BETA): return Q(e)-10*Q(k)*b+5*Q(r)*b*b
def Delta(r,k,e): return (10*Q(k))**2-20*Q(r)*Q(e)
def alpha2(w):
    rv,kv,ev=v; rw,kw,ew=w
    den=5*(rv*D(rw,kw)-rw*D(rv,kv))
    return (A(*v)*D(rw,kw)-A(*w)*D(*v[:2]))/den if den else None
def full_signature(w):
    rv,kv,ev=v; rw,kw,ew=w
    def F(b):
        return A(*v,b)*D(rw,kw,b)-A(rw,kw,ew,b)*D(rv,kv,b)
    c0=F(Q(0)); fp=F(Q(1)); fm=F(Q(-1)); c1=(fp-fm)/2; c2=(fp+fm)/2-c0
    g=5*(rv*D(rw,kw,Q(0))-rw*D(rv,kv,Q(0)))
    vals=[-g,c2,c1,c0]
    lead=next(x for x in vals if x)
    return tuple(x/lead for x in vals)
recs=[]
for m in range(1,11):
  for rw in range(0,6):
    if (m-3*rw)%2: continue
    kw=(m-3*rw)//2; ru,ku=5-rw,-2-kw
    for E2 in range(-200,201):
      ew=Q(E2,2); eu=Q(-2)-ew
      if Delta(rw,kw,ew)>=0 and Delta(ru,ku,eu)>=0:
        a2=alpha2((rw,kw,ew))
        if a2 is not None and a2>0: recs.append((a2,(rw,kw,ew),(ru,ku,eu)))
assert len(recs)==18
unordered={tuple(sorted((w,u))) for _,w,u in recs}
assert len(unordered)==9
sigs={full_signature(w) for _,w,_ in recs}
assert len(sigs)==6
top=[r for r in recs if r[0]==Q(13,10)]
assert len(top)==4
top_unordered={tuple(sorted((w,u))) for _,w,u in top}
assert top_unordered=={tuple(sorted(((1,0,Q(-7)),(4,-2,Q(5))))),tuple(sorted(((2,-1,Q(5,2)),(3,-1,Q(-9,2)))))}
assert len({full_signature(w) for _,w,_ in top})==1
print('oriented_records=18')
print('unordered_decompositions=9')
print('distinct_wall_loci=6')
print('top_alpha2=13/10')
print('top_unordered_decompositions=2')
print('CERTIFICATE_OK')
