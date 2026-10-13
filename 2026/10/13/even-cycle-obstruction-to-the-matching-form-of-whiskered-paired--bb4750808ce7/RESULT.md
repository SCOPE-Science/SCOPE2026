# Even-cycle obstruction to the matching form of whiskered paired domination

## Finding
For a finite simple graph \(G\) of order \(n\ge1\), form its fully whiskered graph \(W(G)=G\circ K_1\), with a distinct pendant vertex \(v'\) adjacent only to each \(v\in V(G)\). Define
\[
P_{W(G)}(z)=\sum_{S\text{ paired-dominating in }W(G)}z^{|S|},\qquad
M_G(z)=\sum_{j=0}^{\lfloor n/2\rfloor}m_j(G)z^{n-2j},
\]
where \(m_j(G)\) is the number of matchings with exactly \(j\) edges. Coefficients of the two polynomials are compared in the same power of \(z\).

**Theorem.** For every such \(G\),
\[
P_{W(G)}(z)=z^n\sum_{U\subseteq V(G)}
\mathbf{1}\{G[U]\text{ has a perfect matching}\}\,z^{n-|U|}
\preceq z^n M_G(z).
\]
Equality holds **if and only if** \(G\) has no even cycle (not necessarily induced). Thus an even cycle is exactly the obstruction to identifying paired-dominating sets of \(W(G)\) with matchings of \(G\) by the set of covered vertices.

In particular, for every forest \(F\) on \(n\ge1\) vertices, with adjacency matrix \(A(F)\),
\[
\boxed{P_{W(F)}(z)=z^n\det(zI_n-iA(F)).}
\]
All zeros of \(P_{W(F)}\) lie on the imaginary axis, and its coefficient data determine the adjacency spectrum of \(F\), including multiplicities. Writing \(\nu(F)\) for the matching number, the minimum paired-dominating cardinality is \(2n-2\nu(F)\), and exactly \(m_{\nu(F)}(F)\) sets attain it. The scalar minimum also holds for general \(G\) and was already known; the claimed finding is the all-cardinality equality criterion and its spectral forest specialization.

## Assumptions and scope
Graphs are finite, simple, undirected, and may be disconnected or contain isolated vertices. The corona here always means **one pendant vertex for each original vertex**. A set \(S\) dominates when every vertex belongs to \(S\) or has a neighbor in \(S\). It is paired-dominating when \(W(G)[S]\) contains a perfect matching (not necessarily an induced matching). The empty induced graph is taken to admit its unique empty perfect matching; this convention accounts for choosing every pendant vertex in addition to every original vertex. All polynomial coefficients are integer counts; \(i^2=-1\). The matching number \(\nu(G)\) is the largest number of disjoint edges in \(G\).

## Proof
Let \(C=V(G)\) denote the original, or core, vertices and let \(C'=\{v':v\in C\}\) be the private leaves. Every paired-dominating set \(S\) contains every core vertex: otherwise some core vertex \(v\notin S\) forces its leaf \(v'\in S\) merely to dominate that leaf, but \(v'\) then has degree zero in the induced graph \(W(G)[S]\), precluding a perfect matching. Conversely any set containing all of \(C\) dominates \(W(G)\).

