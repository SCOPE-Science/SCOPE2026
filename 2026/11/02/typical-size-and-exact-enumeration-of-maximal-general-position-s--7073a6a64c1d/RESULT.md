# Typical size and exact enumeration of maximal general-position sets in triangular graphs

## Finding
Let \(T_n=L(K_n)\), \(n\ge4\). Write \(M_n(z)\) for the polynomial whose coefficient of \(z^j\) counts inclusion-maximal general-position sets of size \(j\) in \(T_n\). Then
\[
M_n(z)=n![x^n]\left(\exp B(x,z)+x\exp(x^3z^3/6)\right),
\qquad
B(x,z)=\frac{x^2z}{2}+\frac{x^3z^3}{6}+\sum_{s\ge4}\frac{x^s z^{s-1}}{(s-1)!}.
\]
If \(S_n\) is chosen uniformly from the inclusion-maximal general-position sets of \(T_n\), then
\[
\frac{(n-|S_n|)\log n}{n}\longrightarrow 1\qquad\text{in probability as }n\to\infty.
\]
The exact enumerator and this limiting typical-size law form one joint claim; the pre-existing classification of maximal configurations into stars and triangles is credited below.

## Assumptions and scope
A vertex of \(T_n\) corresponds to a two-element subset of \([n]\). Distinct vertices are adjacent exactly when the corresponding pairs intersect. A general-position set has no three distinct selected vertices occurring on one shortest path; inclusion-maximal refers to adding a vertex without preserving this property, not maximum cardinality. The graph \(T_n\) has diameter two for \(n\ge4\). All enumerated sets are labeled by the original \([n]\). The limiting probability statement fixes no degree, and is over uniform choices among all inclusion-maximal configurations for each \(n\).

## Proof
**The combinatorial decomposition.** In a graph of diameter two, a vertex subset is in general position if and only if its induced components are cliques. For the line graph of a complete graph, the corresponding chosen edges decompose into vertex-disjoint stars and triangles: any clique of at least three edges is either a star or a triangle; a clique of two edges is a two-edge star. A two-edge star is not inclusion-maximal, since its missing third triangle edge can be added. Hence each star component has either one edge or at least three edges. If there is any star component, every ground vertex is covered: a new edge incident with an uncovered vertex and the center of a star preserves the component-clique property. If all components are triangles, at most one ground vertex may be uncovered: an edge between two uncovered vertices could otherwise be added. Conversely these covered block decompositions, and all-triangle decompositions with one isolated ground vertex, are inclusion-maximal; any new edge either joins two existing components, or creates an induced three-vertex path inside a star or triangle component. This decomposition is the structural consequence of the published line-graph classification, not a new assertion about possible shapes.

A labeled block of size two contributes one edge, a block of size three contributes a triangle of three edges, and each block of size \(s\ge4\) contributes one of \(s\) possible stars of size \(s-1\) edges. Therefore the exponential formula for labeled set partitions gives the term \(\exp B(x,z)\). The exceptional all-triangle partitions with exactly one uncovered ground vertex contribute \(x\exp(x^3z^3/6)\). This proves the exact polynomial.

