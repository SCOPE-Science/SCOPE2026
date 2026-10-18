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
The proof is entirely analytic and covers every real \(a\in(0,1)\) and every pair \((\ell,u)\in[0,a]^2\). Its critical checks are: (i) exact section-based upper bounds; (ii) equality of restricted coordinate marginals before and after both patches; (iii) preservation of the full section, including its endpoint by continuity; (iv) the comonotone coupling's upper-tail intersection mass, equal to the minimum of its two terminal marginal masses; (v) explicit corner probabilities for every sufficiently small \(\varepsilon\), with no assumption that the two patches are disjoint.

The standalone `check_tail.py` executable was run with Python's standard-library `fractions.Fraction`. It passed **26,912 exact rational assertions** across five grid resolutions, all nontrivial rational square widths, and sixteen lower/upper mixing pairs per width. It independently checks the finite two-stage measure calculation and section preservation with overlapping squares. Finite checkerboards are not used to infer an infinite limit; the continuous quantile-coupling argument supplies it.

Relevant source comparisons include full substantive sections of Xie–Zou (2026), the primary 2008 section-construction paper included in Saminger-Platz's habilitation compilation, the 2009 rectangular-patchwork primary article, and de Amo et al. (2013). The 2011 joint diagonal/opposite diagonal paper was accessible by abstract only, which leaves residual priority risk. There is no independent validation or external certification.
