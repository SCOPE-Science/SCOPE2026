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

The proof is symbolic and rests on the source's own inverse identity. If the declared candidate \(p^*=-\delta/\lambda\) were a constant equilibrium, then the model gives \({}^{C}\mathfrak D p^*=0\). Proposition 1 would therefore give
\[
0=
\frac{p^*(\omega(t)-\omega(0))}{\omega(t)}.
\]
For \(p^*\ne0\) and positive \(\omega\), this is equivalent to \(\omega(t)=\omega(0)\) for every \(t\).

The bundled `verifier.py` uses exact rational arithmetic for the explicit witness. It checks the source baseline values \(a=10\), \(a_1=5\), \(b=-1/2\), \(b_1=1/2\), \(c=1\), obtaining \(\lambda=-1\), \(\delta=5\), and \(p^*=5\). With \(\omega(t)=1+t\), it verifies at \(t=1\) that the Proposition 1 increment is exactly \(5/2\), while \(\lambda p^*+\delta=0\).

No finite experiment is used to infer the universal claim. The verifier only replays the exact witness and the algebraic incompatibility.
