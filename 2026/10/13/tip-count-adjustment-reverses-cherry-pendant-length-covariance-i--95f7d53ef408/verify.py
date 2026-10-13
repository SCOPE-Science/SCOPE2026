#!/usr/bin/env python3
import math

# Dimensionless time tau=lambda*t and r=exp(tau).
def moments(tau):
    r=math.exp(tau)
    log_r=tau
    EN=r
    EN2=2*r*r-r
    EC=(r-r**-2)/3
    ENC=(2*r*r-r-2*r**-2+r**-1)/3
    EC2=((r-1)*(10*r**5+7*r**4+7*r**3+17*r**2+2*r+2))/(45*r**4)
    EL=(r-r**-1)/2
    EH=2*(r**3-3*log_r-1)/(9*r**2)
    ENL=r*r-1.5*r+1-0.5/r
    EJ=(r*r-2*log_r-1)/(2*r)
    EL2=(3*r**4-5*r**3+6*r*r-6*r*log_r-3*r-1)/(6*r*r)
    ECL=(12*r**5-19*r**4+12*r**3+6*r*r-24*r*log_r-8*r-3)/(36*r**3)
    return (EN,EN2,EC,ENC,EC2,EL,EH,ENL,EJ,EL2,ECL)

def rhs(vals):
    EN,EN2,EC,ENC,EC2,EL,EH,ENL,EJ,EL2,ECL=vals
    return (
        EN,
        2*EN2+EN,
        EN-2*EC,
        EN2-ENC+EN-2*EC,
        2*ENC+EN-4*EC2-2*EC,
        EN-EL,
        2*EC-2*EH,
        EN2-EL,
        2*EL-EJ,
        2*ENL-2*EL2+EJ,
        ENC+ENL-3*ECL-EL+EH,
    )

def derivative_component(tau,k,h=2e-6):
    # Five-point central derivative.
    fm2=moments(tau-2*h)[k]
    fm1=moments(tau-h)[k]
    fp1=moments(tau+h)[k]
    fp2=moments(tau+2*h)[k]
    return (fm2-8*fm1+8*fp1-fp2)/(12*h)

max_res=0.0
checks=0
for tau in (0.05,0.1,0.25,0.5,1.0,1.5,2.0,3.0,4.0):
    vals=moments(tau)
    want=rhs(vals)
    for k in range(len(vals)):
        got=derivative_component(tau,k)
        scale=max(1.0,abs(want[k]))
        res=abs(got-want[k])/scale
        max_res=max(max_res,res)
        checks+=1

sign_checks=0
for j in range(1,10001):
    tau=8*j/10000
    r=math.exp(tau)
    g=r**4-6*r*r+24*r*math.log(r)-4*r+9
    F=6*r**5-19*r**4+18*r**3+12*r*r-24*r*math.log(r)-8*r-9
    var_u=(r-1)*(2*r**4+2*r**3+2*r*r+7*r+7)/(45*r**4)
    var_v=(5*r**3-12*r*math.log(r)-5)/(12*r*r)
    cov_uv=-g/(36*r**3)
    cov_cp=F/(36*r**3)
    assert g>0 and F>0 and var_u>0 and var_v>0 and cov_uv<0 and cov_cp>0
    sign_checks+=1

# Correlation tends to -sqrt(6)/12.
tau=16.0
r=math.exp(tau)
g=r**4-6*r*r+24*r*math.log(r)-4*r+9
cov_uv=-g/(36*r**3)
var_u=(r-1)*(2*r**4+2*r**3+2*r*r+7*r+7)/(45*r**4)
var_v=(5*r**3-12*r*math.log(r)-5)/(12*r*r)
corr=cov_uv/math.sqrt(var_u*var_v)
target=-math.sqrt(6)/12
assert abs(corr-target)<2e-6
assert max_res < 2e-7, max_res
print(f"ODE checks: {checks}; sign checks: {sign_checks}; max relative ODE residual: {max_res:.3e}")
print(f"tau=16 residual correlation: {corr:.12f}; limit: {target:.12f}")
