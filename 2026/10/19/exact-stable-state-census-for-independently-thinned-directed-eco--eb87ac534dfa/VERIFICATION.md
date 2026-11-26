---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A missing link cuts the dependency cycle into feed-forward paths. Starting at each cut, the limiting logistic carrying capacity gives x_i*=max(0,1−σ e_i x_(i+1)*). Once the input has converged, comparison by constant-capacity logistic equations proves convergence from positive data. In weak inhibition the capacities are positive; in strong inhibition the recursion alternates 0 and 1 along each path, and all capacities are nonzero. At equilibrium the triangular Jacobian requires selection of exactly this recursion for a Hurwitz state: the diagonal is −x_i* on occupied sites and the invasion rate on vacant sites. On the intact cycle the positive equilibrium is uniquely uniform since I+σP is invertible off σ=1. Its eigenvalues are −(1+σ exp(2πik/n))/(1+σ); the least cosine is −1 on even n and −cos(π/n) on odd n. For a Hurwitz boundary state a vacancy must have negative invasion rate; this is impossible for σ<1. For σ>1 two vacancies cannot be adjacent. A vacancy forces its predecessor to be one, which forces the next predecessor to be vacant; this propagates around the cycle and yields just the even alternations. Their full Jacobian is block triangular with strictly negative diagonals. Thus the sole exceptional graph event is intactness, with probability q^n. At a fixed vertex, j consecutive retained edges followed by a cut has probability (1−q)q^j, and it gives a survivor exactly when j is even. Summing j<n proves the expectation with K=0 on intact graphs, including q=0,1. The exponential rare-deletion limit uses fixed σ>1 and the odd threshold tending to 1. The reported finite support enumeration was inspected, not executed; no claim about non-equilibrium attractors or the excluded critical gains follows.

## originality

PASS

Prior work includes random-system stable-community statistics, general stable-support constraints and the negative-feedback secant threshold. The stated distinct result is the exhaustive Hurwitz census in this independently thinned directed cycle, combined with its finite-size multiplicity law and mean richness on broken graphs. The secant threshold alone is not new.

## value

PASS

This is an analytically tractable benchmark for a motivated ensemble quantity: the number of stable communities under uncertain network structure. A single cut erases the exceptional parity-dependent stable-state counts, a structural conclusion that supports the exact finite-size probability and rare-deletion limits. Full transverse stability and the incomplete-graph survivor mean add quantitative information not available from an interior secant test alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
