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

Independently reconstructed the drift and first-exit argument in RESULT.md:32–62. Both branches give the same linear increment μ+α|x| for x+y; the quadratic correction gives the exact additional term λ[y²−(−δx+E₂)²]. On the ball, Q=x²+y²+μ² and s=|x|+|y|+μ satisfy s²≤3Q and s≤3η. Thus the cost from the remainder sum is at most 6CQ, and λ(−δx+E₂)²≤2λD²x²+54λC²η²Q. The radius conditions leave at least μ/2+α|x|/2+(6C+1)y² of drift, on the switch as well. These conditions admit a positive radius including C=0. The bound |Φ|≤K yields a contradiction if all iterates through floor(4K/μ)+1 stay in the closed ball; only updates from inside are needed. The proof uses no sign restrictions on δL,δR and no smoothness beyond the stated remainder hypotheses. The inspected verify.py is a supplementary finite exact-fraction test of the weaker drift μ/2 for one remainder pair and four determinant-sign patterns; it was not executed and is not needed for the proof.

## originality

PASS

The supported increment over prior work is quantified uniform exit for both arbitrary quadratically bounded coordinate remainders in the specified planar companion family. Neither the exact affine theorem nor the published special nonlinear example implies that claim. The closest later indexed overlap covers a different, scalar-feedback class. This is bounded evidence, not a definitive priority claim.

## value

PASS

A motivated partial resolution of an explicit nonlinear nonsmooth-fold question: at a fixed local radius the same quantitative O(μ⁻¹) exit estimate works over both branches and an infinite family of remainders, including parameter-dependent cross terms. The quadratic gauge handles a genuine breakdown of the linear drift near the switch. This is not a claim about higher dimensions, arbitrary first-order-small errors, or global divergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
