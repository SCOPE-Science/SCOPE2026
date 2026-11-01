# The complete \(S_3\times S_4\) homology character of the \(K_{3,4}\) Morse complex

## Finding
Let \(X=\mathfrak M(K_{3,4})\) denote the **ordinary discrete Morse complex** of the simple complete bipartite graph with parts of three and four vertices. The full graph automorphism group \(G=S_3\times S_4\) acts on its rational homology. The only nonzero reduced rational homology is \(\widetilde H_5(X;\mathbb Q)\), of dimension \(432\). Its **complete character** is the following matrix. Row labels are cycle types in \(S_3\); column labels are cycle types in \(S_4\), in the indicated order.

| Cycle type in \(S_3\) / \(S_4\) | \((1,1,1,1)\) | \((2,1,1)\) | \((2,2)\) | \((3,1)\) | \((4)\) |
|---|---:|---:|---:|---:|---:|
| \((1,1,1)\) | 432 | -16 | 4 | 0 | -2 |
| \((2,1)\) | 0 | 0 | 4 | 0 | -2 |
| \((3)\) | -3 | -1 | 1 | -3 | 1 |

As a rational \(G\)-module this is the direct sum \(\bigoplus_{\lambda\vdash3,\,\mu\vdash4}(S^\lambda\boxtimes S^\mu)^{\oplus m_{\lambda,\mu}}\), with these complete multiplicities:

| Irreducible shape \(\lambda\) / \(\mu\) | \((4)\) | \((3,1)\) | \((2,2)\) | \((2,1,1)\) | \((1,1,1,1)\) |
|---|---:|---:|---:|---:|---:|
| \((3)\) | 2 | 8 | 7 | 9 | 4 |
| \((2,1)\) | 5 | 17 | 12 | 19 | 8 |
| \((1,1,1)\) | 2 | 8 | 6 | 10 | 3 |

Every one of the fifteen irreducibles appears. In particular, \(\dim\widetilde H_5(X;\mathbb Q)^G=2\). The previously known nonequivariant wedge of 432 five-spheres is **not** claimed as new; the new claim is its full group action.

## Assumptions and scope
The labeled vertex set is \(A=\{0,1,2\}\) and \(B=\{3,4,5,6\}\), with exactly all edges joining opposite parts. A vertex of \(X\) is a directed incidence \(u\to v\), one of 24 arcs. A set of arcs forms a simplex exactly when every tail appears at most once and the directed arcs have no directed cycles; these are rooted forests with arcs directed toward the roots. The group \(S_3\times S_4\) permutes the labels within the parts and therefore acts on this complex. Integral homotopy type was proved previously; only the rational equivariant statement is investigated here.

## Proof
**Finite complex and homology concentration.** Each graph vertex chooses either no parent or one of its neighbors; there are exactly \(5^3\cdot4^4=32000\) candidate assignments. Reject assignments containing a directed cycle, keep each nonempty set of chosen arcs, and orient faces by increasing arc index sorted first by tail, then head. Exhaustive acyclic-state enumeration gives the face counts in dimensions zero through five
\[
(24,234,1192,3357,4968,3024).
\]
Independently, Chari–Joswig's rooted-forest interpretation and the matrix-forest theorem yield the generating polynomial for the number of rooted forests with \(k\) selected arcs as the coefficient of \(t^{7-k}\) in
\[
\det(tI+L)=t(t+3)^3(t+4)^2(t+7),
\]
using the Laplacian eigenvalues \(0,3,3,3,4,4,7\). This independently gives the same six face counts.

For each simplicial boundary, construct columns from the full signed simplicial incidence matrices, reduce them modulo two, and perform exact bit-vector elimination. Boundary ranks for maps from dimensions one through five are, respectively,
\[
(23,211,981,2376,2592).
\]
The complex is connected because the first boundary has rank 23 on 24 vertices. Over \(\mathbb Q\), every boundary rank is at least its rank modulo two; the chain identity \(\partial^2=0\) forces each pair of consecutive ranks to sum to at most the intervening chain dimension. Starting from the first rank (at most 23), the listed ranks **saturate** every such upper bound: \(23+211=234\), \(211+981=1192\), \(981+2376=3357\), \(2376+2592=4968\). Thus these are also the exact rational ranks. Consequently only reduced rational degree five survives, and its dimension is \(3024-2592=432\).

