from itertools import product

def calc(p):
  n=4
  def symp(u,w): return (u[0]*w[2]+u[1]*w[3]-u[2]*w[0]-u[3]*w[1])%p
  def norm(v):
    v=tuple(x%p for x in v)
    neg=tuple((-x)%p for x in v)
    return min(v,neg)
  zero=(0,)*4
  V=sorted({norm(v) for v in product(range(p),repeat=4) if v!=zero})
  fixedv=(1,0,0,0)
  def T(w):return tuple((w[i]+symp(w,fixedv)*fixedv[i])%p for i in range(4))
  def wedge(u,w):return tuple((u[i]*w[j]-u[j]*w[i])%p for i in range(4) for j in range(i+1,4))
  surfaces={}
  for i,u in enumerate(V):
    for w in V[i+1:]:
      if symp(u,w):continue
      v_w=wedge(u,w)
      if not any(v_w): continue
      key=norm(v_w)
      if key not in surfaces: surfaces[key]=(u,w)
  c1=(p*p-1)//2; pi=(p**4-1)//2
  assert len(V)==pi and len(surfaces)==pi,(p,len(V),len(surfaces),pi)
  fixed_V=sum(norm(T(u))==u for u in V)
  fixed_P=0; fixed_flags=0; fixed_surfaces=[]
  for key,(u,w) in surfaces.items():
    moved=norm(wedge(T(u),T(w)))
    if moved==key:
      fixed_P+=1
      fixed_surfaces.append(key)
      P={norm(tuple((a*u[k]+b*w[k])%p for k in range(4))) for a in range(p) for b in range(p) if (a,b)!=(0,0)}
      assert len(P)==c1
      assert all(norm(T(x))==x for x in P)
      fixed_flags+=len(P)
  assert fixed_V==(p**3-1)//2
  assert fixed_P==c1
  assert fixed_flags==c1*c1
  h=1+(p-6)*(p*p-1)//24
  assert h==1+(p-6)*(p*p-1)/24
  beta=pi*(c1-2)+1
  dim2=beta+2*h*pi
  trace2=1-fixed_V-fixed_P+fixed_flags+2*h*fixed_P
  dim3=pi;trace3=fixed_P
  m2=(dim2-trace2)//p;a2=(dim2+(p-1)*trace2)//p
  m3=(dim3-trace3)//p;a3=(dim3+(p-1)*trace3)//p
  assert (dim2-trace2)%p==0 and (dim3-trace3)%p==0
  assert a2+(p-1)*m2==dim2 and a3+(p-1)*m3==dim3
  print({'p':p,'vertices':len(V),'surfaces':len(surfaces),'fixed_vertices':fixed_V,'fixed_surfaces':fixed_P,'fixed_incidence':fixed_flags,'genus':h,'dim_Hc2':dim2,'dim_Hc3':dim3,'trace_Hc2':trace2,'trace_Hc3':trace3,'C_p_trivial_Hc2':a2,'C_p_cyclotomic_Hc2':m2,'C_p_trivial_Hc3':a3,'C_p_cyclotomic_Hc3':m3})
for p in (3,5,7):calc(p)
print('VERIFY_OK')
