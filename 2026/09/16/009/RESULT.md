# Short-interval zero-density for SL(2,Z) Hecke-Maass L-functions via the short-interval Luo sieve

## Context
Zero-density estimates bound how many zeros of families of L-functions can lie away from the critical line. For Dirichlet L-functions the large sieve plus Gallagher zero-detection gives classical averaged bounds. For GL(2) the role of characters is played by Hecke eigenvalues lambda_j(n) of Maass cusp forms, and the Kuznetsov trace formula converts spectral sums into Kloosterman sums. Luo discovered an Eisenstein-Kloosterman cancellation improving the twisted spectral large sieve. Qi-Qiao (arXiv:2608.29558) made this effective on short spectral intervals T<t_j<=T+M for M>T^{4/7}. The present result transfers that sieve saving into an explicit short-interval zero-density bound and determines the sharp threshold and the conductor-dropping barrier.

## Definitions
Let {u_j} be an orthonormal basis of Hecke-Maass cusp forms for SL_2(Z) with Laplace eigenvalue 1/4+t_j^2 (t_j>0), Hecke eigenvalues lambda_j(n), and harmonic weight omega_j=|rho_j(1)|^2/cosh(pi t_j). For sigma>=1/2, H>=2 let N_j(sigma,H) count zeros rho=beta+i gamma of L(s,u_j) with beta>=sigma, |gamma|<=H with multiplicity. Let Lambda(M,T,N) be the Qi-Qiao saving factor: T sqrt(MN) for T^2/M<N<=M^{5/2}, T N^{7/10} for M^{5/2}<N<=T^{5/2}, N^{3/2}/T for T^{5/2}<N<M^2T^2, versus the trivial short-interval sieve M(T+N). Let R=M(T+N)/Lambda.

## Result
There exist absolute effectively computable constants C,c_0,delta>0 and B>=1 and fixed explicit A>0 (taken A=2, B=4, c_0=1) such that for all large T, all M with T^{4/7}(log T)^C<M<=T, all sigma with 1/2+c_0/log T<=sigma<=1, and all H with 2<=H<=T^A:
(1/MT) sum_{T<t_j<=T+M} omega_j N_j(sigma,H) << H^B T^{-delta(sigma-1/2)} (log T)^{O(1)}.
Moreover in the Luo range T^2/M<=N<=M^2T^2 the bound with Lambda strictly improves on the trivial-sieve benchmark: R>=1 throughout with R>>T^eta on compact interior subranges, while at M~T^{1/2} one has R<1 in the middle range so the saving does not reach the conductor-dropping barrier. Hence T^{4/7} up to (log T)^C is the smallest M for this method and is sharp. This is a harmonically weighted upper bound with multiplicity only; no unweighted, asymptotic, or pointwise zero-free claim is made.

## Proof/Evidence
Uses Qi-Qiao Theorem 1 as black box plus standard Gallagher zero-detection and cited GL(2) inputs (Riemann-von Mangoldt, Rankin-Selberg, convexity, divisor/Stirling/Weil bounds). Key connection: tau-shift tau=gamma+t_j writes n^{-sigma-i gamma}lambda_j(n)=[n^{-sigma-i tau}][lambda_j(n)n^{it_j}], making coefficients j-independent and the twist admissible for QQ; discrete gamma sums are enlarged to L^2 integrals over interval length L=M+2H via Gallagher smoothing, costing L/M absorbed in H^B. Dyadic N-blocks contribute (L/MT)S(M,T,N) after N^{2sigma-1} cancellation; optimizing sieve bound against trivial bound over mollifier length Y=T^c yields the H^B T^{-delta(sigma-1/2)} shape. Threshold algebra: continuity at M^{5/2},T^{5/2} verified; left/right endpoints tie (R=1); middle branch R~MN^{3/10}/T minimized at N=M^{5/2} gives R_min~M^{7/4}/T>1 iff M>T^{4/7}; at M=T^{1/2}, M^{7/4}/T=T^{-1/8}<1. Re-ran artifact threshold_check.py at T=1e12: continuity rel.diff ~1e-15; M=T^{1/2} gives R=0.251 at left edge; M=T^{4/7} gives R=1 at edge, R=114 at N=T^2; larger M larger R.

## Limitations
Qi-Qiao Kuznetsov-Poisson machinery and standard GL(2) lemmas are cited not re-proved. Constants delta,C and log powers are existential. Endpoints N=T^2/M and N=M^2T^2 tie (R=1); strict power saving is interior. Finite-range uniform upper bound only; harmonic weight not removed; zeros with multiplicity; H<=T^2, M<=T required.

## Reproducibility
Run python3 output/artifacts/threshold_check.py to reproduce continuity and R values. Check QQ Eqs.(1.5)-(1.7) and hypotheses T^{4/7}<M<=T<T^2/M range conditions against DRAFT Step 2.

## References
Qi-Qiao arXiv:2608.29558 Theorem 1; Luo spectral large sieve (1995); Deshouillers-Iwaniec; Gallagher zero-detection; Lewis 2017 dissertation (long-interval predecessor); Sandeep 2024 zero-free spectral averages.
