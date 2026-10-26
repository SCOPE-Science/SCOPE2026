# Twelve quantifier-rank-three theories of finite 2-regular graphs

## Finding

**Theorem.** Among nonempty finite simple undirected graphs of degree exactly \(2\), there are exactly **twelve** equivalence classes under agreement on all first-order sentences of quantifier rank at most \(3\), in the language of adjacency and equality. Moreover, six explicit sentences of rank at most \(3\), defined below, jointly determine the entire rank-\(3\) theory.

Write \(E(x,y)\) for adjacency; all quantifiers range over vertices. Define the following six Boolean observations:

- \(T\): some three distinct vertices form a triangle, expressible as \(\exists x\exists y\exists z\,[E(x,y)\land E(y,z)\land E(z,x)]\).
- \(Q\): distinct nonadjacent vertices have identical open neighborhoods, expressible as \(\exists x\exists y\,[x\ne y\land\neg E(x,y)\land\forall z\,(E(x,z)\leftrightarrow E(y,z))]\).
- \(F\): there are distinct nonadjacent \(x,y\) with both a common neighbor and a neighbor of \(x\) that is not adjacent to \(y\). Formally \(\exists x\exists y\,[x\ne y\land\neg E(x,y)\land\exists z\,(E(x,z)\land E(y,z))\land\exists w\,(E(x,w)\land\neg E(y,w))]\).
- \(I\): three pairwise distinct, pairwise nonadjacent vertices exist, expressible by \(\exists x\exists y\exists z\) followed by their six inequality/nonadjacency conditions.
- \(D\): one or two vertices dominate the graph, expressible as \(\exists x\exists y\forall z\,[z=x\lor z=y\lor E(z,x)\lor E(z,y)]\).
- \(U\): a universal vertex exists, expressible as \(\exists x\forall y\,[x=y\lor E(x,y)]\).

Each formula has quantifier rank at most \(3\), with \(U\) having rank \(2\). For a 2-regular graph, \(T,Q,F\) say exactly whether it contains, respectively, a cycle of length \(3\), of length \(4\), and of length at least \(5\). The following table gives all twelve rank-\(3\) classes. A row's representative is the disjoint union of cycles of the displayed lengths; the signature order is \((T,Q,F,I,D,U)\), with true/false coded \(1/0\).

| Representative cycle lengths | Signature | Complete structural description |
| --- | --- | --- |
| \((3)\) | \((1,0,0,0,1,1)\) | Exactly one triangle |
| \((3,3)\) | \((1,0,0,0,1,0)\) | Exactly two triangles |
| \((3,3,3)\) | \((1,0,0,1,0,0)\) | At least three triangles, no other cycles |
| \((4)\) | \((0,1,0,0,1,0)\) | Exactly one four-cycle |
| \((4,4)\) | \((0,1,0,1,0,0)\) | At least two four-cycles, no other cycles |
| \((5)\) | \((0,0,1,0,1,0)\) | Exactly one five-cycle |
| \((6)\) | \((0,0,1,1,1,0)\) | Exactly one six-cycle |
| \((7)\) | \((0,0,1,1,0,0)\) | One cycle of length at least \(7\), or at least two cycles each of length at least \(5\); no shorter cycles |
| \((3,4)\) | \((1,1,0,1,0,0)\) | At least one triangle and one four-cycle; no longer cycles |
| \((3,5)\) | \((1,0,1,1,0,0)\) | Triangles and cycles of length at least \(5\), but no four-cycles |
| \((4,5)\) | \((0,1,1,1,0,0)\) | Four-cycles and cycles of length at least \(5\), but no triangles |
| \((3,4,5)\) | \((1,1,1,1,0,0)\) | All three length categories present |

Consequently, two nonempty finite 2-regular graphs satisfy the same first-order sentences of quantifier rank at most \(3\) **if and only if** their six Boolean observations agree.

## Assumptions and scope

Graphs are finite, nonempty, simple, undirected and \(2\)-regular; hence each connected component is a simple cycle of length at least \(3\). Quantifier rank counts nested first-order quantifiers, without restricting the number of variable names. The statement is about **elementary rank-\(3\) equivalence**, not first-order equivalence without a quantifier-rank bound, nor counting logic or the fragment using only three variable symbols.

## Proof

**1. Finite reduction.** Brown and Hoshino's cycle theorem [1, Theorems 4.1 and 4.9] says that all cycles of length at least \(7\) are indistinguishable by first-order sentences of quantifier rank at most \(3\). The standard Ehrenfeucht–Fraïssé composition strategy shows that if \(A\equiv_3 B\), then \(A\sqcup C\equiv_3 B\sqcup C\): maintain a componentwise matching of played vertices and use each component's winning strategy. Likewise, for any fixed nonempty graph \(A\), the disjoint unions of three and of any larger number of copies of \(A\) are rank-\(3\) equivalent: in three moves Spoiler can touch at most three components, so Duplicator can always match them to previously unused components. Thus every graph in the theorem is rank-\(3\) equivalent to one with \(0,1,2\), or \(3\) copies of each of \(C_3,C_4,C_5,C_6,C_7\). Excluding the all-zero multiplicities gives exactly \(4^5-1=1023\) canonical cases. The reduction does **not** assume that components of distinct lengths are interchangeable.

