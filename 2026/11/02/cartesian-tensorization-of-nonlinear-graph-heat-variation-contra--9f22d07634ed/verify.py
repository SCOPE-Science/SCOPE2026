"""Exact finite sanity checks for Cartesian nonlinear diffusion and edge variation.

Run: python verify_cartesian_bv.py
Only finite tests are performed; the universal statements require the proof.
"""
from itertools import product

def path(n): return n, [(i,i+1,1) for i in range(n-1)]
def clique(n): return n, [(i,j,1) for i in range(n) for j in range(i+1,n)]
def star(leaves): return leaves+1, [(0,j,1) for j in range(1,leaves+1)]
def cycle(n): return n, [(i,(i+1)%n,1) for i in range(n)]

def axes(factors):
    sizes=[n for n,_ in factors]
    vertices=list(product(*(range(n) for n in sizes)))
    index={v:i for i,v in enumerate(vertices)}
    directions=[]
    for dim,(n,es) in enumerate(factors):
        links=[]
        for v in vertices:
            for a,b,c in es:
                if v[dim]==a:
                    other=list(v);other[dim]=b
                    links.append((index[v],index[tuple(other)],c))
        directions.append(links)
    return len(vertices),directions,index

def flux(v,p): return v*abs(v)**(p-2)
def directional(u,edges,p):
    velocity=[0]*len(u)
    for a,b,c in edges:
        z=c*flux(u[b]-u[a],p)
        velocity[a]+=z;velocity[b]-=z
    return velocity

def upper_var_derivative(u,velocity,edges):
    result=0
    for a,b,c in edges:
        gap=u[b]-u[a]; speed=velocity[b]-velocity[a]
        result += (abs(speed) if gap==0 else (speed if gap>0 else -speed))
    return result

def check(factors,p):
    n,dirs,_=axes(factors)
    checked=0
    for u in product((0,1,2),repeat=n):
        vel=[directional(u,edges,p) for edges in dirs]
        for i,edges in enumerate(dirs):
            for j,v in enumerate(vel):
                z=upper_var_derivative(u,v,edges)
                assert z<=0,(factors,p,u,i,j,z)
                checked+=1
    return checked

def witness():
    factors=[star(4),clique(2)]
    n,dirs,index=axes(factors)
    u=[int(v[0]==1) for v in index]
    velocities=[directional(u,edges,3) for edges in dirs]
    globalv=[sum(v[k] for v in velocities) for k in range(n)]
    rate=sum(upper_var_derivative(u,globalv,edges) for edges in dirs)
    assert rate==2,(rate,u)
    return rate

if __name__=='__main__':
    N=0
    for factors in ([path(3),clique(3)], [cycle(4),path(2)], [star(3),path(2)]):
        for p in (2,3,4):
            count=check(factors,p)
            N+=count
            print('PASS',[(n,len(e)) for n,e in factors],'p=',p,'exact derivatives=',count)
    print('PASS lifted four-leaf star variation growth =',witness())
    print('TOTAL_PASS',N)
