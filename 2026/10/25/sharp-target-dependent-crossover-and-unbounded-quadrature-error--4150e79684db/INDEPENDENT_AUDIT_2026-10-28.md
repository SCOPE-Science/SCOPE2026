# Independent mathematical audit

## correctness

PASS

PASS: For diagonal SPD kernel diag(L,1^m), sampled RKHS coordinate sections are orthogonal and optimal weight on sampled i is g_i, leaving squared worst-case error Lg_0² 1_{spike omitted}+sum_{i≥1}g_i² 1_{i omitted}. Residual-diagonal RPChol pivoting draws sequential without replacement proportional to unchanged diagonal masses, giving p_R=product_{j=0}^{k-1}(m-j)/(L+m-j); k-DPP volume sampling gives p_D=(m-k+1)/(kL+m-k+1). Both equal at L=1; derivative of log p_R is strictly more negative than log p_D for L>1,k≥2, so p_R<p_D. Exchangeability of m small coordinates plus exactly m+1-k omissions proves E_J=Lg_0²p_J+(m-k+1-p_J)Q/m, Q=sum g_i². Therefore the exact sign of E_D-E_R is sign(Lg_0²-Q/m); equality and opposite strict orderings both occur. For g=e_0, p_R~(m)_k L^-k, p_D~(m-k+1)/(kL), giving E_D/E_R~L^(k-1)/[k(m)_{k-1}]. Independently enumerated ALL ordered pivot paths and determinantal k-subsets with exact rational probabilities for 2≤m≤5, 2≤k≤m, L=3/2,3,10, and several targets; all identities match. This is a finite dimensional family with exact algebra valid for every stated m,k,L, not a continuous-domain theorem.

## originality

PASS

PASS qualified: RPChol kernel quadrature and volume sampling with optimal RKHS weights are known (Epperly–Moreno 2023, Belhadji et al 2020). Yu 2010 compares inclusion probabilities of successive/rejective unequal-probability sampling, so a qualitative dominant-coordinate omission advantage is known. The additional complete sign-classification of expected SQUARED quadrature risks for all target g and asymptotically unbounded ratio on the one-spike family are not stated in the inspected previous studies. A sampling-theoretic equivalent of the diagonal weighted-risk calculation is plausible and explicitly retained as priority risk; not claiming first inclusion-probability inequality.

## value

PASS

PASS: A motivated open comparison asks whether random pivoted Cholesky or fixed-size determinantal sampling yields better quadrature. The explicit same-kernel/same-budget diagonal model shows target dependence with an indefinite (one-positive/m-negative) risk difference and unbounded performance ratio, ruling out uniform dominance. The result is narrow but a complete interpretable counterexample and exact classification, not a meaningless arbitrary spectral slice. No extrapolation to continuous kernels, noisy data, or unsquared-risk ratios.

The dated certificate retains the supplied scientific assessment, sources and limitations.
