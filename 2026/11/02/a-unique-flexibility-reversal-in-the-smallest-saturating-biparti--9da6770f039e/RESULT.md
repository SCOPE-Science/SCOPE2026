# A unique flexibility reversal in the smallest saturating bipartite matching market

## Finding

Consider two allocations of exactly two flexible vertices in a balanced bipartite compatibility market. A possible edge is independently present with probability \(p\) if both endpoints are inflexible, and with probability \(q\) if *either* endpoint is flexible; a pair of flexible endpoints still has probability \(q\), not a larger probability. Let \(M_{\mathrm{one}}\) and \(M_{\mathrm{split}}\) be the maximum-cardinality matchings when both flexible vertices lie on one side and when one lies on each side, respectively. Write \(D_n(p,q)=\mathbb E M_{\mathrm{one}}-\mathbb E M_{\mathrm{split}}\).

On the \(2\times2\) market, for every \(0\le p\le q\le1\),
\[
D_2(p,q)=(q-p)(1-q)(2q^2-q+1)\ge0.
\]
In contrast, on the \(3\times3\) market and for every fixed \(0<p<1\), there is exactly one \(q_*(p)\in(p,1)\) such that
\[
D_3(p,q)>0\quad(p<q<q_*(p)),\qquad
D_3(p,q)<0\quad(q_*(p)<q\le1).
\]
At \(q=p\) the designs coincide. Thus a strict reversal between the designs first becomes possible with three vertices per side. The split design may have strictly *fewer* expected edges and nevertheless yield a strictly *larger* expected maximum matching.

## Assumptions and scope

For \(n\in\{2,3\}\), let the vertex sets be \(L=R=\{0,\ldots,n-1\}\). In the one-sided design take flexible sets \(F_L=\{0,1\}\), \(F_R=\varnothing\); in the split design take \(F_L=F_R=\{0\}\). For each of the \(n^2\) potential edges \((i,j)\), draw an independent Bernoulli random variable with success probability \(q\) when \(i\in F_L\) or \(j\in F_R\), and \(p\) otherwise. The two flexible vertices are deterministically designated. The quantity \(M\) is the cardinality of a maximum bipartite matching in the realized graph. No online arrival process, utility weights, or adaptive choice is assumed.

The central theorem is for \(0<p<1\) and \(p\le q\le1\); endpoint cases follow from explicit formulas. All computations are exact polynomial identities, not sampling estimates.

## Proof

**1. Exact graph-state polynomial.** For a design with specified flexible sets, the expectation is the finite sum
\[
\mathbb E M=\sum_{G\subseteq K_{n,n}}\nu(G)
   p^{a(G)}(1-p)^{b(G)}q^{c(G)}(1-q)^{d(G)},
\]
where \(a,b,c,d\) count present and absent edges of the respective probability classes and \(\nu(G)\) is the maximum matching cardinality. Expanding this identity for all \(2^4=16\) graphs at \(n=2\) gives
\[
D_2(p,q)=(q-p)(1-q)(2q^2-q+1).
\]
The quadratic factor is strictly positive: \(2q^2-q+1=2(q-1/4)^2+7/8\).

Expanding all \(2^9=512\) graphs at \(n=3\) and cancelling yields \(D_3(p,q)=(q-p)P(p,q)\), where
\[
\begin{aligned}
P(p,q)={}&p^3(6q^5-25q^4+34q^3-22q^2+8q-2)\\
&+p^2(-15q^5+55q^4-64q^3+35q^2-12q+3)\\
&+p(9q^5-31q^4+31q^3-12q^2+3q-1)\\
&-3q^5+11q^4-14q^3+8q^2-3q+1.
\end{aligned}
\]
The attached standard-library verifier derives the expectations directly from the 512 graph states, with two distinct exhaustive matching algorithms, and checks these two identities as exact integer-coefficient polynomial equalities.

