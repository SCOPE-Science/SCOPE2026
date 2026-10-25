# Exact maximal-packing enumerator of all one-leaf coronas

## Finding
Let \(H\) be any finite simple graph on \(n\ge 1\) vertices, including graphs with disconnected components or isolated vertices. Form \(C(H)\) by adding a private leaf \(v'\) adjacent to every core vertex \(v\in V(H)\). A *packing* is a set of vertices with pairwise disjoint closed neighborhoods, equivalently with pairwise graph distance at least three; *maximal* means inclusion-maximal, not necessarily largest.

For each packing \(S\) of \(H\), define
\[
 P_S=S\cup\{v':v\in V(H)\setminus N_H[S]\}.
\]
**Theorem.** The map \(S\mapsto P_S\) is a bijection from **all** packings of \(H\), including the empty packing, to **all maximal** packings of \(C(H)\). In particular, if the exponent records cardinality, the complete maximal-packing enumerator is
\[
 \boxed{\mathcal M_{C(H)}(z)=\sum_{S\subseteq V(H)\,\mathrm{packing}}z^{\,n-\sum_{v\in S}\deg_H(v)}.}
\]
The identities obtained from this bijection are
\[
 \boxed{\rho(C(H))=n,\qquad
 \rho_L(C(H))=n-\max_{S\,\mathrm{packing\ of}\ H}\sum_{v\in S}\deg_H(v),\qquad
 [z^n]\mathcal M_{C(H)}(z)=2^{i(H)},}
\]
where \(i(H)\) denotes the number of isolated vertices of \(H\), \(\rho\) the largest packing size, and \(\rho_L\) the smallest size of a maximal packing.

For every \(d\)-regular \(H\), with \(d\ge1\), the set of attainable maximal-packing cardinalities is **exactly**
\[
 \boxed{\{n-dk:0\le k\le\rho(H)\},}
\]
and the coefficient of \(z^{n-dk}\) is precisely the number of size-\(k\) packings of \(H\). Thus the possible cardinalities can have arbitrarily large gaps even for connected graphs: for \(m\ge2\),
\[
 \boxed{\mathcal M_{C(K_m)}(z)=z^m+mz.}
\]
A concrete infinite family with more than two allowed sizes is the sunlet graph \(C(C_n)\), for which \(n\ge3\) and
\[
 \boxed{\mathcal M_{C(C_n)}(z)=z^n+
 \sum_{k=1}^{\lfloor n/3\rfloor}
 \frac{n}{n-2k}\binom{n-2k}{k}\,z^{n-2k}.}
\]

## Assumptions and scope
All graphs are finite, simple, and undirected; graph distance between different connected components is treated as infinite. Distinct private leaves are distinct labelled vertices, and every subset is counted exactly once, with no quotient by automorphisms. Every packable support \(S\) includes the empty set in the sum. The graph \(H\) may have no edges; then \(\mathcal M_{C(H)}(z)=2^nz^n\). Regular-graph consequences assume positive degree. The cycle formula assumes \(n\ge3\), while the complete-graph formula assumes \(m\ge2\).

## Proof
**1. Every maximal packing determines its core.** For any two distinct core vertices \(u,v\), distance in \(C(H)\) agrees with distance in \(H\); for \(u\ne v\), a path from core vertex \(u\) to leaf \(v'\) has distance \(\operatorname{dist}_H(u,v)+1\), and two distinct leaves have distance \(\operatorname{dist}_H(u,v)+2\). These formulas remain valid with infinite distance for different components. Every packing \(P\) of \(C(H)\) therefore has a core subset \(S=P\cap V(H)\) which is a packing in \(H\), and its selected leaves must have labels \(v\notin N_H[S]\). If such a leaf \(v'\) is missing, it can be added to \(P\): it is far enough from every selected core vertex and every other distinct leaf. Thus maximality forces \(P=P_S\).

**2. Every core packing gives a maximal packing.** Given any packing \(S\) in \(H\), the sets of chosen core vertices and leaves in \(P_S\) are mutually distance at least three, so \(P_S\) is a packing. Each missing leaf \(v'\) has \(v\in N_H[S]\), hence is within distance at most two of a selected core vertex. Each missing core vertex \(v\) is either in \(N_H[S]\), and hence within distance at most one of \(S\), or lies outside \(N_H[S]\), in which case its own leaf \(v'\) is selected. No further vertex can be added; \(P_S\) is maximal. Its core subset is exactly \(S\), establishing the bijection.

**3. Cardinalities and the enumerator.** Because distinct vertices of a packing \(S\) have distance at least three, their closed core neighborhoods are disjoint. Consequently,
\[
 |N_H[S]|=\sum_{v\in S}(1+\deg_H(v))
 =|S|+\sum_{v\in S}\deg_H(v).
\]
Counting the core vertices and the forced leaves of \(P_S\) gives
\[
 |P_S|=|S|+n-|N_H[S]|=n-\sum_{v\in S}\deg_H(v).
\]
Summing over the bijection proves the polynomial identity. Any packing in the corona uses at most one of the adjacent vertices \(v,v'\) for each of the \(n\) pairs, so has size at most \(n\). All leaves form a packing of size \(n\), giving \(\rho(C(H))=n\). Maximizing the degree sum yields the lower packing identity. An exponent \(n\) requires every selected core vertex to have degree zero; the \(i(H)\) isolated core vertices may be independently included or excluded, giving exactly \(2^{i(H)}\) maximum packings.

**4. Regular bases and spectral gaps.** If \(H\) is \(d\)-regular, every size-\(k\) core packing has degree sum \(dk\). A largest packing contains a subpacking of every smaller nonnegative size, so all integers \(0\le k\le\rho(H)\) occur and there are no other exponents. In \(K_m\), the only core packings are the empty set and its \(m\) singletons, so the polynomial reduces to \(z^m+mz\). For arbitrarily large \(m\), none of the cardinalities \(2,\ldots,m-1\) occurs despite the corona being connected.

**5. Cycle bases.** A \(k\)-element packing in \(C_n\) consists of \(k\) cyclically chosen vertices with at least two unused vertices between successive chosen vertices, so \(3k\le n\). For \(k\ge1\), choose a distinguished selected vertex in \(n\) ways, then write the numbers of extra unselected vertices in the \(k\) cyclic gaps as a weak composition of \(n-3k\). There are \(\binom{n-2k-1}{k-1}\) such compositions. Every packing was counted exactly \(k\) times through its distinguished vertex. The number of these packings is therefore
\[
 \frac nk\binom{n-2k-1}{k-1}
 =\frac{n}{n-2k}\binom{n-2k}{k}.
\]
For \(k=0\) there is one empty packing. Since every vertex of \(C_n\) has degree two, substituting the count into the general polynomial gives the sunlet formula.

## Verification
A separate straightforward graph-enumeration program (`verify.py`) enumerates all subsets of each corona, tests the pairwise distance condition, and tests inclusion-maximality by attempting every missing vertex. It compares the resulting **sets**, not only the coefficients, with those generated from core packings. The program checks all labelled graphs with at most five vertices and 150 additional seeded six- and seven-vertex graphs: 1,249 base graphs and 10,647 maximal corona packings in total. It also checks the two-term polynomial of the complete-graph coronas for six orders. Running `python verify.py` produces `VERIFY_OK` and the full count log in `verify_output.txt`. These finite checks are cross-checks; the proof above covers all finite orders.

## Relationship to prior work
Boyer, Goddard, and Henning (2026) introduced the corona construction in their study of packing and isolation, observed that all private leaves form a packing isolating set, and investigated lower packings and well-packed trees. That work motivates the present all-maximal question, but its inspected results do not provide a bijection or a full size enumerator for arbitrary leaf coronas. Mojdeh, Peterin, Samadi, and Yero (2020) determine **maximum** packing cardinalities for general rooted products; they do not classify all inclusion-maximal packings. Cabrera Martínez, Puertas, and Rodríguez-Velázquez (2021) study the \(2\)-packing differential via the objective \(\sum_{v\in S}(\deg(v)-1)\), distinct from the degree-weight objective and all-set counting identity here. The precise distinction between closed-neighborhood packing and **open** packing is essential. An exhaustive priority or equivalence classification of all terminology in the literature has not been established.

## Limitations
The result counts inclusion-maximal **closed-neighborhood** packings, not maximal open packings or all nonmaximal packings. The exact general polynomial is an explicit sum over core packings and can be computationally hard to evaluate; a polynomial-time algorithm for arbitrary base graphs is not asserted. The proof neither establishes a new upper bound for domination numbers nor solves a general packing optimization problem. The bibliographic searches did not exhaust all unindexed results or possible reformulations via independent sets in graph squares. No independent mathematical audit is claimed.

## References
1. Geoffrey Boyer, Wayne Goddard, Michael A. Henning, *On the Relationships between Domination, Isolation, and Packing*, arXiv:2606.18172v1, first publicly submitted 2026-06-16, https://arxiv.org/html/2606.18172v1 .
2. Doost Ali Mojdeh, Iztok Peterin, Babak Samadi, Ismael G. Yero, *(Open) packing number of some graph products*, arXiv:1901.06813v3, 2020, https://arxiv.org/html/1901.06813v3 .
3. A. Cabrera Martínez, M. L. Puertas, J. A. Rodríguez-Velázquez, *On the 2-Packing Differential of a Graph*, Results in Mathematics 76 (2021), article 157, https://doi.org/10.1007/s00025-021-01473-8 .
4. A. P. Burger, M. A. Henning, J. H. van Vuuren, *On the ratios between packing and domination parameters of a graph*, Discrete Mathematics 309 (2009), 2473–2478, https://doi.org/10.1016/j.disc.2008.05.030 .
