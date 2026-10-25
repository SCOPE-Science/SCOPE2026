# Sharp simultaneous face-gap majorization for three-level ranked posets

## Finding
Let \(A_m\) denote an antichain of size \(m\). For positive integers \(a,b\), put \(P_{a,b}=A_a\oplus\{q\}\oplus A_b\): every bottom element lies below \(q\), which lies below every top element. This is the smallest natural complete-ranked family that contains the five-element Hibi–Li X-obstruction when both outside layers have size at least two.

Write \(d=a+b+1\), and for a \(d\)-polytope \(K\) set \(F_K(t)=\sum_{k=0}^{d}f_k(K)t^k\), where the whole polytope contributes the coefficient at \(t^d\); the empty face is excluded. Let
\[
D_{a,b}(t)=F_{\mathcal C(P_{a,b})}(t)-F_{\mathcal O(P_{a,b})}(t),\quad
G_m(t)=1-(1+t)^{m+1}+t(2+t)^m.
\]
Then \(D_{a,b}(t)=G_a(t)G_b(t)\). For \(N=a+b\ge4\), every transfer of one element from the larger outside layer to the smaller layer, when their sizes differ by at least two, **strictly increases each coefficient \([t^k]D_{a,b}(t)\) for every \(2\le k\le N\)**. Coefficients in degrees \(0,1,N+1\) remain zero. Thus, among fixed-size members of this family, the balanced split uniquely maximizes **all** intermediate-dimensional chain-minus-order face gaps simultaneously, up to exchanging the two layers. The extreme split \((1,N-1)\) and its reversal jointly minimize the gaps, all equal to zero.

For \(2\le a\le b-2\) the improvement admits the stronger exact identity
\[
D_{a+1,b-1}(t)-D_{a,b}(t)
=t^2(1+t)^2s_{(b-3,a-1)}(1,1+t,2+t),
\]
where \(s_{(u,v)}\) is the ordinary Schur polynomial of the two-row partition \((u,v)\). The boundary transfer \(a=1\) increases the gap from zero to a polynomial strictly positive in precisely the same degrees. The two endpoint coefficients are
\[
[t^2]D_{a,b}=(2^a-a-1)(2^b-b-1),\qquad
[t^N]D_{a,b}=(a-1)(b-1).
\]

## Assumptions and scope
The dimensions and quantifiers are as follows: \(a,b\in\mathbb Z_{\ge1}\), \(d=a+b+1\), and the strict balancing claim has \(a+b=N\ge4\), \(a<b-1\). The results concern the standard Stanley order polytope \(\mathcal O(P)\), with \(0\le x_p\le1\) and \(x_p\le x_r\) for \(p<r\), and chain polytope \(\mathcal C(P)\), with nonnegative coordinates and sum along every chain at most one. The indexing of \(F_K\) counts vertices in degree zero, edges in degree one, and the full polytope in degree \(d\), rather than the shifted face enumerator sometimes used in the literature. Polynomial coefficientwise comparison is always at equal total \(N\); no claim is made for arbitrary posets or for intermediate chain-order polytopes.

## Proof
**1. Exact face enumerators.** Put \(A=(2+t)^a\), \(B=(2+t)^b\), \(U=(1+t)^a\), \(V=(1+t)^b\). The order polytope is the free join of an \(a\)-cube and a \(b\)-cube, corresponding respectively to assigning the middle coordinate one or zero. Every face of a free join is the join of a face of either factor (allowing the empty face), so its nonempty-face enumerator is
\[
F_{\mathcal O}=A+B+tAB.
\]
The chain polytope is a pyramid over the subdirect sum \(B_{a,b}=\operatorname{conv}(([0,1]^a,0)\cup(0,[0,1]^b))\) with common zero vertex, formed in the hyperplane where the middle coordinate vanishes. For each cube, \(U\) (respectively \(V\)) counts its nonempty faces containing zero, while \(A-U\) (respectively \(B-V\)) counts the others. All nonempty faces of the base are counted by: the faces in one cube, with their common zero vertex counted once; joins of nonzero-dimensional zero-containing faces in both cubes; and joins of origin-avoiding faces from both cubes (whose dimension is the sum of their dimensions plus one). Consequently,
\[
F_{B_{a,b}}=A+B-1+(U-1)(V-1)+t(A-U)(B-V).
\]
A pyramid over a base with nonempty-face polynomial \(F\) has nonempty-face polynomial \(1+(1+t)F\). Therefore
\[
F_{\mathcal C}=1+(1+t)F_{B_{a,b}}.
\]
Subtracting the free-join formula and collecting the two factors gives \(D_{a,b}=G_aG_b\) exactly.

**2. A complete homogeneous expansion.** For \(m\ge2\), the generating-function identity
\[
\sum_{m\ge2}G_m(t)z^{m-2}
=\frac{t(1+t)}{(1-z)(1-(1+t)z)(1-(2+t)z)}
\]
follows by summing the three terms in the definition of \(G_m\) as geometric series and combining denominators. Writing \(h_r\) for the complete homogeneous symmetric polynomial of degree \(r\) in three variables, we obtain
\[
G_m(t)=t(1+t)h_{m-2}(1,1+t,2+t)\qquad(m\ge2),
\]
with \(G_1(t)=0\). In particular \(G_m\) has strictly positive coefficients in degrees \(1,\ldots,m\) whenever \(m\ge2\).

