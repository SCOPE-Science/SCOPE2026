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

# Reproducibility and verification

Run the standalone, dependency-free `checker.py` from a directory containing that file with `python checker.py`. It fully enumerates all binary incidence matrices of shape \(m\)-by-\(n\) for \(m,n\ge1\) and \(m+n\le6\), discards disconnected graphs and matrices with isolated vertices, groups by both guilds' sorted degree multisets, and compares every exact conditional extinction-count histogram for \(k=0,\ldots,n\) deleted pollinators. Completeness rests on examining every one of the \(2^{mn}\) bitmasks for each admissible shape.

Observed output:

`VERIFY_OK labeled_connected_small=387 matched_degree_profiles=44 seven_species_trees=2 moment_polynomial_identities=3 exact_probability_tests=4`

For the seven-vertex witness, the code recomputes each of the two graph incidence matrices and symbolic extinction-count probability polynomials, checks mean equality, checks \(\Delta V=2q^2(1-q)^2\), checks \(\Delta m_3=6q^2(1-q)^2(1-q-q^2-q^3)\), and confirms four exact rational parameter instances. The proof in `RESULT.md` establishes the universal identity for any exchangeable deletion law (not just iid) and the strict sign of the polynomial away from its unique positive root; neither conclusion is extrapolated from the finite numerical checks. Only the six-vertex minimality part uses exhaustive finite computation.

No independent external audit or validation is claimed.
