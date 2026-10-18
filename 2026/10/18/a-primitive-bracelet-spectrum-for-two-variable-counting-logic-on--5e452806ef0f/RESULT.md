# A primitive-bracelet spectrum for two-variable counting logic on pseudoforests

## Finding

Let \(\mathcal P\) be the class of all finite simple undirected pseudoforests, including the empty graph: every connected component has at most one cycle. In the adjacency-only relational language, two members of \(\mathcal P\) satisfy the same sentences of two-variable first-order logic with counting, \(C^2\), precisely when they have identical **tree-component multiplicities** and **primitive decorated-bracelet repetition totals**, as defined below. This is a complete, all-order invariant rather than a bounded-size test.

Let \(\mathfrak T\) be the unlabelled unrooted finite trees, \(\mathfrak R\) the unlabelled rooted finite trees, and \(\mathfrak B\) the set of primitive bracelets (words modulo rotation and reversal, with least rotational period equal to their length) over alphabet \(\mathfrak R\). For \(\beta\in\mathfrak B\), write \(p(\beta)\) for its period length, \(w(\beta)\) for the sum of the numbers of vertices in its rooted-tree letters, and \(r(\beta)=\max\{1,\lceil3/p(\beta)\rceil\}\). The exact ordinary generating function \(F(z)=\sum_{n\ge0}c_nz^n\), with \(c_n\) counting \(C^2\)-equivalence classes of \(n\)-vertex pseudoforests, is

\[
 F(z)=\prod_{T\in\mathfrak T}\frac1{1-z^{|T|}}\ \prod_{\beta\in\mathfrak B}\left(1+\frac{z^{r(\beta)w(\beta)}}{1-z^{w(\beta)}}\right).
\]

The products are formal power series: every coefficient involves only finitely many factors. Their coefficients for \(0\le n\le9\) are

\[
 (c_0,c_1,\ldots,c_9)=(1,1,2,4,9,19,45,106,267,685).
\]

The first nonisomorphic \(C^2\)-equivalent pseudoforests occur at six vertices, and the unique such unordered pair at that order is \(C_6\) versus \(C_3\sqcup C_3\). In particular, every pair of connected unicyclic graphs indistinguishable by \(C^2\) is isomorphic (the equivalence here is relative to the class of connected unicyclic graphs, not against arbitrary graphs).

## Assumptions and scope

A tree may have one vertex. Each connected unicyclic graph consists of a simple cycle of length at least three, with an attached rooted tree at every cycle vertex; the root is the cycle vertex. Its **decorated cyclic word** lists those rooted trees in cyclic order, modulo reversal. Write its least rotational period as a primitive word of length \(p\) repeated \(k\) times. Let the **bracelet invariant** \(b_\beta(G)\) be the sum of these repetition numbers \(k\) over all unicyclic components with primitive decorated bracelet \(\beta\). Let \(t_T(G)\) count the tree components isomorphic to \(T\in\mathfrak T\).

The exact equivalence criterion is

\[
 G\equiv_{C^2}H\quad\Longleftrightarrow\quad
 t_T(G)=t_T(H)\ \text{for every }T\in\mathfrak T,
 \quad b_\beta(G)=b_\beta(H)\ \text{for every }\beta\in\mathfrak B.
\]

The symbols \(C_n\) refer to ordinary simple undirected cycles; disjoint union is \(\sqcup\). No connectivity, colour predicates, edge orientations, counting restrictions, or order bound are added to the logic. The empty graph is included; omitting it deletes only the constant term of the series.

## Proof

**1. Refinement and rooted universal covers.** Initialize every vertex with the same colour. At round \(d+1\), replace a vertex's colour by its round-\(d\) colour together with the multiset of neighbours' round-\(d\) colours, using a common palette across compared graphs. The round-\(d\) colour equals the isomorphism type of the rooted universal cover truncated at depth \(d\). This is the standard inductive colour-refinement/cover correspondence [1, Lemma 2.6]. For finite graphs, two stable colour histograms agree if and only if the multisets of complete rooted universal-cover types agree: a discrepancy between complete rooted types appears at some finite truncation depth, and finitely many vertices admit a common finite depth separating every distinct type. By the Immerman–Lander equivalence, stated in [2, Section 1], stable colour histograms agree precisely for \(C^2\)-equivalent graphs.

**2. Tree components.** A tree's universal cover is itself. Thus a vertex in a tree component gives a finite rooted-cover type, while vertices in unicyclic components give infinite rooted-cover types. A finite rooted-cover type determines the complete unrooted tree component and the vertex orbit within it. Consequently, the histogram of finite rooted types determines, and is determined by, all values \(t_T(G)\).

