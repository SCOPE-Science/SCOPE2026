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

The analytical certificate consists of: (i) orthogonal cosine/sine Gram diagonalization giving the exact evaluator; (ii) a high-gap norm comparison for \(d\ge\pi\); (iii) \(|\sin(xd/2)|\le |x|\sin(d/2)\) for \(0<d<\pi\) and \(|x|\ge1\); (iv) positivity of \(F''(d)=4\sin d(\sin d-d\cos d)\) for \(0<d<\pi\); and (v) Taylor expansion of the explicit kernel at \(d=0\). Each critical identity and range appears in `RESULT.md`.

`CHECK.py` requires Python and `mpmath` and can be executed as `python CHECK.py` from the directory containing this file. The script was run at 65 decimal digits and completed with `PASS: 448 high-precision supplementary assertions`. It evaluates representative real gaps and points, exact maximizing representers, small-gap coefficients, and complex-coefficient Cauchy–Schwarz cases. These finite checks corroborate formulas; they are not an exhaustive or independent proof.

No independent mathematical audit has been performed. Comparison with inaccessible earlier literature is necessarily limited; this is an originality risk, not a numerical verification issue.
