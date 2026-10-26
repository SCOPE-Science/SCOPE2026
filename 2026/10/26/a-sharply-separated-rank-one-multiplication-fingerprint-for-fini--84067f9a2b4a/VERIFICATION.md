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

# Reproducibility and verification

Execute `python3 verify_kernel_fingerprint.py` with Python 3. No nonstandard packages or external data are needed.

The script generates every integer partition through \(n=32\) and checks the uniqueness of the computed power sums and successful greedy inverse for all 43,819 partitions. For \(2\le n\le32\), it sorts every fingerprint and verifies that the true minimum adjacent difference is exactly \(2^n-2\). It constructs actual transformations on \(n\le6\) points to check the rank-one product counts in 29 direct profiles, and enumerates actual ordinary permutations as outer factors for \(n\le4\) in 11 profiles.

The expected terminal marker is `VERIFY_OK_KERNEL_FINGERPRINT direct_profiles=29 direct_outer_profiles=11 partition_decodes=43819 sharp_gaps_n=2..32`.

These are finite consistency checks only. They do not certify universal claims or the historical-priority assessment; both depend on the explicit proof and primary-literature comparison respectively. The proof of the abstract-isomorphism corollary uses Tsyaputa's Theorem 2, which is not independently reconstructed in the verifier.
