from itertools import product
from collections import Counter

def field(q):
  if q==4:
    add=lambda x,y:x^y
    def mul(x,y):
      out=0
      for i in range(2):
        if x>>i&1:
          for j in range(2):
            if y>>j&1:out^=1<<(i+j)
      # modulus X²+X+1
      for k in (2,):
        if out>>k&1:out^=7<<(k-2)
      return out
  else:
    add=lambda x,y:(x+y)%q
    mul=lambda x,y:(x*y)%q
  return add,mul

def compute(q):
  plus,mul=field(q)
  num_total=num_rank1=num_rank1_idemp=num_rank1_nil=0
  spectrum=Counter()
  by_case=Counter()
  for a,b,c,d in product(range(q),repeat=4):
    if (plus(mul(a,d),mul(b,c))==0 if q==4 or q==2 else (mul(a,d)-mul(b,c))%q==0):continue
    n1=n0=n2=n_id=n_nil=0
    for u,v,w,z in product(range(q),repeat=4):
      e11=(plus(mul(a,mul(u,u)),mul(c,mul(v,v))),plus(mul(b,mul(u,u)),mul(d,mul(v,v))))
      e22=(plus(mul(a,mul(w,w)),mul(c,mul(z,z))),plus(mul(b,mul(w,w)),mul(d,mul(z,z))))
      lhs1=(plus(mul(a,u),mul(b,w)),plus(mul(a,v),mul(b,z)))
      lhs2=(plus(mul(c,u),mul(d,w)),plus(mul(c,v),mul(d,z)))
      if e11!=lhs1 or e22!=lhs2:continue
      if plus(mul(a,mul(u,w)),mul(c,mul(v,z)))!=0 or plus(mul(b,mul(u,w)),mul(d,mul(v,z)))!=0:continue
      det=(plus(mul(u,z),mul(v,w)) if q==4 or q==2 else (mul(u,z)-mul(v,w))%q)
      if (u,v,w,z)==(0,0,0,0):n0+=1
      elif det!=0:n2+=1
      else:
        n1+=1
        # φ²=[u*u+w*v, v*u+z*v], [u*w+w*z,v*w+z*z] in column notation
        comp=(plus(mul(u,u),mul(v,w)),plus(mul(u,v),mul(v,z)),plus(mul(w,u),mul(z,w)),plus(mul(w,v),mul(z,z)))
        if comp==(u,v,w,z):n_id+=1
        elif comp==(0,0,0,0):n_nil+=1
        else: raise AssertionError(('unexpected',q,a,b,c,d,u,v,w,z,comp))
    assert n0==1
    spectrum[n2]+=1
    by_case[(int(a!=0),int(b!=0),int(c!=0),int(d!=0))]+=n1
    num_total+=n0+n1+n2
    num_rank1+=n1
    num_rank1_idemp+=n_id
    num_rank1_nil+=n_nil
  S=(q-1)**2;s=(2 if q%2 else 1);r=__import__('math').gcd(3,q-1)
  G=q*S*(q+1)
  expected=2*G+S*(5*q-s+r)
  assert num_total==expected,(q,num_total,expected)
  assert num_rank1==4*q*S,(q,num_rank1,4*q*S)
  assert num_rank1_idemp==num_rank1_nil==2*q*S
  print(q,'TOTAL',num_total,'RANK1',num_rank1,'SQUAREZERO',num_rank1_nil,'IDEMP',num_rank1_idemp,'GROUP_ORDER_HISTOGRAM',dict(spectrum),'case',dict(by_case))

if __name__=='__main__':
  for q in (2,3,4,5,7):compute(q)
  print('VERIFY_OK')
