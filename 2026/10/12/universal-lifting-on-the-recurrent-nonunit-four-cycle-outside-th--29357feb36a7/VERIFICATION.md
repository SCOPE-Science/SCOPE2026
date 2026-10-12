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

The proof was checked at two levels. First, the four quotient identities and the returned-conic identity were expanded exactly as polynomial identities by `verify.py`. Second, the nonvanishing step was checked symbolically through the discriminant reductions
\[
(c-2)^2-c(c-4)=4,\qquad (c+2)^2-c(c+4)=4.
\]
For integer \(c\ge2\), a square discriminant for \(P_0\) or \(P_2\) would give two positive same-parity factors of \(4\), forcing \(c=4\). A square discriminant for \(P_1\) or \(P_3\) would force \(c=0\), outside scope. Thus for \(c\ne4\) all four quotient coordinates in one cycle are nonzero. The exact returned-conic identity then permits induction without any finite-search assumption.

The verifier also checks directly that \((c,x,y)=(4,-2,4)\) lies on the conic and has first quotient zero. It does not attempt to classify the remaining \(c=4\) points.
