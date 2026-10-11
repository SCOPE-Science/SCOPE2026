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

The exact equilibrium reduction uses only the three printed equations. For nonzero equilibria, \(x_3=-x_1\) and \(x_2=a+1\), leaving \(r^2+r=1-b(a+1)\). The determinant of \(\lambda I-J_\sigma\) was expanded independently and gives \(\lambda^3+b\lambda^2+\alpha\lambda+\alpha\), independent of \(\sigma\).

Because \(a>0\) and pair existence gives \(b(a+1)<1\), one has \(0<b<1\). With \(\alpha>0\), the Routh first column has exactly two sign changes, so the nonzero equilibria have exactly two unstable eigenvalues and no imaginary-axis eigenvalue.

For the source values \((a,b)=(1,1/25)\), the checker uses exact arithmetic in \(\mathbb Q(\sqrt{13})\) to verify \(r^2+r=23/25\), the closed form for \(\alpha\), and the Routh signs. It then evaluates the exact cubic numerically only as a consistency check. The checker also verifies that the left and right derivatives of \(-|x_1|\) at zero are unequal.

Limits: the checker does not establish global dynamics or a nonsmooth linearization theorem at \(E_0\). The accepted claim does not require either.
