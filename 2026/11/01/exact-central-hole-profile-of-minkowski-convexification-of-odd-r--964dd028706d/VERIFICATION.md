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

# Reproduction and limitations

Run `python3 verify.py` in an environment containing Python 3.10+ and `shapely>=2`. The script constructs polygonal vertex translates and their union geometrically, checks their areas against the derived closed form for several odd polygon orders and numerous parameters, checks the ratio identity, and confirms an outer-facet omission for a test dilation below one. It raises an exception on any failed comparison and prints the number of completed checks. This is a finite numerical consistency check, not an exhaustive search and not a proof for all orders and real dilations. The analytic sector-coverage argument in `RESULT.md` supplies the universal result. Independent verification by an external reviewer has not been performed.
