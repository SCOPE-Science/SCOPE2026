import math

def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly)))/2.0)

def clip_half(poly, sign, level):
    # Keep sign*y <= level.
    out=[]
    for i,a in enumerate(poly):
        b=poly[(i+1)%len(poly)]
        fa=sign*a[1]-level
        fb=sign*b[1]-level
        ina=fa <= 1e-13
        inb=fb <= 1e-13
        if ina:
            out.append(a)
        if ina != inb:
            t=fa/(fa-fb)
            out.append((a[0]+t*(b[0]-a[0]), a[1]+t*(b[1]-a[1])))
    return out

def strip(poly, s):
    return clip_half(clip_half(poly,1.0,s),-1.0,s)

vals=[]
for n in range(3,102,2):
    a=math.pi/n
    poly=[(math.cos((2*j+1)*a),math.sin((2*j+1)*a)) for j in range(n)]
    A=area(poly)
    U=area(strip(poly,math.sin(a)))
    measured=2*n*U/A
    closed=8-2*(1/math.cos(a)-1)**2
    assert abs(measured-closed) < 3e-11, (n,measured,closed)
    vals.append(closed)
assert all(vals[i+1] > vals[i] for i in range(len(vals)-1))
assert abs(vals[0]-6.0) < 1e-12
print('VERIFY_OK')
for n in (3,5,7,9,11,51,101):
    a=math.pi/n
    print(n, 8-2*(1/math.cos(a)-1)**2)
