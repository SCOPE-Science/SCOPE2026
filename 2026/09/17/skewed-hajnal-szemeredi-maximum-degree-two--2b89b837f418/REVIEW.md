# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The main theorem is reduced to three exhaustive cases according to the number of prescribed classes of size \(s+1\).

For no large class, the hypotheses are exactly within Birken's proved bound \(n_i\le\lfloor n/3\rfloor\).

For one large class, Lemma 3 supplies an independent class of the required size whose deletion is bipartite. The remaining prescribed classes all have size at most \(s\), while the remaining bipartite graph has independence number at least \(s\); Theorem 2 therefore realizes the residual vector.

For two large classes, necessarily \(n=3s+2\). An equitable 3-coloring has class sizes \(s+1,s+1,s\), and splitting the independent class of size \(s\) realizes every possible collection of the remaining prescribed sizes.

Theorem 2 was checked at the level of both allocation and local realization. Its flow condition for a color subset \(A\) is
\[
\sum_{i\in A}c_i\le \sum_j\min\{h_j,|A|q_j\}.
\]
For \(|A|=1\) this is exactly the assumed independence-number bound; for \(|A|\ge2\) it is automatic because \(2q_j\ge h_j\). Integrality yields local multiplicities. Paths and even cycles then realize those multiplicities under their sharp largest-class constraints.

Lemma 3 is valid componentwise because every selected vertex of an odd cycle extends to a maximum independent set of that cycle, while every maximum-degree-two component has independence number at least one third of its order.

No counterexample was found in finite sanity checks on small maximum-degree-two graphs; the published result does not rely on computation.

## Originality

**PASS, to the best of our knowledge.**

Birken's arXiv:2609.18629v1 explicitly states the stronger nondivisible-order assertion as Conjecture 5 in its future-work section. The paper proves the smaller-class bound but does not settle the \(r=2\) case of Conjecture 5.

Kuchukova--Perkins--Povill formulate the earlier prescribed-class-size conjecture with the uniform cap \(\lfloor n/(\Delta+1)\rfloor\), which Birken proves. Their work does not contain the larger-class statement resolved here.

Literature checks included the exact conjecture wording and combinations of “prescribed coloring”, “skewed coloring”, “fixed color class sizes”, “maximum degree two”, “paths”, “cycles”, “bounded coloring”, and “capacitated coloring”. No prior theorem was located that implies the \(r=2\) case or the exact bipartite maximum-degree-two criterion of Theorem 2.

Residual risk remains for two reasons. First, Birken's conjecture is extremely recent, so parallel work may not yet be indexed. Second, older constrained-coloring literature uses several terminologies; an equivalent version of the auxiliary Theorem 2 may exist under a different formulation. The originality claim is therefore limited to the best of our knowledge, with strongest confidence in the explicit resolution of Birken's stated \(r=2\) case.

## Value

**PASS.**

The main result settles the first nontrivial maximum-degree case of an explicit recent strengthening of the Hajnal--Szemerédi theorem rather than merely improving a numerical example. The proof also isolates a sharp structural theorem for prescribed colorings of bipartite maximum-degree-two graphs, giving an exact necessary-and-sufficient condition in terms of the independence number.

## Sources inspected

- Mathis Birken, *A Hajnal--Szemerédi theorem for skewed colorings*, arXiv:2609.18629v1. The theorem statement, definition of prescribed coloring, and Future Work/Conjecture 5 were inspected.
- Aiya Kuchukova, Will Perkins, Xavier Povill, *Sampling Colorings with Fixed Color Class Sizes*, ICALP 2026 / arXiv:2603.08259. The prescribed-coloring conjecture and surrounding discussion were inspected.
- Search results for older bounded/capacitated/prescribed coloring terminology were inspected for possible equivalent coverage; no directly matching theorem was identified.

No inaccessible source was found whose available metadata gave concrete reason to believe it already contains the main result. The possibility of an unindexed or differently phrased source remains part of the residual originality risk above.
