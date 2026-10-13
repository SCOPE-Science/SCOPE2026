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
# Verification scope and commands

The analytic proof in `RESULT.md` applies to every integer \(n\ge2\) and every real \(0\le\varepsilon\le1/2\). The two-parameter Gram Schur spectrum and the exact chord interpolation are sufficient for the infinite statement; finite computations cannot substitute for that reasoning.

The package includes the standalone `verify.py`. Run `python3 verify.py`. It checks 7,804 exact-rational cases with Python's standard-library `fractions.Fraction` on all formula branches, endpoint values, the Schur complement, symmetric triangle inequalities, a discrete chord identity, small cut counts, and the explicit universal \(1/4\) gap witnesses. Observed result: `VERIFY_OK 7804 exact-rational tests`.

For an additional, independent check of the cut-polytope optimum, install NumPy and SciPy and run `python3 verify.py --lp`. This enumerates cut sign vectors for each \(2\le n\le6\) and solves 95 linear programs with leaf-marginal inequalities using HiGHS. Observed result: `LP_OK 95 independent finite linear programs` after the exact-rational checks. SciPy 1.17.0 was used for these optional checks. The LP solver is numerical; its output is not a proof of all parameter values or dimensions.

Critical proof steps that require mathematical inspection are (i) the averaging of feasible correlation matrices over leaf permutations, (ii) both eigenvalues of the Schur complement and the regular-simplex construction, (iii) the reduction of all triangle/perimeter inequalities, especially the \(n=3\) cap, and (iv) concavity and monotonicity of the piecewise-linear interpolation of \(k(n-k)\) on the relevant mean range. In particular, the cut comparator allows mixtures satisfying marginal constraints; it is **not** a deterministically constrained integer optimum.
