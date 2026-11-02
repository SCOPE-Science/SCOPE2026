# Sharp endpoint–Hilbert compatibility spectrum for three-point conditional expectations

## Finding
Fix any three-point probability space with strictly positive masses \(a,b,c\), where \(a+b+c=1\). Let \(P\) be conditional expectation onto the partition \(\{\{1,2\},\{3\}\}\), and let \(Q\) be conditional expectation onto \(\{\{1\},\{2,3\}\}\). Define the commutator \(K=PQ-QP\), its Hilbert operator norm \(h=\|K\|_{L^2\to L^2}\), and its endpoint operator norm \(e=\|K\|_{L^\infty\to L^\infty}\).

For \(0<h\le1/2\), put
\[
z_-(h)=\frac{1-\sqrt{1-4h^2}}2,
\qquad z_+(h)=\frac{1+\sqrt{1-4h^2}}2.
\]
**The complete set of attainable endpoint norms at a prescribed Hilbert commutator norm \(h\) is the closed interval**
\[
\boxed{\quad
2\max\{z_-(h),\sqrt{z_-(h)}-z_-(h)\}
\ \le e\le\ 2z_+(h).
\quad}
\]
Every number in this interval is realized by strictly positive masses on exactly three points. In particular, the sharp upper envelope is \(1+\sqrt{1-4h^2}\), which tends to \(2\) as \(h\downarrow0\); the sharp lower envelope tends to \(0\). Therefore Hilbert-norm almost commutativity of two conditional expectations does not give endpoint-norm almost commutativity even on three-point spaces with full support. Two-point probability spaces cannot exhibit this obstruction.

## Assumptions and scope
All functions are real-valued. Each atom has strictly positive mass, and all operator norms use the **same** probability measure. Conditional expectations are defined by weighted block averages. The two partitions are fixed as displayed; any two distinct nontrivial binary partitions of a three-point space are equivalent after relabeling. Norms are operator norms, not numerical radii. The parameter \(h\) is necessarily strictly positive and at most \(1/2\). There is no claim of endpoint continuity at the degenerate boundary where an atom loses its mass.

## Proof
**1. Exact weighted commutator.** Set \(x=a/(a+b)\), \(y=c/(b+c)\). Then \(0<x,y<1\), and the expectation matrices acting on coordinate functions are
\[
P=\begin{pmatrix}x&1-x&0\\x&1-x&0\\0&0&1\end{pmatrix},
\qquad
Q=\begin{pmatrix}1&0&0\\0&1-y&y\\0&1-y&y\end{pmatrix}.
\]
Consequently, writing \(z=xy\), direct multiplication gives
\[
K=\begin{pmatrix}
0&-(y-z)&y-z\\
z&0&-z\\
-(x-z)&x-z&0
\end{pmatrix}.
\]
The exact \(L^\infty\) norm is the maximum absolute row sum, attained by choosing the signs of the inputs to match the maximizing row. Thus
\[
\boxed{\ e=2\max\{z,x-z,y-z\}.\ }
\]

**2. Exact Hilbert norm.** The operators \(P,Q\) are orthogonal projections in the weighted real Hilbert space \(L^2(a,b,c)\). Therefore \(K^*=-K\). Its three-dimensional real matrix is similar, by the positive square-root mass diagonal, to a skew-symmetric matrix. Since \(K\ne0\), its nonzero singular values both equal \(h\), and \(-\operatorname{tr}(K^2)=2h^2\). Using the matrix above, put \(A=y-z\), \(B=x-z\). Then
\[
-\tfrac12\operatorname{tr}(K^2)=Az+AB+Bz
=xy(1-xy)=z(1-z).
\]
Hence
\[
\boxed{\ h^2=z(1-z).\ }
\]
This well-known two-projection angle structure is not, by itself, the new endpoint compatibility statement.

**3. Every pair of parameters is permitted.** Conversely, for arbitrary \(0<x,y<1\), choose unnormalized positive masses \(a=x/(1-x)\), \(b=1\), \(c=y/(1-y)\), then divide all three by their sum. This recovers exactly the chosen \(x,y\). Thus no hidden constraints arise from probability normalization. At fixed \(h\), solving \(z(1-z)=h^2\) yields precisely \(z=z_-(h)\) or \(z=z_+(h)\).

