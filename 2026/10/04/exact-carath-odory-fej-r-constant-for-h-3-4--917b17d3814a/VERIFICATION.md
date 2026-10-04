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

The proof has two independent mathematical components. First, the contact certificate
\[
sT(1/2)+T(5/14)=1+s-\lambda(r+s)
\]
with \(r=\cos(2\pi/7)\) and \(s=\cos(\pi/7)\) yields the sharp upper bound. Second, the proposed extremizer has the exact factorization
\[
\frac{32(1-r)}7(x+1)(x+r)^2(q-x),\qquad q=\frac{5+2r-4r^2}{4}>1,
\]
for \(-1\le x\le1\), proving global nonnegativity.

Run `python3 verify.py`. The checker performs exact arithmetic in \(\mathbb Q[r]/(8r^3+4r^2-4r-1)\). It checks the coefficient-by-coefficient factorization, the identities for the two contact points, the equality \(1+s=2r(r+s)\), and the nonzero determinant of the three equality conditions used for uniqueness. Success prints `VERIFY_OK`.

The checker does not certify that a finite sample is representative of the continuum. The continuum positivity and the selection of the real root \(r=\cos(2\pi/7)\) are supplied by the analytic factorization and angle inequalities in the proof.
