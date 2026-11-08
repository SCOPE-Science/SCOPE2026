# Independent mathematical audit

## correctness

PASS

For exactly two real columns with Gram eigenvalues L>1,1 and exactly two independent standard-Gaussian sketch rows, the sketch norm difference is the indefinite quadratic form alpha X-beta Y with X,Y independent chi-squared_2, alpha beta=L and alpha-beta=delta=|G11-G22|. Exponential integration gives wrong-pivot probability beta/(alpha+beta)=(1-delta/sqrt(delta²+4L))/2. Because loss on a wrong pivot is exactly delta, the expected regret formula follows for delta in the full interval [0,L-1] attained by Gram rotations. Substituting u=delta/sqrt(delta²+4L) gives squared objective proportional to u²(1-u)/(1+u), whose derivative has the single interior positive root s=(sqrt5-1)/2. The feasible upper bound u=(L-1)/(L+1) crosses s at Lc=2+sqrt5, giving the claimed piecewise maximum and all equality orientations, including boundary and delta=0. Independent seeded Gaussian simulation and exact boundary computations agree across 20 regimes; sampling does not prove the optimization.

## originality

PASS

Best-of-knowledge PASS. The randomized QRCP pivot rule and embedding analyses occur in Martinsson et al, Duersch–Gu and Melnichenko et al; the chi-square quadratic-form sign law is classical and is NOT credited as novel. The final claim is the sharp optimization of an explicitly specified expected first-pivot regret across all fixed-spectrum column orientations, with golden-ratio transition and equality cases. The inspected QR algorithms and classical distribution references do not supply this extremal orientation law.

## value

PASS

The squared first QR diagonal is precisely the pivoted column norm, so regret is a natural local objective. The unexpectedly oblique worst orientation for L>2+sqrt5 makes singular-value anisotropy insufficient to forecast minimal-sketch pivot fidelity. Exact global bound, transition, optimizer orientation and sqrt(L) scaling provide a useful adversarial benchmark, without unsupported downstream stability claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
