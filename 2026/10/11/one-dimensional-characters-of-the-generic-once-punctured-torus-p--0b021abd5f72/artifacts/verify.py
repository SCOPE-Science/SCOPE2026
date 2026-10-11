import sympy as s
q,a,b,c,h=s.symbols('q a b c h', nonzero=True)
A=q**-2-1-q**2+q**4
B=q**-4-q**-2-1+q**2
D=q**-3+q**-1-q-q**3
dq=q**2-q**-2
rels=[]
rels.append(s.expand(dq*a*b + A*a-B*b+B*c+D*h))
rels.append(s.expand(dq*b*c + B*a-B*b+A*c+D*h))
rels.append(s.expand(dq*c*a + A*a-A*b+A*c+D*h))
rels.append(s.expand((q**-3-2*q**-1+2*q**3-q**5)*a+(q**-4-2+q**4)*h+(q**-1-q**3)*a*b-(q**-3-q)*a*c))
rels.append(s.expand(-(q**-1-2*q+2*q**5-q**7)*a+(q**-1-2*q+2*q**5-q**7)*c-(q-q**5)*a*b+(q-q**5)*b*c))
rels.append(s.expand(-(q**-3-2*q**-1+2*q**3-q**5)*c-(q**-4-2+q**4)*h+(q**-3-q)*a*c-(q**-1-q**3)*b*c))
rels.append(s.expand(a*b*c +(q**-6-2*q**-4-q**-2+4-q**2-2*q**4+q**6)*c +(2*q**-5-3*q**-3-2*q**-1+4*q-q**5)*h +(q**-2-2+q**2)*a*c +(q**-4-2+q**4)*b*c +(q**-1-q)*a*h -(q**-5-q**-3)*b*h +(q**-1-q)*c*h - q**-2*h**2))
alpha=-(q-1)**2/q
beta=-(q**2-1)**2/q**2
gamma=-(q**4-1)**2/q**4
nu=(q+1)**2/q
H=lambda A0,B0,C0:s.factor(q*(A0*C0+(q**2-1)*(A0-B0+C0))/(q**2+1))
triples=[(0,0,0),(alpha,alpha,alpha),(gamma,gamma,gamma),(nu,nu,nu),
         (0,beta,beta),(beta,0,beta),(beta,beta,0),
         (gamma,beta,beta),(beta,gamma,beta),(beta,beta,gamma)]
for T in triples:
    subs={a:T[0],b:T[1],c:T[2],h:H(*T)}
    assert all(s.factor(s.together(R.subs(subs)))==0 for R in rels), T
# Completeness factor certificates after solving the third deformed commutator for h.
hstar=q*(a*c+(q**2-1)*(a-b+c))/(q**2+1)
# R1-R2 branch condition.
branch=s.factor(s.together((rels[0]-rels[1]).subs(h,hstar)))
expected=(q-1)*(q+1)*(q**2+1)*(a-c)*(b*q**2+(q**2-1)**2)/q**4
assert s.factor(branch-expected)==0
# a=c: R1 forces a=b or a=beta.
r1_ac=s.factor(s.together(rels[0].subs({c:a,h:hstar.subs(c,a)})))
expected_ac=-(a-b)*(q-1)*(q+1)*(q**2+1)*(a*q**2+(q**2-1)**2)/q**4
assert s.factor(r1_ac-expected_ac)==0
# diagonal cubic factor.
cubic_diag=s.factor(s.together(rels[-1].subs({b:a,c:a,h:hstar.subs({b:a,c:a})})))
expected_diag=a*(-a*q+(q+1)**2)*(a*q+(q-1)**2)*(a*q**4+(q**4-1)**2)/(q**6*(q**2+1)**2)
assert s.factor(cubic_diag-expected_diag)==0
# a=c=beta: cubic leaves b=0 or b=gamma when q^6 !=1.
cubic_acbeta=s.factor(s.together(rels[-1].subs({a:beta,c:beta,h:hstar.subs({a:beta,c:beta})})))
expected_acbeta=-b*(q-1)**2*(q+1)**2*(q**2-q+1)*(q**2+q+1)*(b*q**4+(q**4-1)**2)/(q**8*(q**2+1)**2)
assert s.factor(cubic_acbeta-expected_acbeta)==0
# b=beta: R1 forces a=beta or c=beta.
r1_bbeta=s.factor(s.together(rels[0].subs({b:beta,h:hstar.subs(b,beta)})))
expected_bbeta=-(q-1)*(q+1)*(q**2+1)*(a*q**2+(q**2-1)**2)*(c*q**2+(q**2-1)**2)/q**6
assert s.factor(r1_bbeta-expected_bbeta)==0
# a=b=beta and b=c=beta branches of cubic.
cubic_abeta=s.factor(s.together(rels[-1].subs({a:beta,b:beta,h:hstar.subs({a:beta,b:beta})})))
expected_abeta=-c*(q-1)**2*(q+1)**2*(q**2-q+1)*(q**2+q+1)*(c*q**4+(q**4-1)**2)/(q**8*(q**2+1)**2)
assert s.factor(cubic_abeta-expected_abeta)==0
cubic_cbeta=s.factor(s.together(rels[-1].subs({b:beta,c:beta,h:hstar.subs({b:beta,c:beta})})))
expected_cbeta=-a*(q-1)**2*(q+1)**2*(q**2-q+1)*(q**2+q+1)*(a*q**4+(q**4-1)**2)/(q**8*(q**2+1)**2)
assert s.factor(cubic_cbeta-expected_cbeta)==0
print('VERIFY_OK candidates=10 scalar_relations=7 completeness_branches=6')
