# Sharp all-order extension for the third Toeplitz determinant of starlike functions

## Finding

For every \(0\le\alpha<1\) and every normalized analytic function \(f(\zeta)=\zeta+\sum_{n\ge2}a_n\zeta^n\) on the unit disk satisfying \(\operatorname{Re}(\zeta f'(\zeta)/f(\zeta))>\alpha\), define the symmetric third Toeplitz determinant

\[
T_3(2;f)=\det\begin{pmatrix}a_2&a_3&a_4\\a_3&a_2&a_3\\a_4&a_3&a_2\end{pmatrix}.
\]

Its exact sharp bound over the full order interval is

\[
\boxed{\sup_{f\in\mathcal S^*(\alpha)}|T_3(2;f)|=\frac49(1-\alpha)^3(9-7\alpha+2\alpha^2)(21-22\alpha+8\alpha^2).}
\]

The only extremizers are \(f_\pm(\zeta)=\zeta(1\mp i\zeta)^{-2(1-\alpha)}\). The main extension is the formerly untreated interval \(2/3<\alpha<1\); the same sharp formula for \(0\le\alpha\le2/3\) was proved by Panja, Majumder and Banerjee [1].

## Assumptions and scope

The disk is \(\mathbb D=\{\zeta\in\mathbb C:|\zeta|<1\}\). The starlike function is normalized by \(f(0)=0\), \(f'(0)=1\), and the displayed strict real-part inequality applies at all nonzero \(\zeta\in\mathbb D\) (with value \(1\) at the origin). The Toeplitz matrix is complex symmetric, not Hermitian. The theorem concerns one complex variable and the exact coefficient index \(T_3(2)\), not \(T_3(1)\) or higher-dimensional directional tensors.

Set \(d=1-\alpha\), so \(0<d\le1\). The positive-real-part function

\[
p(\zeta)=\frac{\zeta f'(\zeta)/f(\zeta)-\alpha}{d}=1+2x\zeta+2y\zeta^2+2w\zeta^3+\cdots
\]

is a Carathéodory function, with \(|x|,|y|,|w|\le1\) by the Herglotz representation.

## Proof

**1. A sharp three-moment inequality.** For any analytic \(p\) on \(\mathbb D\) with \(p(0)=1\), \(\operatorname{Re}p>0\) and coefficients \(x,y,w\) normalized above, prove

\[
\boxed{|6x^2+2xw-3y^2|\le7.}\tag{1}
\]

The estimate is sharp, with equality exactly for \(p(\zeta)=(1\pm i\zeta)/(1\mp i\zeta)\).

Indeed write \(p=(1+\zeta\omega)/(1-\zeta\omega)\), with \(\omega:\mathbb D\to\overline{\mathbb D}\) analytic and \(\omega(0)=x\). By Schwarz--Pick and one Schur step there exist \(u,v\in\overline{\mathbb D}\) such that, putting \(h=1-|x|^2\),

\[
 y=x^2+hu,\qquad
 w=x^3+h\left(2xu-\overline{x}u^2+(1-|u|^2)v\right).\tag{2}
\]

For \(|x|<1\), formula (2) follows by writing \(\omega(\zeta)=(x+\zeta\eta(\zeta))/(1+\overline{x}\zeta\eta(\zeta))\) with \(\eta(0)=u\), \(\eta'(0)=(1-|u|^2)v\). Boundary cases \(|x|=1\) or \(|u|=1\) follow by the maximum principle, or by a limit.

Substitute (2) into the polynomial inside (1):

\[
6x^2+2xw-3y^2=x^2(6-x^2)-h\left[2x^2u+(3-|x|^2)u^2-2x(1-|u|^2)v\right].\tag{3}
\]

Set \(r=|x|\), \(s=|u|\). By (3) and the triangle inequality,

\[
\begin{aligned}
|6x^2+2xw-3y^2|
&\le r^2(6+r^2)+(1-r^2)B_r(s),\\
B_r(s)&=2r+2r^2s+(3-r^2-2r)s^2.
\end{aligned}
\]

The quadratic coefficient \(3-r^2-2r=(1-r)(3+r)\) is nonnegative. Thus \(B_r\) is convex on \([0,1]\), and

\[
\max_{0\le s\le1}B_r(s)=\max\{2r,3+r^2\}=3+r^2.
\]

It follows that

\[
|6x^2+2xw-3y^2|\le r^2(6+r^2)+(1-r^2)(3+r^2)=3+4r^2\le7.
\]

If equality holds, then \(r=1\). Schwarz's lemma forces \(\omega\equiv x\), hence \(y=x^2\), \(w=x^3\), and the left side is \(|x^2(6-x^2)|\). Its value is \(7\) precisely when \(x^2=-1\), i.e. \(x=\pm i\). This also verifies attainability.

**2. Coefficient factorization.** Comparison of coefficients in \(\zeta f'/f=\alpha+dp\) gives

\[
\begin{aligned}
a_2&=2dx,\\
a_3&=dy+2d^2x^2,\\
a_4&=\frac{2d}{3}w+2d^2xy+\frac{4d^3}{3}x^3.
\end{aligned}\tag{4}
\]

Direct determinant expansion yields

\[
T_3(2;f)=(a_2-a_4)(a_2^2+a_2a_4-2a_3^2).\tag{5}
\]

By (4) and \(|x|,|y|,|w|\le1\),

\[
|a_2-a_4|\le\frac{2d}{3}\left(4+3d+2d^2\right).\tag{6}
\]

The second factor in (5) is exactly

\[
a_2^2+a_2a_4-2a_3^2=\frac{2d^2}{3}\bigl(6x^2+2xw-3y^2-6dx^2y-8d^2x^4\bigr).\tag{7}
\]

Using (1) in (7) gives, for every \(d>0\),

\[
|a_2^2+a_2a_4-2a_3^2|\le\frac{2d^2}{3}\left(7+6d+8d^2\right).\tag{8}
\]

Multiplying (6) and (8),

\[
|T_3(2;f)|\le\frac{4d^3}{9}(4+3d+2d^2)(7+6d+8d^2).
\]

Since \(d=1-\alpha\), the two parenthesized factors equal \(9-7\alpha+2\alpha^2\) and \(21-22\alpha+8\alpha^2\), respectively.

**3. Sharpness and uniqueness.** Take \(x=\pm i\). Then \(y=x^2=-1\), \(w=x^3=\mp i\), and both (6) and (8) are equalities, with aligned summands, for every \(d\in(0,1]\). The corresponding \(p\) is \((1+x\zeta)/(1-x\zeta)\), which integrates to \(f(\zeta)=\zeta(1-x\zeta)^{-2d}\). Its logarithmic derivative satisfies \(\operatorname{Re}(\zeta f'/f)>\alpha\) throughout the disk. Conversely equality in the product forces equality in (8), then in the seven-unit lemma because its positive coefficient is not zero. The lemma implies \(x=\pm i\), giving exactly these two extremizers. This proves the theorem.

## Verification

`CHECK.py` symbolically checks the coefficient expansion and determinant factorization, proves exact equality identities for five rational values of \(d\) and both extremizers, and tests 12,000 deterministic admissible Schur-parameter triples (24,000 finite inequalities). It produced `PASS` in a fresh execution. This is a supplementary test only; the analytic Schur-parameter proof, rather than sampling, establishes the uniform inequality for all analytic functions and all orders.

## Relationship to prior work

Panja, Majumder and Banerjee [1, Theorem 2.3, Corollary 2.2, pp. 4–5; proof pp. 12–13] prove the identical sharp polynomial bound only for \(0\le\alpha\le2/3\); the restriction appears explicitly in both statement and final coefficient estimate. The present result retains their constant and sharp extremal functions, but fills the entire complementary order interval \(2/3<\alpha<1\) using the independent three-moment inequality (1). The classical \(\alpha=0\) value \(84\), attributed there to Ali, Thomas and Vasudevarao, is already known and is not part of the novelty claim. Giri [2] proves Toeplitz estimates for certain subclasses of starlike mappings, and Giri–Kumar [3] treat a gap/symmetry-restricted family; the accessible abstracts do not establish the specific missing full-order bound. Their full papers could not be inspected for a definitive implication comparison.

## Limitations

Only one-variable normalized starlike functions, the complex-symmetric \(T_3(2)\), and \(0\le\alpha<1\) are covered. The endpoint \(\alpha=1\) has a degenerate class and is not part of the theorem. This result does not assert an extension to Banach-space or polydisk starlike mappings. The main related full text [1] was inspected; [2] and [3] were accessible at abstract/summary level only, so implicit equivalent coverage in those sources or older nonindexed literature remains a residual originality risk. No independent mathematical audit has been performed.

## References

[1] S. Panja, S. Majumder, A. Banerjee, *Toeplitz determinants for starlike mappings of order alpha in several complex variables*, arXiv:2610.15497v1, first public 2026-10-11, https://arxiv.org/abs/2610.15497; full accessible manuscript at https://borowiecki.dev/pdf/2610.15497.

[2] S. Giri, *Toeplitz determinant and generalized Zalcman conjecture for subclasses of starlike mappings in higher dimensions*, arXiv:2608.16562v1, first public 2026-08-17, https://arxiv.org/abs/2608.16562.

[3] S. Giri and S. Sivaprasad Kumar, *Generalized Toeplitz determinants for starlike mappings in several complex variables*, arXiv:2601.03039v1, first public 2026-01-06, https://arxiv.org/abs/2601.03039.
