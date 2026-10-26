# Mathematical review

**Correctness — PASS.** The identity \(u=(m+a)p-a\mathbf1\), the weighted Cauchy--Schwarz lower bound for any positive mean-preserving correction, and the mass-concentration upper bound for radial scaling yield the exact two-smallest-weight inequality. The explicit single-negative-coordinate limit sequence attains its sharp supremum. The LGL specialization uses both endpoint weights. Exact rational tests agree with the analytical argument; no extrapolation from finite tests is required.

**Originality — PASS, with residual literature risk.** The underlying ray limiter and conservative projection principles are established prior art. Liu--Guo--Jiang--Sun and Wu supply full entropy/positivity admissibility mechanisms, not the correction-ratio theorem. Fu--Cheng--Shu directly contrast scaling and projection and observe that scaling may damp more, but do not give the exact weight-dependent supremum or its quadratic-in-degree LGL form in the inspected text; their projection optimizes a different weighted-coordinate objective. The Laiu--Hauck comparative 2018/2019 manuscript remained partially inaccessible; broader prior coverage cannot be ruled out.

**Mathematical value — PASS.** The new quantitative answer isolates the precise cost of conservative nodal radial limiting and shows a sharp unbounded degree-dependence for a standard quadrature. This is more informative than the elementary statement that metric projection is shortest and is relevant to limiter selection, quadrature choice, and the analysis of correction-induced damping. It does not claim entropy-feasible optimality or PDE error bounds.

**Sources and scope.** Primary numerical-analysis source: arXiv:2603.27478, first posted 2026-03-29, primary MSC 65M60. Nearby work: arXiv:2604.00301, Fu--Cheng--Shu (2026) §§3.3 and 4, and Laiu--Hauck, J. Sci. Comput. 78 (2019). The theorem concerns nodal positivity in weighted \(\ell_2\), one conserved quadrature average, and strictly positive quadrature weights. It does not cover positivity between nodes, simultaneous entropy constraints, or a complete time-marching solver.

Self-review: passed. Independent audit: not yet performed.
