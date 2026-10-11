# A sharp phase transition for an order-three character pair
## Finding
Let \(G\) be a compact abelian group with normalized Haar measure, let \(\lambda_0,\lambda_1\in\widehat G\) be distinct characters, and suppose that the relative character
\[
\chi=\lambda_1\overline{\lambda_0}
\]
has order exactly \(3\). For every real \(p>2\), define the sharp two-character \(\Lambda(p)\) constant
\[
K_p=\sup_{(a,b)\ne(0,0)}
\frac{\|a\lambda_0+b\lambda_1\|_{L^p(G)}}
{\bigl(|a|^2+|b|^2\bigr)^{1/2}}.
\]
Then
\[
K_p^p=
\begin{cases}
\left(\dfrac32\right)^{p/2-1},&2<p<4,\\[2mm]
\dfrac32,&p=4,\\[2mm]
\dfrac{2^{p/2}+2^{\,1-p/2}}3,&p>4.
\end{cases}
\]
Every nonzero extremizer satisfies \(|a|=|b|\). Writing
\[
\phi=\arg\!\bigl(b\overline a\bigr),
\]
the complete phase classification is
\[
\begin{cases}
e^{3i\phi}=-1,&2<p<4,\\
\text{arbitrary relative phase},&p=4,\\
e^{3i\phi}=1,&p>4.
\end{cases}
\]
Thus \(p=4\) is an exact phase-transition point. Below it, the extremal squared-magnitude samples are a permutation of
\[
\left(0,\frac32,\frac32\right),
\]
whereas above it they are a permutation of
\[
\left(2,\frac12,\frac12\right).
\]

## Assumptions and scope
The Haar measure is normalized to total mass \(1\). The statement concerns exactly two distinct characters whose quotient has order \(3\), and all real exponents \(p>2\). No claim is made here for relative character order other than \(3\), for more than two frequencies, or for \(p\le2\).

Because multiplication by \(\lambda_0\) is unimodular, the norm depends only on \(\chi\). Since \(\chi\) has order \(3\), its pushforward of Haar measure is the uniform measure on the three cube roots of unity. Therefore the problem is exactly a three-sample moment maximization.

## Proof
Let \(\omega=e^{2\pi i/3}\). By the order-three pushforward just noted,
\[
\|a\lambda_0+b\lambda_1\|_p^p
=\frac13\sum_{j=0}^{2}|a+b\omega^j|^p.
\]
Normalize
\[
|a|^2+|b|^2=1.
\]
Set
\[
r=2|a||b|\in[0,1],
\qquad
\phi=\arg\!\bigl(b\overline a\bigr),
\qquad
s=\frac p2>1.
\]
The three squared magnitudes are
\[
u_j(r,\phi)=1+r\cos\!\left(\phi+\frac{2\pi j}{3}\right),
\]
so the normalized \(p\)-th moment is
\[
F_s(r,\phi)=\frac13\sum_{j=0}^{2}u_j(r,\phi)^s.
\]

For fixed \(\phi\), each summand is convex in \(r\), because \(x\mapsto x^s\) is convex on \([0,\infty)\). Hence \(F_s(\,\cdot\,,\phi)\) is convex on \([0,1]\), and its maximum occurs at an endpoint. At \(r=0\),
\[
F_s(0,\phi)=1.
\]
At \(r=1\), the three nonnegative numbers \(u_j(1,\phi)\) have mean \(1\) and are not all equal. Strict convexity gives
\[
F_s(1,\phi)>1.
\]
Consequently every global maximizer has \(r=1\), which is equivalent to
\[
|a|=|b|.
\]

