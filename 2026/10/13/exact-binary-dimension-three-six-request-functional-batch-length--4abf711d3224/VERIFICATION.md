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

Run `python3 verify.py` in a directory containing both `verify.py` and `certificates.tsv` (UTF-8). The checker confirms the exact columns `1,2,3,4,5,6,7,1,2,4,7`, rank three, all 924 sorted request patterns with no duplicates or omissions, precisely six disjoint nonempty recovery sets for each pattern, allowed coordinate indices and the spanning condition over the binary field. It also computes all seven nonzero codeword weights and obtains minimum distance six.

Observed: `VERIFY_OK 924/924 recovery lists; rank=3; minimum distance=6; sizes= {1: 3798, 2: 1669, 3: 77}`. There are 5,544 validated recovery sets and no recovery set exceeds three coordinates.

The certificate establishes the finite upper bound for this displayed matrix and all requests. The lower bound is a general Hamming-distance/Griesmer proof in `RESULT.md`. No unspecified computation or unavailable external package is used. This verification is an internal finite reproducibility check, not independent scientific validation.
