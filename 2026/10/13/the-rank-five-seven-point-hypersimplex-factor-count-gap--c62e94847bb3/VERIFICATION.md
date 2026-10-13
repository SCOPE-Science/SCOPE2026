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

# Exact verification

Run `python3 verify.py` alongside `witnesses.json`. It relies only on Python standard-library `fractions`, `itertools`, `json`, `math` and `pathlib`. It verifies, for all thirteen included integer matrices, the zero diagonal, all off-diagonal scalings nonzero, symmetric rank exactly five, the number of nonzero principal five-minors, and the actual dual rank-two parallel partition inferred from complementary bases. It independently enumerates all integer partitions satisfying the necessary dual-matroid cocircuit bounds. The successful result is `VERIFY_OK; 13 exact witnesses` with values \(10\) and \(12\) through \(21\).

The universal argument is the proof in `RESULT.md`; the checker establishes sharpness for all listed finite patterns but does not independently certify an infinite theorem or novelty. No assertion is made about maximum-likelihood degrees or the scheme structure of the parameter loci. Independent audit has not been performed.
