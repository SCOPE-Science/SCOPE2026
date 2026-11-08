---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS. At equilibrium (1,1,g,g), for q=m^2+n^2>=0 on (0,pi)^2 Neumann, the modal 4x4 determinant independently recomputed symbolically equals [((z+A)(z+E))^2+(z+E-gq)^2], A=2+3q/10, E=1+3q. Positive real z cannot solve it. Factorization into conjugate-coefficient quadratics yields exactly one positive gain imaginary-axis crossing g_c(q) with positive transverse real-part derivative. Exact symbolic computation independently verified g1=(85+189sqrt105)/100 and g2=(55+72sqrt205)/50 and the full quartic Routh-Hurwitz Delta2,Delta3 identities. For ALL q>=2, concavity of H(q,g) in g and explicitly coefficientwise positive shift H(2+h,g2) for h>0 ensure Delta3>0 on 0<=g<g2, with the remaining RH inequalities positive. The q=0 polynomial factors stably; q=1 is exactly two spatial modes cos x, cos y, each has one unstable conjugate pair for g1<g<g2. No finite mode sampling is substituted for the infinite-mode proof, and nothing nonlinear is claimed.

## originality

PASS

PASS best-of-knowledge. The original 2026 four-field model paper, materially inspected in arXiv v2, gives reaction-cross-diffusion structure and sufficient stationary Turing sign diagnostics such as negative constant term, not the exact oscillatory gain interval in which every constant term is positive and higher Neumann modes stable. General attraction/repulsion chemotaxis oscillations establish that waves can exist in other models; none of the inspected sources implies these two radicals or exact infinite-spectrum mode selection.

## value

PASS

PASS. The two sharp algebraic thresholds identify a maximal gain regime exhibiting exclusively oscillatory first-spatial-eigenspace instability while infinitely many higher modes remain stable. It addresses a genuine blind spot of stationary Turing tests with a rigorous all-mode certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
