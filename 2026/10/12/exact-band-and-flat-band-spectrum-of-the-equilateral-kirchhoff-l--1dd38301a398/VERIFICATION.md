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

The proof uses exact edge solutions and a one-cell Floquet reduction. For nonresonant \(k\), the backbone outgoing derivatives and the loop derivative sum reduce the Kirchhoff condition to
\[
u_{j+1}+u_{j-1}=2(2\cos k-1)u_j,
\]
so the real-fiber criterion is exactly \(|2\cos k-1|\le1\), equivalent to \(\cos k\ge0\).

At \(k=n\pi\), zero vertex values reduce the entire derivative condition to
\[
a_j-(-1)^n a_{j-1}+(1-(-1)^n)b_j=0.
\]
For even \(n\), one-loop sine modes satisfy this equation. For odd \(n\), taking one backbone amplitude equal to \(1\) forces the two adjacent loop amplitudes to be \(-1/2\), giving a compact eigenfunction. Separated translations certify infinite multiplicity.

`verify.py` checks these identities and parity balances. Its finite sample checks do not establish completeness; completeness comes from the exact Floquet condition plus the separate resonant analysis. The verification does not cover unequal edge lengths, nonzero phases, nonzero quasi-\(\delta\) coupling, or added potentials.
