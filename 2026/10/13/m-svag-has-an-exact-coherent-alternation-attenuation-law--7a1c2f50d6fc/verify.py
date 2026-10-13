import math

def rho(beta,t):
    return (1-beta)*(1+beta**(t+1))/((1+beta)*(1-beta**(t+1)))

def run(beta,G,T,alternating):
    mraw=0.0
    vraw=0.0
    rows=[]
    for t in range(T):
        g=G*((-1.0)**t if alternating else 1.0)
        mraw=beta*mraw+(1-beta)*g
        vraw=beta*vraw+(1-beta)*g*g
        bc=1-beta**(t+1)
        m=mraw/bc
        v=vraw/bc
        if t==0:
            s=0.0
            gam=1.0
        else:
            rr=rho(beta,t)
            s=(v-m*m)/(1-rr)
            den=m*m+rr*s
            gam=m*m/den if den!=0 else 0.0
        rows.append((g,m,v,s,gam,gam*m))
    return rows

for beta in (0.1,0.5,0.9,0.99):
    G=2.3
    rows=run(beta,G,3000,True)
    for t in (0,1,2,5,10,30):
        g,m,v,s,gam,u=rows[t]
        closed=((1-beta)/(1+beta))*((1-(-beta)**(t+1))/(1-beta**(t+1)))
        assert abs(m/g-closed)<2e-13
        assert abs(v-G*G)<2e-12

    r=(1-beta)/(1+beta)
    s_inf=G*G*(1+r)
    gam_inf=r/(1+2*r)
    total_inf=r*r/(1+2*r)
    g,m,v,s,gam,u=rows[-1]
    assert abs(s-s_inf)<3e-10*max(1.0,s_inf)
    assert abs(gam-gam_inf)<3e-10
    assert abs(u/g-total_inf)<3e-10

    dc=run(beta,G,20,False)
    for t,(g,m,v,s,gam,u) in enumerate(dc):
        assert abs(m-G)<2e-12
        assert abs(v-G*G)<2e-12
        if t>0:
            assert abs(s)<2e-10
            assert abs(gam-1.0)<2e-10
            assert abs(u/g-1.0)<2e-10

beta=0.9
r=(1-beta)/(1+beta)
assert abs(r-1/19)<2e-16
assert abs(r/(1+2*r)-1/21)<2e-16
assert abs(r*r/(1+2*r)-1/399)<2e-16
assert abs((1+r)-20/19)<2e-16

print("verification passed")
