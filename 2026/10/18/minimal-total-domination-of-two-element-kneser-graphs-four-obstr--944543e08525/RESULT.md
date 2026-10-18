# Minimal total domination of two-element Kneser graphs: four obstructions and two sharp coefficient transitions

## Finding

Let \(K(n,2)\) be the Kneser graph whose vertices are the two-element subsets of \([n]\), adjacent exactly when disjoint, and let \(n\ge4\). A *total dominating set* (TDS) is a vertex subset with a selected neighbor for **every** graph vertex, including those selected. A *minimal* TDS is inclusion-minimal, not merely smallest. Write
\[
P_n(z)=\sum_{S\text{ inclusion-minimal TDS of }K(n,2)}z^{|S|}.
\]
Then
\[
\boxed{P_n(z)=15\binom n6z^3+10\binom n5z^4+12\binom n5z^5+\binom n4z^6,}
\]
where \(\binom nr=0\) for \(r>n\). In particular, all inclusion-minimal TDS correspond, through the natural edge interpretation, to exactly four edge-containing graph types on \([n]\), with any remaining vertices isolated:
\[
3K_2,\qquad K_3\sqcup K_2,\qquad C_5,\qquad K_4.
\]
The upper total domination number (largest size of an inclusion-minimal TDS) is \(6\) for all \(n\ge4\). The possible inclusion-minimal cardinalities are \(\{6\}\) for \(n=4\), \(\{4,5,6\}\) for \(n=5\), and \(\{3,4,5,6\}\) for \(n\ge6\).

The full (zero-padded) coefficient sequence of \(P_n\) is **log-concave exactly for** \(4\le n\le8\), and **unimodal exactly for** \(4\le n\le9\). Thus log-concavity first fails at \(n=9\), and unimodality first fails at \(n=10\); both fail at every larger order.

## Assumptions and scope

All graphs are finite, simple, and undirected. The symbol \(F\) denotes the spanning graph on \([n]\) whose edges are the chosen vertices \(S\subseteq V(K(n,2))\); unchosen base vertices remain isolated in \(F\). Let \(\tau(F)\) be the minimum number of base vertices meeting every edge of \(F\), with \(\tau(\varnothing)=0\). An edge-critical graph with cover number \(3\) has \(\tau(F)=3\) but \(\tau(F-e)\le2\) for every \(e\in E(F)\). The notation \(K_2\), \(K_3\), \(K_4\), and \(C_5\) refers to the usual connected graphs, and \(\sqcup\) denotes disjoint union. The word *minimal* refers to set inclusion. No assertion is made about Kneser graphs \(K(n,r)\) for \(r>2\).

A finite nonnegative sequence \((a_0,\dots,a_d)\) is log-concave if \(a_j^2\ge a_{j-1}a_{j+1}\) for every interior index; it is unimodal if it increases weakly to an index and decreases weakly thereafter. Leading zeros are included in the declared coefficient sequence; they do not alter these conclusions.

## Proof

**1. Reduction to critical vertex covers.** Every vertex of \(K(n,2)\) is a pair \(Q\subseteq[n]\). It has a neighbor in the chosen set \(S=E(F)\) exactly when some edge of \(F\) is disjoint from \(Q\). Therefore \(S\) is total dominating if and only if no pair \(Q\) covers every edge of \(F\). Every vertex cover of size \(0\) or \(1\) extends to a pair because \(n\ge4\), hence this is equivalent to \(\tau(F)\ge3\). Furthermore, deleting one selected vertex of \(K(n,2)\) deletes one edge of \(F\). As total domination is monotone under adding selected vertices, inclusion-minimality is equivalent to \(\tau(F)\ge3\) and \(\tau(F-e)\le2\) for **every** edge \(e\) of \(F\). Adding an endpoint of \(e\) to a cover of \(F-e\) gives \(\tau(F)\le3\), so such \(F\) has \(\tau(F)=3\).

