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

# Reproduction and evidence

The analytic proof uses only a log-odds transformation, exact inversion of the affine belief update, the elementary inequality \(x(1-x)\le 1/4\), and Taylor expansions of \(\log((1+2u)/(1-2u))\) and \(\operatorname{arctanh}(d)\). It covers every parameter in the declared domain and every output in the extended strip. There is no reliance on finite enumeration to prove global inverse counts.

Run `python check_fold.py` with Python 3 and `mpmath` to verify the exact physical three-preimage example numerically at 70 digits and check the fold width and orientation. The output ends with `ALL EXACT / HIGH-PRECISION ASSERTIONS PASSED` on the tested environment. Exact algebraic cross-checks of the determinant, cubic coefficient, and rational example were also carried out using symbolic algebra. The public script is diagnostic, not an independent certificate. The source-map equation is in [1], Section 2, and the proof is self-contained in RESULT.md.

The extension to arbitrary real \(q\) is mathematical; its full-range inverse counts are not universal fiber counts on the bounded physical rectangle. No computation or proof here establishes chaoticity, global attractor classification, or historical uniqueness. The external independent audit has not been performed.
