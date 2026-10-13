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

# Verification scope

Run `python verify_rescue.py` from a directory containing the standalone checker. The script uses only standard-library modules and a fixed pseudo-random seed. It evaluates the exact global envelope of the amplified quadratic at the two interval endpoints and its internal vertex if present. It cross-checks 1,600 bands, 19,200 alternative positive correction steps, 1,200 exact-rational endpoint balancing identities, the wide-band stability boundary, and sample large-frequency limiting cases. A successful execution prints a `VERIFY_OK` status. The script independently implements the proposed formula but its finite examples are not a formal or exhaustive mathematical proof.

The proof in `RESULT.md` is the basis of the universal conclusion. Neither a machine formalization nor independent expert review has been performed. The verified source publication date is the original article's electronic publication date, not the later arXiv upload. Historical originality depends on inspected sources and leaves open the possibility of equivalent less-indexed approximation-theory work. The slow-cluster corollary is only a nonexpansion conclusion under the stated SPD separated-spectrum condition; it supplies no nonnormal or floating-point bound.
