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

Run `python3 verify.py` in the directory containing this file. The verifier uses only the Python standard library.

It performs two exhaustive searches over the complete finite domain. The necklace-transversal search checks all \(5^6=15625\) choices of one representative from each primitive cyclic necklace. A separate subset search checks all \(\binom{30}{6}=593775\) six-subsets of primitive words using independently constructed pair-compatibility masks. Both must produce exactly the same \(86\) maximum codes.

The verifier then reconstructs the Hamming-weight profile, complement/reversal fixed-point counts, all orbits under the declared order-four natural group, and the size-two stabilizer types. It compares these values with `census.json` and verifies that `maxima.txt` is exactly the regenerated maximum-code list.

The computation proves only this finite length-five binary statement. It does not infer an infinite theorem from experimentation, and it does not test whether the declared natural group is the full automorphism group.
