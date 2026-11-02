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

# Reproducible verification

Run `python3 verify.py` with a standard Python installation and no external packages. The checker verifies exact rational-moment equalities for all \(560\) distinct ordered triples from a fixed interior rational lattice, the impossibility of two negative quadrature weights in those cases, all four possible sign patterns, the analytical sign-law integrals against separate midpoint integrations, the coefficient \(12\int_0^1(x^2-x+1/3)\,dx=2\), and the exact hyperbola-area identity. A seeded Monte Carlo simulation of \(250{,}000\) independent triples compares observed sign frequencies to the derived values; its tolerances are diagnostic.

The complete proof is given in `RESULT.md`. Enumerating finitely many rational nodes and sampling finitely many random triples cannot establish statements for all real nodes or an asymptotic tail limit. The proof, rather than checker output alone, establishes those claims. Independent scientific verification has not been performed.
