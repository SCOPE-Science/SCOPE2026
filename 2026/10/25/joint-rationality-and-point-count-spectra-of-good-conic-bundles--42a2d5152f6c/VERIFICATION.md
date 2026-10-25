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

# Reproducibility and limits

Run `python3 verify.py` from the extracted artifact directory. The script uses only the Python standard library and exact rational arithmetic. Its enumerator independently traverses all \(2^{n-1}n!\) even signed permutations for each \(n\in\{4,5,6,7\}\), scores positive and negative fixed cycles, and tests the three rationality cycle patterns. The coefficient-extraction side is computed from explicit labeled-cycle series. It compares the complete unconditional and rational-tagged Laurent distributions and checks the exact rationality totals and sharp boundary mass. Expected final line: `VERIFY_OK`.

The general identities follow from the five mathematical proof steps in `RESULT.md`, with monodromy, rationality and equidistribution as cited inputs. This finite computation cannot establish all integer values \(n\ge4\), a finite-field error constant, or publication priority. The underlying sample is the good balanced moduli parameter space used in the cited source, not uniform isomorphism classes. Independent audit: not performed.
