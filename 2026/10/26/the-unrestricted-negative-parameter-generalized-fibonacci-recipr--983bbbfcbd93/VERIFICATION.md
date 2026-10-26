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

# Verification of the negative-parameter reciprocal-tail floor

Run `python3 verify.py` with standard Python 3. The program reconstructs each integer recurrence from its defining initial conditions without floating-point arithmetic. Its two comparisons use the exact rational partial sum \(L=\sum_{k=n}^{K}1/U_{rk}\) with \(K=n+60\) and the explicit rational upper bound

\[L<S_{n,r}<L+\frac{q}{(q-1)U_{r(K+1)}},\qquad q=(s-1)^r\ge2.\]

The tail bound follows because the Binet expression gives \(U_{r(k+1)}/U_{rk}>\alpha^r\ge(s-1)^r\) for every \(k\ge1\). For each checked parameter tuple it verifies \(L>1/D\) and, when \(D>1\), the upper bound is less than \(1/(D-1)\), where \(D=U_{rn}-U_{r(n-1)}\). If \(D=1\), the latter inequality is unnecessary and \(S_{n,r}^{-1}>0=D-1\) follows automatically.

Exact finite test set: all \(3\le s\le18\), \(1\le t<s\), \(1\le r\le5\), \(1\le n\le10\), giving \(7600\) parameter quadruples. Expected ending message: `VERIFY_OK 7600 parameter/index quadruples with rational upper/lower bounds`.

The mathematical proof in `RESULT.md` establishes the theorem for infinitely many parameters and arbitrarily large indices by a separate uniform analytic bound. The finite verifier is a consistency check only, not evidence of exhaustive coverage of all integer parameters. No independent audit has been performed.
