# Complete minimizer classification for the ultraspherical lower envelope

## Statement

For \(a,b>-1\), write
\[
R_n^{(a,b)}(x)=\frac{P_n^{(a,b)}(x)}{P_n^{(a,b)}(1)}.
\]
Fix \(\alpha\ge 0\), set
\[
U_n(x)=R_n^{(\alpha,\alpha)}(x),\qquad
Q_n(x)=R_n^{(\alpha+1,\alpha)}(x),
\]
put \(\xi_0=-1\), and for \(k\ge1\) let \(\xi_k\) be the largest zero of \(Q_k\).
Castillo--Sadigova proved that \(U_k\) attains the pointwise minimum on
\([\xi_{k-1},\xi_k]\).

The set of *all* minimising degrees is in fact completely determined.

**Theorem.** For every \(\alpha\ge0\):

1. if \(x\in(\xi_{k-1},\xi_k)\), \(k\ge1\), then
   \[
   \operatorname*{argmin}_{n\ge0}U_n(x)=\{k\};
   \]
2. if \(x=\xi_k\), \(k\ge1\), then
   \[
   \operatorname*{argmin}_{n\ge0}U_n(\xi_k)=\{k,k+1\},
   \]
   except for the single case
   \[
   \alpha=0,\qquad k=1,\qquad \xi_1=-\frac13,
   \]
   where
   \[
   \operatorname*{argmin}_{n\ge0}P_n(-1/3)=\{1,2,5\};
   \]
3. at the two endpoints,
   \[
   \operatorname*{argmin}_{n\ge0}U_n(-1)=\{1,3,5,\ldots\},
   \qquad
   \operatorname*{argmin}_{n\ge0}U_n(1)=\mathbb N_0.
   \]

Consequently, for \(-1<x<1\), the Legendre triple
\[
(\alpha,x,k)=(0,-1/3,5)
\]
is the only instance in which a minimising degree \(k\) fails de Oliveira Filho's
monotonicity condition
\[
U_0(x)\ge U_1(x)\ge\cdots\ge U_k(x).
\]
Thus the counterexample exhibited by Castillo--Sadigova is the unique obstruction
within the full ultraspherical family \(\alpha\ge0\).

## Proof

The proof sharpens the inequalities in Castillo--Sadigova, arXiv:2609.15473,
by retaining their equality cases.

### 1. A strict auxiliary-polynomial bound

Put \(\lambda=\alpha+\tfrac12\). For \(c>0\), let \(W_N^{(c,\lambda)}\) be defined by
\[
W_{-1}=W_0=1,
\]
\[
(c+r+2\lambda)W_{r+1}(x)
=
2(c+r+\lambda)xW_r(x)-(c+r)W_{r-1}(x).
\]
Corollary 3.2 of Castillo--Sadigova states that, if
\[
x=\cos\theta,\qquad
0\le\theta\le \min\!\left\{\frac\pi2,\frac{4\pi\lambda}c\right\},
\]
then \(W_N^{(c,\lambda)}(x)\le1\).

For \(0<\theta\) this inequality is strict for every \(N\ge1\):
\[
\boxed{W_N^{(c,\lambda)}(\cos\theta)<1,\qquad N\ge1.}
\]

Here are the equality-sensitive points in the source proof. Its positive connection
formula is
\[
W_N^{(c,\lambda)}
=
\sum_{j=0}^N d_{N,j}W_j^{(K,1/2)},
\qquad
d_{N,j}\ge0,\quad \sum_jd_{N,j}=1,\quad d_{N,N}>0,
\]
with \(K=c/(2\lambda)\). Thus it suffices to make the \(\lambda=1/2\) bound
strict at degree \(N\).

For the rotation-controlled degrees, the source writes the first coordinate of the
transfer vector as a convex combination of products of cosines. The term obtained
by projecting at the first step and taking the identity at all later steps is
\[
\sin\theta\,\cos(N\theta).
\]
Its coefficient is positive. Under \((N+1)\theta\le2\pi\) and \(N\ge1\),
\(0<N\theta<2\pi\), so this term is strictly smaller than \(\sin\theta\), while
all terms are at most \(\sin\theta\). Hence \(W_N^{(K,1/2)}<1\).

