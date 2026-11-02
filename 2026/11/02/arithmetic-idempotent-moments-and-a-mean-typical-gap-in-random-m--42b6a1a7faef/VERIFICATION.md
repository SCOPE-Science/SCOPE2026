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

# Verification scope
The accompanying `verify.py` uses only the Python standard library. It directly constructs multiplication in labeled finite-field evolution algebras and enumerates all vectors, rather than computing the answers by substituting the theorem's formulas. It independently computes moment predictions from the permutation cycle-index recurrence and compares exact rational moments. The extension fields \(\mathbb F_4\) and \(\mathbb F_8\) are represented by \(\mathbb F_2[t]/(t^2+t+1)\) and \(\mathbb F_2[t]/(t^3+t+1)\), respectively, and the exact parity-sensitive idempotent-free probabilities are also checked.

On execution, all cases \(q=2,3,4\), \(1\le n\le4\), and \(q=5,7,8\), \(1\le n\le3\), pass and the program emits `VERIFY_OK`. These are exhaustive finite checks of the sampled ensembles (not Monte Carlo). The separate direct finite reconstruction verifies no cases of dimension greater than four, and cannot prove the \(n\to\infty\) claims. The full mathematical arguments for the general cycle law, exact moments, root-of-unity coefficient asymptotics, and logarithmic concentration appear in `RESULT.md`.

The verification is limited to algebraic claims; no independent peer review or independent mathematical audit was performed.
