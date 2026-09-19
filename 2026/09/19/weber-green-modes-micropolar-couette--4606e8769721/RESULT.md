# Exact Weber Green modes and quadratic splitting in micropolar Couette flow

## Statement

Qi and Yu study the two-dimensional micropolar equations near Couette flow in the balanced-viscosity case
\[
\nu=\kappa=\frac{\mu}{2},
\]
and, after their time rescaling and the sheared Fourier coordinate
\(\widetilde\eta=\eta+At\xi\), reduce the linear Green symbol to
\[
\partial_t\widehat G=B(t)\widehat G,\qquad \widehat G(0)=I,
\]
with
\[
B(t)=
\begin{pmatrix}
-q(t)&q(t)\\
1&-q(t)-2
\end{pmatrix},
\qquad
q(t)=\xi^2+(\widetilde\eta-At\xi)^2.
\]
Their Section 3 derives a scalar second-order equation and estimates it by a Volterra representation and Gronwall bounds. In this parameter slice the scalar equation is in fact exactly Weber's equation, so the entire \(2\times2\) sheared Fourier Green matrix has a closed parabolic-cylinder representation.

Fix \(A>0\) and a sheared Fourier label \((\xi,\widetilde\eta)\).

### Nonzero streamwise frequency

Assume \(\xi\neq0\) and set
\[
\rho=|A\xi|,\qquad
t_c=\frac{\widetilde\eta}{A\xi},\qquad
z(t)=\sqrt{2\rho}\,(t-t_c),
\]
\[
\nu_W=-\frac12-\frac{\xi^2+1}{2\rho},
\qquad
Q(t)=\int_0^t(q(s)+1)\,ds.
\]
Equivalently,
\[
Q(t)
=(\xi^2+1+\widetilde\eta^2)t
-A\xi\widetilde\eta\,t^2
+\frac{A^2\xi^2}{3}t^3.
\]

Let \(D_\nu\) denote the parabolic-cylinder function and define
\[
Y(t)=
\begin{pmatrix}
D_{\nu_W}(z(t)) & D_{\nu_W}(-z(t))\\
\sqrt{2\rho}\,D'_{\nu_W}(z(t))&
-\sqrt{2\rho}\,D'_{\nu_W}(-z(t))
\end{pmatrix},
\qquad
R=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}.
\]
Then the exact fundamental matrix is
\[
\boxed{
\widehat G(t)
=
e^{-Q(t)}
R\,Y(t)Y(0)^{-1}R^{-1}.
}
\]
Since \(\nu_W<-1/2\),
\[
\det Y(t)=
\frac{2\sqrt{\pi\rho}}{\Gamma(-\nu_W)}
\neq0,
\]
so this expression is nonsingular for every \(t\).

There is also an exact Liouville identity
\[
\boxed{
\det \widehat G(t)=e^{-2Q(t)}.
}
\]

For fixed \((\xi,\widetilde\eta)\) with \(\xi\neq0\), let
\(s_{\max}(t)\ge s_{\min}(t)>0\) be the singular values of \(\widehat G(t)\).
As \(t\to\infty\),
\[
\boxed{
s_{\max}(t)
=
\Theta\!\left(
e^{-Q(t)+z(t)^2/4}\,
z(t)^{-\nu_W}
\right),
}
\]
and therefore, by the determinant identity,
\[
\boxed{
s_{\min}(t)
=
\Theta\!\left(
e^{-Q(t)-z(t)^2/4}\,
z(t)^{\nu_W}
\right).
}
\]
Equivalently,
\[
\log s_{\max}
=
-Q+\frac{z^2}{4}-\nu_W\log z+O(1),
\]
\[
\log s_{\min}
=
-Q-\frac{z^2}{4}+\nu_W\log z+O(1).
\]
Hence
\[
\boxed{
\log\kappa_2(\widehat G(t))
=
\frac{z(t)^2}{2}
-2\nu_W\log z(t)+O(1),
}
\]
where \(\kappa_2=s_{\max}/s_{\min}\).

Thus both singular directions have the same cubic enhanced-dissipation exponent,
\[
\boxed{
\lim_{t\to\infty}\frac{\log s_{\max}(t)}{t^3}
=
\lim_{t\to\infty}\frac{\log s_{\min}(t)}{t^3}
=
-\frac{A^2\xi^2}{3},
}
\]
but they split at the next scale by the opposite quadratic corrections
\(\pm \rho(t-t_c)^2/2\), together with explicit logarithmic powers. The Green mode is therefore strongly nonnormal even though both singular values decay super-exponentially on the \(t^3\) scale.

### Streamwise-zero frequency

If \(\xi=0\), then \(q=\widetilde\eta^2\) is constant. Put
\[
C=
\begin{pmatrix}
1&q\\
1&-1
\end{pmatrix},
\qquad
C^2=(q+1)I.
\]
The Green mode is elementary:
\[
\boxed{
\widehat G(t)
=
e^{-(q+1)t}
\left[
\cosh(\sqrt{q+1}\,t)I
+
\frac{\sinh(\sqrt{q+1}\,t)}{\sqrt{q+1}}C
\right].
}
\]
This includes the neutral spatial mean at \(q=0\).

## Proof

