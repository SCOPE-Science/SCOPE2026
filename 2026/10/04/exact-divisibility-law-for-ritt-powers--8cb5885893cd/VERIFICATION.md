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

The final claim was checked directly from the standard discrete-derivative characterization of Ritt operators.

1. If \(T^N\) is Ritt, then \(T\) is power bounded by writing every exponent modulo \(N\).
2. Spectral mapping gives \(\lambda^N=1\) for each \(\lambda\in\sigma(T)\cap\mathbb T\), so the peripheral set is finite and the lcm \(d\) is defined.
3. Any Ritt exponent must be divisible by \(d\).
4. For \(S=T^d\) and \(a=N/d\), the spectrum of \(S\) contains no nontrivial \(a\)-th root of unity. Hence \(Q_a(S)\), with \(Q_a(z)=1+z+\cdots+z^{{a-1}}\), is invertible.
5. The identity \(I-S^a=(I-S)Q_a(S)\) transfers the Ritt derivative estimate from \(S^a\) to \(S\).
6. A telescoping sum proves that every positive power of a Ritt operator is Ritt.

No numerical computation, finite enumeration, or external certificate is required. The proof does not establish existence of a Ritt power when none is assumed, and it does not optimize the quantitative Ritt constant.
