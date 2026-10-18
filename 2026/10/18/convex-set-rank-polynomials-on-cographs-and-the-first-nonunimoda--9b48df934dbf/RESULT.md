# Convex-set rank polynomials on cographs and the first nonunimodal induced-path convex geometry

## Finding
For every finite simple cograph \(G\), the entire rank-generating polynomial
\[
 F_G(z)=\sum_{S\in\mathcal C_2(G)}z^{|S|}
\]
of its induced-length-two-path closure system admits an explicit polynomial-time cotree recursion (formulas below). Here \(\mathcal C_2(G)\) consists of the vertex sets containing the middle vertex of every *induced* three-vertex path whose endpoints they contain. The recurrence uses simultaneously the clique polynomial \(K_G(z)\) and the two standard cograph operations, disjoint union and complete join. It computes all coefficients in \(O(n^2)\) integer arithmetic operations from a binary cotree of an \(n\)-vertex cograph (without asserting a quadratic bit-complexity bound).

In the subclass of *trivially perfect graphs*, for which this closure system is a convex geometry, the coefficient sequence of \(F_G\) is unimodal for every graph on at most four vertices. On five vertices, the **only** nonunimodal example up to isomorphism is the star \(K_{1,4}\). More generally, for every \(d\ge1\),
\[
 F_{K_{1,d}}(z)=1+dz+z(1+z)^d;
\]
its coefficient sequence is unimodal exactly for \(d\le3\) and log-concave exactly for \(d\le2\). These last cutoffs are specifically about the size distribution of *induced-path-convex sets*, not the different distribution of ordinary all-path \(P_3\)-convex sets.

## Assumptions and scope
Graphs are finite, simple, undirected, and may be disconnected. The empty set is convex and the empty vertex set is a clique; the associated constant terms are both one. A set \(S\) is convex if for every vertex \(v\notin S\), the neighborhood \(N(v)\cap S\) is a clique; equivalently no induced path with three vertices has its endpoints in \(S\) and its middle vertex outside. The clique polynomial \(K_G(z)=\sum_{S\text{ clique}}z^{|S|}\) includes the empty clique. A cograph is a graph constructed from one-vertex graphs by iterated disjoint unions \(\sqcup\) and complete joins \(\vee\), equivalently a graph without an induced four-vertex path. A trivially perfect graph is a cograph without an induced four-cycle, equivalently a graph built from singleton graphs by disjoint union and adjoining universal vertices.

For a polynomial \(P\) and an integer \(a\ge0\), write \(z^aP\) for a degree shift. For a graph \(X\), let \(e_X\) equal one when \(X\) is complete and zero otherwise. Both operands in the join rule below are nonempty, with orders \(a\) and \(b\). Arithmetic-operation complexity counts exact operations on integer coefficients; no bound is asserted on coefficient bit lengths.

## Proof
**1. Exact recursion.** On the empty graph, \(F_{\varnothing}(z)=K_{\varnothing}(z)=1\). On the one-vertex graph, \(F_{K_1}(z)=K_{K_1}(z)=1+z\). For disjoint nonempty graphs \(A,B\), convexity is componentwise and every nonempty clique lies in one component. Thus
\[
 F_{A\sqcup B}=F_AF_B,\qquad K_{A\sqcup B}=K_A+K_B-1.
\]
In the complete join, a clique is exactly the union of a clique from each side, so \(K_{A\vee B}=K_AK_B\). Define \(D_X=F_X-K_X\), the generating polynomial of convex noncliques of \(X\). We claim the complete join formula
\[
 \boxed{F_{A\vee B}=K_AK_B+e_Bz^bD_A+e_Az^aD_B+(1-e_A)(1-e_B)z^{a+b}.}
\]
Indeed, let \(S=S_A\cup S_B\) be a convex set. Restricting an induced three-vertex path to either side shows that both \(S_A\) and \(S_B\) are convex on their respective sides. If \(S_A\) is a nonclique, it contains nonadjacent vertices \(u,w\); any omitted vertex of \(B\) would be the middle vertex of the induced path \(u,v,w\), so \(S_B=V(B)\). The symmetrical implication applies to a nonclique \(S_B\). If both selected parts are cliques, their union is a clique, accounted for by \(K_AK_B\). If just the selected \(A\)-part is a nonclique, then the selected \(B\)-part is all of \(B\); to have the selected \(B\)-part a clique, \(B\) must be complete. This yields \(e_Bz^bD_A\). The symmetric case yields \(e_Az^aD_B\). If both parts are noncliques, both must be full, requiring both \(A\) and \(B\) noncomplete; this is the unique whole vertex set counted in the last summand. Conversely, each of these four forms has no excluded middle vertex of an induced three-vertex path: the sole possible obstruction is an excluded vertex on the opposite side from nonadjacent selected endpoints, and the cases eliminate it. The four classes are disjoint and exhaustive, proving the formula.

