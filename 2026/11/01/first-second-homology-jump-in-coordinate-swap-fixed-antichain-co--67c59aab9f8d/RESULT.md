# First second-homology jump in coordinate-swap fixed antichain complexes

## Finding
Let \(P_n=[n]\times[n]\) with coordinatewise order, let \(X_n\) be its antichain complex, and let \(\tau(i,j)=(j,i)\). Write \(F_n=|X_n|^{\langle\tau\rangle}\) for the **actual geometric fixed-point space**, not the vertexwise fixed induced subcomplex.

**Theorem.** For every \(n\ge3\), the fixed-point space \(F_n\) has exactly five connected components. Its canonical orbit-simplex triangulation has
\[
f_{r-1}(F_n)=\binom n{2r-1}+\binom n{2r}\qquad(r\ge1),
\]
where out-of-range binomial coefficients are zero. Hence \(\chi(F_n)=1+\operatorname{Im}(1+i)^n-\operatorname{Re}(1+i)^n\). Moreover, the first nonzero second integral homology occurs at \(n=8\):
\[
\widetilde H_2(F_n;\mathbb Z)=0\quad(1\le n\le7),\qquad
\widetilde H_2(F_8;\mathbb Z)\cong\mathbb Z^8.
\]
The entire reduced integral homology at this first threshold is
\[
\widetilde H_j(F_8;\mathbb Z)\cong
\begin{cases}\mathbb Z^4&j=0,\\\mathbb Z^{28}&j=1,\\\mathbb Z^8&j=2,\\0&\text{otherwise}.\end{cases}
\]
No claim is made here about the higher homology or homotopy type for arbitrary \(n>8\).

## Assumptions and scope
The antichain complex has as vertices the \(n^2\) elements of the product poset and as simplices its pairwise incomparable subsets. A geometric simplex is fixed by \(\tau\) precisely when its barycentric coordinate is constant along every occupied two-element orbit. Accordingly each admissible orbit supplies **one vertex** of a canonical triangulation of the fixed set. This construction works over the real geometric realization and does not confuse fixed geometric points with pointwise-fixed original vertices.

## Proof
There are two kinds of vertex orbits: \(d_k=\{(k,k)\}\) and \(p_{ij}=\{(i,j),(j,i)\}\), with \(1\le i<j\le n\). Each is internally an antichain. Two diagonal vertices are incompatible. The diagonal \(d_k\) is compatible with \(p_{ij}\) if and only if \(i<k<j\). Two distinct pair vertices \(p_{ij}\) and \(p_{ab}\) are compatible precisely when \(i<a<b<j\) or \(a<i<j<b\). These conditions follow by checking all cross-orbit coordinatewise comparabilities.

Thus any fixed simplex consists of a strictly nested sequence of endpoint pairs, optionally with a single diagonal orbit strictly inside its smallest interval. Associating the ordered endpoints, together with the optional central index, gives a bijection from its \(r\)-vertex faces to the \((2r)\)- and \((2r-1)\)-subsets of \([n]\). This proves the face-number formula. Alternating the face counts and using the binomial theorem gives the Euler-characteristic identity.

For \(n\ge3\), the four vertices \(d_1,d_n,p_{1,2},p_{n-1,n}\) are isolated. Every other diagonal vertex, and every pair with both endpoints strictly interior, is directly adjacent to \(p_{1,n}\). Any other nonisolated pair beginning at \(1\) or ending at \(n\) connects through an interior diagonal orbit to \(p_{1,n}\). Hence the other vertices form exactly one connected component.

For the integral computation, order each face lexicographically by its orbit-vertex labels. In the ordinary integral simplicial chain group, define the boundary of an oriented \(q\)-simplex by
\[
\partial_q[v_0,\ldots,v_q]=\sum_{a=0}^{q}(-1)^a[v_0,\ldots,\widehat v_a,\ldots,v_q].
\]
The accompanying independent finite verifier constructs the orbit-compatibility graph from the above coordinate inequalities, exhaustively enumerates **all** simplices for each \(3\le n\le8\), constructs these exact integer boundary matrices, and calculates their Smith normal forms over \(\mathbb Z\). For every checked matrix all nonzero Smith invariant factors are \(1\). The ranks, with columns \(\operatorname{rank}\partial_1,\operatorname{rank}\partial_2,\operatorname{rank}\partial_3\), are:

| \(n\) | Face counts by dimension | Boundary ranks |
|---|---|---|
| 3 | \((6,1)\) | \((1,0,0)\) |
| 4 | \((10,5)\) | \((5,0,0)\) |
| 5 | \((15,15,1)\) | \((10,1,0)\) |
| 6 | \((21,35,7)\) | \((16,7,0)\) |
| 7 | \((28,70,28,1)\) | \((23,27,1)\) |
| 8 | \((36,126,84,9)\) | \((31,67,9)\) |

Every boundary satisfies \(\partial_{q-1}\partial_q=0\) by the simplicial identity. The Smith factors \(1\) ensure that images are primitive subgroups of the ambient free chain groups; hence their quotients inside the cycle groups have no torsion. The chain-group ranks and boundary ranks therefore determine integral homology. At \(n=8\), \(84-67-9=8\) gives the second Betti number and \(126-31-67=28\) gives the first. At \(n=5,6,7\), the same calculation gives \(\widetilde H_2=0\); at \(n=1,2,3,4\), there are no nonzero second homology classes by the absence of two-dimensional cycles. This establishes the claimed first threshold.

## Verification
Run `python3 verify_grid_fixed.py` using Python 3 with SymPy 1.14 or a compatible SymPy version. The program reconstructs the orbit graph without relying on precomputed simplex tables, compares every dimension's face count with the binomial formula, checks the full count \(2^n-1\), performs independent mod-two elimination, and then computes every nonzero integer Smith factor. Expected final line: `PASS complete`. A finite calculation verifies the specific claimed cutoff, not any unproved all-orders Betti formula.

## Relationship to prior work
Barik, Mondal and Mukherjee (arXiv:2604.12606; first public version April 14, 2026) give a recursive acyclic-matching construction for independence complexes of comparability graphs of rectangular grid posets and their clique blow-ups. That nonequivariant homotopy framework motivates examining the natural coordinate-exchange symmetry in the square case. Its stated results concern the original antichain complex, not the geometric fixed-point subset; the latter is made from admissible orbit barycenters and is a different simplicial complex. The present result supplies the precise geometric fixed model and the first appearance of nontrivial two-dimensional integral fixed-locus homology. Generic tools for equivariant poset topology do not supply these concrete ranks without analysis.

## Limitations
The cutoff calculation is exhaustive only for \(n\le8\). Higher-order patterns suggested by finite data are **not** asserted. The result is an integral homology statement, not a claim that the fixed locus is a wedge of spheres. The computational verification requires SymPy's exact Smith-normal-form implementation; independent external mathematical review has not occurred. A semantically equivalent unindexed computation may exist.

## References
- Sucharita Barik, Anupam Mondal, Sajal Mukherjee, *A recursive construction of an acyclic matching on the independence complex of a graph with a simplicial vertex*, arXiv:2604.12606, first posted 2026-04-14, https://arxiv.org/abs/2604.12606.
- Michelle L. Wachs, *Poset Topology: Tools and Applications*, 2006, https://sites.math.duke.edu/~ezra/PCMI2004/wachs.jcp.pdf (general order-complex background, not a claimed direct comparison for the calculated fixed locus).
