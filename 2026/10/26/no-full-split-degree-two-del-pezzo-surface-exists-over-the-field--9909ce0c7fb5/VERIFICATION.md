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

# Verification of the thirty-seven-element obstruction

The included self-contained Python program `verify.py` uses only integer arithmetic, not computer algebra or data tables. Run `python3 verify.py` with Python 3. It checks the incidence normalization, the maximum \(6h+2e\) over all nonnegative \(h,e,f\) satisfying \(6h+3e+f=378\) and \(h\le21\), the surface rational point count, and the strict Hasse lower bound via squaring positive integers. Successful output is `VERIFY_OK: 28 bitangents, max incidence 294, branch points >=2, fullness impossible at q=37`.

This program **does not** prove the geometric input \(h\le21\) independently, does not enumerate quartics over \(\mathbb F_{37}\), and is not an independent scientific audit. The non-elementary premises are: Kowalevskaya/Kuwata's four-bitangents/involution criterion valid for characteristic different from two; the maximum 21 involutions on a smooth complex genus-three curve; and tame lifting of the automorphism action in characteristic 37 (Dolgachev--Martin). The proof derives the fullness equation anew from incidence and fiber counts, so no numeric empirical evidence is used to justify an infinite family claim.
