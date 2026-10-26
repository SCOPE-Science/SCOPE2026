---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

The proof reduces the three-variable nonlinear update to one geometric leaf gap and the exact outer normalized recurrence. The decisive identities are \(B-\lambda=1\), \(\lambda\le1\) if and only if \(s\le2/3\) within \(s>1/2\), and \(B/(\lambda-1)=s/(3s-2)>1\) when \(s>2/3\). Since the median is the projection onto the leaf interval, the interior region is invariant and must not be replaced by a nearest-endpoint rule.

The accompanying `verify.py` executes exact `fractions.Fraction` arithmetic. It verifies the explicit witness, strict alternation for a finite prefix, the symbolic threshold equalities on chosen rational coefficients, and the rational consensus formula. Algebraic induction in `RESULT.md`, not finite calculation, proves infinite alternation and the all-initial-state stabilization assertion. No external or independent verification has been performed.
