# Independent mathematical audit

## correctness

PASS

Use F_s(x)=k(1-s)x²/2. Its jumps cancel the signed work at both switches, and Itô's formula gives W_t+F_{S_t}(X_t)-F_{S_0}(X_0)=Dk∫_0^t 1_{S_u=0}du+k√(2D)∫_0^t X_u 1_{S_u=0}dB_u. Centering the occupation via chain corrector c·1_{s=0}, c=Dk/(a+b), gives a martingale with jumps ±c, orthogonal continuous and jump parts, and stationary bracket rate 2Dk²u_0+c²(bp_0+ap_1). Here the generator's stationary second-moment equations give u_1=D/k and bu_0=2Dp_0+au_1, recovering both variance terms and mean Dkp_0. The affine intercycle recursion has independent cycle innovations with finite moments and E e^{-rkT_on}<1 for every r>0, supporting the stationary finite fourth moment and ergodicity. The boundary term is bounded in L²; Cauchy–Schwarz bounds its contribution to variance/t by O(t^{-1/2}). The ergodic bracket limit and the bounded-jump Lindeberg condition give the martingale CLT and the same work CLT after removing the boundary. Substitution a=pλ, b=(1-p)λ gives a positive constant plus a strictly positive multiple of 1/λ and reproduces 2D²k+9D²k²/(4γ) at a=b=γ. The supplied mixed-moment ODE check was inspected; no finite-time numerical computation is needed for these limits.

## originality

PASS

The mean dissipation rate is known and excluded. The inspected same-model earlier literature does not supply the evaluated deterministic-time variance rate for stationary signed switching work, its Gaussian limit at unequal rates, or the strict fixed-duty dependence. A later catalogue entry exactly overlaps the symmetric specialization only. Credit the arbitrary-rate fluctuation finding, not global priority or general martingale and thermodynamic identities.

## value

PASS

Variance per deterministic observation time is an independently useful measure of work fluctuations in the established intermittent-trap model. At fixed duty fraction the known mean cannot distinguish switching speeds, but the exact variance can and quantifies both the slow-switching divergence and the positive fast-switching floor. The CLT identifies the scale of typical fluctuations of the signed work; neither per-switch moments nor finite-time exponential moments are claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