**2. Exact finite back-and-forth invariant.** For vertices \(a,b\), define \(P(a,b)\) from: (i) whether \(a=b\); (ii) whether \(E(a,b)\); and (iii) the set of adjacency patterns \((E(a,c),E(b,c))\in\{0,1\}^2\) realized by vertices \(c\notin\{a,b\}\). Since the graph is loopless, the omitted cases \(c=a,b\) are determined by (i) and (ii). Hence \(P(a,b)\) is precisely the full rank-\(1\) first-order type of the ordered pair \((a,b)\). The rank-\(2\) type of a vertex \(a\) is determined by the set \(S(a)=\{P(a,b):b\in V\}\), and the rank-\(3\) theory of the graph is determined by the set \(\{S(a):a\in V\}\). These are the three successive exact back-and-forth/Hintikka recursions; each is an equivalence, not merely a necessary condition.

**3. Exhaustive reduced comparison.** The standalone deterministic program `checker.py` calculates the exact rank-\(3\) type above and the truth values of \(T,Q,F,I,D,U\) for all \(1023\) canonical cases. It asserts both implications between equality of the type and equality of the six-bit signature. Both induced partitions contain exactly twelve blocks; `enumeration.txt` records each signature, a smallest representative, and its class size among canonical cases. The loops exhaust five independently chosen multiplicities in \(\{0,1,2,3\}\), omitting only the empty graph. The code handles adjacency and equality of **every** candidate pair, and its extension mask considers **all** distinct third vertices. This proves completeness of the classification over the canonical finite family; Step 1 extends it to every allowed graph.

**4. Sharpness and explicit definability.** The truth values in the displayed table are distinct. Every listed observation is itself a sentence of rank at most \(3\), so two rows cannot be rank-\(3\) equivalent. Conversely, Step 3 shows that agreeing on all six observations forces the exact rank-\(3\) types to agree. On a disjoint union of cycles, the structural meanings of \(T,Q,F\) follow by inspecting degree-two neighborhoods: opposite vertices of a four-cycle have equal neighborhoods; a distance-two pair in any longer cycle has a common and an exclusive neighbor; neither phenomenon occurs within triangles. The other columns follow from the independence number and minimum dominating-set size of cycles and additivity across components. This verifies the structural descriptions separately from the machine-based type comparison.

## Verification

Run `python3 checker.py` with Python 3; it checks exactly \(1023\) canonical graphs, finds twelve rank-\(3\) classes, and verifies that the six explicit sentences separate and characterize every class. Run `python3 game_crosscheck.py` for a second implementation using direct alternating Spoiler/Duplicator minimax: all \(144\) ordered comparisons of the twelve representatives, and five additional within-class comparisons, agree. The deterministic output for the first program is supplied as `enumeration.txt`. These finite computations are **exhaustive only for the provably finite canonical family**; the reduction in Step 1 is essential for the unbounded theorem.

## Relationship to prior work

Brown and Hoshino [1] give the complete rank-dependent Ehrenfeucht–Fraïssé comparison for two **connected** paths or two **connected** cycles and explicitly identify further graph families, including regular graphs, as open for exploration. The theorem here uses their sharp rank-three cycle threshold as a component lemma and computes the complete disconnected finite 2-regular picture, including an explicit six-sentence signature and the exact number twelve. General finite-model-theory back-and-forth and disjoint-union composition principles [2,3] imply a finite reduction in principle, but the checked sources do not state this twelve-class catalogue or its elementary distinguishing signature.

## Limitations

Only rank \(3\) and nonempty undirected simple degree-two graphs are classified. The \(1023\)-case verification is exact under the displayed reduction; it is not a substitute for the reduction or a claim of exhaustive search through all published literature. The conclusion concerns ordinary first-order logic, not counting quantifiers. Further unindexed results on quantifier-rank classifications of two-factors could affect the originality assessment. Independent audit has not been performed.

## References

[1] J. Brown and R. Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, Ars Combinatoria **83** (2007), 193–212. Published 30 April 2007. Primary full text: https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf ; publisher record: https://combinatorialpress.com/ars-articles/volume-083-ars-articles/the-ehrenfeucht-fraisse-game-for-paths-and-cycles/ .

[2] H.-D. Ebbinghaus and J. Flum, *Finite Model Theory*, Springer, 1995, general Ehrenfeucht–Fraïssé and quantifier-rank apparatus.

[3] A. Dawar, *Finite and Algorithmic Model Theory II: Automata-Based Methods*, lecture 22, August 2016, disjoint-sum composition of elementary-rank equivalence. https://simons.berkeley.edu/sites/default/files/docs/5233/lecture22.pdf .
