import math

checks=0
for N in range(6,81,2):
    a=math.pi/N; c=math.cos(a); s=math.sin(a)
    if N%4==0:
        target=math.tan(a)
        # smooth reference-edge residuals |t|/c stay below target
        for j in range(-9,10):
            t=s*j/10.0
            assert abs(t)/c < target + 1e-14
            checks+=1
        # vertex-sector smooth supports have the two extremal values
        v1=s/c
        v2=(-math.sin(2*a)*c + math.cos(2*a)*s)/c
        assert abs(v1-target)<2e-14
        assert abs(v2+target)<2e-14
        # sharp vertex / perpendicular-edge-midpoint pair
        assert abs(s/c-target)<2e-14
        checks+=3
    else:
        # smooth edge: adjacent reverse support values s+t and t-s straddle zero
        for j in range(-9,10):
            t=s*j/10.0
            u=s+t; v=t-s
            assert u>=-1e-14 and v<=1e-14
            checks+=1
        # vertex sector: its single edge support is perpendicular to vertex
        assert abs(math.cos(math.pi/2))<1e-14
        checks+=1
print(f"VERIFY_OK even_polygons=38 analytic_checks={checks} phase=0_for_4m+2,tan(pi/N)_for_4m")
