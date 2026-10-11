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

The universal theorem is proved analytically; no finite computation is used to pass from sampled cases to all integers \(m\).

The sharp upper certificate is
\[
P(\pi)+2P\left(\pi-\frac{2\pi}{3m}\right)=3-a\left(1+2\cos\frac{2\pi}{3m}\right),
\]
so feasibility implies the stated bound. For the displayed coefficients, the checker verifies the two contact zeros, the derivative contact, and the exact coefficient identities numerically to floating-point tolerance over a broad range of \(m\).

For attainment, the proof reduces to \(R(y)\ge g(y)\) on \([-1,1]\), where \(R\) is the quadratic Hermite interpolant of \(g(y)=A\cos((\arccos y)/m)\). The analytic sign argument is \(g^{(3)}(y)>0\) on \((-1,1)\), giving
\[
g(y)-R(y)=\frac{g^{(3)}(\xi)}6(y-1)(y+1/2)^2\le0.
\]
The checker samples this majorization and the resulting trigonometric polynomial for \(2\le m\le200\). Such sampling is only a regression check; it does not certify the infinite parameter range.

The uniqueness step is symbolic: at equality, nonnegativity and the upper certificate force both contact values to vanish, while the interior contact also has zero derivative. After \(a=A\) is fixed, these conditions reduce to the independent equations \(B+C=A-1\) and \(B-2C=q\).
