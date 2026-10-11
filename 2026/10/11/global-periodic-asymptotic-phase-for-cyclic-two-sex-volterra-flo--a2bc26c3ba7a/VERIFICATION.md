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

# Verification and scope

The scientific result is a self-contained analytic theorem. To replay the decisive identities, form the symmetric bilinear offspring map from the \((1\pm\theta)/2\) coefficients in RESULT.md, define \(s=(x+y)/2\), \(d=(x-y)/2\), and use \(\sum s_i=1\), \(\sum d_i=0\). An actual SymPy expansion of all three components gave zero for each difference between the exact quadratic offspring map and its reduced expression. A separate symbolic expansion gave zero for the derivative of the product under the unforced cyclic field.

The check of the nonlinear bounds is elementary: the triangle inequality and \(|d_i|\le s_i\) imply \(|\partial_t\log H|\le2\theta De^{-t}\), while the resulting \(s_i\ge m_0\) implies the improved \(|\partial_t\log H|\le\theta D^2e^{-2t}/m_0\). Integration produces the exact numerical factors. The periodic phase argument uses a smooth transversal through the regular product levels and its associated coordinates, in which the flow is angular translation with an energy-dependent angular frequency. Differentiation gives growth at most linear in time, and integration against the quadratic forcing yields the claimed \(O((1+t)^2e^{-2t})\) tracking. The central maximum is nondegenerate and yields the separate \(O(e^{-t})\) estimate.

A numerical diagnostic used \(\theta=1/2\), \(s(0)=(1/2,1/3,1/6)\), \(d(0)=(1/15,-1/20,-1/60)\), and SciPy `solve_ivp` with relative tolerance `1e-11` and absolute tolerance `1e-13`. It observed positive coordinates and the expected decay. The numerical computation is **not** evidence for the universal quantifiers, uniqueness, or convergence rates; those come from the analytical proof above. No external certification or independent audit is claimed.

Limitations: the assertion excludes missing collective species, asymmetric offspring laws, higher-dimensional cyclic analogues, and discrete operator iterates. The preceding source comparison was same-model only; the 2024 Lobachevskii full text could not be checked. Scientific originality remains subject to independent inspection of that residual source and alternative terminology.
