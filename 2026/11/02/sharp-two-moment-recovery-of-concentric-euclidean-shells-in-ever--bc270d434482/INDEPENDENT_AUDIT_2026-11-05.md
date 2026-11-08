# Independent mathematical audit

## correctness

PASS

For independent uniform-volume points in the d-dimensional shell 0<=a<b, radial moments are mu_{2j}=b^{2j} d/(d+2j)(1-q^{d+2j})/(1-q^d), q=a/b. Rotational isotropy gives M2=2mu2 and M4=2mu4+(2+4/d)mu2², so their ratio Q_d(q) is the stated explicit rational function. Put q=e^{-t}. The log derivative of F_d(q)=(1-q^d)(1-q^{d+4})/(1-q^{d+2})² equals the positive central discrete second difference of g_t(s)=s/(exp(st)-1), strictly convex for s>0; hence Q_d strictly decreases for all d>=2. Its endpoint values are (d+2)(d+3)/[d(d+4)] for the solid ball and 1+1/d for zero thickness. Exact asymptotic losses have orders q^d and (1-q)^2 with coefficients (d+2)^2/[2d(d+4)] and 1/6, giving optimal inverse Hölder exponents 1/d and 1/2 in their respective regimes. Independently verified rational moments and both sharp endpoint coefficients symbolically in d=2..8; the analytic convexity supplies the all-d proof.

## originality

PASS

Tu–Fischbach 2002 gives broad forward distance densities for arbitrary radial densities inside balls, explicitly including layered shells; this dominates computation of forward moments but does not supply the strict two-even-moment inverse injectivity or sharp boundary inverse moduli. The prior Resultary finding on visibility of segments in odd-dimensional shells concerns a different probability, not pairwise Euclidean distance moments. The exact inverse classification is not a routine numeric substitution once the two-moment monotonicity and stability are separately proved.

## value

PASS

Two unknown radii cannot be reconstructed from the one scale-bearing second moment; using the dimensionless fourth/second ratio to identify shell thickness is a natural minimal inverse problem. The result gives an exact full parameter classification, an observable feasible interval, and sharp conditioning at both geometric degenerations in every d>=2. These exact inverse facts are useful for deterministic geometric inference and are not mere recomputation of a known forward density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
