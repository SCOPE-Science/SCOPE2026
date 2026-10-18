# Complete subunit Zak-zero classification for the cubic cardinal B-spline

## Finding

Let \(B_4=\mathbf1_{[-1/2,1/2]}^{*4}\) be the centered cardinal cubic B-spline, and define its scaled Zak transform by
\[
Z_\lambda B_4(x,\nu)=\sqrt\lambda\sum_{k\in\mathbb Z}B_4(\lambda(x-k))e^{2\pi i k\nu}.
\]
For every real \(1/2\le\lambda\le1\), its entire zero set in the half-open fundamental square \([0,1)^2\) lies on the half-frequency fiber \(\nu=1/2\). The zero set is exactly
\[
\begin{cases}
\{(x,1/2):4-2/\lambda\le x\le2/\lambda-3,\ 0\le x<1\},&1/2\le\lambda\le4/7,\\
\{(1/2,1/2)\},&4/7<\lambda\le1.
\end{cases}
\]
At the lower endpoint \(\lambda=1/2\), the first description is the entire horizontal line \([0,1)\times\{1/2\}\). At \(\lambda=4/7\), the interval degenerates to the single point \((1/2,1/2)\). Thus \(4/7\) is the sharp zero-isolation threshold throughout this full subunit scale interval.

## Assumptions and scope

There are no rationality assumptions on \(\lambda\) or \(x\). The order is exactly four (polynomial degree three); the normalization \(\sqrt\lambda\) is nonvanishing and does not affect zeros. The definition uses the standard centered B-spline with integral one and support \([-2,2]\). All endpoints of the fundamental square are handled using the Zak quasi-periodicity and its real-signal symmetry; the zero interval at \(\lambda=1/2\) is taken half-open.

## Proof

**1. Reduction away from half frequency.** By evenness and reality of \(B_4\), and by the identity
\(Z_\lambda B_4(1-x,\nu)=e^{2\pi i\nu}\overline{Z_\lambda B_4(x,\nu)}\), it suffices for a nonzero imaginary part to consider \(0<x\le1/2\) and \(0<\nu<1/2\). Write \(\theta=2\pi\nu\). Only shifts of magnitude at most four can contribute, because \(2/\lambda\le4\). Set
\[
d_j=B_4(\lambda(j-x))-B_4(\lambda(j+x)),\qquad j=1,\ldots,4.
\]
Then \(d_j\ge0\), and \(d_1>0\) because \(B_4\) is strictly decreasing on \((0,2)\). Pairing the positive and negative shifts gives
\[
\frac{\Im Z_\lambda B_4(x,\nu)}{\sqrt\lambda\sin\theta}
=d_1+2c\,d_2+(4c^2-1)d_3+(8c^3-4c)d_4=:R(c),
\quad c=\cos\theta.
\]
For \(y=(1+c)/2\in(0,1)\), this cubic has degree-three Bernstein form
\[
R(c)=b_0(1-y)^3+3b_1y(1-y)^2+3b_2y^2(1-y)+b_3y^3,
\]
with the four explicit coefficients
\[
\begin{aligned}
b_0&=d_1-2d_2+3d_3-4d_4,\\
b_1&=d_1-\tfrac23d_2-\tfrac73d_3+\tfrac{28}3d_4,\\
b_2&=d_1+\tfrac23d_2-\tfrac73d_3-\tfrac{28}3d_4,\\
b_3&=d_1+2d_2+3d_3+4d_4.
\end{aligned}
\]

**2. Uniform positivity certificate.** We prove \(b_j\ge0\) for every \(1/2\le\lambda\le1\) and \(0\le x\le1/2\), exactly (not by sampling). Put \(T=2/\lambda-2\in[0,2]\) and \(X=x\in[0,1/2]\). The identity
\[
6B_4(u)=(2-|u|)_+^3-4(1-|u|)_+^3
\]
makes each \(D_j=6\lambda^{-3}d_j\) a piecewise cubic polynomial in \((T,X)\). Its branch boundaries inside the rectangle are the six rational affine lines
\[
T-X=0,\quad T-1+X=0,\quad T-1-X=0,\quad
T-2+X=0,\quad T/2-1+X=0,\quad T/2-X=0.
\]
Subdivide the rectangle along these lines. There are nine positive-area convex polygonal cells. Triangulating them without adding interior points gives ten rational triangles, of total area one. The accompanying standalone `b4_exact_certificate.py` computes all four scaled \(b_j\) as exact rational cubic polynomials on each cell, rewrites each polynomial in the standard total-degree-three triangular Bernstein basis, and verifies that **all 400 rational Bernstein coefficients are nonnegative**. The Bernstein basis is nonnegative and sums to one on each triangle, hence each \(b_j\ge0\) at *every real point* of the full parameter rectangle. Cell-edge formulas agree by continuity of \(B_4\); their zero terms agree across branches. The certificate contains no numerical threshold or interval-sampling inference.

