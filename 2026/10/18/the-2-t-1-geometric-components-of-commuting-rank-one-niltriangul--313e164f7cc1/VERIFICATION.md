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

# Verification scope
The proof is given in `RESULT.md`, including the full list of minors, commutator equations, component incidence descriptions and finite-field stratification. The standalone `verify_rankone_n4.py` computes every rank condition through literal \(2\times2\) minors and commutation through full \(4\times4\) products. It does not infer commutation from the claimed component description or use the claimed finite-field formula to generate tuples.

Run `python3 verify_rankone_n4.py` with Python 3 and no third-party modules. Tested \((q,t)\) pairs are \((2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,1),(4,2),(5,1),(5,2)\). The finite field of four elements is implemented independently using its quadratic polynomial. All eleven cases passed; \(q=2\), \(t=2,3\) additionally passed exhaustive union coverage and unique-component-witness checks. The final success marker was `VERIFY_OK_TRIANGULAR_RANKONE`.

The calculations exhaust only these finite instances. The arbitrary-field component proof, arbitrarily long tuple theorem, and formula for every prime power rest on the direct symbolic arguments in `RESULT.md`. Independent mathematical audit has not been performed.
