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

The proof was reconstructed from the exact rank-one \(q\)-numerical-radius formula and elementary rank-one identities. The critical checks are:

1. With \(r=|q|\) and \(\tau=|\operatorname{tr}A|/\|A\|\), the published formula reduces exactly to
   \[
   \omega_q(A)=\frac{\|A\|}{2}\left(1+r\tau+\sqrt{1-r^2}\sqrt{1-\tau^2}\right).
   \]
2. Since \(\Omega_q(A)=W_q(A)/q\), closed-unit-disk containment is exactly \(\omega_q(A)\le r\).
3. The function \(r\tau+\sqrt{1-r^2}\sqrt{1-\tau^2}\) has its minimum over \([0,1]\) at an endpoint, with the endpoint comparison changing at \(r=2^{-1/2}\).
4. The endpoint \(\tau=1\) is exactly the scalar rank-one projection case; \(\tau=0\) is exactly the nonzero rank-one square-zero case.
5. On the square-zero branch, the envelope equals one exactly at \(r=4/5\), after which it equals the universal coefficient \(\rho_q\).

No numerical experiment is used as proof. The verification does not address higher-rank operators. The originality comparison is limited by the availability and terminology of prior literature, as described in `REVIEW.md` and `AUDIT.json`.