**2. The cover-number-two critical lemma.** Suppose \(J\) has \(\tau(J)=2\) and \(\tau(J-e)\le1\) for every edge. If \(J\) has two disjoint edges, those edges alone already require two cover vertices; any third edge would make one of the two deletions leave these two edges unchanged, contrary to criticality. Thus \(J\) is \(2K_2\), apart from isolated vertices. If \(J\) has no two disjoint edges, its edges pairwise intersect. A simple graph with pairwise intersecting edges is a star or a triangle. As \(\tau(J)=2\), it must be a triangle. Conversely, \(2K_2\) and \(K_3\) are edge-critical with cover number two.

**3. High degree forces a four-clique.** Let \(F\) be edge-critical with \(\tau(F)=3\) and take a vertex \(v\) of degree at least three. Choose an edge \(e\) not incident to \(v\): such an edge exists, for otherwise \(\tau(F)=1\). Any cover of \(F-e\) of size at most two must contain \(v\), since its three incident edges survive and cannot be covered by only two other vertices. Consequently \(\tau(F-v-e)\le1\). Moreover \(\tau(F-v)=2\): the inequality \(\tau(F-v)\ge2\) follows from \(\tau(F)=3\), and adding an endpoint of \(e\) to a cover of \(F-v-e\) yields a two-cover of \(F-v\). The same reasoning holds for every edge \(e\) of \(F-v\), so \(F-v\) satisfies the cover-number-two critical lemma.

If \(F-v=2K_2\), each two-cover of \(F-v\) contains exactly one endpoint of each of its two edges. For every incident edge \(vx\), a two-cover of \(F-vx\) **cannot** use \(v\), because \(F-v\) needs two vertices. It must therefore cover \(F-v\) and also contain every vertex of \(N_F(v)\setminus\{x\}\). When \(\deg_F(v)\ge3\), such covers cannot exist for every choice of \(x\): an external neighbor cannot belong to a minimum cover of \(2K_2\), and any three endpoints of the two matching edges include both endpoints of one edge, leaving the other uncovered after the appropriate choice of \(x\). Hence this case is impossible.

If \(F-v=K_3\), its two-covers are exactly the two-element subsets of the triangle. The same incident-edge argument forces all neighbors of \(v\) into this triangle. As \(\deg_F(v)\ge3\), the neighbor set is the full triangle, and \(F=K_4\) apart from isolates. Direct deletion shows \(K_4\) is edge-critical with cover number three.

**4. Maximum degree at most two.** Here every nontrivial component is a path or cycle. Edge-criticality of the disjoint union forces every nontrivial component to be edge-critical for its own vertex-cover number. Among paths, the only edge-critical one is \(K_2\): in any path of at least three edges, deleting the second edge leaves the minimum cover number unchanged (this follows immediately by the alternating-vertex cover formula \(\tau(P_s)=\lfloor s/2\rfloor\)); a three-vertex path already has an end-edge deletion preserving its cover number. An even cycle is not critical, because deleting any edge yields a path with the same cover number. Every odd cycle is critical, because \(\tau(C_{2q+1})=q+1\), whereas \(\tau(P_{2q+1})=q\). Therefore the component types are isolated edges and odd cycles. Their cover-number contributions are \(1\) for an isolated edge and \(q+1\) for \(C_{2q+1}\). Requiring total cover number three leaves precisely \(3K_2\), \(C_3\sqcup K_2\), and \(C_5\), including possible isolated vertices. The four displayed families are distinct, and direct inspection establishes edge-criticality for each.

**5. Enumeration and cardinality spectrum.** Choose the base support of each type and count labeled realizations on that support. A matching of size three on six fixed vertices has \(6!/(2^3 3!)=15\) realizations; the triangle-plus-edge has \(\binom53=10\); a five-cycle has \(5!/10=12\); a four-clique has one. They have respectively three, four, five, and six edges, producing the stated polynomial. The cardinality spectrum and upper total domination number follow by positivity of these coefficients.

