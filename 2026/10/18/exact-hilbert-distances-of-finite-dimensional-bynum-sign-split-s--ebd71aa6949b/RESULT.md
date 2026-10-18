# Exact Hilbert distances of finite-dimensional Bynum sign-split spaces

## Finding

For every integer \(n\ge2\), equip \(\mathbb R^n\) with the Bynum norm
\[
N(x)=\max\bigl\{\|x_+\|_2,\|x_-\|_2\bigr\},\qquad (x_+)_i=\max(x_i,0),\quad (x_-)_i=\max(-x_i,0).
\]
Let \(d_n\) be its **multiplicative** Banach–Mazur distance to real \(\ell_2^n\). Define \(c_n=(\sqrt{n-1}-1)^2\) and
\[
F_n(t)=\frac{1+(n-1)t}{1+nt}\,\max\{1+nt,\;2+c_nt\},\qquad t\ge0.
\]
Then
\[
\boxed{d_n^2=\min_{t\ge0}F_n(t)}.
\]
The exact values are
\[
\boxed{d_2^2=\frac32,\quad d_3^2=1+\frac1{\sqrt2},\quad d_4^2=1+\frac{\sqrt3}{2},\quad d_5^2=\frac{49}{25},\quad d_n^2=2\ (n\ge7).}
\]
For \(n=6\), put \(c_6=6-2\sqrt5\). The unique positive root \(t_6\) of
\[
(c_6-2)+10c_6t_6+30c_6t_6^2=0
\]
satisfies \(t_6\approx0.0284700655417\), and
\[
\boxed{d_6^2=\frac{(2+c_6t_6)(1+5t_6)}{1+6t_6}\approx1.99380799.}
\]
An optimal Euclidean pullback in every dimension has quadratic form
\[
Q_t(x)=\sum_{i=1}^n x_i^2+t\left(\sum_{i=1}^n x_i\right)^2,
\]
where the unique optimal **symmetric** parameter is \(t=(2\sqrt{n-1})^{-1}\) for \(n=2,3,4\), \(t=1/10\) for \(n=5\), \(t=t_6\) for \(n=6\), and \(t=0\) for \(n\ge7\). In particular the standard Euclidean form is optimal exactly from dimension seven onward.

## Assumptions and scope

All scalars are real. The convention for the norm is Bynum's \(b_{2,\infty}\), restricted to the first \(n\) coordinates; the plus and minus parts are taken coordinatewise. The distance is \(d_n=\inf_{T\in GL(n,\mathbb R)}\|T\|_{B\to2}\|T^{-1}\|_{2\to B}\), **not** its logarithm. The result treats every integer \(n\ge2\), with no claim about uniqueness of nonsymmetric optimal pullbacks or other \(b_{p,q}\) parameters.

## Proof

**1. Reduction to symmetric ellipsoids.** For a positive definite symmetric matrix \(Q\), let
\[
L(Q)=\min_{x\ne0}\frac{x^TQx}{N(x)^2},\qquad
U(Q)=\max_{x\ne0}\frac{x^TQx}{N(x)^2}.
\]
The squared distortion of its associated Euclidean norm is \(U(Q)/L(Q)\). If \(aN(x)^2\le x^TQx\le bN(x)^2\) for all \(x\), then the same inequalities hold after averaging \(Q\) over coordinate permutations, since \(N\) is permutation invariant. Therefore the infimum over all Euclidean pullbacks equals the infimum over positive forms of the shape \(Q=\alpha I+\beta\mathbf1\mathbf1^T\). Here \(\alpha>0\) and \(\beta/\alpha>-1/n\). Rescaling permits \(Q=Q_t\) with \(t>-1/n\).

If \(-1/n<t<0\), test the uniform positive vector \(u=(1/\sqrt n,\ldots,1/\sqrt n)\) and the opposite-coordinate vector \(v=(1,-1,0,\ldots,0)\). Both have \(N=1\), whereas \(Q_t(u)=1+nt\) and \(Q_t(v)=2\). Hence \(U(Q_t)/L(Q_t)\ge2/(1+nt)>2\); since \(Q_0\) has distortion squared \(2\), a minimizer can have \(t\ge0\).

**2. Exact lower Rayleigh bound.** Fix \(t\ge0\) and normalize \(N(x)=1\). By replacing \(x\) by \(-x\), assume \(\|x_+\|_2=1\), and put \(v=\|x_-\|_2\in[0,1]\). The positive support has at most \(n-1\) elements unless \(v=0\). The sums satisfy \(\sum_i(x_+)_i\ge1\), \(\sum_i(x_-)_i\le\sqrt{n-1}v\); for \(v=0\) the same resulting inequality is valid. Thus
\[
Q_t(x)\ge1+v^2+t\bigl(1-\sqrt{n-1}v\bigr)_+^2
\ge \frac{1+nt}{1+(n-1)t},
\]
where the last inequality follows by minimizing the displayed quadratic for \(v\le1/\sqrt{n-1}\) and using \(1+v^2\ge n/(n-1)\) for larger \(v\). Equality occurs for
\[
x=(1,-s,\ldots,-s),\qquad s=\frac{t}{1+(n-1)t},
\]
since \((n-1)s^2\le1\). Hence
\[
\boxed{L(Q_t)=\frac{1+nt}{1+(n-1)t}}.
\]

