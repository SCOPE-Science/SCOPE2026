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

The structural criterion was replayed against the literal definition for every complete multipartite part-size profile with at least two parts and total order at most \(8\), covering \(1,653,904\) labelings. For every profile, an independent multinomial profile enumerator was compared coefficient by coefficient with the brute-force weight distribution, and the minimum weight was compared with \(\min\{4,\max\{2,\min_i n_i\}\}\).

Exact output:

`VERIFY_OK profiles=58 assignments=1653904 coefficient_checks=818 max_order=8`

The computation checks finite instances only. The proof supplies the quantifiers for arbitrary nonempty part sizes and any number of parts \(r\ge2\).
