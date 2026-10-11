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

The complete reconstruction proceeds as follows. Rotational equivariance gives the form
\[
F(r,\theta)=(R(r),\theta+\psi(r)).
\]
The hyperbolic area form \(\sinh r\,dr\wedge d\theta\) and constant Jacobian \(k\) imply
\[
\cosh R=k\cosh r+C.
\]
The boundary data force \(C=0\).

In conformal cylinders \(x=\theta\) and \(y=\log\tanh(r/2)\), the derivative is
\[
\begin{pmatrix}1&s\\0&q\end{pmatrix},\quad
s=\sinh r\,\psi'(r),\quad
q=\frac{k\sinh^2r}{k^2\cosh^2r-1}.
\]
The function \(q\) increases strictly with \(r\), remains below one for \(k>1\), and has minimum at the inner circle. Its largest singular value is at least one. Therefore the sharp constrained dilatation is \(1/q(\varepsilon)\), attained by zero shear. The trace/determinant identity for its singular values gives the necessary and sufficient shear budget
\[
s^2\le(K_0-q)(q-K_0^{-1}).
\]
Smooth nonzero compactly supported angular shears satisfy this criterion after small scaling, verifying nonuniqueness rather than merely listing the radial extremizer.

The unrestricted comparison follows from classical annulus modulus. The conformal-cylinder widths are \(\Delta y\) and \(\Delta Y\); the affine cylinder stretch achieves \(K=\Delta y/\Delta Y\). A direct derivative establishes \(\Delta Y/\Delta y\) as an average of the strictly increasing \(q\), hence strict separation from the area-constrained cost.

The puncture expansion uses \(\sinh\varepsilon\sim\varepsilon\), \(y(\varepsilon)=\log(\varepsilon/2)+O(\varepsilon^2)\), and the finite limit of \(Y_k(\varepsilon)\) for fixed \(k>1\). This yields the claimed \(\varepsilon^{-2}\) and \(\log(1/\varepsilon)\) rates. In the critical coupling \(k=1+c\varepsilon^2\), the inner target radius is \(\varepsilon\sqrt{1+2c}+O(\varepsilon^3)\), giving the exact finite constrained limit \(1+2c\) and unrestricted limit one.

Independent floating-point tests of closed formulas were carried out for different \(k,b,\varepsilon\) and for \(k=1+c\varepsilon^2\) with \(c=0.1,1,4\). They check the algebra and predicted numerical trends, but are not used to certify any infinite or limiting claim. No result is claimed for non-equivariant constant-Jacobian maps; the singular ratios hold in the stated fixed-parameter or matched-limit regimes only.
