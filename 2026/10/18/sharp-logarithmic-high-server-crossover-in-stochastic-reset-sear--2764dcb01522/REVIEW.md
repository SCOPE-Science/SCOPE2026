# Independent mathematical audit

## correctness

PASS

For Brownian search on [0,L] absorbed at 0, reflected at L, Poisson returns at r, and stable G/M/c if T_r(x)>1/(cμ), the exact no-reset critical point exists for C=cμL²/D>2 and has z=x_c/L=1−√(1−2/C), b=1−z. First passage and renewal give T_r(x)=[cosh k/cosh((1−x/L)k)−1]/r, k=L√(r/D); equating T_r(x_c)=T_0 gives (1+k²/C)cosh(bk)−cosh k=0. Its k^(2n) coefficient for n≥2 is [(1−b²)b^(2n−2)/(2n)!]×[n(2n−1)−Σ_{j=0}^{n−1}b^(−2j)]. For t=b^(−2), the bracket changes from positive to negative exactly once when C>5/2, using g_n=Σt^j−n(2n−1) and convex eventual first differences. For 2<C≤5/2 all coefficients nonpositive with one strict, so no positive root; C=2 directly none; when C>5/2, one sign change plus H(k)<0 as k→∞ establishes one positive root. At large C, letting y=kz, the exact root has log cosh ratio y+o(1), RHS Cy²(1+o(1)), first gives y/log C→1 then y=log C+2loglog C+o(1), and √r=cμL/√D×(log C+2loglog C+o(1)). Independent 65-digit mpmath tests confirmed no-root signs for C=2.2,2.5 and positive unique roots for C=2.5001,3,5,10,80,10^3,10^6,10^12 (y≈0.047869,2.64060,4.30215,5.66686,8.69509,11.85171,19.78540,34.725998); relative correction y/(log C+2loglog C) approaches 1.01 by C=10^12. Initial double-precision tiny-y cancellation was corrected by arbitrary precision; finite tests do not prove general uniqueness.

## originality

PASS

Best-of-knowledge PASS for global positive-root uniqueness threshold C>5/2 and precise large-server r_eq∼c²(log C)² with 2loglog correction. Source Giral-Barajas–Bressloff establishes exact mean first passage equation and numerical crossover rates, explicitly fitting finite data to a power c^β with β>2; it does not prove this analytic one-root rule or logarithmically corrected asymptotic.

## value

PASS

The equalizing reset rate demarcates when resetting harms or helps queue stability and is natural to optimize as server capacity grows. A rigorous positivity threshold and universal c²(log c)² scale (with 2loglog correction) explain why source finite-c polynomial fits suggest a spurious fixed exponent >2; this is a meaningful quantitative phase boundary not a routine reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
