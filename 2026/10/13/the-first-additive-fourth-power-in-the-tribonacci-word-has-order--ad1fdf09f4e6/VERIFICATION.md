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

Run `python3 verify.py` beside `certificate.json`.

The script builds \(\sigma^8(0)\) both by direct morphism iteration and by the finite Tribonacci recurrence, obtaining the same length-\(149\) prefix.

For each candidate order \(n=1,\ldots,6\), it reconstructs every observed factor of length \(4n\). The observed factor counts are \(9,17,25,33,41,49\), which equal the published Tribonacci complexity values \(2(4n)+1\). Thus the factor lists are exhaustive once the published complexity theorem is invoked.

The checker then splits every factor into four equal blocks and recomputes their integer symbol sums. It verifies that no factor qualifies at orders \(1\) through \(5\), while exactly one qualifies at order \(6\). It checks the exact factor, its four blocks, their common sum \(4\), and its first occurrence in the certified prefix.

The finite computation is not extrapolated beyond the six stated orders. Independent audit has not been performed.
