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

Run `python3 VERIFY.py` using only the Python 3 standard library. The checked result is:

`VERIFY_OK general_sequences=1359 multiplier_pairs=65025 sharp_families=25`

The verifier constructs weighted coefficient vectors, applies synchronous carrying via independently written quotient-remainder and per-index accumulation updates, checks exact weighted-sum conservation, and tests the asserted stopping-depth inequalities. General-sequence tests cover all nonzero length-one-to-five vectors with entries from \(\{0,1,2,3\}\). Factor tests cover all ordered \((a,b)\) with \(1\leq a,b\leq255\). Sharpness examples cover every odd \(k\) from 3 through 51. These are finite correctness checks and do not validate arbitrary-size inputs; the published mathematical proof in `RESULT.md` supplies the universal induction.

The originality review examined Iizumi's definitions of the same mathematical model and open question in publisher-indexed full-article material, compared the distinct randomized carry-chain literature, and searched available public research records. The direct publisher page could not be fetched reliably, leaving an explicit source-access risk; no unrelated research source is silently certified by the finite checker. Independent audit status remains `not_performed`.
