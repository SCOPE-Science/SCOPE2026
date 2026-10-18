# Three-anchor Pasch detection and blockwise blindness in Steiner incidence graphs

## Finding

**Blockwise blindness.** Let \(D=(V,\mathcal B)\) be any nontrivial simple Steiner \(2\)-design with parameters \(S(2,k,v)\), where \(3\le k<v\). Form the point-block incidence graph \(I(D)\) with two unary predicates distinguishing points from blocks. Give \(t\) distinct points separate, named unary colours, with \(0\le t\le k\), under the sole restriction that the marked points lie in a common block. Every two such coloured incidence graphs with the same \((v,k,t)\) are equivalent under two-variable first-order logic with counting, \(C^2\). In particular, even naming **every point of one block** conveys no information about the design beyond its parameters to \(C^2\).

**Sharp three-point threshold for Steiner triple systems.** If three separately marked points \(a,b,c\) of an \(S(2,3,v)\) are noncollinear, write \(x_{ab}\), \(x_{ac}\), \(x_{bc}\) for the unique third points on their respective pair blocks. There is a fixed \(C^2\) sentence of quantifier rank four that holds precisely when \(\{x_{ab},x_{ac},x_{bc}\}\) is a block, equivalently when these six points and four blocks form a Pasch configuration.

This threshold is attained by two explicit nonisomorphic Steiner triple systems of order fifteen: the projective \(\mathrm{PG}(3,2)\) triple system and a Bose triple system on \(\mathbb Z_5\times\mathbb Z_3\). Any choices of at most two separately marked points in these systems yield \(C^2\)-equivalent incidence graphs; any three marked collinear points also yield equivalent incidence graphs. For any noncollinear marked triples the projective and Bose systems agree on \(C^2\) sentences of quantifier rank at most three but are separated by the Pasch sentence of rank four. Thus the least number of point landmarks needed for this pair to be distinguished by \(C^2\) is **three**, and the least sentence quantifier rank with three noncollinear landmarks is **four**.

## Assumptions and scope

All structures are finite; the incidence graphs are simple, undirected, and bipartite with the point/block sorts named. The marked point predicates are pairwise disjoint singleton sets, and the comparison respects their order. A Steiner \(S(2,k,v)\) design is a set of \(k\)-subsets (blocks) of a \(v\)-point set in which each unordered pair of distinct points belongs to exactly one block. Nontrivial means \(v>k\). Put \(r=(v-1)/(k-1)\) and \(b=vr/k\): every point lies on \(r\) blocks and there are \(b\) blocks. All logic comparisons are among arbitrary finite vertex-coloured graphs in the same signature, not just among Steiner designs; only the two **input** witnesses need be designs.

The Pasch test is asserted for three **noncollinear** points. Its minimum-rank statement is specific to the two displayed order-fifteen systems; no assertion is made about an optimal quantifier rank for arbitrary designs. The blockwise result does not imply that marking points not contained in a common block is uninformative.

## Proof

### An equitable partition valid for every collinear marking

Choose a block \(B_0\) containing the \(t\) distinctly marked points \(a_1,\ldots,a_t\), and write \(U=B_0\setminus\{a_1,\ldots,a_t\}\), \(W=V\setminus B_0\). Partition point vertices into the named singletons, the unmarked set \(U\) if nonempty, and \(W\). When \(t=0\), no point receives a landmark colour, but one may still choose any auxiliary block \(B_0\) for this equitable partition. Partition block vertices into \(\{B_0\}\); the \(t\) classes \(A_i\) of blocks other than \(B_0\) through \(a_i\); the class \(A_U\) of blocks other than \(B_0\) meeting \(U\), when \(U\ne\varnothing\); and \(A_W\), the blocks disjoint from \(B_0\). Discard any empty cells.

The pair-uniqueness axiom implies every block other than \(B_0\) meets \(B_0\) in at most one point. Consequently these are disjoint block classes of sizes
\[
|\{B_0\}|=1,\qquad |A_i|=r-1,\qquad |A_U|=(k-t)(r-1),\qquad |A_W|=b-1-k(r-1).
\]
The point-class sizes are \(1\) for every named point, \(k-t\) for \(U\), and \(v-k\) for \(W\).

