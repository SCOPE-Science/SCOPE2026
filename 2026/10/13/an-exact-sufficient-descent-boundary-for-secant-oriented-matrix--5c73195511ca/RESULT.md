# An exact sufficient-descent boundary for secant-oriented Matrix Dai--Liao updates
## Finding
Consider the Matrix Dai--Liao (MatDL) direction
\[
d_{k+1}=-P_{k+1}g_{k+1},\qquad
P_{k+1}=I-\frac{s_ky_k^\top}{s_k^\top y_k}+T_k\frac{s_ks_k^\top}{s_k^\top y_k},
\]
with the rank-one matrix parameter
\[
T_k=t_kI+\nu_k y_ky_k^\top.
\]
The 2026 source proposes the secant-oriented constraint
\[
t_k+\nu_k\|y_k\|^2=1,\qquad t_k,\nu_k\ge 0,
\]
and, among its examples, the angle-based \(\rho\)- and \(\eta\)-settings in its equation (3.11).

Write \(s=s_k\), \(y=y_k\), \(t=t_k\), assume \(s^\top y>0\), and define
\[
m=\frac{s^\top y}{\|s\|\|y\|},\qquad z=\frac{s^\top y}{\|y\|^2},\qquad q^2=m^{-2}-1.
\]
Under the secant constraint, so that \(\nu=(1-t)/\|y\|^2\), the exact sufficient-descent boundary is
\[
\Delta(t;m,z)=z(1+tq^2)-\frac{q^2}4[z(1-t)-1]^2>0.
\]
Indeed, this inequality is necessary and sufficient for the symmetric part of \(P\) to be positive definite, and therefore for \(g^\top(-Pg)<0\) for every nonzero \(g\).

This boundary shows a structural incompatibility with angle-only secant rules. Fix any noncollinear angle \(m\in(0,1)\). If a rule \(t=\tau(m)\) has \(\tau(m)<1\), then the negative quadratic term in \(z\) forces \(\Delta(t;m,z)\to-\infty\) as \(z\to\infty\). If \(\tau(m)=1\), then
\[
\Delta(1;m,z)=\frac1{m^2}\left(z-\frac{1-m^2}4\right),
\]
which is negative for \(0<z<(1-m^2)/4\). Hence no rule depending only on \(m\) can make every positive-curvature secant pair descent-safe. The source's \(\rho\)- and \(\eta\)-settings are of this angle-only type.

There is also a fully explicit first-step witness satisfying the usual strong Wolfe conditions. Let
\[
A=\frac1{80}\begin{pmatrix}1&\sqrt3\\\sqrt3&4\end{pmatrix},\qquad
b=\begin{pmatrix}-5/8\\0\end{pmatrix},\qquad
f(x)=\frac12x^\top Ax+b^\top x.
\]
Since \(\det A=1/6400>0\) and \(A_{11}>0\), \(A\) is positive definite. Take \(x_0=0\), so
\[
g_0=b,\qquad d_0=-g_0=\begin{pmatrix}5/8\\0\end{pmatrix},
\]
and choose \(\alpha_0=64\). Then
\[
s=\alpha_0d_0=\begin{pmatrix}40\\0\end{pmatrix},\qquad
y=As=\begin{pmatrix}1/2\\\sqrt3/2\end{pmatrix},\qquad
g_1=g_0+y=\begin{pmatrix}-1/8\\\sqrt3/2\end{pmatrix}.
\]
The step is a strong-Wolfe step for, for example, \(c_1=10^{-4}\) and \(c_2=9/10\):
\[
f(x_1)-f(x_0)=-15\le -\frac1{400}=c_1\alpha_0g_0^\top d_0,
\]
and
\[
|g_1^\top d_0|=\frac5{64}\le\frac{45}{128}=c_2|g_0^\top d_0|.
\]
Here \(\|y\|=1\), \(s^\top y=20\), \(m=1/2\), and \(z=20\). For \(\rho=1\), equation (3.11) gives \(t=m=1/2\); for \(\eta=1\), it gives \(t=1-m=1/2\). In both cases \(\nu=1/2\). Thus
\[
T=\begin{pmatrix}5/8&\sqrt3/8\\\sqrt3/8&7/8\end{pmatrix},\qquad
P=\begin{pmatrix}50&-\sqrt3\\10\sqrt3&1\end{pmatrix}.
\]
The symmetric part has determinant
\[
\det\frac{P+P^\top}2=-\frac{43}4<0,
\]
and, at the actual new gradient,
\[
g_1^\top Pg_1=-\frac5{32},\qquad g_1^\top d_1=\frac5{32}>0.
\]
So both displayed secant-oriented variants can generate an ascent direction immediately after an admissible strong-Wolfe descent step, even on a two-dimensional strongly convex quadratic.

## Assumptions and scope
The exact boundary concerns the source matrix \(P\) under the source secant system \(t+\nu\|y\|^2=1\), with \(s^\top y>0\). The angle-only impossibility statement fixes \(m\in(0,1)\) and permits arbitrary positive scale ratio \(z\). It does not assert that every MatDL configuration is unsafe: the source separately develops descent-oriented parameter conditions, and its ZZL-recovering configuration is a different branch. The explicit witness concerns the source's \(\rho=1\) and \(\eta=1\) secant variants and one admissible strong-Wolfe step; it does not claim that a particular line-search implementation must select \(\alpha_0=64\).

