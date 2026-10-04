# Exact incidence check for the sixteen (-1)-curves on dP4.
from itertools import combinations

# A class is d H - sum m_i E_i, with E_i represented by m_i=-1.
def inter(a,b):
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))

curves=[]
for i in range(5):
    v=[0]+[0]*5; v[i+1]=-1
    curves.append((f"E{i+1}",tuple(v)))
for i,j in combinations(range(5),2):
    v=[1]+[0]*5; v[i+1]=1; v[j+1]=1
    curves.append((f"L{i+1}{j+1}",tuple(v)))
curves.append(("Q",(2,1,1,1,1,1)))
assert len(curves)==16
assert all(inter(v,v)==-1 for _,v in curves)

edges=[]
for i,j in combinations(range(16),2):
    z=inter(curves[i][1],curves[j][1])
    assert z in (0,1), (curves[i][0],curves[j][0],z)
    if z==1: edges.append((i,j))

deg=[0]*16
for i,j in edges: deg[i]+=1; deg[j]+=1
assert deg==[5]*16
assert len(edges)==40
E=set(edges)
def adj(i,j): return (min(i,j),max(i,j)) in E
tri=[]
for i,j,k in combinations(range(16),3):
    if adj(i,j) and adj(i,k) and adj(j,k): tri.append((i,j,k))
assert tri==[]

chi_W=16*2-len(edges)
chi_X=3+5
chi_Y=chi_X-chi_W
b0,b1=1,10
b2=chi_Y-b0+b1
assert (chi_W,chi_X,chi_Y,b2)==(-8,8,16,25)

print("curve_count=16")
print("incidence_degree=5")
print("pair_intersections=40")
print("triangle_count=0")
print(f"chi_W={chi_W}")
print(f"chi_X={chi_X}")
print(f"chi_Y={chi_Y}")
print(f"b2={b2}")
print("VERIFY_OK")
