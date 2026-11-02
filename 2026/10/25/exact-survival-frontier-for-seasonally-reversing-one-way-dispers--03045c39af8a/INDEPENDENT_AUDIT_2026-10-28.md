# Independent mathematical audit

## correctness

PASS

For 0<a<b,m,T>0, A1=[[a,m],[0,-b-m]] and A2=[[-b-m,0],[m,a]], with A2=P A1 P. Write E=exp(A1 T/2)=[[u,m(u-v)/K],[0,v]], K=a+b+m. The period M=(PE)^2 has Perron multiplier mu_+^2 where mu_+=(q+sqrt(q^2+4uv))/2, and yields Lambda=(a-b-m)/2+(2/T)asinh((m/K)sinh(KT/4)). This is the exact common exponent for nonzero nonnegative initial states. For h=m/K, F(s)=asinh(h sinh s) satisfies F(0)=0 and F''(s)>0, hence F(s)/s strictly increases: Lambda(T downarrow0)=(a-b)/2<0, Lambda(T upward infinity)=a>0. The m derivative is positive by sinh(s)/s>1 and squared numerator comparison, so the unique zero Tc(m) is smooth and decreases. At Tc, (m/K) sinh(KTc/4)=sinh((b+m-a)Tc/4). Expanding the ratio for m downarrow0 gives (m/K)exp(aTc/2)->1. With x=KTc/4 and m upward infinity, the limiting sign is 2ax cosh x-(a+b)sinh x and uniqueness follows monotonicity x coth x; mTc->4x*. Independent direct 2x2 matrix exponential comparisons on 48 parameter tuples matched within 6.6e-14 and give numerical corroboration only, not infinite-parameter proof.

## originality

PASS

The exact symmetric-in-season two-habitat finite-parameter Floquet exponent and both sharp critical asymptotics were not found already established. This is narrower than established qualitative dispersal-induced growth; strongly relevant Liu/Wang theorem text remains unavailable and presents priority risk.

## value

PASS

Strict two-parameter monotonicity and the complete one-dimensional survival threshold determine when seasonality rescues two individual sinks and quantify two singular timing scales. Such exact persistence boundaries are natural for switched positive systems and nontrivial beyond the known qualitative model; both endpoint constants are useful for subsequent asymptotic comparison, independent of claimed broad modeling generality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
