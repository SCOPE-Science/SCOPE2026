# Secure-total-domination polynomials and minimal-set gaps of clique bouquets

## Finding

Let \(t\ge 2\), let \(r_1,\ldots,r_t\) be integers at least \(2\), and let
\[
B(r_1,\ldots,r_t)=K_1\vee\bigl(K_{r_1}\sqcup\cdots\sqcup K_{r_t}\bigr).
\]
The vertex \(c\) in the first \(K_1\) is the common center; its neighbors decompose into pairwise anticomplete cliques \(C_i\) of cardinality \(r_i\). A set \(S\) is *secure total dominating* if every vertex has a selected open neighbor and, for every \(v\notin S\), some adjacent \(u\in S\) can be replaced by \(v\) while leaving a total dominating set.

**Complete characterization.** A subset \(S\subseteq V(B)\) is secure total dominating if and only if exactly one of these conditions holds:

1. \(c\in S\) and \(|S\cap C_i|\ge1\) for every \(i\);
2. \(c\notin S\) and \(|S\cap C_i|\ge2\) for every \(i\).

Let \(F_B(z)=\sum_{S\text{ secure total dominating}}z^{|S|}\). Its exact polynomial is
\[
\boxed{F_B(z)=z\prod_{i=1}^{t}\bigl((1+z)^{r_i}-1\bigr)
+\prod_{i=1}^{t}\bigl((1+z)^{r_i}-1-r_i z\bigr).}
\]

Moreover, an inclusion-minimal secure total dominating set is exactly either the center together with one vertex from each clique, or a center-free set containing exactly two vertices from each clique. Consequently its complete cardinality polynomial is
\[
\boxed{M_B(z)=\left(\prod_{i=1}^{t}r_i\right)z^{t+1}
+\left(\prod_{i=1}^{t}\binom{r_i}{2}\right)z^{2t}.}
\]
Thus \(\gamma_{st}(B)=t+1\), the largest size of an inclusion-minimal secure total dominating set is \(2t\), and the inclusion-minimal cardinality spectrum is precisely \(\{t+1,2t\}\). When \(t\ge3\), there are \(t-2\) *missing* intermediate cardinalities. This yields arbitrarily large gaps for connected chordal block graphs (indeed, for connected cographs).

For \(r_i=2\) in every blade (a friendship graph), the polynomials simplify to
\[
F_B(z)=z^{t+1}(z+2)^t+z^{2t},\qquad
M_B(z)=2^t z^{t+1}+z^{2t}.
\]
For three triangular blades specifically, \(F_B(z)=8z^4+12z^5+7z^6+z^7\) but \(M_B(z)=8z^4+z^6\).

## Assumptions and scope

Graphs are finite, simple, undirected. The join \(\vee\) connects the single new center to every vertex of the disjoint union, without adding edges between distinct \(C_i\). The quantifiers above are all \(t\ge2\) and all integer vectors \((r_1,\ldots,r_t)\) with \(r_i\ge2\). Open-neighborhood total domination requires every vertex, selected or not, to have a *different* selected neighbor. In the secure condition, the exchanged set needs to be total dominating; it need not itself be secure. Inclusion-minimal means no proper subset is secure total dominating; it is not the same as minimum-cardinality.

## Proof

**Case \(c\notin S\).** For any clique \(C_i\), a selected vertex has neighbors in \(S\) only inside that same clique, and an unselected vertex also has no selected neighbor outside its clique. Therefore \(S\) is total dominating precisely when \(|S\cap C_i|\ge2\) for each \(i\). These conditions imply security: if an unselected vertex \(v\in C_i\) is attacked, exchange it with any selected vertex of \(C_i\); all clique counts are preserved, so total domination remains. If the unselected center \(c\) is attacked, exchange \(c\) for any selected vertex \(u\) of some clique \(C_j\); after the exchange, \(c\) is selected and every clique still has at least one selected vertex (\(C_j\) originally had at least two). Hence every vertex has a selected neighbor, including \(c\), so the exchange succeeds. The necessity of the counts already follows from total domination.

**Case \(c\in S\).** Total domination of the center requires at least one selected noncentral vertex. Suppose some clique \(C_j\) is completely unselected. Every \(v\in C_j\) has only the center among its selected neighbors. Its only possible defender is therefore \(c\). After replacing \(c\) by \(v\), the selected vertex \(v\) has no selected neighbor: vertices in other cliques are nonadjacent to it, and no other vertex of \(C_j\) was selected. This violates total domination, so security forces all \(|S\cap C_i|\ge1\). Conversely, if every clique meets \(S\), then \(S\) is total dominating, and every unselected vertex \(v\in C_i\) can exchange with any selected \(u\in C_i\): the center stays selected and the clique counts remain at least one. This produces another total dominating set. Thus the characterization is both necessary and sufficient.

