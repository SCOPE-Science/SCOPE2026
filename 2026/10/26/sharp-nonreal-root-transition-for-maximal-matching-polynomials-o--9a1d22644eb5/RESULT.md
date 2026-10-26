# Sharp nonreal-root transition for maximal-matching polynomials of triangular coronas

## Finding

For every integer \(r\ge1\), let \(T_r\) be the tree obtained by subdividing each of the \(r\) edges of the star \(K_{1,r}\) exactly once. Its vertices are a center \(c\), branch vertices \(a_1,\ldots,a_r\), and tips \(b_1,\ldots,b_r\), with edges \(ca_i\) and \(a_ib_i\). Let \(H_r=T_r\circ K_2\) be the *triangle corona*: at each vertex \(v\) of \(T_r\), attach two private vertices \(v'\) and \(v''\), together with the three edges \(vv'\), \(vv''\), and \(v'v''\). These are simple, connected block graphs (triangular cacti).

A matching is a collection of pairwise vertex-disjoint edges. It is *maximal* when no further edge can be added. Define the maximal-matching polynomial
\[
\mathfrak m_{H}(z)=\sum_{M\text{ maximal matching of }H}z^{|M|}.
\]

**Theorem.** For every \(r\ge1\),
\[
\boxed{\mathfrak m_{H_r}(z)=z^{2r+1}\left[2(z+8)^r+(z+6)^r+3rz(z+8)^{r-1}\right].}
\]
The bracketed polynomial has exactly **one** real root if \(r\) is odd, and exactly **two** real roots if \(r\) is even. Every nonzero root is simple, and every real nonzero root is negative. Hence the polynomial has nonreal zeros for every \(r\ge3\). More precisely, the number of nonreal roots counted with multiplicity is \(r-1\) for odd \(r\), and \(r-2\) for even \(r\).

This failure begins at the smallest possible base order *within the class of triangle coronas*: for every simple base graph \(G\) on at most six vertices, \(\mathfrak m_{G\circ K_2}(z)\) is real-rooted, whereas \(T_3\) has seven vertices and
\[
\mathfrak m_{T_3\circ K_2}(z)=z^7(1240+1068z+210z^2+12z^3).
\]
The discriminant of the cubic factor is \(-13{,}023{,}936\). The assertion for base order at most six is a finite, exhaustive computation, with the exact verifier included; it is not inferred from sampling.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled when enumerated computationally. The corona operation joins each base vertex to both vertices of a fresh \(K_2\), creating a triangle; it is **not** the attachment of two pendant leaves and not the ordinary one-leaf corona. The variable \(z\) counts matching edges. Distinguish inclusion-*maximal* matchings from maximum-cardinality matchings. The theorem is exact over the integers for every \(r\ge1\). The six-vertex sharpness statement ranges over every labeled simple graph (including disconnected ones) with at most six vertices.

## Proof

**Local-state lemma.** Let \(G\) be any simple graph with \(n\) vertices, and let \(\mathsf{Match}(G)\) denote its matchings, including the empty matching. For \(M\in\mathsf{Match}(G)\), put \(R=V(G)\setminus V(M)\). Then
\[
\mathfrak m_{G\circ K_2}(z)
=z^n\sum_{M\in\mathsf{Match}(G)}z^{|M|}
\sum_{\substack{U\subseteq R\\ U\text{ independent in }G}}2^{|R|-|U|}.
\tag{1}
\]

To prove (1), restrict a maximal matching of the corona to the original base edges; these form a matching \(M\) of \(G\). At a base vertex covered by \(M\), the two private vertices have to be matched to one another, or the private edge could be added. At a base vertex not covered by \(M\), at least one of the three edges of its private triangle must be selected, or its two private vertices would both be unmatched. Exactly one triangle edge can be selected. There are two *spoke* choices that match the base vertex, or one *private-edge* choice that leaves it unmatched. The set \(U\) of base vertices in the private-edge state must be independent: otherwise their common base edge could be added. Conversely, every choice satisfying this condition is maximal, since no triangle edge or base edge has both endpoints unmatched. Every such matching contains \(n+|M|\) edges: \(n\) edges inside the attached triangles and \(|M|\) base edges. There are \(2^{|R|-|U|}\) choices of spokes. This proves (1) bijectively, including empty and disconnected base graphs.

**The subdivided star.** The center \(c\) has three mutually exclusive possibilities.

If \(c\) is matched to a private vertex, there are two choices. On each arm, selecting the base edge \(a_ib_i\) contributes one extra edge, hence a factor \(z\); otherwise the two base vertices choose spoke/private states but cannot both be private, contributing \(4+2+2=8\). The corresponding factor is \(2(8+z)^r\).

If \(c\) is left unmatched (its private edge is selected), no \(a_i\) may be left unmatched. On each arm, choosing \(a_ib_i\) contributes \(z\), while omitting it forces \(a_i\) to choose one of two spokes, with three choices at \(b_i\), contributing \(6\). The factor is \((6+z)^r\).

Finally, \(c\) may be matched along a base edge to one of the \(r\) branch vertices \(a_i\). That edge contributes \(z\); its remaining tip \(b_i\) has three private-triangle choices; every other arm contributes \(8+z\). The factor is \(3rz(8+z)^{r-1}\). Factoring out the mandatory \(2r+1\) triangle edges proves the displayed polynomial.

**Exact root count.** Write the bracketed factor as \(P_r(z)\), and for \(z\ne-8\) put
\[
w=\frac{z+6}{z+8}.
\]
Then \(z/(z+8)=4w-3\), whence
\[
\frac{P_r(z)}{(z+8)^r}=w^r+12rw+(2-9r)=:Q_r(w).
\tag{2}
\]
The point \(z=-8\) is never a root of \(P_r\), and \(Q_r(1)=3r+3>0\). Therefore the fractional linear substitution gives a bijection of the roots of \(P_r\) and \(Q_r\), preserving reality and multiplicity.

For odd \(r\), \(Q_r'(w)=r(w^{r-1}+12)>0\) for every real \(w\). As \(Q_r\) has odd degree, it has exactly one real root. For even \(r\), \(Q_r'\) has exactly one real zero, a strict minimum, and \(Q_r(0)=2-9r<0\), while \(Q_r(w)\to+\infty\) at both ends of the real line. Hence there are exactly two real roots. For \(r>1\), a common zero of \(Q_r\) and \(Q_r'\) would have to satisfy both \(w^{r-1}=-12\) and \(w=(9r-2)/(12(r-1))>0\), impossible. The case \(r=1\) is linear. Thus all nonzero roots are simple. As \(P_r\) has strictly positive coefficients, it has no nonnegative real roots.

**Sharpness through base order six.** For a base graph on six named vertices, its edge set is encoded uniquely by fifteen bits, so the \(2^{15}=32768\) integers in the verifier cover every labeled graph, without graph-isomorphism assumptions. Equation (1) is evaluated with exact integer arithmetic by recursively enumerating base matchings and counting permissible spoke/private states. The resulting normalized polynomial has degree at most three. Every one of the 32768 cases has nonnegative quadratic or cubic discriminant, so all its roots are real; lower-degree cases are immediate. An isolated base vertex contributes precisely three choices to the normalized polynomial, multiplying it by \(3\). Adding isolated vertices therefore reduces every base graph of order at most five to one of order six without altering nonzero roots. A separate algorithm enumerates actual maximal matchings in complete corona graphs and agrees with (1) for all 64 labeled four-vertex bases and for the seven-vertex witness. This supplies an exhaustive finite certificate for the cutoff. The infinite family and exact root counts were proved analytically above.

## Verification

Run the included standalone standard-library program using `python3 verify.py`. It checks all \(32768\) six-vertex labeled graphs with exact discriminants; the matching-degree distribution is \((1,191,7753,24823)\) for degrees \(0,1,2,3\), with \(160\) zero discriminants. It separately enumerates maximal matchings directly in the full attached graph for representative cases, including \(H_3\), and cross-checks every four-vertex base graph directly. It also checks the closed form against the core-state calculation for \(1\le r\le8\) and evaluates the cubic discriminant exactly. The final output is `VERIFY_OK`. The code's finite sweep proves only the stated six-vertex cutoff, not the unbounded theorem; the latter follows from (2).

## Relationship to prior work

Došlić and Zubac (2015; published online 30 November 2015) introduce the maximal-matching polynomial, prove general spectrum properties, and in their §7.2 treat total maximal-matching counts for the path corona \(P_n\circ K_2\). Their Proposition 7.3 supplies a recurrence with initial counts \(3,9,28\). Formula (1) reproduces these numbers for paths of zero, one, and two edges. Their inspected paper does not give the subdivided-star corona polynomial or the corresponding exact root count and seven-vertex threshold.

Tavakoli (first published 28 September 2022) proves bounds for the saturation number of arbitrary coronas and the exact scalar value when the attached graph is randomly matchable. In particular, it implies that \(s(G\circ K_2)=|V(G)|\); that scalar result is not new here. It neither enumerates maximal matchings by size for the present family nor determines their zeros. The 2021 study by Klavžar, Tavakoli, and Abrishami concerns *global forcing sets* distinguishing maximal matchings, a different invariant; only its abstract was available for comparison.

The novelty assessed here is the explicit subdivided-star all-size polynomial, the transformation (2) giving a complete nonreal-root count in an infinite family of connected block graphs, and the exact finite threshold over arbitrary base graphs of smaller order. This is not a claim that maximal-matching polynomials in general have real roots, nor a claim about their log-concavity.

## Limitations

The base-order cutoff depends on a fully specified finite enumeration of \(32768\) graphs; it is reproducible but not a symbolic classification of the six-vertex isomorphism types. The exact root-count assertion for the infinite family does not depend on computation. Targeted literature and mathematical-record searches did not identify an equivalent statement, but absence from those sources does not prove universal priority. The full 2021 global-forcing paper was not inspected, and other unindexed or differently formulated treatments could overlap. The ordinary matching generating polynomial and the *maximal*-matching polynomial are different objects: a real-rootedness result for the former is not automatically transferable to the latter.

## References

1. T. Došlić and I. Zubac, “Counting maximal matchings in linear polymers,” *Ars Mathematica Contemporanea* **11** (2016), 255–276; first published online 30 November 2015. DOI: 10.26493/1855-3974.851.167. Primary full text inspected (particularly §§2 and 7.2).
2. M. Tavakoli, “On a Conjecture about the Saturation Number of Corona Product of Graphs,” *Journal of Mathematics* (2022), Article 3375246, first published 28 September 2022. DOI: 10.1155/2022/3375246. Primary full text inspected (Theorems 1 and 2).
3. S. Klavžar, M. Tavakoli, and G. Abrishami, “Global forcing number for maximal matchings in corona products,” arXiv:2107.13786 (first posted 29 July 2021). Abstract compared; full text not inspected.
