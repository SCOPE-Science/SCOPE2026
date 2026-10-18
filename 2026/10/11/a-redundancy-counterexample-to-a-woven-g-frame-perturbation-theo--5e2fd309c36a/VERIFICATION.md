---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

For 64 indices the first frame analyzes \(e_1\) at scale \(1/2\), and on the next 64 it analyzes \(e_2\); the second family swaps these directions, giving both tight frame bounds \(64/4=16\). The choices \(\lambda_1=\lambda_2=1/100\) and \(\mu=3/4\) make the published scalar smallness expression \(83/100<1\). For all coefficients the norm of separate adjoint differences is \(\|c_{\rm act}\|/\sqrt2\le\mu\|c\|\), whereas the actual synthesis-difference norm is \(8\). Taking the first frame on indices 1--64 and the second frame on 65--128 repeats only the \(e_1\) functional, so this weave annihilates \(e_2\). This directly contradicts the claimed lower bound \(8\), without any limit or numerical approximation. The exact source theorem and the invalid norm substitution in its proof were directly inspected in the primary publisher PDF.

## originality

PASS

The primary paper itself states rather than corrects the theorem; the actual counterexample establishes the precise redundancy gap between componentwise norms and their synthesis sum. The 2021 Zhao weaving perturbation theorem uses global operator control instead, so it does not supply this exact source-specific counterexample. No verified public correction was located; semantic-index unavailability is expressly retained as risk.

## value

PASS

The counterexample invalidates an explicit published sufficient condition in an active class of operator-valued frame perturbation theorems, quantifies the exact missing redundancy factor, and pinpoints a repairable analytic gap rather than a trivial type mismatch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
