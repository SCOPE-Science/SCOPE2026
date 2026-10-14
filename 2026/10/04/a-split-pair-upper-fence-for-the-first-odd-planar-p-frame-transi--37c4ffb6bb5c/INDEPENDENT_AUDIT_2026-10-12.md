# Independent mathematical audit

## correctness

PASS

For odd N=2k+1 and 0<α<π/4, directly count unordered pairs: repeated orthonormal X has k²; split competitor Y has (k−1)²+2(k−1)c^p+2ks^p+d^p with c=cosα,s=sinα,d=cos2α all in (0,1). Thus F_k=2(k−1)c^p+2ks^p+d^p−(2k−1) is continuous strictly decreasing; F_k(0+)=2k>0 and F_k(2)=2s²(2s²−1)<0. Unique q_k∈(0,2) exists and gives p(2k+1)≤q_k because the explicit competitor beats the repeated orthonormal configuration for all p>q_k. Rewriting F=2k(c^p+s^p−1)+(1−2c^p+d^p) and a mean-value theorem gives k(2−q_k)→[1−2c²+d²]/[2(c²log c+s²log s)]>0 as q_k→2. Independently solved monotone equations: at π/8, C=0.497260512828602 and k(2−q_k) rises 0.4393 (k=2) to 0.49713 (k=1000); at k=2, α=π/7 root 1.777662643085261. Numerical evaluations corroborate, not replace, the proof. This is a one-sided bound only.

## originality

PASS

Ben Av et al. already introduce the identical split competitor Y(α) for N=5 (k=2) and numerically conjecture first transition p≈1.77766251887019. That N5 family is NOT new. The assessed final claim instead proves a global-competitor upper bound for every odd N and an explicit positive 1/k transition-gap obstruction not stated in their paper; numerical N5 root is only a reproducible corollary. Literature lower-side bounds do not imply an upper bound.

## value

PASS

The exact upper fence addresses the named open odd-N planar p-frame phase transition and supplies a quantitative obstruction to convergence faster than order 1/k. A natural competitor originally observed at N=5 becomes an all-odd analytic family and yields a positive explicit asymptotic constant; it supplies a mathematically meaningful one-sided rate rather than a tiny numerical improvement alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
