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

The exact domain is the unit-edge equilateral octahedron with the cyclic preferred-orientation coupling and positive wave number \(k>0\). The primary input is the set of four published component secular determinants.

Critical proof checks:

1. With \(x=\cos^2(k/2)\) and \(y=k^2\), the \(j=1,3\) residual bracket expands to \(4(y+1)^2x^2-2(y+1)^2x+y\), which equals \(\bigl(2(y+1)x-y\bigr)\bigl(2(y+1)x-1\bigr)\).
2. The \(j=0\) residual branch is \(2(y+1)x-1=0\); the \(j=2\) residual branch is \(2(y+1)x-y=0\). These become the two tangent-square equations in the finding.
3. The scalar root sets cannot overlap: overlap would require \(k=1\), which is not a root. Neither root set meets the elementary sine or quarter-cosine factors.
4. Derivatives of the two tangent-square equations are nonzero at every positive root. Therefore each containing component determinant has a simple zero and one-dimensional boundary-system kernel. The first scalar factor appears in sectors \(0,1,3\); the second appears in sectors \(1,2,3\). Hence each corresponding graph eigenvalue has multiplicity three.
5. The local expansions around \(K_n=(2n+1)\pi\) and \(L_n=\pi/2+n\pi\) give the claimed leading offsets and remainders.

`verify.py` checks the polynomial identities with exact integer coefficients and numerically bisects representative roots over several scales, confirming convergence of \(K_n|k-K_n|\) to \(\sqrt2\) and of \((k-L_n)L_n^2\) to \((-1)^n\).

Limits: finite numerical checks do not establish the infinite theorem; the proof above does. No claim is made about negative eigenvalues, unequal edge lengths, or other vertex couplings.
