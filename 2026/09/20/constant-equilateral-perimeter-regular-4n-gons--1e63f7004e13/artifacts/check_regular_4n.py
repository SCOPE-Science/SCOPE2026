from math import cos, sin, pi, sqrt

def vertices(N):
    th = 2*pi/N
    return [(cos(j*th), sin(j*th)) for j in range(N)]

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def sub(a,b): return (a[0]-b[0], a[1]-b[1])
def scale(c,a): return (c*a[0], c*a[1])
def lerp(a,b,t): return add(scale(1-t,a), scale(t,b))

def gauge(w,N):
    """Gauge of the regular N-gon with circumradius one."""
    th = 2*pi/N
    den = cos(th/2)
    return max((w[0]*cos((j+0.5)*th)+w[1]*sin((j+0.5)*th))/den
               for j in range(N))

def triangle(N,t):
    V=vertices(N)
    th=2*pi/N
    r=N%12
    x=lerp(V[0],V[1],t)
    if r==4:
        m=(N-4)//12
        k=4*m+1
        s=sin((m+1)*th)/sin(m*th)
        tau=1/(s+2)
        if t <= tau:
            y=lerp(V[k],V[k+1],tau+s*t)
            j=N-k-1
            z=lerp(V[j],V[j+1],1-tau+t)
        else:
            y=lerp(V[k],V[k+1],1-tau+(t-tau)/s)
            j=N-k
            z=lerp(V[j],V[j+1],(t-tau)/s)
        return x,y,z
    if r==8:
        m=(N-8)//12
        k=4*m+2
        s=sin(m*th)/sin((m+1)*th)
        tau=1/(s+2)
        if t <= tau:
            y=lerp(V[k],V[k+1],1-tau+t)
            j=N-k-1
            z=lerp(V[j],V[j+1],tau+s*t)
        else:
            y=lerp(V[k+1],V[k+2],(t-tau)/s)
            j=N-k-1
            z=lerp(V[j],V[j+1],1-tau+(t-tau)/s)
        return x,y,z
    raise ValueError("This script checks N congruent to 4 or 8 modulo 12, with N>8.")

def check(N, samples=501):
    vals=[]
    side_gap=0.0
    for i in range(samples):
        t=0.5*i/(samples-1)
        x,y,z=triangle(N,t)
        ds=[gauge(sub(x,y),N), gauge(sub(x,z),N), gauge(sub(y,z),N)]
        side_gap=max(side_gap,max(ds)-min(ds))
        vals.append(sum(ds)/3)
    return min(vals), max(vals), side_gap

if __name__=="__main__":
    Ns=[16,20,28,32,40,44,52,56,64,68,76,80,100]
    for N in Ns:
        lo,hi,gap=check(N)
        print(f"N={N:3d} side={0.5*(lo+hi):.15f} "
              f"perimeter={1.5*(lo+hi):.15f} "
              f"side_gap={gap:.3e} span={hi-lo:.3e}")
