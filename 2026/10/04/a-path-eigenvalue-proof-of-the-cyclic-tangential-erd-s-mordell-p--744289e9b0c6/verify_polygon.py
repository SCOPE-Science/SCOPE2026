import math, random

rng = random.Random(210031)
max_main_violation = 0.0
max_vertex_formula_error = 0.0
max_path_violation = 0.0
max_regular_error = 0.0
checks = 0

def dot(a,b): return a[0]*b[0]+a[1]*b[1]

for n in range(3, 16):
    c = math.cos(math.pi/n)
    sec = 1.0/c
    # Random cyclic polygons, including occasional very large consecutive arcs.
    for trial in range(160):
        raw = [rng.expovariate(1.0) for _ in range(n)]
        total = sum(raw)
        gaps = [2*math.pi*x/total for x in raw]
        # Avoid essentially antipodal adjacent vertices, where tangent intersections are at infinity.
        if any(abs(g-math.pi) < 1e-9 for g in gaps):
            continue
        theta=[0.0]
        for g in gaps[:-1]: theta.append(theta[-1]+g)
        V=[(math.cos(t),math.sin(t)) for t in theta]
        # interior convex combination
        w=[rng.expovariate(1.0) for _ in range(n)]
        sw=sum(w); w=[x/sw for x in w]
        P=(sum(w[i]*V[i][0] for i in range(n)), sum(w[i]*V[i][1] for i in range(n)))
        sumD=0.0; sumd=0.0
        for i in range(n):
            j=(i+1)%n
            t1=theta[i]
            t2=(theta[j] if j else 2*math.pi)
            a=(t2-t1)/2.0
            phi=(t1+t2)/2.0
            u=(math.cos(phi),math.sin(phi))
            d=math.cos(a)-dot(u,P)
            D=1.0-dot(V[i],P)
            if d < -2e-12 or D < -2e-12:
                raise AssertionError((n,trial,'negative distance',d,D,gaps))
            sumd += d; sumD += D
        viol=sec*sumd-sumD
        max_main_violation=max(max_main_violation,viol)
        if viol > 3e-11:
            raise AssertionError((n,trial,'main inequality',viol))
        checks += 1

        # At vertex 0 compare geometric sums to the path reduction.
        P0=V[0]
        geomD=0.0; geomd=0.0
        x=[0.0]
        acc=0.0
        for g in gaps:
            acc += g/2.0
            x.append(acc)
        for i in range(n):
            j=(i+1)%n
            t1=theta[i]; t2=(theta[j] if j else 2*math.pi)
            a=(t2-t1)/2.0; phi=(t1+t2)/2.0
            u=(math.cos(phi),math.sin(phi))
            geomd += math.cos(a)-dot(u,P0)
            geomD += 1.0-dot(V[i],P0)
        y=[math.sin(xx) for xx in x]
        pathD=2*sum(y[j]*y[j] for j in range(1,n))
        pathd=2*sum(y[j]*y[j+1] for j in range(n))
        err=max(abs(geomD-pathD),abs(geomd-pathd))
        max_vertex_formula_error=max(max_vertex_formula_error,err)
        if err > 3e-11: raise AssertionError((n,trial,'vertex reduction',err))
        pv=sum(y[j]*y[j+1] for j in range(n))-c*sum(y[j]*y[j] for j in range(1,n))
        max_path_violation=max(max_path_violation,pv)
        if pv > 3e-11: raise AssertionError((n,trial,'path inequality',pv))
        checks += 2

    # Regular polygon: equality for random interior P.
    theta=[2*math.pi*i/n for i in range(n)]
    V=[(math.cos(t),math.sin(t)) for t in theta]
    for trial in range(60):
        w=[rng.expovariate(1.0) for _ in range(n)]
        sw=sum(w); w=[x/sw for x in w]
        P=(sum(w[i]*V[i][0] for i in range(n)),sum(w[i]*V[i][1] for i in range(n)))
        sumD=sum(1-dot(V[i],P) for i in range(n))
        sumd=0.0
        for i in range(n):
            j=(i+1)%n
            t1=theta[i]; t2=(theta[j] if j else 2*math.pi)
            a=(t2-t1)/2; phi=(t1+t2)/2
            u=(math.cos(phi),math.sin(phi))
            sumd += math.cos(a)-dot(u,P)
        err=abs(sumD-sec*sumd)
        max_regular_error=max(max_regular_error,err)
        if err > 3e-11: raise AssertionError((n,trial,'regular equality',err))
        checks += 1

print('VERIFY_OK')
print('checks', checks)
print('max_main_violation', format(max_main_violation,'.3e'))
print('max_vertex_formula_error', format(max_vertex_formula_error,'.3e'))
print('max_path_violation', format(max_path_violation,'.3e'))
print('max_regular_error', format(max_regular_error,'.3e'))
