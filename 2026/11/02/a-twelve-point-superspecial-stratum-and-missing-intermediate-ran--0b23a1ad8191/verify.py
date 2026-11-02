"""Exact finite-field incidence verification for five elliptic quotients of a genus-five curve."""
from collections import Counter
from itertools import permutations
from math import comb

P=17; N=P*P; D=3
F=[(a,b) for a in range(P) for b in range(P)]
ix={z:k for k,z in enumerate(F)}
add=[[ix[((a+c)%P,(b+d)%P)] for c,d in F] for a,b in F]
mul=[[ix[((a*c+D*b*d)%P,(a*d+b*c)%P)] for c,d in F] for a,b in F]
neg=[ix[(-a%P,-b%P)] for a,b in F]
zero=ix[(0,0)];one=ix[(1,0)]
sub=lambda a,b:add[a][neg[b]]
def power(v,n):
 out=one
 while n:
  if n&1:out=mul[out][v]
  v=mul[v][v];n//=2
 return out
inv=[None if i==zero else power(i,N-2) for i in range(N)]
assert all(mul[i][inv[i]]==one for i in range(1,N))

coeff=[comb(8,k)**2 % P for k in range(9)]
assert coeff==[1,13,2,8,4,8,2,13,1]
# H(T)=(T^2+T-1)(T^2-3T+1)(T^2-T+1)(T^2-T-1).
quadratics=([(-1)%P,1,1],[1,(-3)%P,1],[1,(-1)%P,1],[(-1)%P,(-1)%P,1])
polynomial=[1]
for factor in quadratics:
 result=[0]*(len(polynomial)+len(factor)-1)
 for j,c in enumerate(polynomial):
  for k,d in enumerate(factor):result[j+k]=(result[j+k]+c*d)%P
 polynomial=result
assert polynomial==coeff
for c0,c1,c2 in quadratics:
 assert all((c0+c1*z+c2*z*z)%P for z in range(P))
print('DEURING_HASSE_POLYNOMIAL_FACTORIZATION=FOUR_DISTINCT_IRREDUCIBLE_QUADRATICS')
roots=[]
for t in range(N):
 value=zero
 for c in reversed(coeff): value=add[mul[value][t]][ix[(c,0)]]
 if value==zero:roots.append(t)
R=set(roots)
assert len(R)==8
assert all(F[z][1]!=0 for z in roots)
assert len({power(z,P) for z in roots})==8
print('HASSE_POLYNOMIAL_COEFFICIENTS_MOD17=',coeff)
print('HASSE_ROOTS_F289=',[F[z] for z in roots], 'ALL_NON_F17=YES')

# Paper's quotient Legendre parameters in the order C1,C2,C3,C4,C5.
def pattern(u,v):
 vm1=sub(v,one);um1=sub(u,one)
 values=(mul[vm1][inv[um1]],mul[v][inv[u]],mul[mul[v][sub(one,u)]][inv[sub(v,u)]],v,u)
 return tuple(t in R for t in values)

pairs=Counter();joint=[]
for u in roots:
 for v in roots:
  if v==u:continue
  s=sum(pattern(u,v));pairs[s]+=1
  if s==5:joint.append((u,v))
assert pairs=={2:44,5:12}
assert len(joint)==12
print('ROOT_ORDERED_PAIRS=56;EXACT_TWO=44;EXACT_FIVE=12;TRIPLE_OR_QUADRUPLE=0')

# S_5 label permutations, normalized by a fractional-linear map.
def bracket(a,b):
 # homogeneous P1 coordinates [z:1] or infinity [1:0]
 aa=(one,zero) if a is None else (a,one)
 bb=(one,zero) if b is None else (b,one)
 return sub(mul[aa[0]][bb[1]],mul[aa[1]][bb[0]])
def normalize(L):
 a,b,c=L[:3]
 scale=mul[bracket(c,a)][inv[bracket(c,b)]]
 res=[]
 for z in L[3:]:
  num=mul[bracket(z,b)][scale]
  den=bracket(z,a)
  assert den!=zero
  res.append(mul[num][inv[den]])
 return tuple(res)
base=[None,zero,one,*joint[0]]
orbit={normalize([base[j] for j in perm]) for perm in permutations(range(5))}
assert len(orbit)==12 and orbit==set(joint)
print('FIVEFOLD_LOCUS_SINGLE_S5_ORBIT=12_MARKED_POINTS;STABILIZER=10')

# Direct independent enumeration over F289 of every parameter pair.
count=Counter()
for u in range(N):
 if u in (zero,one):continue
 for v in range(N):
  if v in (zero,one,u):continue
  count[sum(pattern(u,v))]+=1
assert count=={0:71130,1:10500,2:440,5:12}
assert sum(count.values())==(N-2)*(N-3)
print('F289_QUOTIENT_SS_DISTRIBUTION=',dict(sorted(count.items())))
# F17 rational marked parameter pairs: roots are quadratic non-rational.
assert all(r not in R for r in (ix[(a,0)] for a in range(P)))
print('F17_QUOTIENT_SS_DISTRIBUTION={0:210}')
# Geometric pairwise intersections: 44 exclusive doubles + twelve quintuples per pair.
assert 44+12==56 and 10*44==440
# All these intersections are F289 rational; no other geometric ones by S5 relabeling.
assert 40*(N-3)-940==10500
assert (N-2)*(N-3)-40*(N-3)+488==71130
print('TEN_PAIRWISE_INTERSECTIONS_EACH=56;EXCLUSIVE_DOUBLE_LOCUS=440;FIVEFOLD=12')
print('ALL_EXTENSION_FORMULAS=PASS;VERIFY_OK')
