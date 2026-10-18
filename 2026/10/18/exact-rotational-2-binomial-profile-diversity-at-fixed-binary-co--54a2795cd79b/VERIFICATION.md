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

# Verification details

Run `python3 rotation_checker.py` with standard Python 3 and no third-party packages. The checker independently computes every scattered pair and singleton count for all rotations rather than relying solely on the positional-moment identity.

Recorded successful output:

`PASS_EXACT_ALL_BOUNDARY pairs_nk 66 words 8166 n_range=2..12 gcd2_3_multiplicities=verified`

The checker tests the exact rational finite sum against direct enumeration for all \(66\) nontrivial \((n,k)\) with \(2\le n\le12\), the deterministic lower bound and exact periodicity equality criterion for every word, and the more detailed doubleton/tripleton multiplicity expectations in the gcd-two/three cases.

The unrestricted identity follows from the proof in `RESULT.md`; computation covering \(8{,}166\) words cannot certify all lengths. The asymptotic follows from a uniform Stirling expansion under its fixed-gcd interior-density hypotheses; the finite test is not an independent asymptotic certificate.
