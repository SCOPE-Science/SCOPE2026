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

# Reproducibility

Run `python3 verify_dickson_2adic_images.py` with Python 3, standard library only.

The verifier independently computes complete residue images for every \(2\le r\le9\) and \(1\le k\le16\) (128 cases), plus \(2\le r\le5\) at \(k=17,18\) (eight cases), then compares both sets and cardinalities with the exact three-ball formula. The largest exhaustively iterated input domain has \(2^{18}\) elements. It checks center gaps and the stable-density arithmetic through \(r=14\).

Expected checked-package output:

```
VERIFY_OK grid_cases= 128 deep_cases= 8 maximum_r=14 maximum_direct_modulus=262144 image_sets_exact=True density_arithmetic=True
```

No finite computation can prove the all-\(r\), all-\(k\) theorem. The proof is the exact base partition, the isometric polynomial-map lemma, and an induction on ball images in RESULT.md. This verification is not an independent audit.
