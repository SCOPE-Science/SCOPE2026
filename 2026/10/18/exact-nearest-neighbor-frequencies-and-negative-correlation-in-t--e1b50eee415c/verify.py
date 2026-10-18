mu={'S':['S','q1'],'q1':['q2'],'q2':['q3'],'q3':['q4'],'q4':['q5'],'q5':['q7','q8'],'q7':['q9','q10'],'q8':['q11'],'q9':['q5','q12'],'q10':['q13'],'q11':['q14'],'q12':['q15'],'q13':['q16'],'q14':['q17'],'q15':['q18'],'q16':['q19'],'q17':['q20'],'q18':['q22'],'q19':['q23'],'q20':['q24','q1'],'q22':['q9'],'q23':['q25','q10'],'q24':['q26','q1'],'q25':['q20','q27'],'q26':['q23','q8'],'q27':['q15']}
eta={'S':'10','q1':'1','q2':'0','q3':'1','q4':'10','q5':'01','q7':'11','q8':'0','q9':'10','q10':'0','q11':'1','q12':'1','q13':'1','q14':'0','q15':'1','q16':'0','q17':'01','q18':'0','q19':'11','q20':'10','q22':'11','q23':'01','q24':'00','q25':'01','q26':'11','q27':'1'}

from collections import defaultdict
import sympy as s
from sympy.polys.matrices import DomainMatrix
x=s.Symbol('x');r=s.CRootOf(x**3-x-1,0);K=s.QQ.algebraic_field(r);rho=K.from_sympy(r)
L=[k for k in mu if k!='S'];n=len(L);I={k:i for i,k in enumerate(L)}
M=[[K.zero for j in L] for i in L]
for k,bs in mu.items():
 if k=='S':continue
 for h in bs:M[I[h]][I[k]]+=K.one

# Primitive substitution: the Boolean support of M^20 is strictly positive.
support=[[int(M[i][j]!=K.zero) for j in range(n)] for i in range(n)]
h=[row[:] for row in support]
for step in range(2,21):
    h=[[int(any(h[i][k] and support[k][j] for k in range(n))) for j in range(n)] for i in range(n)]
assert all(all(row) for row in h)

A=[[M[i][j]-(rho if i==j else K.zero) for j in range(n)] for i in range(n)]
A[-1]=[K.one]*n
rhs=[[K.zero] for i in range(n)];rhs[-1][0]=K.one
v=DomainMatrix(A,(n,n),K).lu_solve(DomainMatrix(rhs,(n,1),K)).to_list()
assert all(K.to_sympy(z[0]).evalf(20)>0 for z in v)

B=defaultdict(lambda:K.zero)
for k in L:
 for a,b in zip(mu[k],mu[k][1:]):B[(a,b)]+=v[I[k]][0]
pairs=set(B);frontier=set(B)
while frontier:
 nxt={(mu[a][-1],mu[b][0]) for a,b in frontier}-pairs
 pairs|=nxt;frontier=nxt
pairs=sorted(pairs);P={p:i for i,p in enumerate(pairs)};m=len(pairs)
Q=[[K.zero for j in range(m)] for i in range(m)]
for j,(a,b) in enumerate(pairs):Q[P[(mu[a][-1],mu[b][0])]][j]+=K.one
AA=[[ (rho if i==j else K.zero)-Q[i][j] for j in range(m)] for i in range(m)]

w=DomainMatrix(AA,(m,m),K).lu_solve(DomainMatrix([[B[p]] for p in pairs],(m,1),K)).to_list()

length=sum((v[I[k]][0]*K(len(eta[k])) for k in L),K.zero)
num=sum((v[I[k]][0]*K(sum(a=='1' and b=='1' for a,b in zip(eta[k],eta[k][1:]))) for k in L),K.zero)
num+=sum((w[P[a,b]][0] for a,b in pairs if eta[a][-1]=='1' and eta[b][0]=='1'),K.zero)
f=num/length
expected=(K(4)+K(9)*rho-K(8)*rho*rho)/K(7)
assert f==expected
assert len(L)==25 and len(pairs)==67
c=K.one+rho-rho*rho
assert c*c==rho-K.one
assert sum(v[j][0] for j in range(n))==K.one
assert sum(x[0] for x in w)==K.one
assert sum(v[I[k]][0]*K(eta[k].count('1')) for k in L)/length ==c
assert K.to_sympy(f-c*c).evalf(30)<0

# Independent finite recurrence-versus-morphism check, not the infinite proof.
a=[0,1]
for j in range(2,8194):
    a.append(j-a[j-a[j-a[j-1]]])
word=['S']
for i in range(45):
    word=[b for t in word for b in mu[t]]
    if len(word)>20000:break
stream=''.join(eta[z] for z in word)
d=''.join(str(a[j+1]-a[j]) for j in range(len(a)-1))
assert stream[:len(d)]==d
assert len(d)==8193
assert all(t in '01' for t in d)
print('VERIFY_OK: exact algebraic 25-state letter/67-pair solver, negative covariance, 8193-term recurrence test')
