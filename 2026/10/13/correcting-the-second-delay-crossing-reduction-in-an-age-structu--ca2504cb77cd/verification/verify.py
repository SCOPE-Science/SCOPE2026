#!/usr/bin/env python3
import cmath, math
A=0.4006; B=-0.3195; C=0.3595; D=-0.9
L=2.1616; H=-0.3262; Q=0.3624; w=1.4
K=w**4+(A*A-2*B-D*D+Q*Q)*w*w+B*B+L*L-C*C-H*H
U=(L-A*Q)*w*w+H*C-B*L
V=-Q*w**3+(B*Q-A*L+D*H)*w
Kp=w**4+(A*A-2*B+D*D-Q*Q)*w*w+B*B+L*L-C*C-H*H
Vp=Q*w**3-(B*Q+A*L)*w-D*H
a=(B-w*w)+1j*A*w
b=L+1j*Q*w
c=C+1j*D*w
for theta in (0.17,0.7,1.9,3.2):
    direct=abs(a+b*cmath.exp(-1j*theta))**2-abs(c+H*cmath.exp(-1j*theta))**2
    corrected=K-2*U*math.cos(theta)+2*V*math.sin(theta)
    assert abs(direct-corrected)<1e-11
ratio=K/(2*math.hypot(U,V))
ratio_print=Kp/(2*math.hypot(U,Vp))
assert abs(ratio-0.873811900596866)<1e-12
assert ratio<1.0 and ratio_print>1.0
phi=math.atan2(V,U)
assert abs(U-math.hypot(U,V)*math.cos(phi))<1e-12
assert abs(V-math.hypot(U,V)*math.sin(phi))<1e-12
print("VERIFY_OK")