At each binary cotree node, polynomial multiplication of the child coefficient arrays takes \(O(ab)\) exact arithmetic operations for subtree sizes \(a,b\), and addition/shifts/completeness tests take \(O(a+b)\). Summing \(ab\) over internal nodes counts each unordered pair of vertices exactly once, so is \(\binom n2\); summing subtree sizes is \(O(n^2)\). Every coefficient is therefore computable in \(O(n^2)\) arithmetic operations. This is a full rank distribution rather than solely the total number \(F_G(1)\).

**2. Stars and coefficient shapes.** In \(K_{1,d}\), a convex set omitting the center contains at most one leaf; every set containing the center is convex. The former contribute \(1+dz\), the latter contribute \(z(1+z)^d\). Thus the coefficients, in ascending size, are
\[
 1,\ d+1,\ d,\ \binom d2,\ \binom d3,\ldots,\binom d d.
\]
For \(d\ge4\) the strict valley \(d+1>d<\binom d2\) contradicts unimodality. For \(d=1,2,3\), the displayed polynomial is directly unimodal. When \(d\ge3\), log-concavity fails at degree two because \(d^2<(d+1)\binom d2\); for \(d=1,2\) all adjacent log-concavity inequalities hold. This proves both sharp cutoffs.

**3. Minimal nonunimodality within convex geometries.** Trivially perfect graphs are exactly the graphs obtained by disjoint unions and by adjoining universal vertices, so every connected nonempty such graph has a universal vertex. The coefficient sequences for connected examples on at most four vertices follow by taking a universal vertex over one of the four graph types on three vertices. At four vertices their possibilities are
\[
 (1,4,3,3,1),\ (1,4,4,3,1),\ (1,4,5,2,1),\ (1,4,6,4,1),
\]
all unimodal. Disconnected examples are products of the smaller connected polynomials: at four vertices the only noncomplete connected component possible is \(P_3\), giving \((1,3,2,1)(1+z)=(1,4,5,3,1)\); all other disconnected examples have polynomial \((1+z)^4\). Lower orders are immediate.

For connected five-vertex cases, remove one universal vertex, obtaining a four-vertex trivially perfect graph \(H\). There are exactly nine such types, organized by their sorted degree multiset; the coefficient sequences of \(F_{K_1\vee H}\) from the recursion are:

| Degrees of \(H\) | \(F_{K_1\vee H}\) coefficients, ascending |
|:--|:--|
| \((0,0,0,0)\) | \((1,5,4,6,4,1)\) |
| \((0,0,1,1)\) | \((1,5,5,6,4,1)\) |
| \((0,1,1,2)\) | \((1,5,6,5,3,1)\) |
| \((1,1,1,1)\) | \((1,5,6,6,4,1)\) |
| \((0,2,2,2)\) | \((1,5,7,7,4,1)\) |
| \((1,1,1,3)\) | \((1,5,7,3,3,1)\) |
| \((1,2,2,3)\) | \((1,5,8,5,3,1)\) |
| \((2,2,3,3)\) | \((1,5,9,7,2,1)\) |
| \((3,3,3,3)\) | \((1,5,10,10,5,1)\) |

