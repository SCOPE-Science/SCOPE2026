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

The theorem is verified analytically rather than by finite sampling.

For the lower bound, an arbitrary slice functional \(x^*=(x_\gamma^*)\) is converted to the positive profile \(c_\gamma=\|x_\gamma^*\|^{q-1}\). The identities \((q-1)p=q\), \(\|c\|_p=1\), and \(\sum_\gamma \|x_\gamma^*\|c_\gamma=1\) were checked directly. Daugavet witnesses are then selected only on coordinates on which the functional is nonzero. The scaling inequality used to pass from unit-vector distance to weighted coordinate distance is proved in RESULT.md.

The scalar minimization was checked symbolically: for \(F(t)=(1+t)^p-t^p\), one has \(F'(t)=p((1+t)^{p-1}-t^{p-1})>0\). Consequently every positive \(c\in S_{\ell_p}\) satisfies
\[
\|a+c\|_p^p-\|a\|_p^p\ge F(\inf_\gamma a_\gamma),
\]
and coordinate unit vectors approaching the infimum attain the bound in the limit.

For the upper bound, the coordinate slice forces one coordinate norm above \(1-\delta\); the remaining \(\ell_p\)-mass is at most \(1-(1-\delta)^p\). Hence the error term
\[
\bigl(\delta^p+1-(1-\delta)^p\bigr)^{1/p}
\]
tends to zero, yielding the matching coordinate infimum.

Checked limits: the singleton case reduces to \(1+\|z\|\); \(z=0\) gives \(1\); and for an infinite index set every \(\ell_p\)-vector has coordinate infimum zero. No claim is made for \(p=1\), \(p=\infty\), complex scalars, non-Daugavet summands, or the \(\Delta\)-constant.
