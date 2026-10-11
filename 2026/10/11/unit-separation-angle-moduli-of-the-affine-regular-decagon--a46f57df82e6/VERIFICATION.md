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
Put
\[
r=\frac{\sqrt5-1}{2},\quad \phi=1+r,\quad r^2=1-r.
\]
After the reference-edge reduction, the three exact branches have sum norms
\[
\max\{3-2r-r^2a,\phi+r^2a\},\quad
3r+(1-2r)a,\quad
\phi+(2-3r)a.
\]
Their domains are respectively \([0,r^2]\), \([r^2,r]\), and \([r,1]\). The first expression has its unique minimum at \(a=r^2/2\), equal to \((9-\sqrt5)/4\); every branch is at most \(4-\sqrt5\), with equality at branch endpoints. `verify.py` checks the decagon geometry, all three branch families, exchanged companions, and both equality witnesses in exact \(\mathbb Q(\sqrt5)\) arithmetic.

No independent audit or independent validation has been performed.
