# Unique optimal circle for superquadratic mixed-power Musielak--Orlicz planes
## Finding
For every real \(2<p<q<\infty\), let \(X_{p,q}\) be \(\mathbb R^2\) with the Luxemburg norm whose closed unit ball is \(B_{p,q}=\{(x,y):|x|^p+|y|^q\le1\}\). Put \(\alpha=2/p\) and \(\beta=2/q\). Then the Euclidean circle is the unique Banach--Mazur optimal ellipse up to positive scale, and \[d_{\mathrm{BM}}(X_{p,q},\ell_2^2)^2=\max_{0\le t\le1}\bigl(t^{\alpha}+(1-t)^{\beta}\bigr)=t_*^{2/p}+(1-t_*)^{2/q},\] where \(t_*\in(0,1)\) is the unique solution of \(\frac{2}{p}t_*^{2/p-1}=\frac{2}{q}(1-t_*)^{2/q-1}\).

Equivalently, among all Euclidean pullback norms \(H_Q(z)=\sqrt{z^TQz}\) with \(Q\) positive definite, the unique optimal quadratic form is a positive scalar multiple of the identity. The maximizing points for the Euclidean squared norm on the \(X_{p,q}\)-unit sphere have \(|x|^p=t_*\) and \(|y|^q=1-t_*\); the coordinate-axis points give the minimum.

## Assumptions and scope
Fix real exponents \(2<p<q<\infty\). The coordinate functions \(u\mapsto u^p\) and \(u\mapsto u^q\) are Young functions, so
\[
B_{p,q}=\{(x,y)\in\mathbb R^2:|x|^p+|y|^q\le1\}
\]
is the unit ball of a two-dimensional Musielak--Orlicz Luxemburg norm. The claim concerns the multiplicative Banach--Mazur distance to the Euclidean plane and permits arbitrary real linear isomorphisms. The strict inequalities \(p>2\) and \(q>2\) are essential to the concavity argument below; the boundary case with one exponent equal to \(2\) is not part of this statement.

## Proof
Let \(N\) denote the Luxemburg norm of \(X_{p,q}\). For a positive-definite matrix \(Q\), define
\[
m(Q)=\inf_{N(z)=1} z^TQz,\qquad M(Q)=\sup_{N(z)=1} z^TQz.
\]
The squared distortion of the corresponding Euclidean pullback is \(M(Q)/m(Q)\).

The norm \(N\) is invariant under the two independent coordinate sign changes. If
\[
m(Q)N(z)^2\le z^TQz\le M(Q)N(z)^2
\]
for every \(z\), then the same inequalities hold for every sign-conjugate of \(Q\). Averaging the four conjugates removes the off-diagonal entries and preserves the same two constants. Hence every quadratic form has a diagonal sign-average with no larger distortion, so it suffices first to optimize diagonal forms.

Write a diagonal form as
\[
H_{a,b}(x,y)^2=ax^2+by^2,\qquad a,b>0.
\]
On the first-quadrant unit sphere put \(t=x^p\). Then \(t\in[0,1]\), \(y^q=1-t\), and with \(\alpha=2/p\), \(\beta=2/q\),
\[
H_{a,b}(x,y)^2=F_{a,b}(t):=a t^\alpha+b(1-t)^\beta.
\]
Because \(0<\beta<\alpha<1\), the function \(F_{a,b}\) is strictly concave. Therefore its minimum on \([0,1]\) is attained at an endpoint and equals \(\min\{a,b\}\). Rescale so that this minimum is \(1\). Then \(a,b\ge1\), with at least one equal to \(1\), and consequently
\[
F_{a,b}(t)\ge F_{1,1}(t)=t^\alpha+(1-t)^\beta
\]
for every \(t\in[0,1]\). Thus every normalized diagonal form has maximum at least
\[
M_{p,q}:=\max_{0\le t\le1}\bigl(t^\alpha+(1-t)^\beta\bigr),
\]
while the identity form has endpoint minimum \(1\) and maximum exactly \(M_{p,q}\). The function \(F_{1,1}\) has an interior maximizer because both exponents lie in \((0,1)\). If a normalized diagonal form has \((a,b)\ne(1,1)\), then at that interior maximizer its value is strictly larger than \(F_{1,1}\), so its distortion is strictly larger. Thus the identity is the unique diagonal optimum up to scale and the optimal squared distortion is \(M_{p,q}\).

