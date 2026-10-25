# Independent mathematical audit

## correctness

PASS

For every lambda in [4 log 2,8 log 2], q=exp(-lambda/4) in [1/4,1/2]. The exact first two S,I censuses in RESULT.md give S1=3q/4, I1=7/8-3q/4, S2=3q^(9/2-3q)/4 and F(q)=16(I2-I1)=18q-7-12q^(9/2-3q). The analytic bound lambda*S2 <=(3/8)log 2<1/2 implies I_(t+1)<I_t for all t>=2, not just tested days; I1>I0. Endpoint signs and F_prime>=(9/2)(1-log 2)>0 show exactly one q*, with first-two-day tie only at q*. Earliest tie gives H=1-S2 when q>q* and H=1-S1 otherwise, with downward transmission-side jump 7/16-3q*/8>1/4. Independent high precision root gave q*=0.43600529910346198 and jump 0.27399801283620176; script was inspected and is only bounded corroboration.

## originality

PASS

The qualitative fact that peak-time infection proxies jump when the maximizing day changes is preexisting (Ozbay, Nielsen & Nguyen). General positive exponential escape and discrete Kermack–McKendrick maps are also preexisting (Diekmann et al.). The assessed claim is narrower and more precise: one-switch classification on the specified positive mass-conserving map, exactly located unique root and jump >1/4. Inspected Ozbay primary text uses network simulations/Euler comparison and does not give this precise theorem; Diekmann complete primary paper was unavailable, so broader implicit coverage remains a risk.

## value

PASS

Peak-day cumulative exposure is mathematically motivated but discontinuous under a continuously varying transmission parameter; this exact bifurcation and nontrivial >1/4 jump with uniform infinite-time tail control quantify a sharp effect in an explicit positive discrete epidemic model. The value is the exact classification, not rediscovering nonmonotonicity or making public-health prescriptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
