#!/usr/bin/env python3
from math import isclose

def elementary(a):
    a1,a2,a3,a4=a
    e1=sum(a)
    e2=a1*a2+a1*a3+a1*a4+a2*a3+a2*a4+a3*a4
    e3=a1*a2*a3+a1*a2*a4+a1*a3*a4+a2*a3*a4
    e4=a1*a2*a3*a4
    return e1,e2,e3,e4

tests=[
 (0.161,0.056,0.404,0.021,0.352,0.039,0.08,1.2),
 (1.2,0.4,0.8,0.3,1.1,0.7,0.5,2.0),
 (0.03,0.07,0.11,0.13,0.17,0.19,0.23,12.0),
 (2.0,3.0,5.0,7.0,11.0,13.0,17.0,1.0001),
 (0.7,1.4,0.9,2.2,1.8,0.6,1.3,100.0),
]
for gE,muE,gL,muL,gN,muN,a4,R in tests:
    a1,a2,a3=gE+muE,gL+muL,gN+muN
    e1,e2,e3,e4=elementary((a1,a2,a3,a4))
    t=(R-1.0)/R
    D=gL*gN+a4*(a3+gL)
    b=t*e4/(gE*D)
    B=b*gE
    c=a3+a4+gL
    eta1,eta2,eta3,eta4=e1,e2+B,e3+B*c,B*D
    assert isclose(eta4,t*e4,rel_tol=1e-12,abs_tol=1e-14)
    direct=eta1*eta2*eta3-eta3*eta3-eta1*eta1*eta4
    base=e1*e2*e3-e3*e3-e1*e1*e4
    expanded=(base+e1*e1*(1-t)*e4
              +B*(c*(e1*e2-2*e3)+e1*e3)
              +B*B*c*(e1-c))
    assert base>0 and e1*e2>3*e3 and e1-c>0
    assert isclose(e1-c,a1+muL,rel_tol=1e-12,abs_tol=1e-14)
    assert direct>0 and expanded>0
    assert isclose(direct,expanded,rel_tol=1e-11,abs_tol=1e-12)
print("VERIFY_OK")
