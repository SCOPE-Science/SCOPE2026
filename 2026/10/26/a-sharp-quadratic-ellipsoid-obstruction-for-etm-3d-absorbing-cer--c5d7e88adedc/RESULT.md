# A sharp quadratic-ellipsoid obstruction for ETM-3D absorbing certificates

## Finding

For the one-parameter ETM-3D quadratic flow, the energy-compatible quadratic-ellipsoid method has a **sharp, unavoidable high-parameter semiaxis**. Let \(W\) be any fixed positive-definite symmetric matrix satisfying \(X^{T}WQ(X)=0\) for every \(X\in\mathbb R^3\), where \(Q(x,y,z)=(yz,-2xz,xy)\). Suppose that, for each sufficiently large \(\rho\), an ellipsoid
\[
E_\rho=\{X:(X-m_\rho)^T W(X-m_\rho)\le r_\rho^2\}
\]
is forward invariant under the ETM-3D flow. Then necessarily \(W=\operatorname{diag}(a,b,c)\), where \(a,c>0\) and \(b=(a+c)/2\), and
\[
\liminf_{\rho\to\infty}\frac{r_\rho}{\sqrt b\,\rho^2}\ge3.
\]
The constant is sharp: the explicit Euclidean absorbing ellipsoid from the motivating paper has semiaxis \(3\rho^2-\rho+3/2+o(1)\). Thus no fixed anisotropic energy-compatible quadratic metric and no adjustment of its center can reduce the leading \(3\rho^2\) growth of the semiaxis in the \(y\)-direction.

## Assumptions and scope

The ETM-3D vector field on \(\mathbb R^3\), with \(\rho\ge0\), is
\[
\dot x=-2x-\rho y+yz,\qquad
\dot y=x-y+\rho z-2xz,\qquad
\dot z=\rho y-5z+xy.
\]
An ellipsoid is forward invariant if every trajectory starting in it remains there for all future times. The matrix \(W\) is independent of \(\rho\); the center \(m_\rho\) and radius \(r_\rho>0\) may depend arbitrarily on \(\rho\). The metric condition \(X^TWQ(X)\equiv0\) specifies the natural class of shifted quadratic energies with no uncancelled cubic energy term. No assertion is made about arbitrary, parameter-dependent, non-energy-compatible metrics.

## Proof

**1. Classification of compatible quadratic metrics.** Write a general real symmetric matrix \(W\). In the cubic polynomial \(X^TWQ(X)\), the coefficients of \(x^2y\), \(x^2z\), and \(xy^2\) force all off-diagonal entries of \(W\) to vanish. The remaining \(xyz\) coefficient is \(a-2b+c\). Positivity gives precisely \(W=\operatorname{diag}(a,b,c)\), with \(a,c>0\), \(b=(a+c)/2>0\).

**2. Necessary quadratic semidefiniteness.** Let \(m=(m_x,m_y,m_z)\), \(q=X-m\), and \(V(X)=\tfrac12q^TWq\). Cubic cancellation gives \(\dot V=\mathcal Q_\rho(q)+\ell_\rho(q)\), a quadratic homogeneous form plus a linear form. Its squared-coordinate coefficients are \(-2a\), \(-b\), and \(-5c\); its coefficients of \(q_xq_y\), \(q_yq_z\), and \(q_xq_z\) are, respectively,
\[
b-a\rho-cm_z,\qquad (b+c)\rho-am_x,\qquad 2bm_y.
\]
On the boundary of any forward-invariant smooth ellipsoid, the outward normal derivative is nonpositive. Apply this at the antipodal boundary points \(q\) and \(-q\). The linear terms cancel, giving \(2\mathcal Q_\rho(q)\le0\). Every direction can be rescaled to the boundary, so \(\mathcal Q_\rho\) is negative semidefinite. Its two-by-two principal minors therefore bound each mixed coefficient by a constant depending only on \(a,b,c\). Thus
\[
m_x=\frac{b+c}{a}\rho+O_W(1),\qquad
m_z=-\frac ac\rho+O_W(1),\qquad m_y=O_W(1).
\]

**3. Unavoidable transverse forcing.** Evaluate the \(y\)-component of the vector field at the ellipsoid center:
\[
f_y(m)=m_x-m_y+\rho m_z-2m_xm_z
=\left(-\frac ac+2\frac{b+c}{c}\right)\rho^2+O_W(\rho)
=3\rho^2+O_W(\rho).
\]
The last identity uses \(2b=a+c\). Along the positive \(y\)-axis from the center, \(q=(0,t,0)\), the normal drift is **exactly**
\[
\dot V=b t\bigl(f_y(m)-t\bigr).
\]
The positive-axis boundary point has \(t=r_\rho/\sqrt b\). Because \(f_y(m)>0\) for all sufficiently large \(\rho\), forward invariance forces \(r_\rho/\sqrt b\ge f_y(m)=3\rho^2+O_W(\rho)\). Divide by \(\rho^2\) and take the lower limit.

**4. Sharpness.** For \(W=I\), the motivating paper provides a forward-invariant, globally absorbing Euclidean ball centered at \((2\rho,0,1-\rho)\), with radius
\[
r_{\rm src}=d+\sqrt C,\quad
h=\frac{\rho(3\rho-1)}2,\quad
d^2=\rho^2+h^2+\frac{(1-\rho)^2}{4},\quad
C=2\rho^2+h^2+\frac{5(1-\rho)^2}{4}.
\]
Direct expansion gives
\[
d-h\longrightarrow\frac5{12},\qquad \sqrt C-h\longrightarrow\frac{13}{12},\qquad
r_{\rm src}=3\rho^2-\rho+\frac32+o(1).
\]
This realizes the lower-bound coefficient \(3\), completing the proof.

## Verification

The accompanying `check.py` symbolically expands the complete shifted energy derivative, verifies all three mixed coefficients, checks the universal \(3\rho^2\) forcing term and the exact high-parameter expansion of the source's radius. The negative-semidefinite implication uses the antipodal-boundary argument, and the positive normal derivative obstruction holds analytically for arbitrarily large \(\rho\); neither is inferred from finite experiments.

## Relationship to prior work

Khalili-Amirabadi and Jalaeian-Farimani's 2026 ETM-3D paper proves the existence of the displayed explicit absorbing ball but labels it conservative. The present result establishes the previously unquantified **asymptotic optimality of its leading semiaxis coefficient across every fixed energy-compatible quadratic metric**, even after optimizing the center. A separate published exact global-stability-threshold result for ETM-3D concerns the first saddle-node and strict centered quadratic Lyapunov stability at small \(\rho\); its claim does not determine the high-\(\rho\) semiaxis optimum considered here.

## Limitations

This is a limitation on the geometry of a specified certificate family. The actual compact invariant sets could have much smaller physical diameter, and nonlinear or parameter-dependent metric methods may produce much smaller trapping regions. No global attractor-size asymptotic is asserted. The closest external algebraic threshold record was available by its mathematical abstract, not its complete source text; a broader uninspected optimization result remains a historical-priority risk. Independent mathematical auditing has not been performed.

## References

1. R. Khalili-Amirabadi and M. Jalaeian-Farimani, *ETM-3D: A One-Parameter Multistable Quadratic Flow with an Explicit Absorbing Set and Intermittent Chaos*, arXiv:2610.04768v1, first posted 2026-10-03, especially Section 2.1, https://arxiv.org/html/2610.04768v1.
2. *Exact global-stability threshold at the first ETM-3D saddle-node*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-global-stability-threshold-at-the-first-etm-3d-saddle-node--997f2098aca6 (indexed abstract compared; full text not accessible in this inspection).
