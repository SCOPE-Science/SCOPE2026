---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For fixed a_j>0, Laplace saddle asymptotics give e^(-2Au)prod I0(2a_j u)=K_d u^(-d/2)(1+O(1/u)), and the derivative is O(u^(-d/2-1)). Sum-to-integral error is O(1) and its difference under the Abel parameter O(delta). The standard Laplace integrals yield d=1 inverse-square-root coefficient sqrt(pi)K; d=2 log coefficient K; d=3 finite F0 and gap 2sqrt(pi)K delta^1/2; d=4 gap K delta log(1/delta); d>=5 finite derivative J_d. The derivative threshold follows from harmonic-log summability. Independent prime frequencies and Parseval prove the exact HS norm identity for positive epsilon. Independent scipy evaluations of the exact coefficient ratio at u=200 for d=1..5 agree with saddle constants to within 0.2 percent. This is a check, not the proof.

## originality

PASS

The Bessel saddle and Abelian integration are classical, and the Hilbert–Schmidt d>=3 membership threshold is already known; no novelty is claimed for those. Bayart–Kouroupis 2024 Theorems 1.1–1.2 characterize broad Schatten membership via mean counting functions, but the inspected paper does not tabulate the five sharp approach-to-boundary moduli or the concrete coefficients for this family. The specialized full five-regime constant classification is additional, though likely derivable by classical principles.

## value

PASS

The exact leading divergence and derivative onset across all finite prime counts give a natural quantitative Hilbert–Schmidt boundary-sensitivity benchmark beyond qualitative membership, with explicit constants and the nonanalytic to differentiable transition. Although the proof uses standard Abelian tools, the precise piecewise norm response is an independently reusable fact of a naturally parameterized Dirichlet operator model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
