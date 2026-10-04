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

The exact proof is in `RESULT.md`. The bundled verifier checks the finite algebraic skeleton used in the section computation.

The script enumerates every quadratic monomial in \(x_0,\ldots,x_5,t\), represents the characteristic-two derivation
\[
D=\sum_{i=0}^5x_i^2\partial_{x_i},
\]
and verifies that its degree-two kernel has dimension \(7\), with basis
\[
x_0^2,\ldots,x_5^2,t^2.
\]
It separately checks
\[
D(x_0x_1+x_2x_3+x_4x_5)=C,
\]
and verifies the support facts used to force the linear coefficient \(\ell\) in \(D(q)=\ell Q+\mu C\) to vanish: \(D(S_2)\) contains neither \(t^3\) nor any \(x_it^2\), while those coefficients in \(\ell Q\) recover exactly the coefficients of \(\ell\).

The script also checks the degree arithmetic
\[
\deg(F_{H/k})=2^4=16,\qquad 16/2=8.
\]
Its stored output ends in `VERIFY_OK`.

The verifier does not certify the sheaf-theoretic norm, descent of invariant sections, or originality. Those are established by the proof and literature comparison.
