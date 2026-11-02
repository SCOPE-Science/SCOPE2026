# Scientific review: priced four-cycle spectral-gap optimum

## Correctness — PASS

A reflection average is feasible and does not decrease the minimum Rayleigh quotient. The even/odd Laplacian blocks, equivalence of \(\lambda_2\ge1\) to \(a\ge1/2\) and \(M-I\succeq0\), and exact AM–GM cost lower bound reconstruct all normalizations and the threshold at \(\tau=9\). A separate unrestricted Rayleigh-vector inequality verifies both the expensive-edge global upper bound and uniqueness. At equality the exact interval of reflection-invariant optimizers satisfies all semidefinite constraints and the budget. Exact-rational and numerical checks supplement these proofs; no infinity claim rests on finite experiments.

## Originality — PASS (qualified)

The closest full-text sources are Ghosh–Boyd (2006), which provides convex algebraic-connectivity bounds; Göring–Helmberg–Reiss (2011), which develops spectral-width duality; and Göring–Helmberg–Wappler (2008), addressing graph realization and semidefinite bounds. Their inspected passages present general machinery rather than the priced four-cycle's sharp boundary, optimizer continuum and globally unique expensive-edge design. Bibliographic searches for Fiedler's tree-optimum paper locate a different topology. This is best-knowledge originality, **not** a claim to exhaustive search or publication priority. Specialized closed-form four-cycle work not retrieved remains a residual risk.

## Value — PASS

The four-cycle is the smallest feedback ring with two competing nonzero Laplacian modes and a switchable closing connection. The exact answer is not a mere substitution into a generic graph invariant: it resolves unrestricted, asymmetric semidefinite edge-budget design, reveals the non-obvious price \(9\) at which the closing link disappears, identifies a flat optimal face precisely at transition, and proves unique path allocation above it. These details distinguish a genuine design phase boundary from routine eigenvalue evaluation.

## Scope and reproducibility

The result assumes nonnegative conductances, positive budget, and a single exceptional edge price. The optimum among asymmetric designs is proved, but complete characterization of all asymmetric optimizers is not claimed below or at threshold. The standalone `verify.py` uses only the standard library and recorded exact-rational and finite numerical tests. The 1990 Fiedler source's full text was not inspected. No independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
