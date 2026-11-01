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

# Verification of the finite rotation obstruction

Run `python3 bp8_integral_rotation.py` in Python 3 with no third-party dependencies. The script generates all 65,535 nonempty arc subsets and retains all 196 valid simplices. It constructs exact mod-two cochain coboundaries by simplex inclusion, checks their ranks, computes the cohomology quotient, and verifies the 3-by-3 rotation matrix and its invariant dimension. The assertion checks are part of the executed program; the final printed line is `VERIFY_OK`.

The finite exact computation establishes the mod-two assertion only for the stated eight-vertex graph. The rational constituents require the published integral Betti numbers and the separate Lefschetz trace argument. The integral non-splitting then follows without further computation from the explicit two-dimensional fixed-space implication of any integral splitting. There is no independent audit or external certification.