**6. Exact coefficient transitions.** For \(n\ge5\), denote the coefficients of \(z^j\) by \(a_j\) for \(3\le j\le6\). The only potentially failing log-concavity inequality is at \(j=4\), because
\[
a_4^2-a_3a_5=10\binom n5^{\!2}(25-3n),
\]
while
\[
a_5^2-a_4a_6=\binom n5\left(144\binom n5-10\binom n4\right)>0
\]
for every \(n\ge5\); all other inequalities have a zero neighboring coefficient. Thus log-concavity holds through order eight and fails from order nine. Moreover
\[
\frac{a_3}{a_4}=\frac{n-5}{4},\qquad \frac{a_5}{a_4}=\frac65,
\]
and \(a_6<a_5\) for every \(n\ge5\). If \(n\le9\), the positive coefficients are weakly increasing through \(a_5\) and then decrease; if \(n\ge10\), \(a_3>a_4<a_5\), precluding unimodality. For \(n=4\), \(P_4(z)=z^6\), which has both properties. This proves both sharp thresholds.

## Verification

The accompanying standard-library script `verify_minimal_total_kneser.py` constructs every neighborhood of \(K(n,2)\) directly and tests all nonempty selected-vertex subsets for total domination and inclusion-minimality. Exhaustive orders \(n=4,5,6,7\) inspect exactly \(2{,}131{,}004\) nonempty subsets and agree coefficient by coefficient with the theorem. Its separate coefficient tester checks both transition predicates on every order \(4\le n\le80\). Run `python verify_minimal_total_kneser.py` to regenerate `verification_output.txt` without dependencies. These finite checks are not used as a proof of the infinite-family assertions.

## Relationship to prior work

Ivančo and Zelinka (1993), *Domination in Kneser graphs*, already determine the minimum total-domination numbers and examples for \(K(n,2)\). Brešar, Cornet, Dravec, and Henning (arXiv:2312.15464, first posted 24 December 2023) obtain general Kneser \(k\)-tuple-total domination results, including the fact that all minimum total dominating sets of \(K(n,2)\) are pairwise-disjoint edge triples when \(n\ge6\). Neither minimum cardinality nor that minimum-set characterization is asserted to be new here.

Subramanian and Selvakumar (2025) introduce minimal-total-domination polynomials for graph substitution constructions, but their general formulas do not give this explicit Kneser-family critical-cover classification or the two sharp coefficient thresholds. Bahadır, Ekim, and Gözüpek (2021) study well-totally-dominated graphs in general, whereas Beaton and Brown (2020 preprint) treat unimodality of the **ordinary** domination polynomial; that polynomial counts all dominating sets rather than inclusion-minimal total dominating sets. The present structural classification supplies a complete minimal-set enumerator, not solely an extremal parameter.

## Limitations

The result applies only to \(K(n,2)\) with \(n\ge4\), to open-neighborhood total domination, and to inclusion-minimal selected sets. It does not classify all total dominating sets or general higher-rank Kneser graphs. The classification of critical vertex-cover configurations may be available in independent extremal-graph terminology, and equivalent polynomial formulas may occur in unindexed sources; no exhaustive priority or independent peer assessment is claimed. The computer checks extend only to the stated finite orders.

## References

1. J. Ivančo and B. Zelinka, *Domination in Kneser graphs*, Mathematica Bohemica **118** (1993), 147–152. DOI: 10.21136/MB.1993.126050. Full text: https://dml.cz/bitstream/handle/10338.dmlcz/126050/MathBohem_118-1993-2_3.pdf.
2. B. Brešar, M. G. Cornet, T. Dravec, and M. A. Henning, *k-Domination invariants on Kneser graphs*, arXiv:2312.15464 (first version 24 December 2023), https://arxiv.org/abs/2312.15464.
3. M. G. Cornet and P. Torres, *k-tuple domination on Kneser graphs*, arXiv:2308.15603 (first version 29 August 2023), https://arxiv.org/abs/2308.15603.
4. M. Subramanian and A. Selvakumar, *Total domination and minimal total domination polynomial of H-join graphs*, Filomat **39** (2025), 267–277. DOI: 10.2298/FIL2501267S.
5. S. Bahadır, T. Ekim, and D. Gözüpek, *Well-totally-dominated graphs*, Ars Mathematica Contemporanea **20** (2021), 209–222. Preprint: arXiv:2010.02341.
6. I. Beaton and J. I. Brown, *On the Unimodality of Domination Polynomials*, arXiv:2012.11813 (2020), https://arxiv.org/abs/2012.11813.
