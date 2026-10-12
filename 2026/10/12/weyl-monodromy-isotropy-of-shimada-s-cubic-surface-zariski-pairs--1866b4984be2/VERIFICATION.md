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
The included `artifacts/verify.py` reconstructs Shimada's six permutations on \(27\) line labels and verifies the full finite calculation.

It checks:
- \(|W(E_6)|=51840\);
- stabilizer orders \(120,240,120,120\);
- pointwise-kernel orders \(1,2,1,1\);
- induced image order \(120\) in every marked arrangement;
- the exceptional kernel generator is \(\sigma_6\);
- \(\sigma_6\) is central in the \(S_2\) stabilizer;
- the derived subgroup there has order \(60\);
- an explicit involution yields a disjoint complement of order \(120\).

The expected final line is `VERIFY_OK`. This is an exhaustive finite calculation in the published permutation representation. It does not verify or claim projective automorphism groups of individual cubic surfaces.
