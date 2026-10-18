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

# Verification and reproducibility

Run `python verify.py` with Python 3. This executes modular binomial-coefficient checks across 413 admissible parameter triples in characteristics 3, 5, 7, 11, 13 and 17 and reports six highlighted examples. No external dependencies or downloads are required.

The essential infinite argument is the exact identity \((1-bz)^a(1+az)^b=(1-a^2z^2)^a(1+az^{p^e})^c\), valid for \(b-a=p^e c\), \(p\nmid ac\), in characteristic \(p\). The code tests its consequences for finite instances but does not certify all cases. The proof checks the image algebra, global normalization, singular support, Jacobian thickness, and conductor independently of enumeration.

Self-review has examined the proof and run the packaged checker. No independent audit has been performed. The cited literature concerns the characteristic-zero normalization and singular-support theory, and possible uncatalogued positive-characteristic overlap remains unexcluded.
