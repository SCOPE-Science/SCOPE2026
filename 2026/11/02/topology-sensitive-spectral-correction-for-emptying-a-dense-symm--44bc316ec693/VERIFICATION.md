---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With one root reservoir at injection p=1−q and removal q, the reversible stationary measure is Bernoulli product and empty mass q^N. Renewal cycle empty Exp(p) followed by root-one-particle excursion gives exact E[B]=(q^{-N}−1)/p. At q=0 full occupancy is the sole nonempty recurrent configuration; the killed finite generator has isolated zero eigenvalue and all other modes have a uniform spectral gap for fixed G. First-order right-eigenvector perturbation solves a killed one-particle occupation Poisson equation: at entrance a, h_q(a)=1−qT_G+O(q²) with T_G=[(D_o−L_G)^−1]_{oo}. Exact reversible boundary-flux identity then yields λ_q=p q^N (1−qT_G+O(q²)), and spectral separation gives q^N B ⇒ Exp(1) with all positive moments. Independent Markov generator code, different from package code, solved killed first passage means and eigenvalues on path P3 (endpoint/root center) and star S4 for q=.035,.07; mean exact to numerical tolerance, scaled eigenvalue matches first correction to O(q²). Independently computed T_P3=5/3, T_P3-center=1, T_S4-center=2/3. The result is fixed graph only; no uniform-in-N claim.

## originality

PASS

Best-of-knowledge originality after inspecting the assigned theorem, searching the relevant published Resultary findings and primary literature, and comparing equivalence, broader results, exact tables and logical implications. Prior leading power q^N and steady tagged waiting do not imply the q-correction without eigenvector occupation-potential calculation. A detailed unpublished/unchecked Appendix of 2609.32314 remains capable of covering it. A more general Markov perturbation theorem would offer a route to derive the coefficient; no inspected source directly evaluated the root-dependent resolvent for this excursion. Because same-paper full text is inaccessible, O is best-of-knowledge rather than categorical exclusion. Priority is not certified; the named residual source-access and prior-coverage risks remain.

## value

PASS

The exact mean and leading exponential law are natural consequences of renewal/metastability, but the first nontrivial spectral coefficient is a resolvent of a killed walk and depends on branch topology/root position. This separates identical-size branches whose mean excursion time coincides, providing a motivated quantitative refinement of rare-event lifetimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
