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

# Reproducibility and scope

Run `python3 verify_forest_modules.py` using Python 3.9 or newer, with no third-party dependencies. The program enumerates the permitted forest faces both by a closed multipartite criterion and by an independent union--find acyclicity test; builds mod-two simplicial boundary ranks; enumerates the complete size-preserving part-symmetry groups of eleven examples; computes the reduced signed simplicial Lefschetz sums; and compares those sums with the stated integral characters.

Its output must match `verification_output.txt` and end with `VERIFY_OK`. All **2,238 automorphisms** in the eleven listed cases are checked, not sampled. Cases include \((1,1,1)\), \((1,1,1,1)\), \((1,2,3)\), \((1,1,2,2)\), \((2,2)\), \((2,3)\), \((2,2,2)\), \((2,3,3)\), \((3,3,3)\), \((2,2,2,2)\), \((2,3,4)\).

The finite check establishes neither uniqueness in the literature nor the full integral theorem. It verifies small instances and the full finite symmetry character in those instances. The proof of the unrestricted integral claim is given by the Mayer--Vietoris and cover-nerve argument in `RESULT.md`; it does not rely on experimental extrapolation. Independent mathematical audit has not been performed.