For the energy-controlled degrees, the source estimates
\[
E_N\le 2yF(y),\qquad y=1-\cos\theta,
\]
and compares \(F\) with the secant \(1-y/2\). The endpoint comparisons used there
are strict for \(y>0\), because
\[
1-\delta_s=\left(\frac{s}{s+1}\right)^2<\frac{s}{s+2},
\qquad
\delta_s=\frac{2s+1}{(s+1)^2}>\frac{2}{s+2}.
\]
Thus \(E_N<2y-y^2=\sin^2\theta\), which gives
\(|W_N^{(K,1/2)}|<1\). In the refined \(K\ge6\) branch the source already obtains
a strict endpoint product bound; the exceptional degrees \(4\) and \(5\) have
\(1-W_N=(1-x)\) times a strictly positive factor, and the remaining degree \(6\)
again has a strict product estimate. This proves the displayed strict bound.

### 2. All cells from the third onward

For \(m\ge k\ge1\), Castillo--Sadigova prove
\[
U_m
=
a_k W_{m-k}^{(k,\lambda)}Q_k
-
b_k W_{m-k-1}^{(k+1,\lambda)}Q_{k-1},
\qquad a_k,b_k>0.
\]
Subtracting the case \(m=k\),
\[
U_m-U_k
=
a_k\!\left(W_{m-k}^{(k,\lambda)}-1\right)Q_k
-
b_k\!\left(W_{m-k-1}^{(k+1,\lambda)}-1\right)Q_{k-1}.
\]

Let \(k\ge3\). On the open cell \((\xi_{k-1},\xi_k)\),
\[
Q_{k-1}>0,\qquad Q_k<0.
\]
The angular estimate in Proposition 4.1 of the source puts both auxiliary families
\(c=k\) and \(c=k+1\) in the strict bound above. If \(m=k+1\), the first
auxiliary index is \(1\), hence the first term in \(U_m-U_k\) is strictly positive.
If \(m\ge k+2\), both auxiliary indices are positive, so both terms are strictly
positive. Therefore
\[
U_m(x)>U_k(x)\qquad(m>k).
\]
For \(m<k\), the contiguous relation
\[
(n+\alpha+1)(1-x)Q_n(x)
=
(\alpha+1)\bigl(U_n(x)-U_{n+1}(x)\bigr)
\]
and the strict positivity of \(Q_n\) to the right of its largest zero give
\[
U_0>U_1>\cdots>U_k.
\]
Thus \(k\) is the unique minimiser in the open cell.

At \(x=\xi_k\), \(Q_k=0\) and \(Q_{k-1}>0\). The same difference formula gives
equality for \(m=k+1\), because the second auxiliary index is \(0\), and strict
positivity for every \(m\ge k+2\), because then
\(W_{m-k-1}^{(k+1,\lambda)}<1\). Earlier degrees are strictly larger.
Hence the only minimisers at \(\xi_k\) are \(k,k+1\).

### 3. The first two cells

Write
\[
d=2\alpha+2\ge2,\qquad
t_0=\frac1{d+1},\qquad
t_1=\frac1{1+\sqrt{d+4}}.
\]
The first two breakpoints are
\[
\xi_1=-t_0,\qquad \xi_2=t_1.
\]

For degrees \(n\ge7\), Section 5 of the source introduces
\[
M(t)=\mathbb E\frac{Y_t^3+Y_t^4}{2}
\]
and proves
\[
U_n(x)\ge -M(|x|).
\]
On the first cell it sets \(F(t)=t-M(t)\), proves \(F(t_0)>0\), \(F(1)=0\),
and proves \(F\) concave. Therefore
\[
F(t)>0\qquad(t_0\le t<1),
\]
so
\[
U_n(-t)>-t=U_1(-t),\qquad n\ge7,\quad t_0\le t<1.
\]
On the second cell, the source proves
\[
-M(|x|)>U_2(x)
\qquad(-t_0\le x\le t_1);
\]
the strictness follows from the positive endpoint estimates for its decreasing
function \(G(y)=-U_2(\sqrt y)-M(\sqrt y)\). Hence no degree \(n\ge7\) can tie
on either finite endpoint \(\xi_1,\xi_2\).

