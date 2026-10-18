import sympy as S,json
x,y=S.symbols('x y')
rows=json.load(open('pencil_census.json'))['orbits']
for row in rows:
  a,b,_=row['rep']; data=[]
  for i in (0,1):
    for j in (0,1):
      mon=[x**(2-e if i else e)*y**(2-f if j else f) for e in range(3) for f in range(3)]
      def F(m):return S.Add(*(mon[k] for k in range(9) if m>>k&1))
      f,g=F(a),F(b); jac=S.expand(S.diff(f,x)*S.diff(g,y)-S.diff(f,y)*S.diff(g,x))
      B=S.groebner([f,g,jac],x,y,modulus=2)
      data.append(len(B.polys)==1 and B.polys[0].as_expr()==1)
  assert all(data),(a,b,data)
  F=lambda m:S.Add(*(x**e*y**f for e in range(3) for f in range(3) if m>>(e*3+f)&1))
  resultant=S.Poly(S.resultant(F(a),F(b),y),x,modulus=2)
  print(a,b,row['size'],'transverse',data,'resultant_y',resultant.as_expr(),'factors',S.factor_list(resultant,modulus=2)[1])
print('ALL 13 REPRESENTATIVE PAIRS GEOMETRICALLY TRANSVERSE')
