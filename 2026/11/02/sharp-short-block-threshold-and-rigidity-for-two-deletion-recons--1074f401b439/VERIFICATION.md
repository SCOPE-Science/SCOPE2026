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

Run `python3 verify.py` from this directory. The program uses Python 3 standard library and enumerates all Bell-number equality patterns of 6, 8 and 10 symbols. It constructs all distinct one- and two-deletion descendants, and checks all admissible pairs. There is no random truncation, external data, optimizer or package dependency.

Expected totals: 203/4140/115975 patterns at lengths 3/4/5, of which 133/3690/113073 are one-deletion distinguishable. The unrestricted maxima are 3/4/6 and the two-symbol maxima are 2/4/4. The only canonical length-five six-maximizer is `(0,1,2,0,1 | 1,0,2,1,0)`. The full length-five intersection histogram is `(87171,20663,4605,541,86,6,1)`.

A second direct enumeration over the full sets of alphabet-three, -four and -five length-five words confirms exactly 3, 12, and 30 unordered six-intersection maximizers. The separate witness checks cover the length-four, length-five binary/nonbinary and length-six binary cases. The elementary length-three witnesses can be inspected by hand. The reported final marker is `SHARP_TWO_DELETION_RIGIDITY_VERIFY_OK`.

The infinite upper bound is inherited from the cited Sun–Ge theorem, while indefinite-length attainment follows from common-prefix extension and the LCS identity; the finite test alone is not a proof at unbounded lengths. The computation is subject to source correctness and runtime integrity.

No independent audit has been performed.
