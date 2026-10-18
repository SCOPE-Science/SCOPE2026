# Independent mathematical audit

## correctness

PASS

Born probabilities of symmetric open-chain MPS |ψ_{n,g}> are g^{D(x)}/[2(1+g)^{n−1}], giving independent original wall Bernoulli θ=g/(1+g). The XOR of two independent words has fair initial bit and independent wall probability h=2g/(1+g)². Pair Z_iZ_j noise multiplies off-diagonal x,y by 1−2a_{j−i} iff XOR bits at i,j differ; squaring gives exact purity E_U ∏_r |1−2a_r|^{2C_r(U)}. At g_n=λ/n, K_n~Bin(n−1,h_n)→Poisson(2λ). For each finite k, random wall positions are asymptotically separated and interior in the sense of first fixing ε>0, controlling exceptional configurations, then letting ε↓0; for distances below separation C_r=kr; for all r, C_r≤kr. At α>2, log tails ∑r^{1−α} converge giving q=∏|1−2p/r^α|^{2r}; for α<1 or 1<α≤2, a positive fraction of crossing attenuation diverges and conditional product→0 for k≥1. Averaging Poisson generating function gives exp[−2λ(1−q)]. At α=2,p_n=c/log n, ΣC_r/r²=k log n+O_k(1), log weight→−4ck, hence crossover exp[−2λ(1−e^{−4c})]. p=0, p=1/2 and nearest-neighbor finite-size checks handled. The proof needs ε→0 rather than claim fixed-ε separation has probability 1; the formulation supports that limiting argument. Inspected MPS/density-matrix verifier and independently checked C_r=kr for isolated wall small r at n=20,80; finite tests do not prove limits.

## originality

PASS

Fechisin et al. 2026 arXiv:2610.00480 provides precisely this MPS and dephasing map, Appendix A domain-wall representation, Appendix G power-law crossing attenuation and alpha-two summability threshold for linear string correlations, Sec.V purity numerics and Appendix H a distinct exactly solvable fixed g=1,alpha=0 case. Complete available HTML was searched/inspected; no Poisson global purity limit for g_n=λ/n and no α=2 inverse-log strength interpolation appears. These two sharp asymptotic formulas and the finite-size purity crossing identity are the surviving contribution, not generic claim that α=2 threshold was unknown.

## value

PASS

The weak-fugacity g_n≈λ/n scaling is a natural dilute-defect regime approaching the GHZ point, and exact nonzero global purity has direct consequences for the feasibility of measuring Rényi-2 observables. The result distinguishes summable/noisy regimes and an inverse-log marginal transition quantitatively for a motivated quantum channel; it explicitly does not prove mixed-phase persistence or state preparation at a fixed thermodynamic phase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
