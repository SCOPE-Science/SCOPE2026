# A sharp two-extension threshold for Schrijver graphs and a common unrestricted three-variable theory

## Finding

For every pair of integers \(r\ge 2\) and \(n\ge 2r\), let \(\mathrm{SG}(n,r)\) be the finite simple graph whose vertices are the \(r\)-element independent sets of the cycle \(C_n\); two vertices are adjacent when their underlying sets are disjoint. Say that a graph is **2-existentially closed** (2-e.c.) if, for any two *distinct* vertices \(A,B\) and each of the four assignments of adjacency/nonadjacency to them, some third vertex \(W\notin\{A,B\}\) realizes that assignment.

**Theorem.** For all \(r\ge2\) and \(n\ge2r\),
\[
\mathrm{SG}(n,r)\text{ is 2-e.c.}\quad\Longleftrightarrow\quad n\ge4r-1.
\]
Moreover, every edge lies in a triangle precisely for \(n\ge4r-1\). All graphs in the 2-e.c. range are equivalent to each other and to the countable random (Rado) graph in ordinary, counting-free first-order logic using at most three reusable variables and **unrestricted quantifier depth**. At the boundary \(n=4r-2\), a three-variable sentence asserting that every edge belongs to a triangle fails, so the transition is sharp in this logic. Nevertheless, by Schrijver's chromatic theorem, \(\chi(\mathrm{SG}(4r-1,r))=2r+1\), which is unbounded along this single three-variable theory.

## Assumptions and scope

The ground cycle has vertices \(0,1,\dots,n-1\), with cyclic adjacency. A stable set is a set containing no cyclically consecutive positions. Graph adjacency, not set inclusion, is the only nonlogical symbol in the logical conclusions. No counting quantifiers, named colors, ground-cycle successor relation, or vertex labels are supplied to the logic. The theorem concerns every integer pair \(r\ge2,n\ge2r\), with no further divisibility or asymptotic assumption. The countable random graph is used only as a comparison structure; finite-variable equivalence is not graph isomorphism or full first-order equivalence.

A combinatorial fact used repeatedly: if \(U\subsetneq V(C_n)\), then \(C_n[U]\) is a disjoint union of paths. In particular it has an independent set of size at least \(\lceil |U|/2\rceil\): select the larger color class in a bipartition of each path.

## Proof

**Necessity and sharpness.** Let \(2r\le n\le4r-2\). The cyclically stable sets
\[
A=\{0,2,\ldots,2r-2\},\qquad B=\{1,3,\ldots,2r-1\}
\]
are disjoint, so they form an edge in \(\mathrm{SG}(n,r)\). A common graph-neighbor would be a stable \(r\)-set in the remaining consecutive path of \(n-2r\) ground vertices, but that path has independence number \(\lceil(n-2r)/2\rceil\le r-1\). Thus this edge has no common neighbor, 2-e.c. fails, and the every-edge-triangle sentence is false. The empty remaining path at \(n=2r\) is included.

**Sufficiency.** Fix \(n\ge4r-1\) and distinct stable \(r\)-sets \(A,B\). Let \(N[x]=\{x-1,x,x+1\}\) in the ground cycle, interpreted modulo \(n\). We construct a stable \(r\)-set \(W\notin\{A,B\}\) for each adjacency pattern.

(1) *Adjacent to both:* The complement \(U=V(C_n)\setminus(A\cup B)\) has at least \(n-2r\ge2r-1\) elements, so the path lemma supplies an independent \(r\)-subset \(W\subseteq U\). It is disjoint from both \(A,B\).

(2) *Adjacent to \(A\), nonadjacent to \(B\):* Choose \(b\in B\setminus A\). Put \(U=V(C_n)\setminus(A\cup N[b])\), so \(|U|\ge n-r-3\ge3r-4\). If \(r\ge3\), the path lemma gives an independent \(r\)-set \(D\subseteq U\), since \(\lceil(3r-4)/2\rceil\ge r\). Each of the \(r\) sets \(\{b\}\cup(D\setminus\{d\})\), for \(d\in D\), is stable, avoids \(A\), and meets \(B\). At most one equals \(B\); none equals \(A\), so an admissible one exists. If \(r=2\), then \(|U|\ge2\), and for two distinct \(u\in U\) the sets \(\{b,u\}\) have the required properties; at most one equals \(B\). The reverse mixed pattern follows by exchanging \(A,B\).