**Enumeration.** If the center is selected, it contributes \(z\), and each \(C_i\) contributes the nonempty subset generating polynomial \((1+z)^{r_i}-1\). If the center is absent, each \(C_i\) contributes the subsets of cardinality at least two, counted by \((1+z)^{r_i}-1-r_i z\). The cases are disjoint and independent across cliques, proving the displayed formula for \(F_B\).

**Inclusion minimality and gap.** The characterization shows that with center present, one may delete extra vertices within any clique while preserving security, down to exactly one representative per clique. Such a minimal representative set has no center-free secure total dominating proper subset, since no clique would contain two selected vertices; deleting the center or any representative destroys security. Without the center, deletion is permissible down to exactly two representatives per clique. Such a set is inclusion-minimal because removing a vertex leaves a clique with fewer than two selected vertices. Conversely any larger center-free set is reducible. There are \(\prod_i r_i\) center-containing minimal sets and \(\prod_i\binom{r_i}{2}\) center-free minimal sets, establishing \(M_B\). Both products are positive under the stated assumptions. Since \(t+1\le2t\), the minimal and upper minimal cardinalities are exactly as claimed, with the claimed gap.

## Verification

The standalone file `verify.py` constructs graph adjacency lists and checks every subset using only the original total-domination and defender-exchange predicates. It then counts actual secure total dominating sets and checks inclusion minimality by scanning all smaller actual secure sets. The computed polynomials are independently compared with coefficient-convolution implementations of the displayed products. Run `python3 verify.py` from the extracted package directory. The expected output is in `verification_output.txt`.

The exhaustive finite check covered 66 ordered clique-size vectors with \(t\in\{2,3,4\}\), every \(r_i\in\{2,3,4\}\), and \(\sum_i r_i\le11\). It examined 127904 vertex subsets in total; all checks passed. Finite tests do not certify infinitely many instances. The general claim is proved by the two-case argument above.

## Relationship to prior work

Secure total domination is defined in Cabrera Martínez, Montejano, and Rodríguez-Velázquez (2019), which studies scalar bounds and structural relationships. Jha (2020) provides a linear-time secure-total-domination-number algorithm for cographs. Clique bouquets are cographs, so the scalar optimization problem for this class is already covered in principle. The claim here is instead the exact *all-set cardinality polynomial* and the two-point *inclusion-minimal-set spectrum* with arbitrarily large gaps; these are not given by a scalar optimization algorithm.

A published mathematical-research record describes a secure-total-domination polynomial of complete multipartite graphs; that graph class is distinct from the present clique bouquets (which have an induced \(2K_2\) when \(t\ge2\) and \(r_i\ge2\)). A different research record describes the dissociation polynomial of generalized windmills, but dissociation is a different vertex-subset property. Searches of these equivalents and neighboring results did not identify the exact enumerators here. Search absence alone cannot establish worldwide priority, and the stated novelty assessment remains subject to independent bibliographic verification.

## Limitations

The graph family is restricted to one universal cut vertex joining disjoint clique blades, each of order at least two. The theorem does not assert anything about general block graphs, arbitrary windmill variants without clique blades, or graphs joined at several cut vertices. The secure-total-domination minimum is not claimed to be new, and cograph algorithms predate this work. Accessible indexed primary full-text sections did not expose an equivalent full enumeration, but some direct publisher access was limited; priority in unindexed or uninspected literature remains a risk. Independent mathematical verification has not been performed.

## References

- A. Cabrera Martínez, L. P. Montejano, and J. A. Rodríguez-Velázquez, "On the Secure Total Domination Number of Graphs," *Symmetry* 11 (2019), 1165. DOI: 10.3390/sym11091165. First publicly verified publisher date: 2019-09-15. Note the published 2021 correction to a lemma unrelated to the present direct proof: DOI 10.3390/sym13091668.
- A. Jha, "Secure total domination in chain graphs and cographs," *AKCE International Journal of Graphs and Combinatorics* 17 (2020), 826–832. DOI: 10.1016/j.akcej.2019.10.005.
- A. Cabrera Martínez, A. Estrada-Moreno, and J. A. Rodríguez-Velázquez, "Secure Total Domination in Rooted Product Graphs," *Mathematics* 8 (2020), 600. DOI: 10.3390/math8040600.
- Published research record, "Secure-total-domination polynomial of complete multipartite graphs," published-finding corpus identifier `2026/10/4/SCOPE-secure-total-domination-polynomial-of-complete-multipartite-grap--03760d8f9284` (comparison of different graph classes).
- Published research record, "Dissociation polynomial and all maximal dissociation sets of generalized windmills," published-finding corpus identifier `2026/10/4/SCOPE-dissociation-polynomial-and-all-maximal-dissociation-sets-of-gen--2c55298c97bc` (comparison of a different parameter).
