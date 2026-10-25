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

Run `python3 verify_bwt_n8.py` using Python 3 with the standard library. The checker exhausts all 70, 420, 420, 420, and 2520 order-reduced profile candidates after the proved even-content restriction, checks the one-cycle criterion and Hamming distance, and asserts the exact six output patterns. A second route directly enumerates the 65,280 primitive four-letter source words, computes the cyclic input runs from the source, sorts their rotations, and computes the BWT. Both routes must agree and finish with `VALIDATION_OK`. A further direct check counts original-length-eight primitive BWT images for alphabet sizes three and four.

The reduction to five profiles and the proof of the odd-block fixed-point obstruction are in RESULT.md. The direct finite checks do not establish analogous theorems at other lengths. Independent external verification was not performed.
