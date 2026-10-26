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

# Verification and scope

The supplied standalone `verify.py` (Python standard library) was executed successfully. It tests the polynomial \(T^7+3T^3-1\) by exact polynomial modular division: irreducibility modulo \(2\), and irreducible degree-two and degree-five factors modulo \(7\), with squarefree reductions. Its expected terminal message begins `VERIFY_OK`. Those factorizations give a separate \(S_7\) specialization. It also checks the parameter exponent identities and coprimalities for dimensions \(2\) through \(24\).

The all-dimensional claim is instead proved symbolically: the critical points of \(t^{-M}-t^{N-M}\) solve \(t^N=-M/(N-M)\), and coprimality \(\gcd(N,M)=1\) ensures distinct branch values. The sphere fundamental-group relation and connectivity force full symmetric monodromy. The scheme-theoretic idempotent count, zero-point simplicity, the existence of a finite étale open, and restriction to the special family are checked in the proof.

Not checked by the finite program: arbitrary dimension via enumeration, all rational specializations, or independent validation of the geometric monodromy argument. Independent audit has not been performed.