Write a column of \(\widehat G\) as \(v=(m,\omega)^\top\). It satisfies
\[
m'=-qm+q\omega,\qquad
\omega'=m-(q+2)\omega.
\]
Define
\[
y=e^{Q}\omega,\qquad Q'=q+1.
\]
Then
\[
\omega=e^{-Q}y,\qquad
m=e^{-Q}(y'+y).
\]
Substitution into either first-order equation gives
\[
\boxed{y''=(q+1)y.}
\]

For \(\xi\neq0\),
\[
q+1=\rho^2(t-t_c)^2+\xi^2+1.
\]
With \(z=\sqrt{2\rho}(t-t_c)\),
\[
y_{zz}
=
\left(\frac{z^2}{4}+\frac{\xi^2+1}{2\rho}\right)y,
\]
or
\[
y_{zz}
+
\left(
\nu_W+\frac12-\frac{z^2}{4}
\right)y=0.
\]
This is Weber's equation. Its two real solutions
\(D_{\nu_W}(z)\) and \(D_{\nu_W}(-z)\) are independent because
\[
W_z\!\left[D_{\nu_W}(z),D_{\nu_W}(-z)\right]
=
\frac{\sqrt{2\pi}}{\Gamma(-\nu_W)},
\]
and \(-\nu_W>0\). Reconstructing \((m,\omega)\) from \((y,y')\), then normalizing at \(t=0\), yields the displayed matrix formula.

Also
\[
\operatorname{tr}B=-2(q+1),
\]
so Liouville's formula gives
\[
\det\widehat G(t)
=
\exp\!\left(\int_0^t\operatorname{tr}B(s)\,ds\right)
=e^{-2Q(t)}.
\]

For the singular-value asymptotics, \(z(t)\to+\infty\). The standard positive-axis parabolic-cylinder asymptotic is
\[
D_{\nu_W}(z)
=
e^{-z^2/4}z^{\nu_W}(1+O(z^{-2})).
\]
Because \(\nu_W<0\), the integral representation for
\(D_{\nu_W}(-z)=U(-\tfrac12-\nu_W,-z)\) gives by Laplace's method
\[
D_{\nu_W}(-z)
=
\frac{\sqrt{2\pi}}{\Gamma(-\nu_W)}
e^{z^2/4}z^{-\nu_W-1}(1+O(z^{-2})).
\]
Its \(t\)-derivative contributes one additional factor comparable to \(z\).
Since \(R\), \(Y(0)^{-1}\), and \(R^{-1}\) are fixed invertible matrices for the chosen mode, the largest singular value is comparable to
\[
e^{-Q}e^{z^2/4}z^{-\nu_W}.
\]
The formula for the smaller singular value follows from
\(s_{\max}s_{\min}=|\det\widehat G|=e^{-2Q}\).

When \(\xi=0\), the coefficient matrix is constant and can be written
\[
B=-(q+1)I+C,\qquad C^2=(q+1)I,
\]
which gives the elementary exponential formula.

## Relation to the source paper

The source paper already derives, in its Eq. (3.6), the scalar equation
\[
F''-(1+P')F=0,\qquad P'=q.
\]
The refinement here is not the existence of a scalar reduction. It is the recognition that, because \(q(t)\) is exactly quadratic in time, this scalar equation is Weber's equation; this yields a closed frequency-space Green matrix and sharp fixed-mode singular-value asymptotics. The source instead proceeds with integral inequalities and obtains a uniform Gaussian-type Fourier bound suitable for its nonlinear argument.

This result does not invalidate those bounds. It supplies an exact benchmark and reveals a nonnormal quadratic mode splitting that their norm estimate does not resolve.

## Verification

`artifacts/verify_weber_micropolar.py` checks the change of variables symbolically, compares the parabolic-cylinder formula against direct numerical integration for three nonzero-frequency modes, verifies the determinant identity, checks the elementary \(\xi=0\) formula against a matrix exponential, and evaluates the bounded remainder in the logarithmic \(s_{\max}\) asymptotic.

The recorded numerical errors are between \(10^{-15}\) and \(10^{-21}\) for the matrix and determinant checks. These computations support the algebra but are not independent validation.

## Limitations

1. The explicit Weber representation uses the balanced-viscosity coefficient matrix of arXiv:2609.20109v1 after its normalization. It is not asserted for arbitrary \((\nu,\kappa,\mu)\).
2. The sharp singular-value formulas are fixed sheared-frequency asymptotics. Their constants are not uniform as \(\xi\to0\) or across frequency regimes.
3. The result does not by itself improve the physical-space \(L^p\) Green estimates or the nonlinear stability threshold. Uniform special-function asymptotics in all frequencies would be needed for that step.
4. The asymptotics concern the linearized Green symbol, not nonlinear transient growth of the full micropolar PDE.
5. Two closely related micropolar-Couette papers were identified in the literature review: Wang--Li (2026), which uses a Fourier-multiplier energy method, and Tao (2026), which proves linear decay and nonlinear threshold results under several viscosity relations. The complete proof text of those papers was not fully inspected in the available sources, so an equivalent hidden special-function reduction remains a residual originality risk.

## References

1. J. Qi and L. Yu, *Stability for the 2D Micropolar equations near Couette flow via Green's function method*, arXiv:2609.20109v1 (2026). https://arxiv.org/abs/2609.20109
2. Y. Wang and L. Li, *Linear and nonlinear enhanced dissipation for the 2-D micropolar equations near Couette flow*, Discrete and Continuous Dynamical Systems - B 32 (2026), 103--118. https://doi.org/10.3934/dcdsb.2025124
3. K. Tao, *On the Stability Threshold of Couette Flow for 2D Incompressible Micropolar Equations*, Mathematical Methods in the Applied Sciences (2026). https://doi.org/10.1002/mma.70878
4. NIST Digital Library of Mathematical Functions, Chapter 12, Parabolic Cylinder Functions, especially Sections 12.2 and 12.5. https://dlmf.nist.gov/12.2 and https://dlmf.nist.gov/12.5