It remains to retain equality cases in the explicit degree-\(\le6\) formulas from
Appendix B. On the first cell, with \(x=-t\),
\[
U_2(-t)+t
=
\frac{(1+t)((d+1)t-1)}d,
\]
so degree \(2\) ties degree \(1\) only at \(t=t_0\). The formulas for degrees
\(3,4,6\) are strictly positive for \(t_0\le t<1\). For degree \(5\),
\[
U_5(-t)+t
=
\frac{t(d+5)(1-t^2)\bigl((d+7)t^2+d-3\bigr)}{d(d+2)}.
\]
The last factor is increasing in \(t\), and at \(t=t_0\) equals
\[
\frac{(d-2)(d-1)(d+2)}{(d+1)^2}.
\]
Thus the only extra equality is
\[
d=2,\quad t=t_0=\frac13,
\]
namely \(\alpha=0\), \(x=-1/3\), and degree \(5\).

On the second cell, the explicit formulas in Appendix B have the following equality
cases: degree \(1\) ties \(U_2\) only at \(-t_0\), degree \(3\) ties only at \(t_1\),
degrees \(4\) and \(6\) are strictly larger throughout, and degree \(5\) is strictly
larger except at \(d=2,x=-t_0\). Indeed,
\[
U_3-U_2
=
\frac{(x-1)((d+3)x^2+2x-1)}d
\]
has its right zero at \(t_1\), while the degree-\(5\) sign analysis in Appendix B is
strict except for the same \(d=2,u=t_0\) endpoint. Therefore
\[
\operatorname*{argmin}U_n(x)=\{1\}
\quad(-1<x<\xi_1),
\]
\[
\operatorname*{argmin}U_n(x)=\{2\}
\quad(\xi_1<x<\xi_2),
\]
\[
\operatorname*{argmin}U_n(\xi_2)=\{2,3\},
\]
and
\[
\operatorname*{argmin}U_n(\xi_1)=
\begin{cases}
\{1,2,5\},&\alpha=0,\\
\{1,2\},&\alpha>0.
\end{cases}
\]

Finally \(U_n(1)=1\) and \(U_n(-1)=(-1)^n\), which gives the endpoint statements.

### 4. Consequence for de Oliveira Filho's Question 1

For an interior point, the minimising degree is unique and the contiguous relation
gives strict decrease up to it. At an ordinary breakpoint \(\xi_k\), the only choices
are \(k\) and \(k+1\), and
\[
U_0>\cdots>U_k=U_{k+1},
\]
so the requested sequence is non-increasing for either minimising index.

The only remaining possibility is the exceptional Legendre point. There
\[
P_1(-1/3)=P_2(-1/3)=P_5(-1/3)=-\frac13,
\]
but
\[
P_3(-1/3)=\frac{11}{27}>-\frac13.
\]
Hence choosing minimising degree \(5\) violates monotonicity, while choosing degrees
\(1\) or \(2\) does not. This proves uniqueness of the obstruction.

## Context and relation to prior literature

Castillo--Sadigova, *The lower envelope of ultraspherical polynomials*,
arXiv:2609.15473 (submitted 14 September 2026), proves the complete lower-envelope
value theorem
\[
U_k(x)=\min_{n\ge0}U_n(x),\qquad \xi_{k-1}\le x\le\xi_k.
\]
Their introduction notes the guaranteed adjacent ties at breakpoints and says that
additional minimising degrees can occur. Section 6 exhibits the Legendre equality
\(P_1(-1/3)=P_2(-1/3)=P_5(-1/3)\), using it to answer de Oliveira Filho's
Question 1 negatively, but it does not classify all minimising indices.

De Oliveira Filho's 2009 thesis formulates Question 1 on p. 47 and Question 2
(the lower-envelope cell conjecture) immediately afterward. Castillo--Sadigova
settle Question 2. The theorem above completes the equality-case analysis left by
that result and shows that the counterexample to Question 1 is isolated and unique.

## Limitations

The result is restricted to the normalized ultraspherical family
\(R_n^{(\alpha,\alpha)}\) with \(\alpha\ge0\). It does not classify minimisers
for general asymmetric Jacobi parameters, nor does it provide quantitative gaps
between the minimum and the next value away from the breakpoints. The originality
assessment is to the best of our knowledge; the directly relevant preprint is very
recent, so an unindexed contemporaneous observation remains a residual risk.

## References

1. K. Castillo and S. Sadigova, *The lower envelope of ultraspherical polynomials*,
   arXiv:2609.15473, 2026. https://arxiv.org/abs/2609.15473
2. F. M. de Oliveira Filho, *New Bounds for Geometric Packing and Coloring via
   Harmonic Analysis and Optimization*, PhD thesis, Universiteit van Amsterdam,
   2009, Section 3.5d. https://ir.cwi.nl/pub/14499