**4. Lower and upper envelopes.** Fix \(z\in(0,1)\) and vary \(x,y\in(0,1)\) with \(xy=z\). Then \(z<x,y<1\), and \(\max(x,y)\ge\sqrt z\). Therefore
\[
2\max\{z,\sqrt z-z\}\le e\le2\max\{z,1-z\}.
\]
The lower bound is attained at \(x=y=\sqrt z\). If \(z\ge1/2\), then \(x-z<1-z\le z\) and \(y-z<1-z\le z\), so **every** admissible pair has \(e=2z\). In particular, the branch \(z=z_+(h)\) always attains the asserted upper envelope \(e=2z_+(h)\).

For the other branch \(z=z_-(h)\le1/2\), the lower envelope is attained at \(x=y=\sqrt{z_-}\). Along the continuous curve \(x\in(z_-,1)\), \(y=z_-/x\), the endpoint expression is continuous, attains the lower envelope, and approaches \(2(1-z_-)\) at either open endpoint. The intermediate value theorem therefore realizes *every* endpoint norm between its lower envelope and \(2(1-z_-)\), excluding at most this upper endpoint. But \(2(1-z_-)=2z_+\), already attained on the \(z_+\) branch. This proves that the entire stated closed interval, and no values outside it, is attainable. At \(h=1/2\), both roots equal \(1/2\), so the interval is the singleton \(e=1\), as required.

**5. Strong endpoint separation and minimal support.** As \(h\downarrow0\), \(z_-(h)\sim h^2\) and \(z_+(h)\to1\). The lower envelope is asymptotic to \(2h\), while the upper envelope tends to \(2\). Both are attained by strictly positive mass triples at every \(h>0\), so the separation is not a formal zero-weight artifact. On a two-point probability space every conditional expectation is either the identity or the expectation onto constants; all such operators commute. Hence three points are the smallest support size for this phenomenon.

## Verification
The standalone `verify_tradeoff.py` uses exact rational arithmetic to compare independently multiplied conditional-expectation matrices with the displayed commutator; it also checks the row-sum and Hilbert trace identities over 4,096 positive rational mass triples. It verifies selected sharp endpoint families with exact fractions. Running `python verify_tradeoff.py` produces `EXACT_WEIGHTED_COMMUTATOR_IDENTITIES_OK 4096` and `SHARP_ENDPOINT_FAMILIES_OK`. This finite check is diagnostic; the universal quantifiers and all intermediate endpoint values follow from the analytic proof.

## Relationship to prior work
The classical alternating-projection literature expresses Hilbert-space convergence in terms of principal angles; Badea and Seifert (2015 preprint, published 2016), particularly their geometric comparisons and main convergence theorem, provide this Hilbert-side context. Cohen (2007) studies convergence of iterated products of conditional expectations in \(L^p\); his full available manuscript concerns powers and maximal estimates, not the endpoint commutator-versus-Hilbert compatibility interval. Previously published calculations for the **same three-site pair** determine a numerical radius on uniform real \(\ell_4^3\), a different invariant; published formulas for ordered binary conditional-expectation products determine individual centered product norms for \(1<p<\infty\), not the sharp norm of their *difference* at the endpoint under a fixed Hilbert commutator norm. The elementary matrix and two-projection identities are not claimed individually as new; the quantitative compatibility spectrum and sharp attained separation are the claim.

## Limitations
The complete compatibility interval is established only for the specified pair of nontrivial two-block expectations on three positive-mass atoms. It does not assert an analogous interval for four or more atoms, arbitrary sigma-algebra pairs, or unrelated positive contractions. Originality is evaluated against inspected available literature; an equivalent unindexed or differently formulated historical statement cannot be ruled out. The proof is self-contained but has not undergone independent scientific audit.

## References
1. C. Badea and D. Seifert, *Ritt operators and convergence in the method of alternating projections*, arXiv:1510.04560, first submitted 2015-10-15, https://arxiv.org/abs/1510.04560 .
2. G. Cohen, *Iterates of a product of conditional expectation operators*, Journal of Functional Analysis 242 (2007), 658–668, DOI:10.1016/j.jfa.2006.09.008; author-hosted manuscript https://www.ee.bgu.ac.il/~guycohen/conex.pdf .
3. *Sharp numerical radius of a three-point conditional-expectation commutator*, publicly indexed research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-numerical-radius-of-a-three-point-conditional-expectation--d81ced4c9642 .
4. *Exact mixing norms and time-reversal obstruction for binary conditional-expectation chains*, publicly indexed research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-mixing-norms-and-time-reversal-obstruction-for-binary-cond--8cff936fbe0f .
