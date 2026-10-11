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
# Reproducibility of the signed-cycle \(\ell_4\) limit

The proof in `RESULT.md` is analytical. There is no external theorem prover or inaccessible calculation required. The exact identity \((a^4+b^4)/2=m^4+6m^2d^2+d^4\), and the two cases of the transformed-gradient inequality, can be expanded directly over rational variables. The attached `verify.py` checks these identities and inequalities over a finite integer grid with exact fractions as diagnostics, and evaluates the displayed trial vectors at five sizes. Run with `python3 verify.py` in the directory containing both files.

The critical infinite steps are not delegated to the script: the minimizers exist by finite-dimensional compactness; the transformed energy bounds piecewise-linear interpolants in \(H^1\); weak lower semicontinuity and the vanishing derivative on the zero level set recover coefficient \(3/8\); the antiperiodic Poincaré bound is sharp; and the sampled cosine supplies recovery across a zero. These steps prove \(ne_n\to3\pi^2/8\) and the resulting operator-norm asymptotic. The scope excludes exact finite-dimensional optimization and all unspecified scalar fields.
