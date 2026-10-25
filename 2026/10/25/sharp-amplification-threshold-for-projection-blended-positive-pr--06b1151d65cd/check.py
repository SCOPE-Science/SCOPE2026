from fractions import Fraction as Q
from math import sqrt
# Exact-rational check for two backward-Euler fine substeps versus one coarse step.
s=[Q(1,2000), Q(5)]
f=[1/(1+t/2)**2 for t in s]
g=[1/(1+t) for t in s]
p=[[Q(1,2),Q(1,2)],[Q(1,2),Q(1,2)]]
h=[[g[i]*(i==j)+(f[i]-g[i])*p[i][j] for j in range(2)] for i in range(2)]
excess=h[0][0]**2+h[1][0]**2-1
assert excess>0
assert all(0<f[i]<g[i]<1 for i in range(2))
# The similarity G-DP ~ G-sqrt(D)P sqrt(D) is SPD and within [F,G].
print('fine:',f,'coarse:',g)
print('mixed map:',h)
print('exact squared norm excess:',excess,'approx',float(excess))
# Rank-one orthogonal projector extremizers for sharp universal envelope.
c2=(2+sqrt(2))/4;s2=(2-sqrt(2))/4;cs=sqrt(2)/4
P=[[1.,0.],[0.,0.]]
F=[[c2,cs],[cs,s2]]
G=[[s2,cs],[cs,c2]]
H=[[F[i][0],G[i][1]] for i in range(2)]
C=(1+sqrt(2))/2
assert abs((H[0][0]+H[0][1])-C)<1e-14
assert abs((H[1][0]+H[1][1])-C)<1e-14
assert abs(H[0][0]-H[1][1])<1e-14
assert abs(H[0][1]-H[1][0])<1e-14
for scale in [0.7,0.82,2/(1+sqrt(2)),0.85,0.99]:
 tau=1e-5
 lam=scale*(tau+(1-tau)*C)
 if scale < 2/(1+sqrt(2))-1e-12: assert lam<1
 if scale > 2/(1+sqrt(2))+1e-3: assert lam>1
print('universal sharp C=',C,'qcrit=',1/C)
print('CHECK_OK')
