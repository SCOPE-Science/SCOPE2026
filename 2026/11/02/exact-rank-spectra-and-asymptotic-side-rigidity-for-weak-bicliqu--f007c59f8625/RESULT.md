# Exact rank spectra and asymptotic side rigidity for weak biclique retractions

## Finding

Let \(K_{a,b}\) be the labeled simple complete bipartite graph with nonempty sides \(X,Y\) of cardinalities \(a,b\geq1\). A **weak endomorphism** is a total vertex map sending every edge either to an edge or to a single vertex. Let \(e_{a,b}(k)\) count its idempotent weak endomorphisms of image size \(k\). Put \(\rho_{a,b}(i,j)\), for \(1\leq i\leq a\) and \(1\leq j\leq b\), equal to
\[
\rho_{a,b}(i,j)=
\begin{cases}
2^{a+b-2},&i=j=1,\\
(i+1)^{a-i},&i\geq2,\ j=1,\\
(j+1)^{b-j},&i=1,\ j\geq2,\\
i^{a-i}j^{b-j},&i,j\geq2.
\end{cases}
\]
Then the **complete idempotent rank polynomial** is
\[
\boxed{\ \sum_{k\geq1}e_{a,b}(k)z^k
=(a+b)z+\sum_{i=1}^a\sum_{j=1}^b
\binom ai\binom bj\rho_{a,b}(i,j)z^{i+j}.\ }
\]
There are no other ranks. In particular, this formula includes both side-preserving and side-crossing idempotents and permits all side sizes, including stars.

For balanced bicliques, let \(I_m=\sum_{i=1}^m\binom mi i^{m-i}\), the number of idempotent transformations of an \(m\)-element set, and let \(\Delta_m\) be the number of idempotent weak endomorphisms of \(K_{m,m}\) that do **not** preserve the two sides individually. The exact excess is
\[
\boxed{\ \Delta_m=2m+m^2(2^{2m-2}-1)
+2m\sum_{i=2}^m\binom mi\bigl((i+1)^{m-i}-i^{m-i}\bigr).\ }
\]
For a uniformly sampled idempotent weak endomorphism of \(K_{m,m}\), as \(m\to\infty\),
\[
\boxed{\ \log\Pr(\text{at least one vertex crosses sides})
=-m\log m+m\log\log m+O(m).\ }
\]
Thus side crossing is superexponentially rare among idempotent weak endomorphisms of balanced dense bicliques, although it occurs in every nonempty biclique.

## Assumptions and scope

Vertices are labeled; maps are total; the graph has no loops. Composition and idempotence are in the full transformation monoid. A side-preserving map means \(f(X)\subseteq X\) and \(f(Y)\subseteq Y\), not merely preservation of the unordered bipartition. All rank formulas hold for every positive integer \(a,b\). The probability statement concerns \(a=b=m\) with \(m\to\infty\), not arbitrary unbalanced growth.

## Proof

**Fixed images.** If \(f^2=f\), its image \(S\) is precisely its set of fixed vertices. Set \(i=|S\cap X|\) and \(j=|S\cap Y|\). Each edge joins \(X\) to \(Y\); its two images are permitted exactly when equal or on opposite sides. If \(i=0\) or \(j=0\), every image lies in one independent side. Since every cross-edge must then have equal images and \(K_{a,b}\) is connected, \(f\) is constant. These give exactly \(a+b\) idempotents of rank one.

Suppose \(i,j\geq1\) and fix the actual labeled image subsets \(S_X,S_Y\). When \(i,j\geq2\), each \(x\in X\) is adjacent to at least two distinct fixed points of \(S_Y\), so \(f(x)\) cannot be in \(Y\): a single image there would have to equal both fixed points. Consequently \(f(X)\subseteq S_X\), and symmetrically \(f(Y)\subseteq S_Y\). The \(a-i\) and \(b-j\) nonfixed vertices have \(i\) and \(j\) choices, independently. There are \(i^{a-i}j^{b-j}\) maps for this image.

When \(i\geq2,j=1\), every vertex of \(Y\) must map to its unique fixed point \(y_0\): its image must be compatible with each of the at least two fixed points in \(S_X\). Each nonfixed \(x\in X\) may independently map to any vertex of \(S_X\cup\{y_0\}\); all cross-edge images are then equal or adjacent. The count is \((i+1)^{a-i}\). The case \(i=1,j\geq2\) is symmetric. When \(i=j=1\), all vertices may independently map to either of the two adjacent fixed points, for \(2^{a+b-2}\) choices. Multiplying these four counts by the choices \(\binom ai\binom bj\) for fixed image sets and adding the constants proves the polynomial without overcounting.

**Exact side-crossing excess.** Every side-preserving idempotent is a pair of arbitrary idempotent transformations on \(X\) and \(Y\). Therefore precisely \(I_a I_b\) such maps exist. In the balanced case, subtracting the side-preserving contribution \(I_m^2\) from the polynomial at \(z=1\) gives exactly the displayed expression for \(\Delta_m\). The three contributions respectively count constant maps, additional maps with exactly one fixed point per side, and additional maps with at least two fixed points on one side and one on the other.

