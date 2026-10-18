import math,itertools
TOL=2e-11
count=0
for m in (1,2,3,4,6):
 N=4*m; beta=math.pi/N; t=math.tan(beta)
 V=[(math.cos(2*math.pi*j/N), math.sin(2*math.pi*j/N)) for j in range(N)]
 G=[(math.cos((2*j+1)*math.pi/N)/math.cos(beta), math.sin((2*j+1)*math.pi/N)/math.cos(beta)) for j in range(N)]
 def norms(M):
  vals=[]
  for x,y in V:
   tx=M[0]*x+M[1]*y;ty=M[2]*x+M[3]*y
   vals.append([abs(gx*tx+gy*ty) for gx,gy in G])
  op=max(map(max,vals)); nr=max(max(vals[j][(j-1)%N],vals[j][j]) for j in range(N));return op,nr
 oj,nj=norms((0,-1,1,0)); assert abs(oj-1)<TOL and abs(nj-t)<TOL
 for a,b,c,d in itertools.product(range(-2,3), repeat=4):
  op,nr=norms((a,b,c,d)); assert nr+TOL*(op+1)>=t*op,(m,a,b,c,d,op,nr,t)
  count+=1
 print(m,t,1/math.cos(beta),round(math.sqrt((1/math.cos(beta))**2-1),15))
print('CHECK_OK',count)
