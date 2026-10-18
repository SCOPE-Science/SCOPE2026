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

Execute `python verify.py` and `python verify_orbits.py` in a Python environment with SymPy installed. These are independent complete parameter-space traversals; no saved raw census is required as an input. The programs have distinct eleven-generator constructions and use different Gröbner monomial orders. Every finite computation is over \(\mathbf F_2\); Gröbner ideal properness is equivalent to the existence of a geometric singular point over the algebraic closure, so testing the four charts is a genuine geometric test, not finite-extension sampling.

The first program's JSON output is stored in `verify_output.json`. It reports \(11\) filling parameters, \(2047\) nonzero filling sections, \(364\) sections nonsingular at all nine rational points, \(66\) geometrically smooth sections, \(27\) distinct rational tangent patterns, and the pair spectrum \(\{3:642,5:981,7:468,9:54\}\). It also reports \(512\) rationally nonsingular pencils, \(272\) with no geometrically smooth member and \(240\) with exactly one, with zero all-smooth pencils.

The second program's JSON output is stored in `verify_orbits_output.json`. It independently reports the identical histogram and \(27\) patterns, confirms \(66\) smooth forms and four polarized projective-coordinate orbit sizes \(6,6,18,36\). Projective action checks are secondary cross-checks, not replacements for the exhaustive chart singularity test.

Reproducible mathematical implications: distinct smooth sections \(F,G\) over \(\mathbf F_2\) have nonzero equal local gradients at every shared-tangent rational point; \(F+G\) vanishes with zero differential there. Each nonzero third pencil member is therefore singular. No statement about fields other than \(\mathbf F_2\) or smoothness at all members over an algebraic closure is implied.

Independent external mathematical validation and bibliographic priority certification have not been performed.