**Asymptotic scale.** For real \(t\in[1,N]\), the maximum of \((N-t)\log t\) occurs at the unique positive solution of \(t(1+\log t)=N\) (apart from harmless small boundary cases). Comparing the monotone left-hand side at \(N/(2\log N)\) and \(2N/\log N\) proves that this maximizing \(t\) is \(\Theta(N/\log N)\). Hence, as \(N\to\infty\),
\[
\max_{1\leq t\leq N}(N-t)\log t
=N\log N-N\log\log N+O(N).
\]
Since \(\binom mi\leq2^m\), this maximization bounds \(I_m\) from above. Choosing \(i=\lfloor m/\log m\rfloor\) and retaining one summand bounds it from below. Thus
\[
\log I_m=m\log m-m\log\log m+O(m).
\]
Write \(S_m=\sum_{i=2}^m\binom mi((i+1)^{m-i}-i^{m-i})\). Bounding above by \(\sum_{i=2}^m\binom mi(i+1)^{m-i}\) and applying the same maximization with \(N=m+1\) gives \(\log S_m\leq m\log m-m\log\log m+O(m)\). For the reverse bound, choose \(i=\lfloor m/\log m\rfloor\geq2\), use \((i+1)^h-i^h\geq h i^{h-1}\) with \(h=m-i\), and retain this positive summand. This gives the matching lower estimate
\[
\log S_m=m\log m-m\log\log m+O(m).
\]
In the exact formula for \(\Delta_m\), the \(m^2 2^{2m-2}\) term has logarithm \(O(m)\), so \(\log\Delta_m=m\log m-m\log\log m+O(m)\). In particular \(\Delta_m=o(I_m^2)\), and
\[
\log\frac{\Delta_m}{I_m^2+\Delta_m}
=\log\Delta_m-2\log I_m+o(1)
=-m\log m+m\log\log m+O(m),
\]
as required.

## Verification

The self-contained script `verify.py` directly enumerates all \((a+b)^{a+b}\) total maps for nine pairs of side sizes, independently checks the edge condition and idempotence, and compares the full rank distribution with the closed formula. The tested pairs are \((1,1),(1,2),(1,3),(1,5),(2,2),(2,3),(2,4),(3,3),(3,4)\). The last two complete distributions are
\[
(e_{3,3}(1),\ldots,e_{3,3}(6))=(6,144,54,42,12,1),
\]
\[
(e_{3,4}(1),\ldots,e_{3,4}(7))=(7,384,198,196,99,18,1).
\]
The output `VERIFY_OK` requires every configuration to match exactly. Exhaustive finite testing corroborates, but does not replace, the unrestricted proof or its asymptotic argument.

## Relationship to prior work

The 2024 work of Dimitrova, Fernandes and Koppitz on partial endomorphisms of star graphs establishes the definition and normal forms for weak maps on the star subfamily; its Proposition 1.1 and Corollary 1.2 concern descriptions and total cardinalities, not the rank polynomial or balanced biclique asymptotic here. The 2023 paper by Dimitrova, Fernandes, Koppitz and Quinteiro studies cycles and their weak endomorphism monoids, so its graph family differs. Li (2013) studies retractions and endotype for strict graph endomorphisms of bipartite graphs; allowing contraction of edges changes the permissible idempotents and introduces the extra terms in our formula. The 2018 Knauer–Pipattanajinda paper counts weak endomorphisms of paths, not rank-refined idempotents of complete bipartite graphs. These comparisons do not establish exhaustive publication priority; an equivalent formula under reflexive graph homomorphisms remains a residual risk.

## Limitations

The claim is restricted to complete bipartite graphs and total weak endomorphisms. It does not classify all weak endomorphisms, their generators, Green relations, or complete multipartite graphs with more than two parts. The asymptotic has an \(O(m)\) remainder in the logarithm and no multiplicative constant. Literature-priority verification is not an independent bibliographic certification.

## References

1. I. Dimitrova, V. H. Fernandes, J. Koppitz, *On partial endomorphisms of a star graph*, arXiv:2401.11741 (first posted 2024-01-22), https://arxiv.org/abs/2401.11741.
2. I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149 (2023-10-06), https://arxiv.org/abs/2310.04149.
3. W. Li, *On endotype of bipartite graphs*, Ars Combinatoria 108 (2013), pp. 415–424, https://combinatorialpress.com/article/ars/Volume%20108/volume-108-paper-38.pdf.
4. U. Knauer and N. Pipattanajinda, *A formula for the number of weak endomorphisms on paths*, Algebra and Discrete Mathematics 26 (2018), pp. 270–279, https://admjournal.luguniv.edu.ua/index.php/adm/article/view/349.
