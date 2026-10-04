import math, random

def norm(v,q):
    if q==math.inf: return max(abs(t) for t in v)
    return sum(abs(t)**q for t in v)**(1/q)

def add(x,y,s=1): return [a+s*b for a,b in zip(x,y)]
def normalize(v,q):
    n=norm(v,q); return [t/n for t in v]
def formula(q,r):
    qp = 1 if q==math.inf else (math.inf if q==1 else q/(q-1))
    s=min(q,qp)
    return 1.0 if r<=s else 2**(1-r/s)

def value(x,y,q,r):
    return (norm(add(x,y),q)**r+norm(add(x,y,-1),q)**r)/(2**r)

random.seed(20261002)
for q in [1,1.25,1.5,2,3,4,8,math.inf]:
  for r in [1,1.2,1.5,2,3,4,6]:
    f=formula(q,r)
    best=10
    for d in [2,3,5]:
      for _ in range(1500):
        x=normalize([random.uniform(-1,1) for _ in range(d)],q)
        y=normalize([random.uniform(-1,1) for _ in range(d)],q)
        best=min(best,value(x,y,q,r))
    if best+2e-6 < f:
      raise SystemExit(f'FAIL random q={q} r={r} best={best} formula={f}')
    # exact-form extremizer, numerical evaluation
    if q<=2:
      c=2**(-1/q)
      x=[c,c]; y=[c,-c]
    else:
      x=[1.0,0.0]; y=[0.0,1.0]
    ev=value(x,y,q,r)
    target=f if r>=min(q, (1 if q==math.inf else (math.inf if q==1 else q/(q-1)))) else 1.0
    # for r below s the sharp extremizer is y=x, not the balanced pair
    if r < min(q, (1 if q==math.inf else (math.inf if q==1 else q/(q-1)))):
      x=[1.0,0.0]; y=x[:]
      ev=value(x,y,q,r); target=1.0
    if abs(ev-target)>2e-10:
      raise SystemExit(f'FAIL extremizer q={q} r={r} ev={ev} target={target}')
print('VERIFY_OK q=1,1.25,1.5,2,3,4,8,infinity; r=1,1.2,1.5,2,3,4,6; random_lower_bounds_and_exact_extremizers')
