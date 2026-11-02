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

Run `python check_power_norms.py` in Python 3, standard library only. The implementation evaluates \(\operatorname{Ces}_2\) norms for finitely supported complex sequences using the exact \(\zeta(2)=\pi^2/6\) tail formula. It compares six scalar shift powers, three different spherical branching profiles, and random complex vectors to the proposed \(p=2\) zeta ratio; it also tests same-phase exact attainment. The verification run reported 2,118 assertions passed. Numerical tolerances account for floating-point arithmetic.

# Mathematical verification

The nonnumerical proof in `RESULT.md` independently establishes: (i) the reverse weighted-covariance inequality for all \(1<p<\infty\), (ii) strict equality characterization for every integer power, (iii) the exact tree descendant-mean inequality, (iv) equality at the root by the triangle inequality, and (v) the integral-test power asymptotic and Gelfand spectral-radius formula. No numerical finite test is asserted to imply an infinite-dimensional result.

# Remaining limits

The method relies on spherical homogeneity and does not handle general edge weights or nonuniform children counts by vertex. Publication priority of any implicit older exact classical Cesàro shift identity has not been independently certified.