The complete nonzero cross-incidence counts are as follows. Each \(a_i\) meets \(B_0\) once and meets \(A_i\) exactly \(r-1\) times. Each point of \(U\) meets \(B_0\) once and \(A_U\) exactly \(r-1\) times. Every point of \(W\) meets each \(A_i\) once, meets \(A_U\) exactly \(k-t\) times, and meets \(A_W\) exactly \(r-k\) times. In the opposite direction, \(B_0\) meets every named point once and meets \(U\) in \(k-t\) points; every block of \(A_i\) meets \(a_i\) once and \(W\) in \(k-1\) points; every block of \(A_U\) meets \(U\) once and \(W\) in \(k-1\) points; every block of \(A_W\) meets \(W\) in \(k\) points. Same-side incidences are zero.

These sizes and degrees depend only on \((v,k,t)\). Thus the displayed partition is colour-compatible and equitable in every design with those parameters. Running simultaneous colour refinement on the disjoint union of two such incidence graphs cannot separate their vertex-colour multiplicities: inductively, each displayed cell receives a common refinement colour and has the same size in both structures. The standard equivalence of colour refinement and \(C^2\)-equivalence proves blockwise blindness.

### The rank-four Pasch sentence

For distinct marked labels \(i,j\in\{a,b,c\}\), let \(\lambda_{ij}(x)\) mean that \(x\) is a block adjacent to the unique marked \(i\)-point and the unique marked \(j\)-point. This is a two-variable formula of quantifier rank one, written as the conjunction of two separately bound one-neighbour existential clauses. Let \(\tau_{ij}(y)\) mean that \(y\) is a point other than those two markers and has a neighbour satisfying \(\lambda_{ij}\). This is a two-variable formula of rank two. Pair-uniqueness makes \(\tau_{ij}\) select precisely \(x_{ij}\).

With the two variable symbols recycled in nested subformulas, the sentence
\[
\Phi:=\exists x\Bigl(\mathrm{Block}(x)\wedge \bigwedge_{ij\in\{ab,ac,bc\}}\exists y\bigl(R(x,y)\wedge\tau_{ij}(y)\bigr)\Bigr)
\]
is in \(C^2\) and has quantifier rank four. Because the marked triple is noncollinear, the three completion points are distinct and are none of the anchors. The sentence says exactly that those three points form a block. Their three pair blocks plus this fourth block form a Pasch configuration, and conversely.

### The projective and Bose order-fifteen witnesses

For the projective witness take the fifteen nonzero vectors of \(\mathbb F_2^4\), with all thirty-five blocks \(\{u,v,u+v\}\) for distinct nonzero \(u,v\). If \(a,b,c\) are not collinear then they are linearly independent, and their pair-completion points \(a+b,a+c,b+c\) sum to zero. Thus **every** noncollinear marked triple in the projective witness passes \(\Phi\).

For the Bose witness take points \(\mathbb Z_5\times\mathbb Z_3\) and the five vertical blocks \(\{(x,0),(x,1),(x,2)\}\), together with, for each unordered pair \(x\ne y\) and each \(i\in\mathbb Z_3\), the block
\[
\bigl\{(x,i),(y,i),(3(x+y)\bmod5,\ i+1\bmod3)\bigr\}.
\]
The factor \(3\) is the inverse of \(2\) modulo five. The two verification programs perform independent exact finite enumerations: both systems have thirty-five distinct three-point blocks and cover all 105 point pairs exactly once; the projective system has 105 four-block Pasch configurations (equivalently 420 noncollinear anchored triples witnessing them), whereas the Bose system has none. Every one of the 455 triples of points is considered, so this is a finite exhaustive check, not extrapolation. In particular \(\Phi\) is false for every noncollinear Bose triple.