The nine types are precisely the four-vertex graphs other than the induced four-path and four-cycle; these are the eleven ordinary four-vertex simple-graph types minus the two forbidden types. In the table, only the first row is nonunimodal, and it is exactly \(K_{1,4}\). For a disconnected five-vertex trivially perfect graph, there is at most one nonclique connected component: such a component has at least three vertices, and two would require at least six vertices. The remaining components are complete graphs of total order at most two; their convex polynomials are binomial factors \((1+z)^r\), \(r\le2\). Convolution of a nonnegative unimodal sequence with \((1,1)\) is unimodal (the consecutive differences are two-step differences of the original unimodal sequence). Therefore all disconnected cases are unimodal. This proves the claimed first obstruction and uniqueness up to isomorphism.

## Verification
The accompanying standalone `verify.py` implements two independent finite calculations: (i) direct enumeration of every subset and its excluded-middle-vertex test, and (ii) a disjoint-union/complete-join decomposition algorithm for the two polynomials. It checks all labelled cographs on one through six vertices: respectively \(1,2,8,52,472,5504\), totaling \(6039\), and compares every coefficient of both polynomials. Among the \(462\) labelled trivially perfect graphs through five vertices, only five labelled five-vertex graphs have a nonunimodal coefficient sequence; these are the five choices of center for \(K_{1,4}\). The script also tests the star coefficient-shape cutoffs through \(d=11\). Its successful output begins with `VERIFY_OK`. These finite checks are sanity tests; the induction and classification above establish the unlimited-domain claims.

## Relationship to prior work
Gutierrez, Protti, and Tondato (2022) introduced induced-path-length-bounded convexity, including the \(l^2\) closure considered here, and characterized when it is a convex geometry as precisely the trivially perfect graphs. That characterization and the standard cograph operations are existing work. Dourado, Penso, and Rautenbach (2022) studied the hull number for this induced-three-vertex-path closure; a hull-number theorem is not a rank-distribution formula. Dourado, Grippo, Lin, and Protti (2026) studied counting convex sets under the different operation generated by *all* three-vertex paths; unlike induced-path closure, an already-adjacent endpoint pair of a triangle can trigger a path in that different convention. The present contribution is the full induced-path-convex rank-polynomial recursion and the sharp first nonunimodal member of the associated convex-geometric subclass. No existing characterization, clique-polynomial identity, or known total-count formula is asserted as original.

## Limitations
This is an exact counting and coefficient-shape result for cographs and their trivially perfect subclass; no assertion of coefficient unimodality is made for all convex geometries or for arbitrary graphs. The first-obstruction statement is only for the subclass of graph-induced \(l^2\) convex geometries. The stated running time counts polynomial arithmetic operations, not bit complexity. The published-literature comparison is necessarily incomplete, and equivalent earlier closure-polynomial formulas remain a residual priority risk. No independent external validation has been performed.

## References
1. M. Gutierrez, F. Protti, S. B. Tondato, *Convex geometries over induced paths with bounded length*, first publicly submitted 2022-03-10, arXiv:2203.05588v1; later Discrete Mathematics 346 (2023), 113133. https://arxiv.org/abs/2203.05588
2. M. C. Dourado, L. D. Penso, D. Rautenbach, *The hull number in the convexity of induced paths of order 3*, Theoretical Computer Science 906 (2022), 52–63. https://doi.org/10.1016/j.tcs.2022.01.004
3. M. C. Dourado, L. N. Grippo, M. C. Lin, F. Protti, *Counting \(P_3\)-convex sets in graphs*, first publicly submitted 2026-03-05, arXiv:2603.04706. https://arxiv.org/abs/2603.04706
