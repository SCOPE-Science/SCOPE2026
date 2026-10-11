import sympy as S
u,v,y,z,Y=S.symbols('u v y z Y', real=True); L=S.Symbol('L')
g,A,b,k,h,p,c,d=S.symbols('g A b k h p c d', positive=True)
ss=d/c; aa=A/(1+k*y); G=g/(1+k*y)-h-p*y
F=S.Matrix([u*(G-aa*u-b*v),v*(G-aa*v-b*u),y*(c*(u+v)-d)])
J=F.jacobian((u,v,y)); yc=(A/b-1)/k; gc=(1+k*yc)*(h+p*yc+b*ss)
subsline={u:z,v:ss-z,y:yc,g:gc}
assert all(S.simplify(x.subs(subsline, simultaneous=True))==0 for x in F)
JL=S.simplify(J.subs(subsline, simultaneous=True))
w=2*z/ss-1
Dline=p+k*(gc-A*ss*(1+w*w)/2)/(1+k*yc)**2
linepoly=L*(L**2+b*ss*L+c*yc*ss*Dline)
assert S.simplify(JL.charpoly(L).as_expr()-linepoly)==0
# symmetric equilibria
Gsym=(1+k*Y)*(h+p*Y+b*ss/2)+A*ss/2
sym={u:ss/2,v:ss/2,y:Y,g:Gsym}
JS=S.simplify(J.subs(sym,simultaneous=True))
q=(A/(1+k*Y)+b)/2
Dsym=p+k*(Gsym-A*ss/2)/(1+k*Y)**2
lam_sym=(b-A/(1+k*Y))*ss/2
sympoly=(L-lam_sym)*(L**2+q*ss*L+c*Y*ss*Dsym)
assert S.simplify(JS.charpoly(L).as_expr()-sympoly)==0
# boundary predator-positive equilibria
Gb=A*ss+(1+k*Y)*(h+p*Y)
Jb=S.simplify(J.subs({u:ss,v:0,y:Y,g:Gb},simultaneous=True))
Db=p+k*(Gb-A*ss)/(1+k*Y)**2
lam_inv=(A/(1+k*Y)-b)*ss
bpoly=(L-lam_inv)*(L**2+A*ss/(1+k*Y)*L+c*Y*ss*Db)
assert S.simplify(Jb.charpoly(L).as_expr()-bpoly)==0
assert S.simplify(gc- (h+A*ss) - ((A/b-1)*h + (A/b)*p*yc))==0
# exactly rational example
qsubs={A:S.Integer(2),b:1,k:1,h:1,p:1,c:1,d:1}
assert S.simplify(gc.subs(qsubs)-6)==0
assert S.simplify(linepoly.subs({**qsubs,z:S.Rational(1,2)}) - L*(L**2+L+S.Rational(9,4)))==0
# critical exchange eigenvalue derivative
deriv =ss*A*k/(2*(1+k*yc)*(k*(gc-A*ss/2)+p*(1+k*yc)**2))
assert S.simplify(deriv.subs(qsubs)-S.Rational(1,18))==0
print('CHECK_OK: line, all three Jacobian factorizations, thresholds, sample and crossing')
