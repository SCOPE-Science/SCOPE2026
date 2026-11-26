---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The literal original N≤5 domain included N=1, at which the specified Simpson score is 0/0; a singleton comparison set is not a defined index. The replacement states N≥2 and distinguishes the lone unscored N=1 profile. For fixed N, entropy decreases with the product of n_i^n_i, and both Simpson conventions decrease with sum n_i² (D_pop = (N−1)D/N). I independently generated sorted multisets of entries 1,…,N of all lengths 1,…,N, retained sum N, and compared integer signs on every unordered pair. For N=2,…,7, the partition counts are 2,3,5,7,11,15; disagreements 0,0,0,0,2,4; strict reversals 0,0,0,0,0,2. At N=6 the keys (entropy product, collision sum) are (256,12) vs (729,12), and (27,6) vs (64,6). At N=7 the reversing keys are (3125,20) vs (6912,18), and (256,12) vs (432,10). The replacement states those exact results, with the correct Simpson fractions and directions. The existing support already uses N≥2 and remains applicable.

## originality

PASS

Best of current knowledge, the supported contribution is the exact first weak and strict disagreement layers for integer censuses without a fixed-richness constraint. Neither the order-1/order-2 reparametrization, known majorization comparisons, a size-100 reversal, nor the closest fixed-richness Resultary theorem supplies those layers. The domain correction removes only an undefined endpoint and preserves this claim.

## value

PASS

The two classic diversity scores answer different concentration questions but cannot disagree at every discrete resolution. The exact first tie-only layer and first opposite strict layer, with all minimal witnesses, give usable small benchmark cases for comparative rankings or counterexamples and separate genuinely opposite judgments from ties. The domain fix does not change either boundary or its witnesses. The gain is a motivated finite classification, not a claim of deep or practical ecological significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
