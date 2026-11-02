---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Circulant adjacency eigenvalues 2 cos(pi k/n)+t(−1)^k give the sharp unit-vector SDP bound by trace(A X)≥lambda_min tr(X). The alternating and two-dimensional extremal modes provide attaining Gram matrices. The latter eigenspace has only discrete sine/cosine modes, whose diagonal constraints force Q=I, proving uniqueness for t>1−cos(pi/n). A cut either crosses all 2n cycle edges (forcing zero antipodal cuts for even n) or misses at least two cycle edges; the explicit antiperiodic sign assignment attains 2n−2+nt. The rank-two vectors are all points of a regular 2n-gon, and any generic halfspace separates n consecutive points, crossing exactly 2n−2 cycle edges and all antipodal edges. Ratio monotonicity on each branch locates the unique maximizer; t=0, equality and t_sdp are handled. Independent brute-force CUT on 3≤n≤9 across five weights and Fourier-eigenvalue checks agreed (873760 masks/test instances).

## originality

PASS

Comparisons of actual mathematical implications support a best-of-knowledge original contribution beyond cited prior facts, with explicit overlap credit and residual priority risks; not a universal guarantee.

## value

PASS

Exact parameter phase diagram of a standard graph optimization relaxation, including a strict separation of SDP and integer transition parameters, unique Gram factors and a striking deterministic rounding-optimality regime despite a positive relaxation gap. This is more informative than computing one weighted graph optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
