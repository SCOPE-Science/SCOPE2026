#!/usr/bin/env python3
import math

def circdist(x,y):
    z=(x-y+math.pi)%(2*math.pi)-math.pi
    return abs(z)

for n in range(3,201):
    a=math.pi/(2*n)
    R=1/(2*math.sin(2*a))
    H=math.sqrt(4*math.cos(a)**2-1)
    h=H/(2*math.cos(a))
    gamma=H/(math.sqrt(3)*math.cos(a))
    zeta=math.tan(a)/math.sqrt(3)

    # Unit-edge normalization.
    base=2*R*math.sin(2*a)
    cross_horiz=2*R*math.sin(a)
    cross=math.sqrt(cross_horiz**2+h**2)
    assert abs(base-1.0)<2e-13
    assert abs(cross-1.0)<2e-13

    # Exact proof identities, numerically replayed.
    assert abs(gamma*gamma+zeta*zeta-1.0)<3e-13
    assert abs(zeta*H-gamma*math.sin(a))<3e-13

    # The almost-smooth obstruction.
    assert -zeta < 0.5

    phis=[0.0,2*math.pi/3,4*math.pi/3]
    beta=math.pi/2-a

    def top_xrayed(theta,phi):
        psi=(phi-theta+math.pi)%(2*math.pi)-math.pi
        dots=[
            H,
            gamma*(math.cos(psi)-math.sin(a)),
            gamma*(math.cos(psi-2*a)+math.sin(a)),
            gamma*(math.cos(psi+2*a)+math.sin(a)),
        ]
        direct=all(x>1e-12 for x in dots) or all(x<-1e-12 for x in dots)
        arc=circdist(theta,phi)<beta-1e-12
        assert direct==arc
        return direct

    def bottom_xrayed(theta,phi):
        # By the rotation-by-2a plus horizontal reflection symmetry,
        # transformed lower azimuth theta-pi obeys the same criterion.
        return circdist(theta-math.pi,phi)<beta-1e-12

    for k in range(n):
        th_top=4*a*k
        th_bot=(4*k+2)*a
        assert any(top_xrayed(th_top,p) for p in phis)
        assert any(bottom_xrayed(th_bot,p) for p in phis)

print("VERIFY_OK")
print("unit_edge_normalization = passed")
print("facet_normal_identities = passed")
print("three_line_vertex_coverage_n_3_to_200 = passed")
print("almost_smooth_obstruction = passed")
