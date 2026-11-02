# Independent mathematical audit

## correctness

PASS

For b>=2, the Av=-v equations force each clique-cell sum to vanish, so the full -1 eigenspace projector is the block diagonal direct sum of R_t=I_t-J_t/t, including R_1=0. F=E_-1 circle E_-1 has cell constant eigenvalue (t-1)/t and cell-contrast eigenvalue (t-2)/t, producing precisely size-two pair-difference null directions and, for a=1, a possible singleton hub. Every other projector kills each pair difference because it lies entirely in the -1 eigenspace, hence all Schur squares kill them. In singleton-core case, positivity of the Perron-vector squared coordinate at the hub removes the remaining hub kernel direction; it is orthogonal to all pair differences. Thus the kernel and rank formula follow. For a>=2, F has all positive eigenvalues >=1/3 and the same kernel as Mhat; PSD addition preserves the lower bound. Size-three internal differences are exactly eigenvalue 1/3 since other spectral projectors have equal columns there. Independent code rebuilt adjacency/spectral projectors for 144 parameter settings and exact -1 eigenspace identities for four settings; these bounded tests corroborate, not prove, the universal argument. No b=1/singleton peripheral/weighted/Laplacian conclusions claimed.

## originality

PASS

Targeted published-finding searches and comparison with original average-mixing projector, commutant, exact-arithmetic and French-windmill rank sources found no prior statement implying the complete arbitrary-core, unequal-blade rank formula AND 1/3 uniform gap. General spectral-idempotent theory supplies the proof framework, not the derived graph-specific projector and its exact cell-block spectrum. Kimmerling 2023 Theorem 5.1.2 establishes full rank for one-hub equal French windmills with blades K_m, m>=3, a strict special case. Best-of-knowledge PASS with substantial unread-dissertation and general-theorem priority risks, not an absolute novelty certificate.

## value

PASS

Unweighted clique-cored windmills are a natural graph family with arbitrarily many possibly unequal dense blade subgraphs meeting in a common clique. The full exact kernel/rank formula identifies precisely the size-two cells losing long-time quantum average-mixing degrees of freedom, including the core-size-two anomaly, while the sharp size-independent 1/3 lower spectral bound quantifies surviving modes. This all-parameter classification is not determined by the previously published uniform one-hub full-rank theorem or by pointwise numerical computations. The contribution is narrow and uses standard projector methods but gives a motivated exact structural invariant and stability constant a researcher could need.

The dated certificate retains the supplied scientific assessment, sources and limitations.
