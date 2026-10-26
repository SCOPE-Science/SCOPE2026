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

# Arithmetic verification

`verify_polynomial.py` independently constructs the coefficients of the fourth power of the normalized quartic needed for its diagonal Hasse–Witt matrix and confirms all three displayed polynomial factorizations.

`verify_f25.py` iterates all \(15625\) ordered coefficient triples in \(\mathbb F_5[v]/(v^2-2)\), checks the exact geometric smoothness conditions, computes \(5\)-rank from the three Hasse entries, and verifies the elliptic-quotient polynomial identity.

`verify_quotients.py` independently iterates \(\mathbb F_{25}\) represented as \(\mathbb F_5[w]/(w^2+w+1)\), obtains the invariant from quartic elliptic quotient models, and checks the full rank table and the restriction to \(\mathbb F_5\). All three scripts run successfully using only Python 3 standard library.

The geometric characterization of the superspecial locus follows from the differences of the three Hasse polynomials and the smoothness inequalities, followed by factorization \((a-2)^2(a^2-2a-2)\); it does **not** depend on exhaustive enumeration of algebraic-closure points.

These are complete reproducible checks of the stated algebraic and finite arithmetic steps. They do not certify originality against every possible earlier source, nor do they constitute an independent external audit.
