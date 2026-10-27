# The isolated-edge kernel of finite symmetric non-contingency frames

## Finding

Fix an integer \(n\ge 1\) and a labelled vertex set \(W=\{1,\ldots,n\}\). Regard each finite simple undirected graph \(G\) on \(W\) as a loop-free symmetric Kripke frame. In the Boolean modal language whose only primitive modality is non-contingency \(\Delta\), put
\[
(G,V),w\models\Delta\varphi\quad\Longleftrightarrow\quad
 N_G(w)\subseteq\llbracket\varphi\rrbracket_{G,V}
 \text{ or }N_G(w)\cap\llbracket\varphi\rrbracket_{G,V}=\varnothing.
\]
The vacuous cases of no successors and one successor both make \(\Delta\varphi\) true.

Two such graphs are **pointwise non-contingency equivalent**, denoted \(G\equiv_\Delta H\), when for **every** propositional valuation \(V\) on the same named vertex set, every formula of this language, and every world \(w\in W\), the two corresponding truth values agree. This is a fixed-domain, same-valuation relation on labelled frames; it is not equivalence merely of frame-valid formulas, graph isomorphism, or modal bisimilarity for one chosen valuation.

Let \(\kappa(G)\) be the graph obtained by deleting every edge that forms an entire connected component isomorphic to \(K_2\), retaining both endpoints as isolated vertices. Then
\[
\boxed{G\equiv_\Delta H\quad\Longleftrightarrow\quad \kappa(G)=\kappa(H).}
\]
Whenever the kernels differ, some valuation of **one** proposition \(p\) and some named world distinguish the graphs by the depth-one formula \(\Delta p\). Conversely, equality of kernels preserves formulas of arbitrary nesting depth. Thus \(\kappa\) is the exact, unique labelled canonical representative of each equivalence class.

If the common kernel has exactly \(s\) isolated vertices, its equivalence class contains exactly
\[
\boxed{I_s=\sum_{j=0}^{\lfloor s/2\rfloor}\frac{s!}{2^j j!(s-2j)!}}
\]
graphs. The representatives are obtained by adding an arbitrary matching between its isolated vertices; \(I_s\) is the familiar involution/matching number.

Write \(C_{n,s}\) for the number of equivalence classes whose kernel has exactly \(s\) isolated vertices, and \(B_m\) for the number of labelled simple graphs on \(m\) vertices with neither isolated vertices nor \(K_2\) components, with \(B_0=1\). Then the **entire class-size distribution**, rather than only its total, is
\[
\boxed{C_{n,s}=\binom ns B_{n-s},\qquad
\sum_{n,s\ge0}C_{n,s}y^s\frac{z^n}{n!}
=\exp\!\left((y-1)z-\frac{z^2}{2}\right)
\sum_{m\ge0}2^{\binom m2}\frac{z^m}{m!}.}
\]
All generating-function equalities here are identities of formal power series. In particular, for \(n\ge3\) the possible kernel isolate counts are precisely \(s\in\{0,1,\ldots,n-3,n\}\), and each such class has size \(I_s\). For \(n=1\) the sole class has size one; for \(n=2\) the sole class has size two.

The total number of equivalence classes is
\[
\boxed{Q_n=\sum_{j=0}^{\lfloor n/2\rfloor}(-1)^j
\frac{n!}{2^j j!(n-2j)!}\,2^{\binom{n-2j}{2}}.}
\]
**The univariate sequence and this inclusion-exclusion formula are previously known as the graph enumeration OEIS A093352.** Their non-contingency interpretation is a consequence of the kernel theorem; neither the bare graph-counting sequence nor the inclusion-exclusion identity is presented as independently new.

For illustration, when \(n=6\), the \(C_{6,s}\) values are \(26864,4368,570,80,1\) for \(s=0,1,2,3,6\), respectively. Their corresponding class sizes are \(1,1,2,4,76\). Thus there are exactly \(31883\) equivalence classes among the \(32768\) labelled six-vertex graphs, with a unique largest class of \(76\) graphs.

## Assumptions and scope