It remains to optimize the phase. With \(r=1\), write
\[
u_j=1+\cos\!\left(\phi+\frac{2\pi j}{3}\right).
\]
Elementary symmetric identities give
\[
\sum_j u_j=3,
\qquad
\sum_{i<j}u_i u_j=\frac94,
\qquad
\prod_j u_j=q=\frac{1+\cos(3\phi)}4.
\]
Thus \(q\in[0,1/2]\), and \(u_0,u_1,u_2\) are the roots of
\[
P_q(t)=t^3-3t^2+\frac94t-q.
\]
Define
\[
\Phi_s(q)=\frac13\sum_{j=0}^{2}u_j(q)^s.
\]
For \(0<q<1/2\), the three roots are positive and distinct. Differentiating \(P_q(u_j(q))=0\) yields
\[
u_j'(q)=\frac1{P_q'(u_j)}.
\]
Hence
\[
3\Phi_s'(q)
=s\sum_{j=0}^{2}\frac{u_j^{\,s-1}}{P_q'(u_j)}.
\]
For three distinct nodes, the sum on the right is the second divided difference of
\[
f(t)=t^{s-1}.
\]
By the mean-value theorem for divided differences, its sign is the sign of \(f''\) at some positive point. Since
\[
f''(t)=(s-1)(s-2)t^{s-3},
\]
we obtain:
\[
\Phi_s'(q)<0\quad(1<s<2),\qquad
\Phi_2'(q)=0,\qquad
\Phi_s'(q)>0\quad(s>2).
\]

Therefore \(q=0\) is the unique maximizing endpoint when \(1<s<2\), every phase is maximizing when \(s=2\), and \(q=1/2\) is the unique maximizing endpoint when \(s>2\). At \(q=0\), the roots are
\[
\left(0,\frac32,\frac32\right),
\]
so
\[
\Phi_s(0)=\frac23\left(\frac32\right)^s
=\left(\frac32\right)^{s-1}.
\]
At \(q=1/2\), the roots are
\[
\left(2,\frac12,\frac12\right),
\]
so
\[
\Phi_s\!\left(\frac12\right)
=\frac{2^s+2^{1-s}}3.
\]
Substituting \(s=p/2\) proves the displayed formula for \(K_p^p\).

Finally,
\[
q=0\iff \cos(3\phi)=-1\iff e^{3i\phi}=-1,
\]
while
\[
q=\frac12\iff \cos(3\phi)=1\iff e^{3i\phi}=1.
\]
Together with \(r=1\), these are exactly the equality conditions stated above.

## Verification
The proof is analytic and does not depend on finite enumeration. The accompanying `verify.py` independently checks the symmetric identities, endpoint formulas, the \(p=4\) phase-independence identity, and a deterministic grid of coefficient ratios and phases for representative exponents on both sides of \(4\). The numerical grid is only a regression test; it is not used to establish the theorem for all real \(p>2\).

The critical nonstandard step is the phase monotonicity. It is proved in the preceding section by expressing the derivative as a second divided difference of \(t^{s-1}\), whose sign is determined by
\[
(s-1)(s-2)t^{s-3}.
\]
This gives the strict reversal exactly at \(s=2\), equivalently \(p=4\).

## Relationship to prior work
Michels' paper on \(\Lambda(p)\)-sets supplies the standard \(L^p/L^2\) framework and notation \(K_p\), but its principal theorem concerns infinite character sets and operator-ideal limit orders. The inspected full arXiv text does not evaluate the two-character order-three constant or classify its extremal phases.

A previously indexed exact result for finite-order character pairs, opaque identifier `22b99d88-ea1a-487a-96b5-00978ba2a4dd`, determines all even moments. For relative order \(3\), it recovers the present values at \(p=4,6,8,\ldots\), including phase freedom at \(p=4\) and the aligned phase condition for even \(p\ge6\). It does not imply the real-exponent interval \(2<p<4\), where the extremizing phase reverses to \(e^{3i\phi}=-1\), nor does it give the monotonicity argument across all non-even exponents.

Gilbert and Rzeszotnik calculate norms of the full Fourier transform between \(L^p\) spaces on finite abelian groups and their duals. That operator is different from the two-dimensional synthesis embedding treated here, and the published abstract does not state the claimed sharp subspace constant or its phase transition.

Targeted searches under the equivalent descriptions “order-three character pair,” “two-dimensional Fourier subspace on \(\mathbb Z_3\),” “cube-root two-term polynomial,” and the explicit constant formulas did not locate a statement implying the theorem. This is evidence for originality, not a proof that no equivalent older formulation exists.

## Limitations
The result is specific to a relative character of order \(3\). It does not classify real-\(p\) behavior for other finite orders, where the phase geometry has more degrees of freedom. The originality comparison leaves a residual risk that the same two-dimensional norm calculation appears in older finite-dimensional \(L^p\) or Banach-space literature under notation unrelated to \(\Lambda(p)\)-sets.

The deterministic numerical checks are finite and therefore do not certify the universal claim; the universal claim rests entirely on the analytic convexity and divided-difference proof.

## References
1. C. Michels, “\(\Lambda(p)\)-sets and the limit order of operator ideals,” arXiv:math/9904176v1, first public version 1999-04-30. Primary MSC includes 43A46.
2. J. Gilbert and Z. Rzeszotnik, “The norm of the Fourier transform on finite abelian groups,” *Annales de l'Institut Fourier* 60 (2010), 1317–1346, DOI 10.5802/aif.2556.
