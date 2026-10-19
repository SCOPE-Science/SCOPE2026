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

The exact mathematical proof is contained in `RESULT.md`; no simulation substitutes for the universal theorems. Run `python3 check.py` in the directory containing the two files. This standard-library program (a) supplies distinct finite-support laws with positive exact rational weights, matched means and matched Laplace transforms at two distinct positive rates; (b) numerically reconstructs the transformed recovered duration from the endemic equilibrium response; and (c) checks the stated pair of distinct infectivity laws. The finite-support test is an algebraic illustration of indistinguishability, NOT an admissible smooth-hazard witness. The theorem's admissible smooth witnesses are obtained by the explicit bump-function nullspace construction in `RESULT.md`.

The sharp finite-mixture threshold is analytic: rational numerator degree, pole/residue uniqueness, a full-row-rank confluent Cauchy Jacobian, and the implicit function theorem. The unrestricted smooth-law uniqueness proof uses holomorphy of a Laplace transform and the compact moment problem. The program checks examples and algebraic inversion only; it is not independent certification or a test of all dimensions, all densities, or real-data robustness. Numerical and statistical stability are not established.
