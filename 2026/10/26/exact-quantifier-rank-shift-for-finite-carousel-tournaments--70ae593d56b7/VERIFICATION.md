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

The companion file `verify_carousel.py` is reproducible using the Python standard library; run `python verify_carousel.py`. The stored `verify_carousel_output.txt` contains the successful run output ending with `VERIFY_OK`.

The verifier checks the six anchored edge rules by direct modular arithmetic for \(1\le m\le75\). Direct recursive atom-type signatures for unlabelled tournaments are checked at ranks one through four through 35 vertices, and rank five through 13 vertices. Independent direct linear-order signatures are checked at ranks one through four, and the claimed arithmetic threshold partition is checked for ranks one through nine and index pairs between one and 99.

The unbounded assertion is proved by the anchored-game and outneighborhood-interpretation lemmas in `RESULT.md`; finite checks alone do not establish it. No machine-checked proof, independent audit, or exhaustive historical novelty guarantee is claimed.
