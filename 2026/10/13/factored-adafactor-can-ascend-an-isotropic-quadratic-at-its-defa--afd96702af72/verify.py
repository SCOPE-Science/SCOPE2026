from decimal import Decimal, getcontext

getcontext().prec = 80

def factored_step(e, eps2, rho, B):
    e=Decimal(e); eps2=Decimal(eps2); rho=Decimal(rho); B=Decimal(B)
    S=B*B+Decimal(6)*e
    u1=(Decimal(2)*S).sqrt()/(Decimal(4)*e.sqrt())
    u2=B*S.sqrt()/(B*B+Decimal(2)*e)
    rms=(u1*u1+u2*u2).sqrt()/Decimal(2)
    scale=max(Decimal(1),rms)
    h1=u1/scale; h2=u2/scale
    prms=((B*B+Decimal(2)*e)/Decimal(4)).sqrt()
    alpha=rho*max(eps2,prms)
    y1=(Decimal(2)*e).sqrt()-alpha*h1
    y2=B-alpha*h2
    f0=(B*B+Decimal(2)*e)/Decimal(2)
    f1=(y1*y1+y2*y2)/Decimal(2)
    return f1/f0, rms, h1, h2

def full_step(e, eps2, rho, B):
    e=Decimal(e); eps2=Decimal(eps2); rho=Decimal(rho); B=Decimal(B)
    u1=(Decimal(2)/Decimal(3)).sqrt()
    u2=B/(B*B+e).sqrt()
    rms=(u1*u1+u2*u2).sqrt()/Decimal(2)
    scale=max(Decimal(1),rms)
    h1=u1/scale; h2=u2/scale
    prms=((B*B+Decimal(2)*e)/Decimal(4)).sqrt()
    alpha=rho*max(eps2,prms)
    y1=(Decimal(2)*e).sqrt()-alpha*h1
    y2=B-alpha*h2
    f0=(B*B+Decimal(2)*e)/Decimal(2)
    f1=(y1*y1+y2*y2)/Decimal(2)
    return f1/f0, rms

# Defining-paper recommended first-step witness.
ratio,rms,h1,h2=factored_step("1e-30","1e-3","1e-2","1")
assert rms > 1
assert ratio > Decimal("1.0000999999999")
assert h1 > Decimal("1.9999999999999999999999999999")
assert h2 < Decimal("1e-13")

ratio_full,rms_full=full_step("1e-30","1e-3","1e-2","1")
assert rms_full < 1
assert ratio_full < Decimal("0.990042")
assert ratio_full < 1

# Scale-separation limits.
for rho_s in ("0.001","0.01","0.1","0.5"):
    rho=Decimal(rho_s)
    target_fact=Decimal(1)+rho*rho
    target_full=Decimal(1)-rho+Decimal(5)*rho*rho/Decimal(12)
    fr=ur=None
    for B_s in ("1e8","1e10","1e12"):
        fr,_,_,_=factored_step("1e-12","1e-9",rho_s,B_s)
        ur,_=full_step("1e-12","1e-9",rho_s,B_s)
    assert abs(fr-target_fact) < Decimal("1e-10")
    assert abs(ur-target_full) < Decimal("1e-10")
    assert target_fact > 1
    assert target_full < 1

# Direct first-step marginals.
e=Decimal("1e-30"); B=Decimal(1)
W=((Decimal(3)*e,e),(e,B*B+e))
r=(sum(W[0]),sum(W[1]))
c=(W[0][0]+W[1][0],W[0][1]+W[1][1])
S=sum(r)
assert r == c
assert r[0] == Decimal(4)*e
assert r[1] == B*B+Decimal(2)*e
assert S == B*B+Decimal(6)*e

print("verification passed")
