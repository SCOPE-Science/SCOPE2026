---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Perron-Frobenius on signless Laplacian makes top Laplacian eigenvalue simple and its eigenvector opposite-signed by bipartition. At h<=2/lambda, coordinate displacement <=h d_i<=2, so no 2-step torus lattice winding (total <=4<2pi); a nonzero real 2-cycle contradicts (2/h)||d||^2 < d^T L d <= lambda||d||^2 via the strict cosine integral. At h*=2/lambda, Lyapunov-Schmidt on the top eigenspace gives cubic coefficient S4/(3lambda), unique positive amplitude branch for h>h*, J_h(u)^2 contracts transversely, and the odd center manifold yields t a_t^2->3lambda/(2S4) outside the strong-stable manifold. Independent two-node benchmark verified lambda=2,S4=4, nearcritical branches, and 100000-step critical ratio 0.999635589. Finite checks do not certify all weighted graphs.

## originality

PASS

Best-of-knowledge positive originality for the full final claim after identifying all presently established subclaims; actual source-material inspections and possible dominating alternatives are recorded. Literature gaps are residual risks, not proof of novelty.

## value

PASS

The true graph-spectral threshold jointly characterizes a global torus obstruction at the endpoint, local emergence and stability of a checkerboard oscillation, and an exact nonexponential critical decay constant for every weighted connected bipartite graph. The endpoint and cubic S4 profile go beyond the known strict descent criterion, and cannot be inferred from linear eigenvalue crossing alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
