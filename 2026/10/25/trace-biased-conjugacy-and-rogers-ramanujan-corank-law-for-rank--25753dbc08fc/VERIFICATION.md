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
# Verification details

The proof reconstructs each rank-one idempotent two-sided averaging operator \(P:M_n(k)\to M_n(k)\) as a unique pair \((E,C)\) with \(P(X)=\operatorname{tr}(CX)E\), \(E^2=E\ne0\), \(EC=CE=C\), and \(\operatorname{tr}C=1\). Its finite-field enumeration and trace-one similarity-orbit count use complementary-subspace flags and an additive-character Euler product. Its asymptotic law follows from dominated convergence and the classical Rogers–Ramanujan identity. These are written arguments for all the stated fields and dimensions.

Run `python3 check_averaging.py` with Python 3 standard library. It tests both averaging identities and idempotence on all matrix-unit pairs for all normalized rank-one maps on \(M_2(\mathbb F_2)\) and \(M_2(\mathbb F_3)\). It also enumerates characteristic and minimal polynomials of all matrices of sizes one through three over those prime fields. The computations match the formulas for exact operator counts and trace-one similarity-class counts and conclude with `RANK_ONE_AVERAGING_AND_TRACE_CLASSES_OK`.

The executable is supplementary finite-field evidence, not an infinite proof or independent audit. Prime-field arithmetic in the checker does not directly verify extension fields, which are instead covered by the written field-independent arguments. Full publication priority, positive-characteristic scheme structure, and any higher operator rank remain unverified or outside scope.