Consequently write \(S=C\cup L'\) with \(L\subseteq C\) and \(L'=\{v':v\in L\}\). Each chosen leaf \(v'\) must be matched to \(v\), leaving precisely the core vertices \(U=C\setminus L\). Therefore \(W(G)[S]\) has a perfect matching **if and only if** \(G[U]\) has one. Since \(|S|=n+|L|=2n-|U|\), summing once for every feasible \(U\) gives the first displayed polynomial.

Let \(p_G(U)\) be the number of perfect matchings of \(G[U]\), with \(p_G(\varnothing)=1\). Each matching of \(G\) covers a unique vertex set \(U\), so
\[
z^nM_G(z)=z^n\sum_{U\subseteq C}p_G(U)z^{n-|U|}.
\]
For every \(U\), \(p_G(U)\ge \mathbf{1}\{p_G(U)>0\}\); this proves coefficientwise domination. Equality of the polynomials holds precisely when \(p_G(U)\le1\) for every \(U\), because all coefficient differences are nonnegative. If two distinct perfect matchings exist on some \(G[U]\), their symmetric difference contains an even cycle (alternating between the two matchings). Conversely any even cycle in \(G\), on vertex set \(U\), supplies two distinct alternating perfect matchings of \(G[U]\). This proves the exact characterization, including non-induced even cycles.

When \(F\) is a forest, expand \(\det(zI_n-iA(F))\) by permutations. A nonzero term cannot involve a permutation cycle of length at least three, since such a cycle would require a cycle in \(F\). Hence every surviving permutation comprises fixed points and disjoint transpositions along edges of \(F\), i.e. a matching. A transposition contributes sign \(-1\), while the product of its two off-diagonal entries is \((-i)^2=-1\); their product is \(+1\). A matching of size \(j\) therefore contributes \(z^{n-2j}\), proving \(\det(zI_n-iA(F))=M_F(z)\). Multiplying by \(z^n\) gives the spectral identity.

Because \(A(F)\) is real symmetric, its eigenvalues \(\lambda_1,\ldots,\lambda_n\) are real, and the determinant above equals \(\prod_j(z-i\lambda_j)\). Thus the roots of the paired-domination polynomial are \(0\) (at least \(n\) times) and the imaginary numbers \(i\lambda_j\), and division by the explicitly known power \(z^n\) recovers the characteristic polynomial under the substitution \(z\mapsto iz\). For forests the matching/set bijection makes the smallest exponent \(2n-2\nu(F)\), with coefficient \(m_{\nu(F)}(F)\). This closes every asserted implication.

As a sharp obstruction example, for the four-cycle \(C_4\) the enumerator is \(P_{W(C_4)}(z)=z^8+4z^6+z^4\), whereas \(z^4 M_{C_4}(z)=z^8+4z^6+2z^4\): the two alternating perfect matchings share the same full core support, so that paired-dominating set is counted only once.

## Verification
The standalone standard-library program `verify.py` directly enumerates every vertex subset of every fully whiskered simple graph of core order \(1\le n\le5\) and checks the domination and perfect-matching conditions independently from the coefficient formula. It also scans four specified graphs of orders six and seven, tests even-cycle detection against multiplicity of induced perfect matchings, and compares polynomial coefficients. On the packaged code the observed output is:

`VERIFY_OK graphs=1103 subset_checks=1106468 even_cycle_graphs=486 strict_differences=486 max_order=7`

These are finite consistency checks; the theorem for arbitrary order follows from the combinatorial proof above. Replay using `python3 verify.py` (Python standard library only). The finite check counts graph instances, including the four separately selected graphs; it does not purport to exhaust graphs of order six or seven.

## Relationship to prior work
Paired domination was introduced by Haynes and Slater (1998). The earliest *day-verified* public reference retained here is Xu's 13 May 2013 survey, Section 8.2. Dettlaff–Raczek–Yero (2016), Lemma 3.2, already gives the minimum paired-domination cardinality for corona-type graphs in terms of a maximum matching. That established scalar result is explicitly not claimed as new. The 2016 introduction to paired-domination polynomials gives their definition and reports special-family examples; its accessible abstract does not settle this proposed identity, and its full text could not be evaluated from the accessible link. Li–Shi–Trinks (2014/2015) study matching-polynomial reconstruction, including pendant-edge aspects, but the theorem here compares a *paired-domination set-counting* polynomial with the matching polynomial through the full support map. In particular the exact even-cycle obstruction and the forest adjacency-spectrum identity go beyond the scalar corona result.

## Limitations
The result concerns only a single private leaf per original vertex; no statement is made for coronas with larger attached graphs or for induced-paired domination. For graphs containing even cycles, the paired-domination polynomial is generally **not** the matching polynomial: a nonzero coefficientwise gap remains, and no root-location theorem is claimed in that case. The first verified public-source day denotes the exact-day 2013 survey inspected, not an asserted 2013 invention of paired domination (which dates to 1998). A potentially relevant 2016 paired-polynomial conference paper was available only at abstract level; uninspected sections may pose residual coverage risk. No independent audit or external certification is asserted.

## References
1. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI and exact public day not established in this package.
2. J.-M. Xu, “On Bondage Numbers of Graphs: A Survey with Some Comments,” *International Journal of Combinatorics* (2013), Article 595210; first published 2013-05-13. https://doi.org/10.1155/2013/595210 (especially Section 8.2).
3. M. Dettlaff, J. Raczek, I. G. Yero, “Edge subdivision and edge multisubdivision versus domination in generalized corona graphs,” *Opuscula Mathematica* 36(5) (2016), 575–588; Lemma 3.2 and its proof. https://journals.bg.agh.edu.pl/OPUSCULA/2016.36.5/OpMath.2016.36.5.575.pdf
4. Puttaswamy, A. Alwardi and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” ICMAGT 2016 conference (September 26–27, 2016). Accessible abstract: https://www.researchgate.net/publication/325108045_Introduction_to_Paired_Domination_Polynomial_of_a_Graph
5. X. Li, Y. Shi, M. Trinks, “Polynomial reconstruction of the matching polynomial,” *Electronic Journal of Graph Theory and Applications* 3(1) (2015), arXiv:1404.3469 (posted 2014-04-14). https://arxiv.org/abs/1404.3469