**3. Exact upper Rayleigh bound.** If \(x\) has one sign, \(N(x)=1\) implies \(Q_t(x)\le1+nt\), with equality at the constant-sign uniform vector. Otherwise, after sign reversal, write \(\|x_+\|_2=1\), \(\|x_-\|_2=v\in(0,1]\). Both signs have at least one coordinate, so, writing \(a=\sqrt{n-1}\),
\[
1\le\sum_i(x_+)_i\le a,\qquad v\le\sum_i(x_-)_i\le av.
\]
Consequently
\[
Q_t(x)\le1+v^2+t\max\{(a-v)^2,(av-1)^2\}.
\]
Each of the two quadratics on the right is convex in \(v\in[0,1]\); their maximum therefore cannot exceed its maximum at an endpoint. At \(v=0\) the endpoint bounds are at most \(1+nt\), while at \(v=1\) both equal \(2+t(a-1)^2\). That latter value is attained by the vector with \(n-1\) positive coordinates \(1/\sqrt{n-1}\) and one negative coordinate \(-1\). Thus
\[
\boxed{U(Q_t)=\max\{1+nt,\;2+c_nt\}},\qquad c_n=(\sqrt{n-1}-1)^2.
\]
The two boxed extrema prove \(d_n^2=\min_{t\ge0}F_n(t)\).

**4. One-variable sharp optimization.** The two branches of the maximum cross at \(t_c=1/(2\sqrt{n-1})\). For \(t\ge t_c\), \(F_n(t)=1+(n-1)t\), which increases strictly. For \(0\le t\le t_c\),
\[
F_n(t)=\frac{(2+c_nt)(1+(n-1)t)}{1+nt},\quad
\operatorname{sgn}F_n'(t)=\operatorname{sgn}H_n(t),
\]
where
\[
H_n(t)=c_n-2+2c_n(n-1)t+nc_n(n-1)t^2.
\]
The polynomial \(H_n\) is strictly increasing for positive \(t\) when \(n>2\), and for \(n=2\) it is the negative constant \(-2\). For \(n=2,3\), \(H_n(t_c)<0\); for \(n=4\), \(H_4(t_c)=0\). Thus \(t_c\) is the unique minimizer for \(n=2,3,4\), giving the first three exact values above. For \(n=5\), \(c_5=1\), and \(H_5(t)=-1+8t+20t^2\) vanishes at \(t=1/10<t_c\). This yields \(F_5(1/10)=49/25\). At \(n=6\), \(0<c_6<2\), so \(H_6\) has precisely one positive root, strictly before \(t_c\), giving the stated formula. Finally \(c_n>2\) for \(n\ge7\), hence \(H_n(0)>0\) and \(F_n\) increases from \(t=0\); its minimum is \(F_n(0)=2\). These sign arguments also establish the asserted uniqueness **among symmetric pullback forms**.

## Verification

The standalone `checker.py` independently evaluates the proposed exact upper and lower Rayleigh bounds on 378,000 pseudorandom signed vectors across dimensions \(2\) through \(10\) and seven nonnegative parameters, checks explicit extremizers, scans a scalar parameter grid against the claimed minima, and tests the exact identity \(d_5^2=49/25\). Run `python3 checker.py` using the Python 3 standard library. The proof above, not sampling, establishes the theorem for **all** dimensions, vectors, and parameters. In the executable, finite grid checks use tolerances and are not exhaustive mathematical certificates.

## Relationship to prior work

Bynum introduced norms separating the positive and negative parts of a sequence in 1972 to study normal structure. Kato, Maligranda, and Takahashi (2001), Section 5 and Example 8, describe \(b_{p,q}\) and use equivalent-norm inequalities to estimate James, Jordan–von Neumann, and normal-structure constants. Their simple comparison with \(\ell_2\) gives the universal distance upper bound \(\sqrt2\) but does not evaluate the exact finite-section distance or give an optimal tilted quadratic form. The present calculation yields strict finite-dimensional improvement through dimension six and proves that \(\sqrt2\) first becomes sharp in dimension seven.

## Limitations

No claim concerns the infinite-dimensional distance beyond consequences already in the literature, the normal-structure coefficient, or general parameters \(p,q\). A mathematical literature search found no explicit published formula for the finite-dimensional case, but a bibliographic search cannot establish uniqueness of a result; specialized or incompletely indexed sources may still exist. Independent audit has not been performed. Numerical checks only support the analytic derivation.

## References

1. W. L. Bynum, *A class of spaces lacking normal structure*, Compositio Mathematica 25 (1972), 233–236. https://www.numdam.org/item/CM_1972__25_3_233_0/ .
2. M. Kato, L. Maligranda, Y. Takahashi, *On James and Jordan–von Neumann constants and the normal structure coefficient of Banach spaces*, Studia Mathematica 144 (2001), 275–295, DOI: 10.4064/sm144-3-5. https://www.impan.pl/shop/en/publication/transaction/download/product/90130 .