To obtain the **rank lower bound**, start colour refinement with point/block sorts and three separately marked noncollinear points. At round one each of the three blocks through a marked pair becomes separately recognisable. At round two their three unmarked third points become separately recognisable; all other unmarked points remain in one common class. More explicitly, the three one-anchor block classes each have size \(r-2\), and the no-anchor block class has size \(b-3-3(r-2)\); the three pair-anchor block classes are singletons. The point classes at round two are the three anchor singletons, the three pair-completion singletons, and the \(v-6\) other points. These multiplicities and all colours through round two depend only on \((v,3)\), not on whether there is a Pasch block. Thus no \(C^2\) **sentence** of quantifier rank at most three distinguishes the projective and Bose witnesses under noncollinear marking. At round three a block sees all three separately coloured completion points precisely in the projective case, yielding the rank-four separator \(\Phi\).

## Verification

Run the included Python-standard-library programs using `python verify_steiner.py` and `python verify_invariant.py`. The first independently constructs both thirty-five-block systems, checks all 105 point-pair occurrences, exhaustively checks all 455 point triples, verifies \(C^2\)-equivalence with zero, one, and two marked points for every choice in both systems, and confirms that noncollinear three-marked profiles first disagree at colour-refinement round three. The second enumerates all \(\binom{35}{4}=52360\) four-block combinations separately for each system and independently checks the equitable degree matrices for every permitted one-, two-, and three-point collinear marking. Detailed recorded outputs are in `VERIFICATION.md`.

These finite calculations certify the explicit fifteen-point examples. The theorem for all design parameters follows instead from the symbolic equitable-partition argument and does not depend on extrapolating those calculations.

## Relationship to prior work

Kiefer, Schweitzer and Selman (arXiv:1503.08792, first public 2015-03-30) develop the general \(C^2\) framework, equitable partitions, and structural identifiability. Arvind, Köbler, Rattan and Verbitsky (arXiv:1502.01255, first public 2015-02-04) analyze colour refinement, equitable partitions, and individualization. Both provide the logical tools used here, but neither inspected treatment states the all-parameter blockwise blindness theorem or the sharp order-fifteen three-anchor Pasch/rank-four boundary. Ling, Colbourn, Grannell and Griggs (2000) develop anti-Pasch Steiner triple systems; their publication is a combinatorial source of context, not a counting-logic classification. The specific Bose witness here is supplied and checked independently, without appealing to an inaccessible construction proof.

The result concerns fifteen-point Steiner *triple systems* (a projective three-dimensional binary geometry and a Bose system), not the incidence graphs of projective **planes**: previous analyses of three noncollinear landmarks in projective-plane Levi graphs do not determine these statements. The general equitable machinery can be specialized to designs only after proving the incidence table above; general amenability criteria do not contain the claimed landmark threshold as a stated result.

## Limitations

The originality assessment is literature-based and not an independence claim. Some specialized earlier work may contain the same design-specific colour-refinement calculation. The 2000 anti-Pasch construction paper was available at bibliographic/abstract level during comparison, but a full-text access request could not be completed without user intervention. This leaves a bounded priority risk, especially for combinatorial properties of the Bose witness, although its \(C^2\) threshold is not indicated by the accessible abstract. No result is claimed for arbitrary marking sets outside a block beyond the three-anchor Pasch test, nor for unrestricted higher-dimensional Weisfeiler–Leman logic. Independent mathematical validation has not been performed.

## References

1. A. C. H. Ling, C. J. Colbourn, M. J. Grannell and T. S. Griggs, "Construction Techniques for Anti-Pasch Steiner Triple Systems," *Journal of the London Mathematical Society* 61 (2000), 641–657. DOI: 10.1112/S0024610700008838. First public date verified: 2000-06-01 (publisher record).
2. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, "Graph Isomorphism, Color Refinement, and Compactness," arXiv:1502.01255, first public 2015-02-04. https://arxiv.org/abs/1502.01255
3. S. Kiefer, P. Schweitzer and E. Selman, "Graphs Identified by Logics with Counting," arXiv:1503.08792, first public 2015-03-30. https://arxiv.org/abs/1503.08792