**Complete symmetry trace.** Enumerate all \(3!4!=144\) bipartition-preserving vertex permutations. An automorphism sends the arc \(u\to v\) to the arc \(g(u)\to g(v)\). For a fixed simplex, the simplicial trace is the sign of the induced permutation of its ordered arcs; for nonfixed simplices its diagonal trace is zero. Thus an exact finite sum of signed fixed simplices computes the ordinary Lefschetz number
\[
L(g)=\sum_{d=0}^{5}(-1)^d\operatorname{tr}(g\mid C_d(X;\mathbb Q)).
\]
Since the only rational homology groups are \(H_0\cong\mathbb Q\) and \(H_5\cong\mathbb Q^{432}\), the sought top-homology character satisfies \(\chi_5(g)=1-L(g)\). The resulting values are constant on all 15 conjugacy classes and give the first displayed matrix. This is an exact proof for the entire 144-element group, not finite sampling of an infinite family.

**Irreducible decomposition.** For each Specht character \(\chi^\lambda\) of \(S_3\) and \(\chi^\mu\) of \(S_4\), compute the exact inner product
\[
m_{\lambda,\mu}=\frac1{144}\sum_{(g,h)\in S_3\times S_4}\chi_5(g,h)\chi^\lambda(g)\chi^\mu(h).
\]
The character tables are integer-valued and the calculation gives the second matrix. Its entries are nonnegative integers; multiplying each multiplicity by the corresponding Specht dimension gives a total of \(432\), as required. The trivial representation occurs with multiplicity two, proving the stated invariant dimension.

## Verification
The self-contained Python 3 standard-library program `verify.py`, included in this package, reconstructs all faces from the defining parent assignments, performs the full exact mod-two boundary-rank eliminations, computes the signed Lefschetz traces for all 144 group elements, asserts the 15 class values, and computes the 15 Specht multiplicities by exact character inner products. Run `python3 verify.py` in the directory containing the extracted files. Its actual recorded output appears in `VERIFICATION_OUTPUT.txt` and ends with `VERIFY_OK`. The procedure does **not** infer an infinite statement from a finite sample; the theorem concerns the explicitly specified finite simplicial complex and its entire finite symmetry group.

## Relationship to prior work
Chari and Joswig's original 2000 paper introduced the graph Morse/rooted-forest interpretation (Proposition 3.1) and the Laplacian face-count connection (Corollary 3.3). It did not present this \(K_{3,4}\) group character. An already published, exact same-object result established \(\mathfrak M(K_{3,4})\simeq\bigvee^{432}S^5\), together with an integral Morse cancellation certificate; the 432 count and homotopy type are therefore expressly **prior knowledge**. That statement alone cannot determine the 15 character values or which irreducible modules occur. Published automorphism-character calculations for the different graphs \(K_{3,3}\) and \(K_{2,4}\), and a balanced-bipartite family, have different simplicial complexes and dimensions; restriction between group representations does not convert one graph complex into another. Searches for the exact parameter and the aliases "rooted-forest complex", "graph Morse complex", and "acyclic discrete vector fields" found no covering published statement. The residual possibility of an equivalent unindexed classification remains.

## Limitations
The result is rational and equivariant, not a classification of the integral \(G\)-lattice, modular characters, or all \(K_{m,n}\). The finite checks are exhaustive and independently executable, but no external independent mathematical audit is claimed. An equivalent theorem in unindexed rooted-forest representation literature could alter the priority assessment. The previously published 432-sphere wedge and all its nonequivariant consequences are not claimed as new.

## References
1. M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234 (first public 2000-11-28), Proposition 3.1 and Corollary 3.3, https://arxiv.org/html/math/0011234v1.
2. *The Morse complex of \(K_{3,4}\) is a wedge of 432 five-spheres*, published research record `48c1007aa5a6`, same-graph prior homotopy theorem.
3. *Complete rational automorphism character of the \(K_{3,3}\) Morse complex*, published record `a7fb33590838`, different graph parameter.
4. *Full \(S_2\times S_4\) homology representation of the \(K_{2,4}\) Morse complex*, published record `36f4259fda88`, different graph parameter.
5. *Equivariant top homology of balanced complete-bipartite Morse complexes*, published record `9305780d4d4c`, different parameter regime.