- Vertices are **named** and identical between compared frames, edges are undirected and loop-free, and valuations on the two graphs must be identical at each named vertex. No quotient by graph isomorphism is taken.
- The language has ordinary classical propositional connectives, constants and arbitrarily nested \(\Delta\); it does not contain primitive necessity \(\Box\), possibility \(\Diamond\), counting modalities, hybrid names or quantification over worlds.
- The equivalence quantifies over all valuations of propositional atoms; nevertheless, the separation theorem uses only one atom and one depth-one formula.
- The counting formulas hold for every \(n\ge1\); for formal generating functions the empty graph at \(n=0\) is included with coefficient one as an auxiliary convention.

## Proof

**Lemma 1: the exact one-step observation of a successor set.** For \(S\subseteq W\), define \(h_S:\mathcal P(W)\to\{0,1\}\) by
\[
h_S(X)=1\quad\Longleftrightarrow\quad S\subseteq X\ \text{or}\ S\cap X=\varnothing.
\]
Then \(h_S=h_T\) on all subsets \(X\subseteq W\) if and only if either both \(S,T\) have cardinality at most one, or \(S=T\) has cardinality at least two. Every \(S\) of size at most one gives the constant-one map. If \(|S|\ge2\) and \(|T|\le1\), pick \(x\in S\) and set \(X=\{x\}\): the two maps disagree. If \(|S|,|T|\ge2\) and \(S\ne T\), then (i) when one is a proper subset of the other, choose \(X\) to be the smaller set; (ii) when they intersect but are incomparable, take \(X=S\); (iii) when they are disjoint, choose a singleton in \(S\). In each case exactly one of \(S,T\) is split into two nonempty parts by \(X\), proving the lemma.

**Lemma 2: one-step tests determine all modal observations.** Given a valuation \(V(p)=X\), the truth of \(\Delta p\) at \(w\) is exactly \(h_{N_G(w)}(X)\). Thus agreement for every valuation of this one formula at every named world is equivalent, by Lemma 1, to equality of the two neighbourhoods whenever either has size at least two and to both neighbourhoods having size at most one otherwise. Such rowwise agreement means the Boolean set transformations \(X\mapsto \{w:h_{N_G(w)}(X)=1\}\) and \(X\mapsto \{w:h_{N_H(w)}(X)=1\}\) coincide on **all** subsets. Induction over formulas, using the identical valuation for atoms and these identical transformations for the \(\Delta\)-step, establishes preservation of all nested formulas. The converse has already been witnessed by \(\Delta p\).

**Lemma 3: the graph kernel.** Because the relations are undirected and loop-free, an edge belongs to an isolated \(K_2\) component if and only if both of its endpoints have degree one. Every other edge has at least one endpoint of degree at least two. Lemma 2 recovers all adjacency lists of vertices of degree at least two exactly, including their neighbours of degree one. Therefore the only possible discrepancy between equivalent graphs consists of edges connecting pairs of degree-one vertices, which are precisely isolated \(K_2\) components. Equivalently their \(\kappa\)-kernels coincide. Conversely, removing or adding such components changes only the neighbourhoods of degree-zero or degree-one vertices and leaves all larger neighbourhoods untouched. Lemma 2 proves equivalence. This also proves the depth-one separation claim and uniqueness of the kernel.

**Lemma 4: all lifts and their multiplicities.** Let \(C\) contain no \(K_2\) component, and let \(I\) be its set of \(s\) isolated vertices. Any graph \(G\) with \(\kappa(G)=C\) must retain every edge of \(C\) and can add edges only among \(I\); each added edge must form a whole \(K_2\) component. Hence those edges form a matching. Conversely every matching produces such a lift. Choosing \(2j\) of the \(s\) vertices and partitioning them into \(j\) unordered pairs gives \(s!/(2^j j!(s-2j)!)\) choices. Summation proves \(I_s\). Since any core has no isolated \(K_2\), its remaining \(n-s\) vertices have no isolated vertices and no \(K_2\) components. Choosing the \(s\) isolated labels proves \(C_{n,s}=\binom ns B_{n-s}\). A graph on \(m\ge3\) vertices can be connected, so \(B_m>0\), whereas \(B_1=B_2=0\). This yields the exact support assertion.