(3) *Nonadjacent to both:* If \(A\cap B\ne\varnothing\), choose \(a\in A\cap B\) and use \(U=V(C_n)\setminus N[a]\). The path lemma gives an independent \((2r-2)\)-subset \(D\subseteq U\), because \(n-3\ge4r-4\). For \(r\ge3\), the \(\binom{2r-2}{r-1}>2\) sets \(\{a\}\cup D'\) with \(D'\subseteq D\) and \(|D'|=r-1\) are stable, meet both \(A,B\), and at least one differs from both anchors. For \(r=2\), at least \(n-3\ge4\) individual vertices \(u\notin N[a]\) give distinct stable sets \(\{a,u\}\); at most two equal the anchors.

If \(A\cap B=\varnothing\), there exist \(a\in A,b\in B\) **not** adjacent in the ground cycle: otherwise their complete \(2\)-by-\(2\) cross-incidence would give a \(4\)-cycle in the ground graph \(C_n\), impossible for \(n\ge7\). Remove \(N[a]\cup N[b]\), at most six ground vertices. The remaining proper induced subgraph consists of paths on at least \(n-6\ge4r-7\) vertices; its independence number is at least \(\lceil(4r-7)/2\rceil\ge r-2\). Adjoin any independent \((r-2)\)-subset to \(\{a,b\}\). This is a stable \(r\)-set intersecting both anchors; being mixed between disjoint sets, it equals neither.

All four patterns are realized. This proves the 2-e.c. equivalence and, combined with part (1), the every-edge-triangle equivalence.

**Three-variable consequence.** The countable random graph has the extension property for every finite adjacency and nonadjacency prescription, hence in particular 2-e.c. In the ordinary three-pebble game between any two 2-e.c. graphs, Duplicator preserves equality and adjacency among occupied pebbles. Whenever a pebble is lifted, at most two distinct anchors remain. A fresh vertex with any prescribed adjacency pattern to those anchors exists in the second graph by the 2-e.c. property, and repeated-point moves can be matched identically. For one or zero anchors, two-point extension also supplies the needed fresh vertices. The invariant is permanent and works for every number of rounds. By the finite-variable pebble-game characterization, the structures agree on all three-variable first-order sentences, without bounding quantifier rank. Conversely the sentence
\[
\forall x\,\forall y\bigl((x\ne y\land E(x,y))\to
\exists z\,(z\ne x\land z\ne y\land E(x,z)\land E(y,z))\bigr)
\]
uses only three variable symbols and separates \(n=4r-2\) from the 2-e.c. range. Finally, Schrijver's theorem gives \(\chi(\mathrm{SG}(n,r))=n-2r+2\); at \(n=4r-1\) this is \(2r+1\), as claimed.

## Verification

The accompanying independent Python programs enumerate every cyclically stable \(r\)-set, construct adjacency from disjointness, and test all four extension patterns for every unordered pair of distinct graph vertices; they also independently construct the sharp non-triangle edge and compute the maximum stable-set size in its complement by brute force. Run `python verify_schrijver.py` and `python verify_boundary.py` using Python 3 standard library, and compare the output with `verification_output.txt` and `boundary_output.txt`. The first program checks 36 finite instances, including every tested size on both sides of the sharp threshold. The second checks 48 explicit boundary witnesses.

These experiments do not establish any untested infinite parameter range. The unrestricted theorem rests on the path-independence argument and the permanent pebble invariant proved above.

## Relationship to prior work

Schrijver (1978) defines stable Kneser graphs and proves their chromatic number and vertex-criticality; the relevant original article has been inspected through its definition and theorem/proof sections. Those assertions do not imply the four-pattern two-point extension threshold nor unrestricted three-variable equivalence. Matoušek and Ziegler (first public arXiv submission 2002-08-09) analyze topological chromatic lower bounds and Schrijver graphs, including colorability; they do not state a two-point extension threshold or the above logical equivalence. Grohe and Otto (2012) establish general finite-variable pebble-game techniques but do not treat this Schrijver family. Schultz (2010) studies homomorphism spaces and test-graph properties of the same family; Torres and Valencia-Pabon (2016) classify shifts and hom-idempotence phenomena. These same-family theorems do not establish local two-point extension patterns or bounded-variable equivalence. A relevant preexisting comparison of **ordinary** Kneser graphs is limited to quantifier rank three and uses a different graph family, hence does not imply the present result. Closely related published research records on the homology of stable Kneser independence complexes concern topological invariants instead of graph two-extension patterns. No covering result was identified in the searched sources, but search absence is not proof of historical priority.

## Limitations

The extension property is 2-e.c., not the full extension property for arbitrary finite patterns. The logic equivalence is counting-free and uses at most three variables; it does not transfer to first-order logic with unrestricted variables, counting quantifiers, or the signature naming the cyclic order. The claim is about the precisely specified stable Kneser family, not arbitrary Kneser graphs. Schrijver's original 1978 publication has no verified exact first-public calendar day in the inspected evidence. Historical-priority comparisons are necessarily bounded.

## References

1. A. Schrijver, *Vertex-critical subgraphs of Kneser graphs*, Nieuw Archief voor Wiskunde (3) **26** (1978), 454–461. Original full text: https://ir.cwi.nl/pub/9898/9898D.pdf .
2. J. Matoušek and G. M. Ziegler, *Topological lower bounds for the chromatic number: A hierarchy*, arXiv:math/0208072, first submitted 2002-08-09; https://arxiv.org/abs/math/0208072 .
3. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, CSL 2012, 289–304. https://drops.dagstuhl.de/opus/volltexte/2012/3679/pdf/25.pdf .
4. C. Schultz, *Paths of homomorphisms from stable Kneser graphs*, arXiv:1006.0474, 2010. https://arxiv.org/abs/1006.0474 .
5. P. Torres and M. Valencia-Pabon, *Shifts of the Stable Kneser Graphs and Hom-Idempotence*, arXiv:1604.07023, 2016. https://arxiv.org/abs/1604.07023 .