**3. Unicyclic components.** The universal cover of a finite unicyclic graph is a tree with exactly two infinite ends. There is a unique bi-infinite path, its **spine**; all connected subtrees hanging from it are finite. These subtrees, rooted at their spine attachment vertices, form a bi-infinite periodic word over \(\mathfrak R\). The period word is exactly the cyclic rooted-tree decoration of the original cycle, repeated in both directions. Every isomorphism of rooted covers preserves the spine setwise, and its action on the spine is a shift or a shift followed by reflection. Therefore the rooted-cover type determines the primitive decorated bracelet \(\beta\), and whether the root lies on the spine. Distinct primitive bracelets never give the same rooted-cover type, even for roots off the spine.

For a fixed bracelet \(\beta\) of length \(p\), each repetition of the primitive word contributes exactly the same multiset of rooted universal-cover types (including all vertices in the attached trees). Indeed, lifting the decorated cycle to the bi-infinite line repeats all decorations without recording the finite cycle's number of periods. A component with cycle word equal to the \(k\)-fold repetition contributes \(k\) times this basic multiset, regardless of \(k\). In particular, counting rooted-cover types whose root is on the spine gives exactly \(p\,b_\beta(G)\) such vertices. Hence histogram equality forces equality of each \(b_\beta\), and equality of all repetition totals conversely forces equality of the entire histogram from unicyclic components. Together with Step 2 this proves the equivalence criterion.

**4. Exact generating function.** For each unrooted tree type \(T\), its multiplicity may be any nonnegative integer, giving \((1-z^{|T|})^{-1}\). For each primitive bracelet \(\beta\) with length \(p\), a simple cycle must contain at least three cycle vertices, so its repetition number is at least \(r(\beta)=\max\{1,\lceil3/p\rceil\}\). The total \(b_\beta\) is either zero or any integer at least \(r(\beta)\): any permitted positive total is realized by a single cycle with that many periods. A repeated period contributes \(w(\beta)\) vertices. Its factor therefore is exactly \(1+\sum_{k\ge r(\beta)}z^{kw(\beta)}\). The tree multiplicities and bracelet totals vary independently. Multiplication of all their factors gives the formula.

**5. Sharp first collision.** With at most five vertices, no bracelet can occur in two separate unicyclic components: each would contain at least three cycle vertices. Thus each nonzero bracelet total comes from one component, whose number of repetitions is fixed, and tree multiplicities are also fixed. Hence the invariant identifies every pseudoforest through order five. At six vertices, \(C_6\) and \(C_3\sqcup C_3\) both have the same unique primitive one-letter bracelet, consisting of the single rooted vertex, with total repetition six. They are nonisomorphic. The only possible ambiguity at order six arises by splitting a total repetition into two legal cycle components; this forces two bare triangles (or one bare six-cycle), proving uniqueness.

## Verification

Two separate finite calculations accompany the statement. `pseudo_count.py` enumerates rooted/unrooted trees and primitive bracelets, multiplies the exact formal-series factors through degree nine, and independently compares the result against the complete NetworkX graph atlas through order seven. `pseudo_verify_independent.py` instead constructs *every* pseudoforest isomorphism type through nine vertices from arbitrary (possibly periodic) decorated cycle bracelets and tree components, computes their colour-refinement classes, and checks all ten coefficients. The first implementation obtains \((1,1,2,4,9,19,45,106,267,685)\); the second matches those numbers and independently counts \((1,1,2,4,9,19,46,108,273,696)\) isomorphism types. Run with Python 3 and NetworkX (see `requirements.txt`). The all-size assertion is proved above; computations are independent finite corroboration, not a substitute for it.

## Relationship to prior work

Krebs and Verbitsky [1] prove the correspondence between colour-refinement colours and truncated universal covers, and investigate the depth needed to detect different covers. Arvind, Köbler, Rattan and Verbitsky [2] discuss the equivalence of colour refinement, two-variable counting logic and fractional isomorphism, and characterize globally identifiable graphs. These established statements are used as inputs. Neither inspected treatment supplies the pseudoforest-specific primitive-bracelet class invariant, its exact formal product, or its enumerated coefficients. The new step is the full two-ended-cover decomposition and the enumeration of distinct finite simple-graph realizations, including the special minimum-period restrictions for one- and two-letter primitive bracelets.

## Limitations

The equivalence criterion is relative to pseudoforests; it does not assert identification against graphs having more than one cycle in a component. The enumeration uses ordinary, uncoloured, simple graphs; adding predicates, orientations, loops or parallel edges changes the invariant. The numerical coefficients are verified only through order nine, although the product identity is all-order. An earlier specialized classification not located in the inspected sources could diminish priority. No independent audit has been performed.

## References

1. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first publicly posted 11 July 2014, especially Section 2 and Lemma 2.6. https://arxiv.org/abs/1407.3175
2. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first publicly posted 4 February 2015, especially Sections 1–2 and the amenability comparison. https://arxiv.org/abs/1502.01255
