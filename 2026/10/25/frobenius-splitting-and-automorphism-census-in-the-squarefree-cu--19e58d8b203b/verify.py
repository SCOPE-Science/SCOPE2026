"""Exact finite-field checks for the squarefree-cubic commutative algebra classification.
Run: python3 verify.py (standard library only).
The checks are exhaustive over symmetric forms and the GL2 orbits in fields F5, F7, F11.
"""
from collections import Counter

def verify(p):
    inv=lambda x: pow(x % p, -1, p)
    mats=[]
    for A in range(p):
      for B in range(p):
       for C in range(p):
        for D in range(p):
         det=(A*D-B*C)%p
         if det: mats.append((A,B,C,D,inv(det)))
    assert len(mats)==(p*p-1)*(p*p-p)

    def act_f(f,g):
      a,b,c,d=f; A,B,C,D,k=g
      z=(a*A**3+b*A*A*C+c*A*C*C+d*C**3,
         3*a*A*A*B+b*(A*A*D+2*A*B*C)+c*(2*A*C*D+B*C*C)+3*d*C*C*D,
         3*a*A*B*B+b*(2*A*B*D+B*B*C)+c*(A*D*D+2*B*C*D)+3*d*C*D*D,
         a*B**3+b*B*B*D+c*B*D*D+d*D**3)
      return tuple((t*k)%p for t in z)

    def act_q(q,g):
      u,v,w=q; A,B,C,D,k=g
      return ((u*A*A+2*v*A*C+w*C*C)%p,
              (u*A*B+v*(A*D+B*C)+w*C*D)%p,
              (u*B*B+2*v*B*D+w*D*D)%p)

    def mu(f, u, v):
      a,b,c,d=f; i3=inv(3)
      x,y=u; z,w=v
      X=x*z; Y=x*w+y*z; Z=y*w
      return ((b*i3*X+c*i3*Y+d*Z)%p,
              (-a*X-b*i3*Y-c*i3*Z)%p)

    def check_twist(f,g):
      A,B,C,D,k=g; f2=act_f(f,g)
      for u,v in [((1,0),(1,0)),((1,0),(0,1)),((0,1),(0,1))]:
        gu=((A*u[0]+B*u[1])%p,(C*u[0]+D*u[1])%p)
        gv=((A*v[0]+B*v[1])%p,(C*v[0]+D*v[1])%p)
        x,y=mu(f,gu,gv)
        rhs=((D*x-B*y)*k%p,(-C*x+A*y)*k%p)
        assert mu(f2,u,v)==rhs,(f,g,u,v)

    def projective_roots(f):
      a,b,c,d=f
      return sum((a*t**3+b*t*t+c*t+d)%p==0 for t in range(p))+(a==0)

    # The three Frobenius-splitting types of squarefree binary cubics.
    nonsquare=next(x for x in range(1,p) if pow(x,(p-1)//2,p)==p-1)
    reps={"split":(0,1,p-1,0), "mixed":(1,0,-nonsquare%p,0)}
    for a in range(p):
      for b in range(1,p):
        f=(1,0,a,b)
        if not projective_roots(f):
          reps["irreducible"]=f
          break
      if "irreducible" in reps:break
    assert sorted(reps)==['irreducible','mixed','split']

    full=set()
    counts=Counter()
    detail={}
    for typ,f in reps.items():
      for g in mats: check_twist(f,g)
      images={act_f(f,g) for g in mats}
      assert len(images)==len(mats)//{'split':6,'mixed':2,'irreducible':3}[typ]
      assert not (full & images)
      full.update(images)
      stabilizer=[g for g in mats if act_f(f,g)==f]
      assert len(stabilizer)=={'split':6,'mixed':2,'irreducible':3}[typ]
      # Exhaustively partition all triples (Q11,Q12,Q22) into stabilizer-orbits.
      unseen={(u,v,w) for u in range(p) for v in range(p) for w in range(p)}
      groups=Counter()
      while unseen:
        t=next(iter(unseen))
        orbit={act_q(t,g) for g in stabilizer}
        assert orbit<=unseen
        unseen-=orbit
        n=len(stabilizer)//len(orbit)
        assert n in [1,2,3,6]
        groups[n]+=1
      expected={'split':{1:p*(p-1)*(p-2)//6, 2:p*p-p,6:p},
                'mixed':{1:p*p*(p-1)//2,2:p*p},
                'irreducible':{1:p*(p*p-1)//3,3:p}}[typ]
      assert dict(groups)==expected,(p,typ,groups,expected)
      counts.update(groups)
      detail[typ]=(len(images),dict(groups))
      # The cubic/multiplication covariance was also tested directly above.
    assert len(full)==len(mats)
    assert dict(counts)=={1:p*p*(p-1),2:2*p*p-p,3:p,6:p},counts
    assert sum(counts.values())==p**3+p*p+p
    print('p=',p,'GL2=',len(mats),'cubic_types=',detail,
          'aut_group_classes=',dict(sorted(counts.items())),
          'total=',sum(counts.values()))

if __name__=='__main__':
  for prime in (5,7,11): verify(prime)
  print('VERIFY_OK')
