# Scientific review

## Correctness — PASS

The stated algorithm matches the primary source's Bernoulli ProxSkip update. Invariance of the normal control follows because the proximity operator for an affine indicator is its orthogonal projector. Splitting primal error into normal and tangent components gives the explicit two-state normal recursion, and a geometric-length skipped block has the exact multiplier \(1-pS_j(c)\). Strict monotonicity of \(S_j\) establishes the complete zero-factor classification. Independent inter-call gaps yield the almost-sure dichotomy and generating function. The sharp minimum follows from one derivative and a uniform lower bound for all higher orders. The bundled exact-rational checks cover representative instances but are not an infinite proof.

## Originality — PASS (qualified assessment)

The source's Algorithm 1 and Theorem 3.6 concern iteration dynamics and asymptotic Lyapunov rates, not exact permanent feasibility. RandProx-Skip includes the same update but provides general contraction theory, not the discrete gap-annihilation law. Deterministic active-manifold identification results are closely motivated but cannot imply the skipped-step dichotomy. A published absorption result for randomized Kaczmarz concerns another iteration, not this normal-control recurrence. No equivalent exact ProxSkip law was found in the searches and inspected text; this is evidence of noncoverage, not proof of global uniqueness. The abstract-only comparison for one ancillary source leaves a limited residual risk.

## Value — PASS

Whether a randomized constraint solver identifies a feasible active manifold *permanently* is distinct from asymptotic expected convergence. The complete resonance/nonresonance classification shows that persistent feasibility can be a discontinuous arithmetic property of the skipping parameters even for a strongly convex problem. The exact waiting-time distribution and unique cross-order optimum quantify the resulting computational latency on a natural constrained test family. The result is narrow by design and does not claim a generally optimal solver.

Self-review: passed. Independent audit: not yet performed.
