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

The standalone `verify.py` reconstructs the claim from the definition using exact integer arithmetic and standard-library code only.

Checks performed:

- all \(\binom{16}{8}=12870\) eight-word subsets are tested and none satisfies the \(B_2\) condition;
- all \(\binom{16}{7}=11440\) seven-word subsets are tested, yielding exactly \(240\) maxima and \(105\) containing \(0000\);
- all \(384\) standard Hamming isometries are generated explicitly;
- the \(240\) maxima are partitioned into exactly two orbits of sizes \(192\) and \(48\);
- the representative stabilizers are counted directly as \(2\) and \(8\), matching orbit–stabilizer;
- the pairwise Hamming-distance profiles are checked on every orbit member;
- the literal maximum census has SHA-256 `70fcbc9fe5012988adc0a84cf0a312248763e502a8e22e19cd041809520cd6db` under the serialization implemented in `verify.py`.

A successful replay ends with `VERIFY_OK`. The computation proves only the stated finite length-four classification. It does not certify any statement for larger dimensions or any equivalence group larger than the standard Hamming-isometry group.
