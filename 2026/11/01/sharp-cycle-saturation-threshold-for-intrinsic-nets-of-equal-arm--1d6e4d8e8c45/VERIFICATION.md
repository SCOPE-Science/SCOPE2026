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
# Verification and limitations

The analytical proof in `RESULT.md` establishes the universal claim. The standalone `check_cover.py` uses exact rational arithmetic and reconstructs intrinsic graph distances from candidate routes through the two common poles, with optional paths along a shortest alternative arm. It exercised 344 parameter configurations and 414,723 discrete point/obstruction checks, including exact equality-threshold cases and strict-threshold symbolic inequalities. Run it with `python3 check_cover.py`; it needs only Python's standard library.

The finite checks are not an exhaustive enumeration of arbitrary positive real lengths and do not independently certify originality. No external independent audit has been performed. The radius in the strict regime is not computed. A potentially relevant older full-length publication was inaccessible for full-text priority inspection, although its bibliographic record and abstract were checked.
