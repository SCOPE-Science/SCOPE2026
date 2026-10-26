import sympy as s
T,Z=s.symbols('t z')
a,b,c,d,e,f=s.symbols('a b c d e f')
P=a*T**2+b*T+c; Q=d*T**2+e*T+f
A=(P**2-27*Q**2)/4; B=A*Q
j=s.cancel(1728*4*A**3/(4*A**3+27*B**2))
assert s.simplify(j-1728*(1-27*(Q/P)**2))==0
D=s.expand(s.discriminant(Q-Z*P,T))
assert s.expand(D-(b*b-4*a*c)*Z**2 -(-2*b*e+4*(d*c+a*f))*Z -(e*e-4*d*f))==0
specialP=T**2+1; specialQ=T**2-1
spJ=s.cancel(j.subs({a:1,b:0,c:1,d:1,e:0,f:-1}))
assert s.simplify(spJ-spJ.subs(T,-T))==0
assert s.simplify(spJ-spJ.subs(T,1/T))==0
assert s.degree(s.together(spJ).as_numer_denom()[0],T)==4
for name,PP,QQ in [('special',specialP,specialQ),('generic',T**2+1,T**2+T+2)]:
 AA=s.expand(PP**2-27*QQ**2)
 assert s.discriminant(AA,T)!=0
 assert s.discriminant(PP,T)!=0
 assert s.discriminant(QQ,T)!=0
 assert s.resultant(PP,QQ,T)!=0
 cc=s.expand(s.discriminant(QQ-Z*PP,T))
 print(name,'critical-value-discriminant',cc,'linear coeff',cc.coeff(Z,1))
 print('  j-map',s.factor(1728*(PP**2-27*QQ**2)/PP**2))
print('VERIFY_OK: invariant j formula, discriminant polarization and explicit V4 symmetries')
