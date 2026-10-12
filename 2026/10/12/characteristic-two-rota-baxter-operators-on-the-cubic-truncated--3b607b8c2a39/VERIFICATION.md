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

The proof in `RESULT.md` is the all-field argument. The finite verifier is an independent stress test of the exact parameterization and orbit computation.

`artifacts/verify.py` exhausts all \(q^9\) linear endomorphisms of the three-dimensional algebra over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\). For \(\mathbb F_2\) and \(\mathbb F_4\), it checks the Rota–Baxter identity on every ordered basis pair, proves by exhaustive comparison that the complete solution set is exactly \(P(1)=at^2\), \(P(t)=bt^2\), \(P(t^2)=0\), recomputes the rank distribution, constructs every automorphism \(t\mapsto ut+vt^2\), and recomputes all conjugacy orbits. It also verifies the mixed-orbit invariant \(a/b^2\).

The \(\mathbb F_3\) enumeration is only a boundary check: it recovers \(2q^2-q=15\) operators, confirming that the characteristic-two collapse is not a field-size artifact. No finite enumeration is used to infer the theorem for arbitrary \(q=2^e\).

The recorded output is in `artifacts/verification_output.txt` and ends with `VERIFY_OK`.
