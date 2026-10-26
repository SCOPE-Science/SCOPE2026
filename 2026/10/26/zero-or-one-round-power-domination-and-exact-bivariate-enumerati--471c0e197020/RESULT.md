# Zero-or-one-round power domination and exact bivariate enumeration in multipartite line graphs

## Finding

For every integer \(r\ge 3\) and every positive integer vector \(\mathbf n=(n_1,\ldots,n_r)\) having at least one entry greater than one, let \(G=K_{n_1,\ldots,n_r}\). A nonempty edge set \(S\subseteq E(G)\), regarded as a vertex set of the line graph \(L(G)\), is power dominating **if and only if** the vertices not incident with any edge of \(S\) induce either an edgeless graph or a star \(K_{1,t}\) for some \(t\ge1\). If the induced graph is edgeless, observation is complete at the domination step; if it is a star, exactly one parallel forcing round suffices; in all other cases no forcing move is possible after the domination step.

Here is an explicit polynomial giving the number of these sets of **every cardinality**, for all multipartite part sizes. Define
\[
E(\mathbf s)=\sum_{1\le i<j\le r}s_i s_j,
\qquad
C_{\mathbf t}(z)=
\sum_{\mathbf 0\le\mathbf s\le\mathbf t}
(-1)^{\sum_i(t_i-s_i)}
\left(\prod_i\binom{t_i}{s_i}\right)
(1+z)^{E(\mathbf s)}-
\mathbf1_{\{\sum_i t_i=0\}}.
\]
Let \(\mathcal A_{\mathbf n}\) consist of the integer vectors \(\mathbf u=(u_1,\ldots,u_r)\) with \(0\le u_i\le n_i\) such that either at most one coordinate is positive, or exactly two coordinates are positive and their minimum is one. Then the complete power-domination polynomial satisfies
\[
\boxed{\mathcal P(L(G);z)=
\sum_{\mathbf u\in\mathcal A_{\mathbf n}}
\left(\prod_{i=1}^{r}\binom{n_i}{u_i}\right)
C_{\mathbf n-\mathbf u}(z).}
\]
The polynomial \(C_{\mathbf t}\) counts **nonempty** edge subsets of \(K_{t_1,\ldots,t_r}\) incident to every vertex of that smaller graph. In the expression above, the terms with \(\mathbf u\) supported on at most one part enumerate the sets requiring zero forcing rounds; the remaining terms enumerate those requiring exactly one forcing round. Thus it also gives the joint cardinality and propagation-round distribution.

The finer bivariate enumerator \(\mathcal P(L(G);z,w)\) marks the number of forcing rounds by \(w\): the expression above splits canonically as \(\mathcal P_0(z)+w\mathcal P_1(z)\), with \(\mathcal P_0\) summing over uncovered supports of size at most one and \(\mathcal P_1\) summing over the remaining admissible uncovered supports. This is a full classification of cardinality *and* propagation behavior throughout multipartite graphs having at least three parts, including mixed part sizes where the residual three-part obstruction is distinct from the bipartite case.

## Assumptions and scope

All graphs are finite, undirected and simple. Every \(n_i\) is positive, \(r\ge3\), and at least one \(n_i\ge2\), and \(S\) is a nonempty subset of \(E(G)\). A line-graph vertex corresponds to an edge of \(G\), and two line-graph vertices are adjacent precisely when the corresponding edges share an endpoint. Power domination starts by observing \(N[S]\), then repeatedly permits any observed vertex having exactly one unobserved neighbor to observe that neighbor. A **parallel forcing round** applies all currently legal forces. The power-domination polynomial is the sum of \(z^{|S|}\) over all successful nonempty initial sets. The coordinatewise inequality \(\mathbf0\le\mathbf s\le\mathbf t\) has its usual meaning; the binomial coefficients and indicators have their standard integer meanings. \(E(\mathbf s)=0\) for support in at most one part. We do not identify power domination with ordinary domination.

## Proof

**Step 1 (exact unobserved graph).** Let \(T\) be the set of endpoints of the edges in \(S\) and put \(U=V(G)\setminus T\). An edge of \(G\) is adjacent in \(L(G)\) to an edge in \(S\), or belongs to \(S\), exactly when it has an endpoint in \(T\). Therefore the initially unobserved line-graph vertices are *exactly* the edges of the induced graph \(H=G[U]\). No other vertices are unobserved.

**Step 2 (no hidden chain reactions).** For an initially observed edge \(xy\) of \(G\), if both endpoints lie in \(T\), it has no neighbor representing an edge of \(H\). If exactly one endpoint \(y\) lies in \(U\), its number of neighbors representing edges of \(H\) is exactly \(\deg_H(y)\). The case where both endpoints lie in \(U\) is an unobserved edge and cannot perform a force. Consequently an initial force is possible precisely when \(H\) has a degree-one vertex \(y\) adjacent in \(G\) to some \(x\in T\). A nonempty \(S\) has endpoints in at least two distinct parts of \(G\), so for every \(y\in U\) there exists such an \(x\in T\) outside \(y\)'s part. In particular, each degree-one vertex of \(H\) can be used to force its unique incident edge.

**Step 3 (complete multipartite classification).** Write \(u_i=|U\cap V_i|\). If zero or one of the \(u_i\) are positive, then \(H\) has no edges; the domination step already observes everything. If exactly two are positive and the smaller equals one, then \(H\) is a star. For each leaf of this star, Step 2 supplies an observed boundary edge with exactly one unobserved neighbor. All the star edges are therefore observed simultaneously in one forcing round. In every other case, either two positive counts are both at least two or at least three counts are positive. Each nonisolated vertex of \(H\) then has degree at least two. Step 2 shows that not a single force is initially legal; no sequence of forces can begin. This proves the iff criterion and the propagation dichotomy.

