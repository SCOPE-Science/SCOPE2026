# Three rank-four theories of finite affine planes with named point and line sorts

## Finding
For every two finite affine planes of orders \(q,r\ge2\), with separately named point and line sorts and the incidence relation, agreement on all first-order sentences of quantifier rank at most four is equivalent to
\[\min\{q,4\}=\min\{r,4\}.\]
There are exactly three classes, represented by orders \(2,3,4\), whose universe sizes are \(10,21,36\). The bound \(36\) is optimal, because no plane of smaller order belongs to the third class. No coordinate or Desarguesian assumption is needed.

## Assumptions and scope
A finite affine plane of order \(q\ge2\) has \(q^2\) points, \(q(q+1)\) lines, exactly \(q\) points per line, exactly \(q+1\) lines per point, and \(q+1\) parallel classes of \(q\) lines each. Distinct points determine a unique line; distinct lines are parallel or meet in one point. The language has unary predicates \(P,L\), partitioning the universe, and symmetric incidence \(I\), holding only between unlike sorts. Equality is available. Quantifier rank counts nesting depth, not the number of quantifiers in separate branches. Structures are nonempty. Only orders for which finite affine planes exist are quantified over.

## Proof
**Separation.** For \(k=2,3\), let \(\Phi_k\) assert that \(k\) distinct lines cover all points:
\[\exists\ell_1\cdots\exists\ell_k\,\bigl(\bigwedge_i L(\ell_i)\wedge\bigwedge_{i<j}\ell_i\ne\ell_j\wedge\forall p\,[P(p)\Rightarrow\bigvee_i I(p,\ell_i)]\bigr).\]
Its quantifier rank is \(k+1\). In order \(q=k\), one parallel class has \(q\) lines and covers all \(q^2\) points, so \(\Phi_k\) holds. If \(q>k\), any \(k\) lines cover at most \(kq<q^2\) points, so it fails. Consequently, order \(2\) is distinguished from every larger order at rank three, and order \(3\) is distinguished from all orders at least \(4\) at rank four.

**Uniformity at orders at least four.** We give a four-round Ehrenfeucht–Fraïssé strategy based solely on affine incidence axioms. To an ordered tuple of at most three selected elements attach its *geometric diagram*: sorts, equalities, point–line incidences, parallelism of every pair of selected distinct lines, collinearity when three distinct points have been selected, and concurrency when three distinct lines have been selected. These are auxiliary invariants used in the game, not symbols added to the language.

Two elementary extension facts hold in every affine plane of order \(q\ge4\):

1. For any geometric diagram of length at most two, the set of geometric diagrams achievable by appending a third element depends only on that diagram and not on the plane. Repeated elements present no difficulty. For distinct new elements, the required choices amount to a fresh point on or off a specified line, a line through or avoiding up to two points, a line in or outside specified parallel classes, or a third line concurrent with two intersecting lines (or disjoint from their intersection). Each allowable case has a witness from the incidence axioms. The only possible exclusions are exhausted pencils/parallel classes; a line has \(q\ge4\) points, a point has \(q+1\ge5\) lines, a parallel class has \(q\ge4\) lines, and there are \(q+1\ge5\) different classes.
2. For any geometric diagram of length three, the set of *atomic* (sort, equality and incidence) diagrams achievable by appending a fourth element depends only on the geometric diagram. To find a new line incident with two or three prescribed points, use their unique joining line and the recorded collinearity; to find a new point incident with two or three prescribed lines, use their intersection and recorded concurrency/parallelism. Exactly-one-incidence requests exclude at most two positions from a line or at most two pencils from a point; \(q\ge4\) and \(q+1\ge5\) leave a fresh option. A new point avoiding all selected lines exists because at most three lines cover \(3q<q^2\) points; a new line avoiding all selected points exists because three point-pencils contain at most \(3(q+1)<q(q+1)\) lines. Any selected opposite-sort vertex additionally forbidden by freshness reduces these conservative margins by at most the number of that sort among the three selected vertices: in the respective all-three constraints this number is zero; the mixed cases have at most two forbidden vertices and at most two incidence constraints. Thus the required fresh witnesses remain available. Impossible incidence masks are excluded by the unique joining-line and meeting-point axioms and are recorded by the geometric diagram.

First respond with the same sort; this preserves the one-element geometric diagram. In round two match a geometric diagram of two elements using the first extension fact. In round three match the diagram of three elements by the same fact. In round four use the second fact to match the atomic diagram of the four pebbles. This is a winning strategy for either choice of starting plane, proving rank-four equivalence for all \(q,r\ge4\).

The two separation sentences and this strategy establish both directions. A plane of order four exists over \(\mathbb F_4\), so the third class has a \(36\)-element representative; smaller planes have order at most three and have different rank-four theories, proving sharpness.

## Verification
The accompanying `affine_sorted_check.py` constructs coordinate affine planes of orders \(2,3,4,5\) (using the irreducible polynomial \(t^2+t+1\) for \(\mathbb F_4\)) and computes quantifier-rank types by exact finite recursive extension sets. It returns the signature classes \(0,1,2,2\) and `VERIFY_OK`. The independent geometric-diagram table checker `affine_geom_lemma_check.py` verifies agreement of the auxiliary one-, two-, and three-position extension tables for orders four and five (respectively \(2,9,64\) diagram states), returning `GEO_EXTENSIONS_MATCH`. These are finite consistency checks, not replacements for the general incidence-axiom argument.

## Relationship to prior work
Classical finite affine-plane incidence theory supplies the projective-completion, parallel-class, and unique-joining-line facts; Lazebnik–Mellinger–Vega study cycle embeddings using the same geometry. General Ehrenfeucht–Fraïssé theory supplies the quantifier-rank/game correspondence. Neither cited source states this three-class rank-four classification. Results about *uncoloured projective-plane* incidence graphs do not imply the present claim: both removing a line at infinity and naming the two sorts change the language and its low-rank diagrams.

## Limitations
The theorem concerns exactly the sorted point–line incidence language, not uncoloured Levi graphs, not higher quantifier ranks, and not arbitrary partial linear spaces. The symbolic extension proof is an elementary finite case analysis; the scripts do not prove the universal lemma for non-Desarguesian planes. Independent mathematical checking and a broader literature audit have not been performed.

## References
- Felix Lazebnik, Keith E. Mellinger, Oscar Vega, *Embedding cycles in finite planes*, arXiv:1305.2646 (first submitted 2013-05-12), especially the finite-affine-plane incidence definitions in §1 and geometric constructions in §2. https://arxiv.org/abs/1305.2646
- Yuguo He, *On the strictness of the quantifier structure hierarchy in first-order logic*, arXiv:1409.7488 (2014), background on quantitative Ehrenfeucht–Fraïssé resources; not a source of the present classification. https://arxiv.org/abs/1409.7488
