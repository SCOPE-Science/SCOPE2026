# Research review: sharp recovery of an initially missing receptive tie

**Correctness — PASS.** The proof starts with the precise strict-inequality confidence rule. It establishes invariance of all initially receptive pairs via the bound \(M_{t+1}\leq M_t/(n-1)\), derives the exact missing-pair disagreement \(d/(n-1)^t\) and confidence \(c_0\delta^t\), then identifies the first strict crossing. In the no-crossing regime a conserved degree-weighted mean proves consensus; in the crossing regime the complete averaging step gives exact finite-time consensus. The two-mean recurrence verifies the final opinion correction. The bundled `verify.py` checked 720 exact-rational trajectories across a range of dimensions and parameters. The proof, not that finite enumeration, establishes the all-size claim.

**Originality — PASS subject to explicit residual risk.** The original Li–Luo–Porter article [1] proves convergence of confidence bounds to zero or one and eventual stabilization of effective graphs; its simulations show missing links within an opinion-consensus cluster. Neither theorem gives the sharp recovery decision \(\delta_c=1/(n-1)\), exact recovery time, or finite-time consensus level. Its §6.2 specifically asks about mediator nodes and parameter effects. Related work on fixed-confidence network bridges [2], heterogeneous adapting thresholds [3], and rewiring opinion networks [4] involves distinct dynamics. Targeted literature and published-finding searches did not identify an equivalent or stronger covering statement. Risk: unindexed specialist literature and full texts not examined for the two less directly related works.

**Value — PASS.** The result directly resolves a mathematically identified mechanism question for a natural family at every network size, separating consensus of expressed opinions from actual restoration of receptiveness. The sharp population-dependent boundary, the exact recovery delay and limiting opinion make the distinction testable within the model. The result is not a general classification of multiple inactive ties, nor a claim about actual human attitudes.

**Independent validation and limits.** The included script provides reproducibility checks but cannot certify proof completeness, publication priority, or empirical applicability. The 2025 journal article is the same research source as the arXiv preprint, not independent confirmation. Independent external review remains outstanding.

Self-review: passed. Independent audit: not yet performed.

## Closest literature

[1] Li, Luo, Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563v3, §§2.2, 3.1, 5, 6.2 (2023/2024); SIAM J. Appl. Dyn. Syst. (2025), DOI:10.1137/23M1558951.

[2] Schawe, Fontaine, Hernández, *The bridges to consensus*, arXiv:2102.10910 (2021).

[3] Vasca, Bernardo, Iervolino, *Practical consensus in bounded confidence opinion dynamics*, Automatica (2021), DOI:10.1016/j.automatica.2021.109683.

[4] *adaptive bounded-confidence model of opinion dynamics on networks*, J. Complex Networks (2023), DOI:10.1093/comnet/cnac055.