## Proof
Choose an orthonormal basis of \(\operatorname{span}\{s,y\}\) with \(e_1=s/\|s\|\) and
\[
\frac y{\|y\|}=m e_1+\sqrt{1-m^2}e_2.
\]
Set \(q=\sqrt{m^{-2}-1}\). Substituting \(\nu=(1-t)/\|y\|^2\) into the source formula for \(P\), direct simplification gives the symmetric part on this two-dimensional span as
\[
\frac{P+P^\top}2=
\begin{pmatrix}
z(1+tq^2)&\frac q2[z(1-t)-1]\\
\frac q2[z(1-t)-1]&1
\end{pmatrix}.
\]
On the orthogonal complement it is the identity. The upper-left entry is positive because \(z>0\), \(t\ge0\), and \(q^2\ge0\). Hence Sylvester's criterion reduces positive definiteness exactly to positivity of the determinant, which is \(\Delta(t;m,z)\).

For fixed \(m<1\), one has \(q^2>0\). If \(t<1\), expansion of \(\Delta\) in \(z\) has leading coefficient \(-q^2(1-t)^2/4<0\), proving failure for all sufficiently large \(z\). If \(t=1\), the displayed closed form gives failure for sufficiently small positive \(z\). This proves the angle-only impossibility.

For the explicit quadratic, all identities in the finding follow by exact matrix multiplication. In particular, \(A\succ0\), the first direction is exactly \(-g_0\), the stated \(\alpha_0\) satisfies both strong-Wolfe inequalities, the two source parameter settings coincide at \(t=\nu=1/2\), and the resulting quadratic form is negative at \(g_1\), yielding an ascent direction.

## Verification
The standalone script `verify_matdl_boundary.py` uses only exact rational arithmetic together with the quadratic field \(\mathbb Q(\sqrt3)\). It checks the Hessian determinant, the source-valid first-step identities, both strong-Wolfe inequalities, the secant parameters, the matrices \(T\) and \(P\), the determinant of the symmetric part, and the sign \(g_1^\top d_1=5/32>0\). The script prints `VERIFY_OK` only after every exact assertion passes.

## Relationship to prior work
Babaie--Kafaki, Kimiaei, and Aminifard introduce the Matrix Dai--Liao framework, derive the general symmetrized-matrix positivity condition, then separately develop descent-oriented and secant-oriented configurations. Their equation (3.10) is the secant system used here, and equation (3.11) supplies the \(\rho\)- and \(\eta\)-rules tested above. The present result identifies the exact intersection of that secant system with sufficient descent and exposes a scale obstruction that is invisible to angle-only settings.

Earlier three-term conjugate-gradient work already established an important qualitative warning: secant-based constructions do not automatically generate descent directions, while specially designed three-term methods can enforce sufficient descent. Those results concern different direction formulas and do not state the exact \((m,z,t)\) boundary for the 2026 Matrix Dai--Liao parameterization, nor the explicit strong-Wolfe quadratic witness above. The Zhang--Zhou--Li method is also distinct: its sufficient-descent property is line-search independent, and the 2026 paper recovers it through a separate MatDL parameter configuration rather than through the \(\rho\)- or \(\eta\)-settings considered here.

## Limitations
The exact boundary is a one-update statement, not a complete convergence analysis. The explicit example proves that an admissible strong-Wolfe step can be followed by an ascent MatDL direction; it does not prove that every line-search implementation selects that step, nor that all secant-oriented parameter values fail on every problem. The literature comparison found prior qualitative warnings about secant conditions and descent, so originality is limited to the exact Matrix Dai--Liao boundary, the angle-only impossibility theorem, and the concrete source-parameter witness. The closest 2017 secant/descent predecessor was available here at abstract level rather than full text; this leaves a residual literature risk, although its stated method is a different three-term construction predating the Matrix Dai--Liao framework.

## References
1. S. Babaie--Kafaki, M. Kimiaei, and Z. Aminifard, “From a Scalar to a Matrix Setting for the Dai--Liao Parameter,” arXiv:2607.17337v1, 2026. DOI: 10.48550/arXiv.2607.17337.
2. Y.-H. Dai and L.-Z. Liao, “New Conjugacy Conditions and Related Nonlinear Conjugate Gradient Methods,” Applied Mathematics and Optimization 43 (2001), 87--101. DOI: 10.1007/s002450010019.
3. L. Zhang, W. Zhou, and D. Li, “Some descent three-term conjugate gradient methods and their global convergence,” Optimization Methods and Software 22 (2007), 697--711. DOI: 10.1080/10556780701223293.
4. K. Sugiki, Y. Narushima, and H. Yabe, “Globally Convergent Three-Term Conjugate Gradient Methods that Use Secant Conditions and Generate Descent Search Directions for Unconstrained Optimization,” Journal of Optimization Theory and Applications 153 (2012), 733--757. DOI: 10.1007/s10957-011-9960-x.
5. H. Kobayashi, Y. Narushima, and H. Yabe, “Descent three-term conjugate gradient methods based on secant conditions for unconstrained optimization,” Optimization Methods and Software 32 (2017), 1313--1329. DOI: 10.1080/10556788.2017.1338288.