**Step 4 (cardinality enumerator).** Fix an admissible uncovered vector \(\mathbf u\). The actual uncovered vertices can be chosen in exactly \(\prod_i\binom{n_i}{u_i}\) ways. On the remaining \(\mathbf t=\mathbf n-\mathbf u\) vertices, the selected edges \(S\) must have every vertex incident to some selected edge, since \(U\) was defined as *all* vertices without selected incidences. By inclusion-exclusion over vertices of degree zero in \(S\), the required generating polynomial is exactly \(\sum_{0\le\mathbf s\le\mathbf t}(-1)^{\sum_i(t_i-s_i)}\prod_i\binom{t_i}{s_i}(1+z)^{E(\mathbf s)}\). When \(\mathbf t=\mathbf0\), this expression counts one empty edge set, which is prohibited; subtracting the indicated unit yields \(C_{\mathbf t}\). For any nonempty \(\mathbf t\), empty edge sets cancel automatically, including when an edge cover is impossible. Distinct selected edge sets have unique uncovered vertex vectors, so summing these disjoint cases proves the displayed polynomial. Restricting the sum to the two kinds of admissible \(\mathbf u\) separately proves the propagation-time refinement.

## Verification

Run `python verify.py` with Python 3 and no third-party dependencies. Its graph-theoretic simulator enumerates 203,826 starting edge subsets (including the 57 empty subsets, correctly rejected) in 57 positive multipartite part-size tuples totaling at most six vertices; all agree with the residual-star test. Independent inclusion-exclusion coefficient calculations agree with exhaustive counts for eight multipartite instances. The verifier also cross-checks the all-singleton boundary family \(J(n,2)\), but those previously studied cases are not part of the new originality claim. As a numerical example,
\[
\mathcal P(K_3\square K_3;z)=36z^2+84z^3+126z^4+126z^5+84z^6+36z^7+9z^8+z^9.
\]
These computations test the hypotheses and implementation; the infinite statements follow from Steps 1–4, not the finite tests.

## Relationship to prior work

Brimkov, Patel, Suriyanarayana and Teich (2018) introduced and analyzed the power-domination polynomial, including structural properties, relations to zero forcing and formulas for other graph families. Their general framework is foundational, but the new mixed multipartite-line-graph criterion and its bivariate all-cardinality, propagation-round formula are not among their stated results. Soh and Koh (2014) established the **scalar** power domination number of products of complete graphs, and their 2016 article discusses such products; the scalar rook-graph consequence here is therefore *not* asserted as new. Shahbaznejad, Kazemi and Pelayo (2021), Section 6, study **middle** graphs (with vertices representing both original vertices and edges), which are not the line graphs considered here. Mertens (2024) computed the **ordinary domination polynomial** for rook graphs; his generating function counts one-step dominating sets, a proper subset of the power-dominating sets here. That work uses the same edge-cover representation for rook graphs, but not the star-residual forcing extension. Existing exact descriptions of power domination for rectangular rook graphs and triangular graphs already cover the two-part and all-singleton specializations; these are not asserted as original here. The genuinely additional claim addresses at least three parts with a non-singleton part, especially the residual three-part obstruction and the exact combined cardinality/forcing-round distribution.

## Limitations

Novelty is assessed against the inspected accessible literature and searched records; it does not imply an exhaustive search of unpublished or unindexed sources. A 2011 thesis on generalizations of line graphs and power domination by Seema Varghese was located, but its full contents could not be inspected; potential priority overlap remains. This result is about ordinary one-neighbor power forcing, not generalized \(k\)-forcing, sensor-failure reliability, ordinary domination or zero forcing alone. The formulas count labeled vertices and named multipartite parts, not isomorphism classes. Previously established rectangular rook and triangular-graph special cases are outside the claimed new scope. No computational experiment is offered as a substitute for the all-parameter proof. Independent human verification has not been carried out.

## References

1. B. Brimkov, R. Patel, V. Suriyanarayana and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1 (first posted 28 May 2018), https://arxiv.org/html/1805.10984v1 .
2. K. W. Soh and K. M. Koh, *A note on power domination problem in diameter two graphs*, AKCE International Journal of Graphs and Combinatorics **11** (2014), 41–53, https://doi.org/10.1080/09728600.2014.12088762 .
3. K. M. Koh and K. W. Soh, *Power domination of the cartesian product of graphs*, AKCE International Journal of Graphs and Combinatorics **13** (2016), 22–30, https://doi.org/10.1016/j.akcej.2016.02.004 .
4. A. Shahbaznejad, A. P. Kazemi and I. Pelayo, *Some Families of Graphs with Small Power Domination Number*, arXiv:2106.13496v1 (2021), https://arxiv.org/html/2106.13496v1 .
5. S. Mertens, *Domination Polynomial of the Rook Graph*, Journal of Integer Sequences **27** (2024), Article 24.3.7, https://cs.uwaterloo.ca/journals/JIS/VOL27/Mertens/mertens6.pdf .
6. S. Varghese, *Studies on some generalizations of line graph and the power domination problem in graphs*, doctoral thesis, Cochin University of Science and Technology (2011), cited in Shahbaznejad–Kazemi–Pelayo (2021); full text not inspected.
