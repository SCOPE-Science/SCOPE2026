#!/usr/bin/env python3
import math

def vertices(n,R=1.0):
    return [(R*math.cos(2*math.pi*j/n),R*math.sin(2*math.pi*j/n)) for j in range(n)]

def support_width(verts,theta):
    nx,ny=math.cos(theta),math.sin(theta)
    vals=[nx*x+ny*y for x,y in verts]
    return max(vals)-min(vals)

def edge_direction(verts,j):
    x1,y1=verts[j]
    x2,y2=verts[(j+1)%len(verts)]
    return math.atan2(y2-y1,x2-x1)

def angle_sine(a,b):
    return abs(math.sin(a-b))

def formula(n,R=1.0):
    if n%2:
        return 4*R*R*math.cos(math.pi/(2*n))**3
    if n%4==0:
        return 4*R*R*math.cos(math.pi/n)**2
    return 4*R*R*math.cos(math.pi/n)

worst=0.0
for n in range(3,301):
    R=1.0
    V=vertices(n,R)
    dirs=[edge_direction(V,j) for j in range(n)]
    widths=[]
    for d in dirs:
        widths.append(support_width(V,d+math.pi/2))

    # Regularity forces all side-normal widths to agree.
    assert max(widths)-min(widths) < 5e-12, (n,max(widths)-min(widths))

    best=float("inf")
    maxsin=0.0
    for i in range(n):
        for j in range(i+1,n):
            s=angle_sine(dirs[i],dirs[j])
            if s < 1e-12:
                continue
            maxsin=max(maxsin,s)
            a=widths[i]*widths[j]/s
            best=min(best,a)

    target=formula(n,R)
    err=abs(best-target)
    worst=max(worst,err)
    assert err < 3e-10, (n,best,target,err)

    if n%4==0:
        s_target=1.0
    elif n%2==0:
        s_target=math.cos(math.pi/n)
    else:
        s_target=math.cos(math.pi/(2*n))
    assert abs(maxsin-s_target)<3e-12,(n,maxsin,s_target)

# Named low-dimensional checks.
assert abs(formula(3)-3*math.sqrt(3)/2)<1e-14
assert abs(formula(4)-2.0)<1e-14
assert abs(formula(6)-2*math.sqrt(3))<1e-14

print("VERIFY_OK")
print("regular_side_counts = 3..300")
print("max_formula_error = %.3e" % worst)
print("edge_direction_sine_maxima = passed")
print("support_width_reconstruction = passed")
