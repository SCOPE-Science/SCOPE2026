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

# Verification

The theorem has an elementary symbolic proof in `RESULT.md`. Run `python3 check.py` on Python 3.8+ without external packages. The script enumerates all ordered pairs of involutions on \(n\) labelled worlds for \(1\le n\le7\), computes graph diameters and checks coefficient predictions using exact `fractions.Fraction` arithmetic. For \(1\le n\le4\), it separately verifies, for **every** valuation of a propositional variable, that the iterated everyone-knows operator equals common knowledge at the computed diameter.

The expected total pair counts are \(1,4,16,100,676,5776,53824\) for \(n=1,\ldots,7\). The actual verifier must print `Semantics checks passed.` only after all assertions succeed. Bounds greater than seven worlds are established in the proof, not by finite enumeration. The code does not test richer intuitionistic orders, larger classes, or additional agents.
