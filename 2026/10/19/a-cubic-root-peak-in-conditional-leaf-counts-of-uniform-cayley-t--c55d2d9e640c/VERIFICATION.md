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

Use a Python 3 interpreter without dependencies:

```text
python3 tree_leaf_distance_verify.py
```

The checker reconstructs every Prüfer code for \(n=3,4,5,6,7,8\), totaling exactly \(280{,}391\) labeled trees. It compares each empirical distance law and each conditional mean against the stated exact rational expressions. It compares consecutive conditional means with the predicted cubic-ratio expression for \(n=3,\ldots,180\), conducting \(15{,}931\) exact differences. Equal neighboring maxima in this interval occur only at \((n,k)=(3,1),(10,2),(25,3),(51,4),(91,5),(148,6)\). Floating-point covariance checks at \(n=100,1000,10000\) have ratios approximately \(-0.166317,-0.208295,-0.223283\), consistent with the proved limit \(-0.2305342522\ldots\). All packaged checks passed.

The exact-rational finite checks do not certify results outside the finite range. The proof uses path-extension counts and a sign comparison for the all-size theorem, together with a moment-controlled Rayleigh limit for the asymptotic theorem. An external independent audit has not been performed.
