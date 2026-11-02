"""Exact finite-field enumeration for quadratic 3-term irreducibility."""

def prime_modulus(p,r):
    if r==1:return (0,1)
    for z in __import__('itertools').product(range(p),repeat=r):
        f=list(z)+[1]
        # test irreducibility by enumerating monic divisors degrees 1..r//2
        ok=True
        for d in range(1,r//2+1):
          for coeff in __import__('itertools').product(range(p),repeat=d):
            div=list(coeff)+[1]
            rem=f[:]
            for j in range(r-d,-1,-1):
              mul=rem[j+d]
              for k in range(d+1):rem[j+k]=(rem[j+k]-mul*div[k])%p
            if all(x==0 for x in rem[:d]):ok=False;break
          if not ok:break
        if ok:return tuple(f)
    raise ValueError('no modulus')

class Field:
  def __init__(self,p,r):
    self.p=p;self.r=r;self.q=p**r;self.mod=prime_modulus(p,r)
    self.elems=list(range(self.q));self.zero=0;self.one=1
    self.terms=[tuple((n//p**i)%p for i in range(r)) for n in self.elems]
    self.encode=lambda z: sum((int(v)%p)*p**i for i,v in enumerate(z))
  def add(self,a,b):return self.encode([(x+y)%self.p for x,y in zip(self.terms[a],self.terms[b])])
  def neg(self,a):return self.encode([-x for x in self.terms[a]])
  def sub(self,a,b):return self.add(a,self.neg(b))
  def mul(self,a,b):
    p,r=self.p,self.r
    if r==1:return(a*b)%p
    out=[0]*(2*r-1);ca=self.terms[a];cb=self.terms[b]
    for i in range(r):
      for j in range(r):out[i+j]=(out[i+j]+ca[i]*cb[j])%p
    for d in range(2*r-2,r-1,-1):
      t=out[d]
      for i in range(r):out[d-r+i]=(out[d-r+i]-t*self.mod[i])%p
    return self.encode(out[:r])
  def square(self,a):return self.mul(a,a)

def test(p,r):
  F=Field(p,r);q=F.q
  two=F.add(1,1)
  squares={F.square(v) for v in F.elems}
  def good(a,b):return F.sub(F.square(a),F.mul(F.mul(two,two),b)) not in squares
  shifts=0
  for u in F.elems[1:]:
    for v in F.elems:
      got=0
      for a in F.elems:
        for b in F.elems:
          if all(good(F.add(a,F.mul(u,j)),F.add(b,F.mul(v,j))) for j in (0,1,two)):
            got+=1
      assert got==(q-1)*(q-3)//8,(p,r,u,v,got,(q-1)*(q-3)//8)
      shifts+=1
  return q,shifts,q*q*shifts

if __name__=='__main__':
  total=0
  for p,r in [(3,1),(5,1),(7,1),(11,1),(13,1),(17,1),(19,1),(3,2),(5,2),(3,3)]:
    q,shifts,trials=test(p,r)
    print('pass',p,r,q,shifts,trials,flush=True)
    total+=shifts
  print('VERIFY_OK shift_cases',total)