**3. Strict balancing by Jacobi–Trudi.** Fix \(2\le a\le b-2\). The difference of the two factorizations is
\[
\begin{aligned}
D_{a+1,b-1}-D_{a,b}
&=t^2(1+t)^2\big(h_{a-1}h_{b-3}-h_{a-2}h_{b-2}\big)(1,1+t,2+t)\\
&=t^2(1+t)^2s_{(b-3,a-1)}(1,1+t,2+t).
\end{aligned}
\]
The second equality is the two-row Jacobi–Trudi determinant. Because \(b\ge a+2\), \((b-3,a-1)\) is a valid partition. Its semistandard-tableau expansion in the positive alphabet \((1,1+t,2+t)\) has nonnegative polynomial coefficients. In particular, filling the entire first row with the second variable and the entire second row with the third variable gives the summand \((1+t)^{b-3}(2+t)^{a-1}\). This summand has **strictly positive coefficients at every degree from zero to \(a+b-4\)**, inclusive. Multiplication by \(t^2(1+t)^2\) proves strict positivity in degrees \(2\) through \(a+b\), and vanishing at the remaining degrees. If \(a=1\), then \(D_{1,b}=0\), while \(D_{2,b-1}=G_2G_{b-1}\) is strictly positive throughout those degrees for \(b\ge3\). Thus every allowable balancing transfer is strict in all intermediate degrees.

**4. Global extremes and sharp endpoints.** A finite succession of balancing transfers reaches \((\lfloor N/2\rfloor,\lceil N/2\rceil)\) from any less balanced split. Every nontrivial step is strict in the same degrees, so the maximizer is unique up to duality. Conversely, the only splits with a singleton outside layer yield zero, while all splits with both layers of size at least two have positive gaps. The endpoint coefficient identities follow by extracting the coefficient of \(t\) and the top coefficient of \(t^m\) in \(G_m\): these are respectively \(2^m-m-1\) and \(m-1\). This completes the proof.

## Verification
Run `python3 verify.py` using the Python standard library. The script checks the exact face-enumerator and factorization identities for 169 layer-size pairs, verifies 68 exact Jacobi–Trudi balancing identities, and separately reconstructs eight full order/chain face vectors from vertex–facet incidences in small dimensions. A successful execution prints `EXACT_OK gap_pairs=169 balancing_steps=68 independent_facets=8`. These finite tests independently corroborate the algebra and the normalizations; they are not used as a proof for unbounded \(a,b\). The generating-function and Schur-tableau arguments above establish the universal statements.

## Relationship to prior work
Freij-Hollanti and Lundström (arXiv:2312.13890, Sections 3–6) develop the subdirect-sum face formulas and establish the componentwise inequality for broad ordinal-sum classes; the factorization here is an explicit cube specialization of their general formulas and is **not claimed as independently novel**. Ahmad, Fourier, and Joswig (arXiv:2309.01626, Sections 3–5) establish monotonicity upon moving rank elements from order to chain coordinates **for the same fixed ranked poset**, not when redistributing the sizes of its two outer levels. Fourier (arXiv:2609.23629, September 20, 2026) proves the weak Hibi–Li face inequality universally, again comparing chain and order polytopes of the same poset. The new claim is the strict coefficientwise comparison **between distinct rank-size vectors at fixed dimension**, with one common simultaneous optimizer and a Schur-positive difference identity. Hibi and Li's X-obstruction characterizes affine equivalence, rather than these quantitative extremizers. A recent facet-gap formula (arXiv:2608.19989) provides another relevant comparator for the endpoint facet coefficient; it does not by its announced scope imply every intermediate-dimensional strict comparison.

## Limitations
The result concerns only complete three-level ranked posets with a singleton middle level. Existing general f-vector/subdirect-sum formulas supply a substantial ingredient, and the strict balancing statement may admit another presentation in uncatalogued enumerative work; full historical priority has not been independently established. The 2026 facet-gap work is relevant for one endpoint coefficient but is not a substitute for the full all-ranks comparison. No theorem about arbitrary posets, intermediate chain-order interpolations, or independent audit is asserted.

## References
- G. Fourier, *The Hibi–Li Face-Number Conjecture*, arXiv:2609.23629 (first public September 20, 2026).
- R. Freij-Hollanti and T. Lundström, *f-vector inequalities for order and chain polytopes*, arXiv:2312.13890, *Mathematica Scandinavica* 130 (2024), 467–486.
- I. Ahmad, G. Fourier and M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, *Discrete Applied Mathematics* 390 (2026), 28–39.
- G. Fourier, *On facet gaps of order and chain polytopes*, arXiv:2608.19989 (2026).
- T. Hibi and N. Li, *Unimodular Equivalence of Order and Chain Polytopes*, arXiv:1208.4029.
- I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, second edition, Chapter I (Jacobi–Trudi and semistandard-tableau expansions).
