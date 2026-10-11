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

# Verification notes

The mathematical proof is contained in `RESULT.md`; its decisive all-exponent step is the strict positivity of the third divided difference of \(t\mapsto t^{q+2}\) for \(q>0\), after verifying that the interpolating quartic retains four distinct positive roots.

Run `python3 verify.py`. The program has no external package dependencies and verifies exact rational characteristic-polynomial identities for 216 triples, including all three choices of central weight. Observed output on the packaged program: `WEIGHTED_SHIFT_SCHATTEN_REARRANGEMENT_EXACT_OK 216`.

Finite exact checks are supplementary evidence only. They cannot establish the positive-root interpolation or the uncountably many exponent inequalities; those are addressed analytically in the proof. No external independent mathematical audit was performed.
