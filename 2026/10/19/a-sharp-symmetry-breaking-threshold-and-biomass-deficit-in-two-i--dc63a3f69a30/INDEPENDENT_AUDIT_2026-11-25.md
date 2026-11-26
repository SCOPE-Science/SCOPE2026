# Independent mathematical audit

## correctness

PASS

For the stated identical Beverton–Holt map write h(z)=Tz/(1+z), H(z)=h(z)tanh(k(z-u)), u=T-1. The sum equation at any asymmetric positive fixed point forces x>u>y after swapping; strict Jensen gives m=(x+y)/2<u. Then t=u-y>s=x-u>0, so h(x)s+h(y)t=u(s+t)+s²/(T+s)-t²/(T-t)<u(s+t). Using tanh(v)<v rules out the stationary difference when ku≤1, including equality. For every ku>1 solve the sum equation for x(y)>u on 0<y<u; the difference quotient tends to 0 and ku at the endpoints, so crosses 1. The analytic mean equation gives m=u-d²/(uT)+O(d⁴) and the odd difference equation has a positive cubic saturation beta=(1/3+(u+2)/T²)/u². On the emerging pair the critical eigenvalue is ku-3 beta d²+O(d⁴)=1-2(ku-1)+O((ku-1)²): the off-diagonal coupling contributes h''(u)H''(u)/(1-1/T) to the d² coefficient, equal to -2H''(u)/(uT), in addition to the diagonal term. The other eigenvalue stays near 1/T. The symmetric multipliers are 1/T and ku; at extinction constant column sums and positivity give spectral radius T. No nonlinear stability at equality, uniqueness of a remote pair, or stability for every ku>1 is inferred. RESULT.md §§1–6 checked; verify.py and VERIFICATION.md inspected, not executed. Their finite parameter checks are not used to prove the threshold.

## originality

PASS

The best available catalogue and literature comparisons establish the broader model class, existence or persistence, and other biomass or pitchfork phenomena, not the exact all-k threshold for asymmetry in this same map. The spectral-radius identity, Jensen argument and local pitchfork machinery are not claimed as independent advances. The distinct claim assessed is the sharp global boundary for strictly positive asymmetric equilibria, with the stable local branches and their biomass deficit.

## value

PASS

The sharp all-parameter equilibrium boundary (including the neutral endpoint), stable nearby nonuniform states, and strict biomass loss together distinguish mechanisms that an extinction-based persistence criterion cannot see. In particular, below-threshold global exclusion and above-threshold existence at arbitrarily large k are not a routine local pitchfork calculation. This is a useful exact benchmark for discrete density-dependent dispersal, not a generic claim about ecosystems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