Since \(b_3=d_1+2d_2+3d_3+4d_4>0\) for \(x>0\), the term \(b_3y^3\) is strictly positive for every \(y\in(0,1)\). Therefore \(R(c)>0\); the Zak transform has no zeros when \(0<x\le1/2\) and \(0<\nu<1/2\). Reflection in \(x\) and complex conjugation in \(\nu\) give the same conclusion throughout \(0<x<1\), \(\nu\notin\{0,1/2\}\). At \(\nu=0\), every summand is nonnegative and at least one is positive. At \(x=0\) and \(0<\nu<1/2\), Poisson summation and \(\widehat B_4(\xi)=\operatorname{sinc}(\xi)^4\) give
\[
Z_\lambda B_4(0,\nu)=\lambda^{-1/2}\sum_{m\in\mathbb Z}\operatorname{sinc}((m+\nu)/\lambda)^4>0,
\]
where \(\operatorname{sinc}(u)=\sin(\pi u)/(\pi u)\), by the \(m=0\) term because \(0<\nu<1/2\le\lambda\). The other half of the frequency square follows by complex conjugation. Thus **all** zeros must have \(\nu=1/2\).

**3. Exact half-frequency classification by frequency aliasing.** Put \(q=1/\lambda\in[1,2]\) and \(d=2-q\in[0,1]\). Poisson summation in the half-frequency fiber gives
\[
Z_{1/q}B_4(x,1/2)=\sqrt q\sum_{k\in\mathbb Z}\operatorname{sinc}(q(k+1/2))^4 e^{2\pi i(k+1/2)x}.
\]
The elementary identity \(\sin(\pi q(k+1/2))=\sin(\pi d(k+1/2))\) (up to a sign irrelevant to the fourth power) implies, for \(0<d\le1\),
\[
Z_{1/q}B_4(x,1/2)=\left(\frac d q\right)^{7/2}Z_{1/d}B_4(x,1/2).
\]
For \(d=0\), each sinc term is zero and the entire half-frequency line vanishes. For \(d>0\), the **previously published** unit-and-superunit-scale Zak-zero theorem for centered B-splines says: if \(1\le1/d<4\), there is only the zero \(x=1/2\); if \(1/d\ge4\), the zeros are exactly \(x\in[2d,1-2d]\). The inequality \(1/d\ge4\) is equivalent to \(\lambda\le4/7\); writing \(2d=4-2/\lambda\) and \(1-2d=2/\lambda-3\) yields the asserted complete zero set, including both boundary cases. This finishes the proof.

## Verification

Run `python3 b4_exact_certificate.py` using Python 3 standard library. It verifies nine full-dimensional sign cells, ten rational triangles covering area exactly one, and 400 nonnegative rational Bernstein control coefficients; 79 of these controls are zero. No floating-point arithmetic is used by the certificate. The finite control set is a **rigorous continuum positivity proof** via the Bernstein basis, whereas the cited unit/superunit Zak-zero theorem supplies the independent infinite-scale input for the half-frequency fiber.

## Relationship to prior work

Hasannasab and Lemvig (2026) establish the unit/superunit exact zero geometry used in Step 3, and study certain smaller scales; that theorem does **not** supply the new off-half-frequency nonvanishing for every real \(\lambda\in[1/2,1]\) at cubic spline order. Lemvig and Nielsen (2016) establish Gabor frame exclusions and Zak obstructions for B-splines, not this full subunit continuum zero classification. A separate known reciprocal-integer refinement case gives the endpoint \(\lambda=1/2\), but not the continuous sharp transition. In fact, their Proposition 4.1 already fixes the half-frequency zero intervals throughout the range here: **the half-frequency location and endpoint \(4/7\) are prior consequences, not claimed new in isolation**. The precise new contribution is the interval-wide proof of strict off-half-frequency nonvanishing, which upgrades that previously known linewise information to an exhaustive two-dimensional zero classification. Previously published half-frequency and larger-scale results and the sinc identity are acknowledged, not asserted novel.

## Limitations

The theorem covers the centered spline of order four only and \(1/2\le\lambda\le1\); nothing is claimed about non-reciprocal scales below \(1/2\), general higher orders, or full Gabor-frame sets. Off-half-frequency strict nonvanishing depends on the verified exact rational Bernstein certificate. The unit/superunit half-frequency zero classification is cited, not reproved. The literature comparison is bounded; possible earlier equivalent formulations have not been exhaustively excluded. Independent validation has not been performed.

## References

1. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116v1 (first public September 11, 2026), https://arxiv.org/abs/2609.13116 . Exact zero description for scaled centered B-splines at unit and larger scales.
2. J. Lemvig and K. H. Nielsen, *Counterexamples to the B-spline conjecture for Gabor frames*, arXiv:1507.03982v3 (2016), https://arxiv.org/abs/1507.03982 . Partial Gabor nonframe obstructions and Zak zero results.