**Lemma 5: census and formal generating functions.** Let \(A(z)=\sum_{m\ge0}2^{\binom m2}z^m/m!\) be the formal exponential generating function of all simple labelled graphs. The exponential formula for sets of connected components removes the single isolated-vertex component and the single two-vertex edge component by multiplying \(A(z)\) by \(\exp(-z-z^2/2)\); thus this product is \(\sum_{m\ge0}B_m z^m/m!\). Adjoining \(s\) isolated labelled vertices tracked by \(y\) multiplies it by \(\exp(yz)\), proving the bivariate formula. Specializing \(y=1\) gives \(\exp(-z^2/2)A(z)\), whose coefficient expansion proves the displayed known formula for \(Q_n\). Finally \(\sum_s C_{n,s}I_s=2^{\binom n2}\), since every graph lies in exactly one kernel fiber; this also follows from the product \(\exp(z^2/2)\) of matching components.

The five lemmas prove the theorem with all asserted quantifiers and boundary values.

## Verification

The standalone standard-library script `checker.py` enumerates all \(2^{\binom n2}\) labelled simple graphs for \(1\le n\le6\). For each graph it computes the truth values of \(\Delta p\) at every world under every one-letter valuation \(V(p)\subseteq W\), constructs its isolated-edge kernel, and verifies that distinct kernels give distinct full one-step semantic signatures. It independently checks the class fibers against matching numbers, the class totals against the known inclusion-exclusion count, and the distribution \(C_{n,s}=\binom ns B_{n-s}\), including the identity \(\sum_s C_{n,s}I_s=2^{\binom n2}\). Executing `python3 checker.py` produced `ALL_CHECKS_OK 66771`.

These exhaustive tests cover only \(n\le6\), **not** every finite graph. The unrestricted statements are proved in Lemmas 1–5, not inferred from finite computation.

## Relationship to prior work

Sierra Miranda, Wang and Zenger (2026) provide the standard non-contingency semantics and develop labelled-sequent completeness for classes defined by generalized path conditions, including symmetry. Their result does not itself state an exact same-valuation quotient of labelled simple graphs, the isolated-edge canonical form, or the full class-fiber distribution. Fan, Wang and van Ditmarsch (2014, 2015) establish non-contingency bisimulation and frame proof systems; Ding and Yang (2026) provide general bundled-modality bisimulation results. Their general equivalence methods are acknowledged, **not** claimed as new here. Passing from those methods to the explicit loop-free symmetric graph kernel and its complete equivalence-fiber spectrum requires an additional structural and counting argument.

The univariate sequence \(Q_n\) is **exactly OEIS A093352**, known independently as the count of labelled graphs without a connected component of order two; the formal exponential generating function was already recorded there. The contribution described here is the identification of that existing graph class as the exact **modal observational quotient**, the depth-one completeness statement, and the complete fiber-size distribution. The enumerative identity itself is not claimed as original.

## Limitations

This is a same-domain, same-valuation, pointwise classification for finite simple undirected loop-free frames only. It does not characterize graph isomorphism, ordinary modal \(\Box\)-equivalence, frame validity, or arbitrary directed/reflexive Kripke frames. Its bivariate distribution specializes existing graph-enumeration ingredients; the novelty assessment concerns their non-contingency semantic interpretation. Earlier general non-contingency bisimulation theory can suggest the same structural collapse, so the degree of priority remains subject to expert comparison. Full text of the relevant 2014 bisimulation article was not available in the reviewed material; only indexed excerpts and bibliographic descriptions were accessible. A July 2026 thesis on bundled fragments is a further possible priority risk whose full text was not inspected. No independent audit has been performed.

## References

1. B. Sierra Miranda, Y. Wang and L. Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975v1 (first posted 2026-09-30), https://arxiv.org/html/2609.38975v1.
2. J. Fan, Y. Wang and H. van Ditmarsch, *Almost Necessary*, *Advances in Modal Logic* 10 (2014), 178–196, https://www.aiml.net/volumes/volume10/Fan-Wang-Ditmarsch.pdf.
3. J. Fan, Y. Wang and H. van Ditmarsch, *Contingency and Knowing Whether*, *Review of Symbolic Logic* 8 (2015), 75–107, https://doi.org/10.1017/S1755020314000343.
4. Y. Ding and Y. Yang, *A General Theory of Propositional Modal Bundled Modalities*, *EPTCS* 447 (2026), 299–320, https://doi.org/10.4204/EPTCS.447.17.
5. OEIS Foundation, A093352, *Number of labeled n-vertex graphs without a 2-component*, https://oeis.org/A093352; formula credited there to Marko Riedel (2022).