**2. One strict crossing.** We claim \(\partial P/\partial q<0\) for \(0<p<1\) and \(p\le q\le1\). To prove it with a checkable finite polynomial certificate, put \(L=u+v+w\) and make the substitution \(p=u/L\), \(q=(u+v)/L\), with \(u>0\), \(v,w\ge0\), \(v+w>0\). Form the homogeneous degree-eight polynomial
\[
H(u,v,w)=-L^8 P_q\left(\frac uL,\frac{u+v}L\right).
\]
Its 45 monomial coefficients, in the order \(u^i v^j w^{8-i-j}\) with \(i=8,7,\ldots,0\) and within each row decreasing \(j\), are exactly
\[
\begin{array}{c|l}
i&\text{coefficients}\\ \hline
8&0\\
7&3,3\\
6&22,42,29\\
5&65,169,170,46\\
4&100,320,396,176,15\\
3&85,325,486,314,90,22\\
2&38,178,347,352,214,98,29\\
1&7,47,144,236,214,108,31,5\\
0&0,4,28,68,75,40,14,8,3
\end{array}
\]
All coefficients are nonnegative; 43 are positive and the only two zeros belong to \(u^8\) and \(v^8\). Since \(u>0\) and at least one of \(v,w\) is positive, some positive monomial is nonzero. Therefore \(H>0\), so \(P_q<0\). The exact coefficients are also provided as machine-readable data in `bernstein_certificate.json`; the verifier constructs them independently from \(P\) and checks all 45.

**3. The two boundary signs.** Direct polynomial factorization gives
\[
\begin{aligned}
P(p,p)&=(1-p)^2(3p^2-2p+1)
 [1+2p^2(1-p)(3-p)]>0,\\
P(p,1)&=-p(1-p)^2<0
\end{aligned}
\]
for \(0<p<1\). Continuity and strict decrease give exactly one \(q_*(p)\in(p,1)\), with the asserted signs of \(D_3=(q-p)P\).

**4. Reversal despite fewer edges.** At \(q=1\),
\[
D_3(p,1)=-p(1-p)^3<0.
\]
Equivalently, \(\mathbb EM_{\mathrm{one}}=3-(1-p)^3\) and \(\mathbb EM_{\mathrm{split}}=3-(1-p)^4\). The one-sided design has \(6\) high-probability and \(3\) baseline edges, whereas the split design has \(5\) high-probability and \(4\) baseline edges, giving
\[
\mathbb E|E_{\mathrm{one}}|-\mathbb E|E_{\mathrm{split}}|=q-p>0.
\]
For a concrete rational sign pair at \(p=1/2\), \(D_3(1/2,3/4)=17/512>0\), but \(D_3(1/2,1)=-1/16<0\). The unique crossing is approximately \(q_*(1/2)=0.8911607696\).

## Verification

Place `verify.py` next to `bernstein_certificate.json` and execute `python3 verify.py` using Python's standard library only. The checker enumerates every graph on \(K_{2,2}\) and \(K_{3,3}\), independently computes its maximum matching by subset dynamic programming and by an exhaustive permutation maximum, generates exact integer-coefficient expectation polynomials, verifies both factorizations, constructs the derivative certificate, compares all 45 coefficients, and checks the boundary identities at exact rational test points. The infinite continuum conclusions use the exact polynomial identities, the nonnegative-coefficient certificate, and elementary monotonicity; the rational test points are supplementary checks, not substitutes for those arguments.

## Relationship to prior work

Ameen, Sentenac, and Yu, *Flexibility allocation in random bipartite matching markets: exact matching rates and dominance regimes* (arXiv:2604.02295, publicly posted April 2, 2026), analyze much larger random markets with independently sampled flexible types and additive type-pair edge probabilities, in which the flexible–flexible pair has its own enhanced probability. Freund, Martin, and Zhao, *Two-Sided Flexibility in Platforms* (arXiv:2404.04709, first publicly posted April 2024), compare flexibility placement in a model emphasizing additive probability boosts and large-market behavior. In particular, neither model identifies the fixed-two-vertex, saturating-at-\(q\) exact \(3\times3\) dominance reversal proved here. The known \(2\times2\) intuition favors concentration; the present result identifies its exact first failure under the stated saturating rule. This is a qualified priority comparison, not a claim that exhaustive literature search can prove nonexistence of an earlier equivalent result.

## Limitations

The theorem concerns expected cardinality of *offline maximum matchings* and specifically two fixed flexible vertices in balanced markets of sizes two and three. It does not assert a universal large-market regime, optimal flexibility allocation for all market sizes, online matching performance, or welfare beyond cardinality. The probability semantics are essential: flexible–flexible edges have probability \(q\), *not* a second additive increment. Earlier unindexed work may contain an equivalent finite-market classification. No independent scientific audit has been performed.

## References

1. T. Ameen, F. Sentenac, and S. H. Yu, *Flexibility allocation in random bipartite matching markets: exact matching rates and dominance regimes*, arXiv:2604.02295 (initial public posting April 2, 2026). https://arxiv.org/abs/2604.02295
2. D. Freund, S. Martin, and J. K. Zhao, *Two-Sided Flexibility in Platforms*, arXiv:2404.04709 (initial public posting April 2024). https://arxiv.org/abs/2404.04709
