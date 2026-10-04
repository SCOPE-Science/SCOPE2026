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

The checked source normalization is
\[
h_{Z_n}(x,t)=\mathbb E\left|\langle x,\Gamma_{n-1}\rangle+t\right|,
\]
with \(\operatorname{Cov}(\Gamma_{n-1})=(\pi/2)I_{n-1}\). Hence \(h_{Z_n}(\theta,0)=1\) for horizontal unit vectors and \(h_{Z_n}(0,1)=1\). The source defines \(F_1(s)=\phi(s)/\sqrt{1+s^2}\), proves that its minimum \(b_\infty\) occurs at a unique \(s_0>0\), and proves \(d_{BM}(Z_n,B_2^n)=b_\infty^{-1}\).

For a candidate ellipsoid with support-square \(q\), the sharp sandwich was checked algebraically to be exactly
\[
b_\infty^2h_{Z_n}^2\le q\le h_{Z_n}^2.
\]
Averaging \(q\) over \(O(n-1)\times\{\pm1\}\) preserves both inequalities because \(Z_n\) is invariant. The source proof of Theorem 5.3 was checked in both parameter ranges: \(\alpha>1\) and \(0<\alpha<1\) each give a strictly larger comparison ratio than \(b_\infty^{-1}\). Thus an averaged sharp optimizer has Euclidean shape.

The scale is forced by two exact contacts. Horizontal directions give the lower bound \(c^2\ge b_\infty^2\); the minimizing-slope directions \((\theta,s_0)/\sqrt{1+s_0^2}\) give the upper bound \(c^2\le b_\infty^2\). Therefore the averaged support-square is exactly \(b_\infty^2\|u\|^2\).

Finally, the equality case of averaging was checked directly. On the horizontal orbit, the pointwise quantity \(q(gu)-b_\infty^2\) is continuous and nonnegative and has zero Haar average, so it vanishes identically. This fixes the horizontal block. The axial coefficient is fixed similarly. On the minimizing-slope orbit, \(b_\infty^2-q(gu)\) is continuous and nonnegative with zero Haar average, so it also vanishes identically. Substitution into the remaining block form forces every cross coefficient to be zero. Hence \(q=b_\infty^2\|\cdot\|^2\).

No finite experiment, numerical approximation, or partial enumeration is used to infer the theorem. The verified scope is every integer \(n\ge3\), for origin-centered ellipsoids only. No claim is made about translated ellipsoid pairs.
