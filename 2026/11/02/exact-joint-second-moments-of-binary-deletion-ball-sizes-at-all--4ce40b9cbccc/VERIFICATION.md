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

# Exact verification and boundaries

Run `python3 verify_joint_moments.py` to verify that the proposed length-generating numerator and denominator match the nine-state tensor transfer as exact polynomial identities through all fourteen degrees required by Cramer's degree bound. The program checks *all* deletion-degree monomials at each length, not just a finite selection of parameters. It also enumerates distinct subsequences by independent masks for every binary word of length at most eight.

Run `python3 verify_variance3.py` to independently extract symbolic rational first and second moments for deletion radius three. It checks the rational identities in the polynomial ring and enumerates all binary input words of lengths three through thirteen, comparing with direct deletion masks through length eleven. Exact rational arithmetic is used throughout. Recorded output from actual successful executions is embedded in `verification_output.txt`.

The all-length theorem is a consequence of a finite algebraic certificate and explicit degree bound, not a claim extrapolated from finite experimentation. No claims are made for nonuniform sources, nonbinary alphabets, limit distributions, independent review, or exhaustive publication priority.
