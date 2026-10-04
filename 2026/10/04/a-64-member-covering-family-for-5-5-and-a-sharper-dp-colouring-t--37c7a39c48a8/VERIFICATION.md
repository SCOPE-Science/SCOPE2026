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

The certificate `covering_family_5.json` is finite and self-contained. The script `verify_covering_family.py` uses only the Python standard library and performs the following checks:

1. the parameter is \(\ell=5\);
2. the family has exactly 64 distinct members;
3. each member contains five genuine permutations of \([5]\);
4. every one of the \(5^5=3125\) tuples in \([5]^5\) is covered in the required pairwise-distinct-image sense.

The finalized replay output is:

`ALL CHECKS PASSED; family_size=64; tuples=3125; minimum_coverage=1; maximum_coverage=8`

This exhausts the finite certificate domain. It does not prove that 64 is optimal, and no such claim is made. The consequence for \(\mu(5)\) additionally uses the published theorem \(\mu(\ell)=\kappa(\ell)\) from arXiv:2609.33966v1.
