# Independent mathematical audit

## correctness

PASS

The stationary initial distribution P(+)= (a+epsilon)/(2a) is explicitly matched to the two-by-two Feynman-Kac tilted generator. Diagonalizing gives F=e^(-at)[cosh(zt)+(b/z)sinh(zt)], z²=a²-v²+2iv epsilon, b=a+iv epsilon/a. With epsilon≠0 and z=u+iw, u>0, the identity Re(b conjugate z)=u(a+w²/a)>0 yields |b-z|<|b+z|; any positive-time root would require e^(2zt)=(b-z)/(b+z), impossible by modulus. For epsilon=0, the overdamped/critical formulas stay positive, and the v>a sinusoid gives all listed simple zero times. The squared modulus derivative is a positive scalar times R cos(2wt+theta)-A(t), where A(t)=(a-u)P e^(2ut)+(a+u)Q e^(-2ut)>0 is strictly convex and tends to infinity. On each positive cosine lobe the sign function is strictly concave, so at most one increasing-modulus component. For v>a as epsilon→0, u~(v/omega)|epsilon|, w→omega, and A(t)/R→(a/v)cosh(2ut) uniformly for bounded scaled times. The unique envelope threshold gives a lobe count asymptotic and coefficient omega² arcosh(v/a)/(2 pi v). Analytic parity of |F|² and the simple symmetric zeros give minimum time shifts O_j(epsilon²) and depth O_j(|epsilon|³) after its exact linear coefficient. Independent scipy matrix exponential vs closed form agreed to <3e-12 for four cases; independent concave-lobe counts at a=1,v=2 checked representative asymmetries (epsilon=0.1 ->3 and 0.01 ->31). These finite numerics do not prove the zero-free or asymptotic statements.

## originality

PASS

Exact stationary asymmetric telegraph dephasing amplitude and qualitative suppression of transient recoherence are prior work, especially Feng et al (2026) Eq.26. Originality is assessed only for the all-time complex zero exclusion, exact inverse-rate-asymmetry growth in the number of strictly increasing coherence-modulus intervals, and fixed-zero rounding coefficient. Compared the observable and parameter perturbation with symmetric-rate nonstationary initialization (Hadipour) and a symmetric-noise frozen-discord transition-count theorem from the published corpus. Those do not entail this all-time counting formula. A further analysis of existing exact amplitude in unindexed work remains a material priority risk.

## value

PASS

Counting connected strict modulus-recovery intervals over all future times is a mathematically natural observable of a physically standard non-Gaussian dephasing model. Arbitrarily small stationary switching-rate asymmetry changes infinitely many exact zeros and revivals to a finite number without zeros; the theorem quantifies that singular crossover with a sharp nonzero rate-dependent 1/|epsilon| coefficient and resolves the local rounding of each formerly dark time. The precise global cutoff and singular count add information not provided by the already-known exact amplitude or qualitative short-time recovery figures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
