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

The exact formulas follow from the explicitly stated boundary-value problem and renewal calculation. The global unfavorable-anchor inequality is a strict Cauchy–Schwarz inequality for \(\cosh u\) and \(\operatorname{sech}u\) on every nontrivial interval, while the fresh-anchor global favorable inequality follows from the positive partial-fraction representation of \(\coth z\). The Laplace comparison follows from strict concavity of a rational transform and Jensen's inequality.

The standalone `verify.py` was run using Python with only its standard library and reported 94 passing numerical assertions. Its independent finite-difference Laplace boundary-value solution, trapezoidal integrals, sampled strict signs and endpoint asymptotics are reproducible by invoking `python verify.py` in the same directory. A finite grid does not prove any universal statement, so the mathematical proof is in `RESULT.md`; the script tests only numerical consistency. The endpoint expansion coefficients were independently compared with symbolic Taylor expansions. The distributional comparison is a Laplace-transform order, not ordinary stochastic dominance.

The scientific novelty assessment is provisional. The elementary renewal framework and individual reset protocols are available in prior literature; the claim is restricted to their global uniform-ensemble contrast and its sharp consequences. Independent mathematical and publication-priority audits have not been performed.
