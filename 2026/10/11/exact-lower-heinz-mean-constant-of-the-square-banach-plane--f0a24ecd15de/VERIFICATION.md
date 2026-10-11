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
# Verification

The claim is proved analytically in `RESULT.md`. The critical checks are:

1. Signed-coordinate permutations reduce every \(x\in S_{\ell_\infty^2}\) to \((1,a)\) with \(0\le a\le1\).
2. For \(x=(1,a)\), the witness \(y=(1,-1)\) gives the norm pair \((2,1+a)\), hence a value at least \(M_\nu(2,1)\).
3. For the axis point \(x=(1,0)\), every unit \(y=(u,v)\) gives an unordered pair \((A,B)\) with one entry at most \(1\) and both at most \(2\). Monotonicity of \(M_\nu\) gives the matching upper bound.
4. Equality at the axis is realized by \(y=(1,1)\), which yields exactly \((A,B)=(2,1)\).

The included `verify.py` performs supplementary finite-grid checks for representative parameters. Those computations are not used as proof of the universal statement.