**Saddle-point probability model.** Put \(b(x)=B(x,1)=xe^x-x-x^2/2-x^3/3\). Let \(r=r_n\) be the unique positive solution to \(r b'(r)=n\), where \(b'(r)=(r+1)e^r-1-r-r^2\). Since \(r b'(r)\sim r^2e^r\), we have \(r/\log n\to1\). Let \(Z_s\), for \(s\ge2\), be independent Poisson variables of respective means \(\lambda_2=r^2/2\), \(\lambda_3=r^3/6\), and \(\lambda_s=r^s/(s-1)!\) for \(s\ge4\). Define \(N=\sum_{s\ge2}sZ_s\) and \(J=Z_2+\sum_{s\ge4}Z_s\). By coefficient extraction of the exponential generating function, conditioning on \(N=n\) produces the uniform random fully-covered configuration; precisely, \(J\) then equals the size deficit \(n-|S|\), because each star loses one edge relative to its ground-vertex count, whereas a triangle loses none.

The means satisfy \(\mathbb E N=n\), \(\mathbb E J=b(r)-r^3/6\sim r e^r\sim n/r\), and \(\operatorname{Var}(J)\le b(r)=O(n/r)\). We next justify the local probability estimate
\[
\Pr(N=n)\sim\big(2\pi n r\big)^{-1/2}.
\]
Indeed \(V=\operatorname{Var}N=r b'(r)+r^2b''(r)\sim nr\). Fourier inversion gives \(\Pr(N=n)=(2\pi)^{-1}\int_{-\pi}^{\pi}\exp(b(re^{it})-b(r)-int)\,dt\). On \(|t|\le\delta/r\), for a fixed sufficiently small \(\delta>0\), the independent Poisson summands with sizes \(s\in[r/2,2r]\) contribute \(\sum_s\lambda_s(1-\cos st)\ge c Vt^2\): those sizes account for asymptotically all of \(V\) by Poisson concentration. On \(\delta/r\le|t|\le\pi\), the identity \(b(re^{it})=re^{it}\exp(re^{it})+O(r^3)\) uniformly gives
\[
b(r)-\Re b(re^{it})\ge re^r\big(1-e^{-r(1-\cos t)}\big)-O(r^3)\ge c' n/r^2.
\]
Both tail contributions are negligible relative to \(V^{-1/2}\). On the central range \(t=u/\sqrt V\) with bounded \(u\), the expansion of the exponent has quadratic term \(-u^2/2\) and third-order remainder bounded by \(O(nr^2 |u|^3/V^{3/2})=o(1)\). Dominated convergence and extension of the central integration range prove the stated local estimate, without assuming aperiodicity: the available block sizes two and three already give lattice span one.

Chebyshev's inequality and this local estimate imply, for each fixed \(\varepsilon>0\),
\[
\Pr\left(\left.\left|J-\mathbb EJ\right|>\varepsilon n/r\ \right|N=n\right)
\le\frac{O(r/n)}{\Pr(N=n)}=O\left(r^{3/2}/\sqrt n\right)=o(1).
\]
Thus the deficit is \((1+o_{\Pr}(1))n/r\) in the covered class.

**Negligibility of the exceptional class.** For \(n=3k+1\), its number is exactly \(n!/(6^k k!)\); otherwise it is zero. The logarithm of this number is at most \((2/3)n\log n+O(n)\). The number \(A_n\) of fully-covered configurations satisfies
\[
A_n=n!\,e^{b(r)}r^{-n}\Pr(N=n),\qquad
\log A_n=n\log n-n\log\log n-O(n),
\]
by the local estimate and Stirling's formula. Hence the exceptional class has vanishing probability under uniform sampling. Combining this with \(r\sim\log n\) establishes the asserted limit.

## Verification
Run `python verify.py` with Python 3. The script independently constructs the original line graph, computes exact shortest-path distances by breadth-first search, exhaustively checks general position and inclusion-maximality for all \(2^{\binom n2}\) vertex subsets at \(n=4,5,6\), and compares size counts against an independent labeled-block recursion. It reports 33,856 tested subsets and matching polynomials, including \(M_4(z)=3z^2+8z^3\), \(M_5(z)=15z^4\), and \(M_6(z)=15z^3+60z^4+6z^5+10z^6\). For \(n=7,8,9,10,11\), it prints further exact recurrence coefficients. These finite checks are diagnostics and do not substitute for the infinite proof.

## Relationship to prior work
Ghorbani et al., arXiv:1903.04286 (2019), determined the maximum general-position cardinality for \(L(K_n)\). Di Stefano et al., arXiv:2306.09965 (2023), proved its minimum inclusion-maximal cardinality and explicitly identified the star/triangle decomposition, which is used here as a premise and checked again. The paper *General position polynomials*, arXiv:2401.05696 (2024), counts **all** general-position sets in various graphs, including the complementary Kneser graph, rather than enumerating inclusion-maximal sets in \(L(K_n)\). The 2022 paper arXiv:2209.12631 concerns the distinct mobile general-position invariant. The contribution here is the explicit maximal-set enumerator and, centrally, the sharp typical deficit scaling. No uniqueness-of-discovery assertion is made.

## Limitations
The limit is first-order in probability, not a central limit theorem, large deviation estimate, or coefficientwise asymptotic. The structural classification underlying the enumeration is previously known. The literature search cannot exclude an unindexed prior equivalent enumerator or asymptotic. Self-contained proof and finite verification have not received independent validation.

## References
1. M. Ghorbani et al., *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286 (initial submission 2019-03-11), https://arxiv.org/abs/1903.04286.
2. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, I. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965 (initial submission 2023-06-16), https://arxiv.org/abs/2306.09965.
3. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General position polynomials*, arXiv:2401.05696 (initial submission 2024-01-11), https://arxiv.org/abs/2401.05696.
4. A. Krishnakumar et al., *Traversing a graph in general position*, arXiv:2209.12631 (2022), https://arxiv.org/abs/2209.12631.