The function \(f(t)=t^\alpha+(1-t)^\beta\) is strictly concave, with \(f'(t)\to+\infty\) as \(t\downarrow0\) and \(f'(t)\to-\infty\) as \(t\uparrow1\). It therefore has a unique maximizer \(t_*\in(0,1)\), characterized by
\[
\alpha t_*^{\alpha-1}=\beta(1-t_*)^{\beta-1},
\]
which is the displayed equation.

It remains to prove uniqueness among all ellipses. Suppose \(Q\) is optimal. Its sign-average is also optimal, and the diagonal argument shows that this average must be a positive scalar multiple of the identity. After rescaling, write
\[
Q=\begin{pmatrix}1&c\\ c&1\end{pmatrix}.
\]
If \(c\ne0\), choose an interior maximizing absolute-value pair \((x_*,y_*)\) with \(|x_*|^p=t_*\) and \(|y_*|^q=1-t_*\). Two sign choices give quadratic values
\[
M_{p,q}\pm2|c|\,|x_*y_*|.
\]
Hence \(M(Q)>M_{p,q}\), while the axis points still have quadratic value \(1\), so \(m(Q)\le1\). This forces \(M(Q)/m(Q)>M_{p,q}\), a contradiction. Thus \(c=0\), proving uniqueness up to scale.

## Verification
The proof is analytic and uses no finite enumeration as a substitute for a global argument. The only scalar optimization is the strictly concave function
\[
f(t)=t^{2/p}+(1-t)^{2/q},\qquad 0\le t\le1,
\]
whose derivative has exactly one zero. Sign averaging is applied to the full two-sided quadratic comparison, so rotated ellipses are not omitted. The uniqueness argument then excludes every nonzero off-diagonal perturbation by evaluating the two sign choices at the interior maximizing absolute-value pair.

As a numerical consistency check only, for \(p=4\) and \(q=6\), the root is approximately \(t_*=0.61978\), giving \(d_{\mathrm{BM}}(X_{4,6},\ell_2^2)^2\approx1.51171647\). This numerical value is not used in the proof.

## Relationship to prior work
Kobos, arXiv:1305.6288, defines finite-dimensional Musielak--Orlicz spaces by coordinate Young functions and the Luxemburg gauge, and explicitly places Banach--Mazur distance in the surrounding finite-dimensional geometry. Its results concern equilateral dimension, not the optimal Euclidean ellipse of the mixed-power plane considered here.

A close published comparison record studies the different norm \(N_{\lambda,p,q}(z)=(\|z\|_p^2+\lambda\|z\|_q^2)^{1/2}\). That norm applies both exponents globally and is invariant under coordinate permutation; the present norm assigns exponent \(p\) to one coordinate and \(q\) to the other and, for \(p\ne q\), has no coordinate-swap isometry. Its exact formula therefore does not imply the theorem above. A previously recorded boundary result treats the disjoint case with one exponent equal to \(2\); it does not cover \(2<p<q\).

## Limitations
The theorem is restricted to two coordinates and to the strictly superquadratic regime \(2<p<q<\infty\). It does not determine the optimal ellipse when one or both exponents are below \(2\), where the one-variable profile is no longer concave. The literature search did not locate an earlier equivalent theorem under Musielak--Orlicz, variable-exponent, mixed-power, or anisotropic-superellipse terminology; an equivalent convex-body approximation result under different terminology remains a residual risk.

## References
1. T. Kobos, “Equilateral dimension of some classes of normed spaces,” arXiv:1305.6288, first public version 2013-05-27.
