# Complete Legendre minimizer classification for the ultraspherical lower envelope

## Scope after the 25 September 2026 source revision

Let \(P_n\) be the Legendre polynomial normalized by \(P_n(1)=1\).  Put \(\xi_0=-1\), and for \(k\ge1\) let \(\xi_k\) be the largest zero of the normalized Jacobi polynomial \(R_k^{(1,0)}\).

Castillo--Sadigova, arXiv:2609.15473v2, now prove the complete minimizer classification for every positive ultraspherical parameter \(\alpha>0\) (their new Proposition 6.3).  That part of the earlier SCOPE record is therefore prior coverage and is withdrawn from the novelty claim.  The remaining result is the endpoint parameter \(\alpha=0\), which v2 illustrates by the exceptional equality at \(-1/3\) but does not classify completely.

## Theorem (Legendre case)

For \(-1<x<1\):

1. If \(x\in(\xi_{k-1},\xi_k)\), then
   \[
   \operatorname*{argmin}_{n\ge0}P_n(x)=\{k\}.
   \]
2. If \(x=\xi_k\), then
   \[
   \operatorname*{argmin}_{n\ge0}P_n(\xi_k)=\{k,k+1\},
   \]
   except at \(k=1\), where \(\xi_1=-1/3\) and
   \[
   \operatorname*{argmin}_{n\ge0}P_n(-1/3)=\{1,2,5\}.
   \]
3. At the endpoints,
   \[
   \operatorname*{argmin}_{n\ge0}P_n(-1)=\{1,3,5,\ldots\},\qquad
   \operatorname*{argmin}_{n\ge0}P_n(1)=\mathbb N_0.
   \]

Consequently, in the Legendre family the choice of minimizing degree \(5\) at \(x=-1/3\) is the unique obstruction to de Oliveira Filho's arbitrary-minimizer monotonicity question.

## Proof

Write \(U_n=P_n\) and \(Q_n=R_n^{(1,0)}\).  Castillo--Sadigova prove the exact representation, for \(m\ge k\ge1\),
\[
U_m=a_k W_{m-k}^{(k,1/2)}Q_k-b_k W_{m-k-1}^{(k+1,1/2)}Q_{k-1},\qquad a_k,b_k>0,
\]
and the bound \(W_N^{(c,1/2)}(x)\le1\) in the angular ranges used for their lower-envelope theorem.

For \(x<1\) and every positive auxiliary degree in those ranges the inequality is strict.  In the rotation-controlled range, expand the transfer product as the source does.  The path that chooses the projection at the first step and the identity part thereafter has positive coefficient and first coordinate
\[
\sin\theta\,\cos(N\theta),\qquad x=\cos\theta.
\]
Because \(0<N\theta<2\pi\), this term is strictly smaller than \(\sin\theta\), while every path is at most \(\sin\theta\).  In the energy-controlled range, the endpoint product estimate is strict for \(0<1-x\) because
\[
\left(\frac{s}{s+1}\right)^2<\frac{s}{s+2},\qquad
\frac{2s+1}{(s+1)^2}>\frac2{s+2},
\]
so convexity gives a strict energy bound.  The two exceptional finite degrees are strict from the explicit positive factors in the source appendix.  Hence
\[
W_N^{(c,1/2)}(x)<1\qquad(N\ge1)
\]
whenever the source proof invokes the auxiliary estimate and \(x<1\).

For cells \(k\ge3\), subtracting the case \(m=k\) in the representation gives
\[
U_m-U_k=a_k(W_{m-k}-1)Q_k-b_k(W_{m-k-1}-1)Q_{k-1}.
\]
On an open cell \((\xi_{k-1},\xi_k)\), \(Q_{k-1}>0\) and \(Q_k<0\), so the strict auxiliary bound makes every later degree strictly larger than \(U_k\).  The contiguous relation
\[
(n+1)(1-x)Q_n(x)=U_n(x)-U_{n+1}(x)
\]
gives strict decrease of all earlier degrees down to \(k\).  At \(x=\xi_k\), the same calculation leaves equality only for degree \(k+1\); all later degrees are strict.

The first two cells are settled by the exact low-degree factors and the high-degree estimate already developed in Castillo--Sadigova.  With \(d=2\), \(t_0=1/3\), the only extra zero in the first-cell comparison is
\[
P_5(-t)+t=\frac{7t(1-t^2)(9t^2-1)}{8},
\]
which vanishes at \(t=1/3\).  Directly,
\[
P_1(-1/3)=P_2(-1/3)=P_5(-1/3)=-1/3,
\]
while the other degrees \(0\le n\le6\) are larger, and the source's high-degree bound gives \(P_n(-1/3)>-1/3\) for \(n\ge7\).  The second-cell factors give only the ordinary \(\{2,3\}\) tie at \(\xi_2\).  Endpoint parity gives the claims at \(\pm1\).

The contiguous relation then makes the sequence non-increasing up to every ordinary minimizing degree.  At the exceptional point, choosing degree \(5\) fails because \(P_2(-1/3)=-1/3<P_3(-1/3)=11/27\).  Since the minimizer classification above has no other non-adjacent tie, this is the unique obstruction in the Legendre case.

## Relation to current prior work

The original SCOPE record was written against arXiv:2609.15473v1.  On 25 September 2026, Castillo--Sadigova posted v2 and added Proposition 6.3, which proves uniqueness inside cells and exactly adjacent ties at breakpoints for every \(\alpha>0\).  Those positive-parameter statements are no longer claimed here.  Their v2 still treats \(\alpha=0\) by exhibiting the \(1,2,5\) equality and negative answer to Question 1; it does not state that this is the only non-adjacent tie or classify all Legendre minimizers.  The theorem above is restricted to that remaining case.

## Independent check

A fresh numerical stress test evaluated Legendre polynomials through degree 80 at interior points and breakpoints of the first ten cells.  Every open cell had the predicted unique minimizer, and every tested breakpoint had exactly the adjacent pair except \(-1/3\), where precisely degrees \(1,2,5\) tied.  This computation is only a consistency check; the proof above is analytic.

## Limitations

- The repaired novelty claim is only for \(\alpha=0\).  The complete \(\alpha>0\) classification is now prior work in arXiv:2609.15473v2.
- No quantitative lower gap from the minimizer is optimized.
- Originality is to the best of current indexed literature.

## References

1. K. Castillo and S. Sadigova, *The lower envelope of ultraspherical polynomials*, arXiv:2609.15473v2 (25 Sep 2026).
2. F. M. de Oliveira Filho, *New Bounds for Geometric Packing and Coloring via Harmonic Analysis and Optimization*, PhD thesis, Universiteit van Amsterdam, 2009, Section 3.5d.
