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
# Verification notes

The mathematical proof is analytic and does not depend on a finite search. `verify_first_correction.py` checks three reproducible finite items: the archimedean integral identity \(\int_1^2\log u\,du=2\log2-1\), numerical values of the coefficient \(\log(2/\pi)-1+2\zeta'(\sigma+1/2)/\zeta(\sigma+1/2)\), and convergence of the prime cutoff \(\sum_p\log p/(p^s-1)\) to \(-\zeta'(s)/\zeta(s)\) for several \(s>1\).

The finite cutoff is not a certificate of the infinite Dirichlet-series identity; that identity follows from the absolutely convergent Euler product for \(\zeta(s)\) when \(s>1\). The program output is therefore a normalization check only.

Unproved here: any estimate uniform as \(\sigma\downarrow1/2\), any support extension, and any second finite-height correction.
