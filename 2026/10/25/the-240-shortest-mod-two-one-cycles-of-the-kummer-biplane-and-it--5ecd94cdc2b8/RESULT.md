# The 240 shortest mod-two one-cycles of the Kummer biplane and its sharp seven-vertex support threshold

## Finding

Let \(V=\mathbb F_2^4=\mathbb F_2^2\oplus\mathbb F_2^2\). Define \(f(a)=0\) for \(a=0\) and \(f(a)=1\) otherwise, \(q(a,b)=f(a)+f(b)\), and \(D=\{v\in V:q(v)=1\}\). Let \(K\) be the simplicial complex comprising every subset of the sixteen six-point blocks \(u+D\), \(u\in V\). This is the classical Kummer biplane block complex, isomorphic to the Lovász open-neighborhood complex of the four-by-four rook graph.

Define the alternating, nondegenerate form \(B(u,v)=q(u+v)+q(u)+q(v)\). The following statements hold.

1. Of the \(560\) unordered triples of distinct points, exactly \(320\) are two-faces of \(K\), characterized by \(B(x+y,x+z)=1\); the other \(240\) satisfy \(B(x+y,x+z)=0\). Those \(240\) missing triples are precisely the four triples from each of \(60\) affine totally isotropic four-point planes.
2. Every missing triple bounds a three-edge mod-two cycle representing the same **nonzero** class in \(H_1(K;\mathbb F_2)\cong\mathbb F_2\). These are all the shortest nonzero mod-two homology cycles. The affine symplectic group \(V\rtimes\operatorname{Sp}_4(2)\), of order \(11520\), acts transitively on their supports.
3. For every subset \(W\subseteq V\), the inclusion \(H_1(K[W];\mathbb F_2)\to H_1(K;\mathbb F_2)\) is nonzero if and only if \(W\) contains at least one missing triple. The sixteen six-point blocks are **exactly the maximal vertex subsets with zero image**. In particular every seven-point subset supports the nonzero class, while some six-point subsets do not. The enumerator of subsets with zero image is
\[
1+16t+120t^2+320t^3+320t^4+96t^5+16t^6.
\]

## Assumptions and scope

All sums and pairings in formulas defining \(q\), \(B\), and the cocycle below are in \(\mathbb F_2\). The simplicial complex includes the empty face and its full one-skeleton consists of every pair of the sixteen distinct points. \(K[W]\) denotes the vertex-induced subcomplex. A three-edge cycle means the boundary of a three-vertex simplex *not* present in \(K\). The claim concerns homology over \(\mathbb F_2\), not integral shortest-cycle classes; no assertion is made about the other biplanes with the same numerical design parameters.

## Proof

**Design and quadratic form.** The six points of \(D\) are those for which precisely one of the two \(\mathbb F_2^2\) coordinates is nonzero. Its translates are the row-plus-column-minus-center blocks under the grid identification \(V\cong\{0,1,2,3\}^2\). Every pair of distinct blocks intersects in exactly two vertices: this follows from the fact that each nonzero difference of block centers has exactly two presentations as the difference of two elements of \(D\). Thus every pair of vertices lies in precisely two blocks, while a triple lies in at most one block.

The function \(f\) is the two-variable anisotropic quadratic form \(f(s,t)=s+t+st\). Therefore \(B\) is a nondegenerate alternating bilinear form on \(V\). For every triple \(x,y,z\) belonging to a common block, \(B(x+y,x+z)=1\): translating into \(D\), either all three vertices belong to the same nonzero coordinate plane, or two belong to one and the remaining vertex to the other; direct evaluation in both cases gives one. This proves the facial implication. There are \(16\binom 63=320\) facial triples because no triple occurs in two blocks. Conversely, the number of triples with \(B(x+y,x+z)=1\) is \(16\cdot15\cdot8/6=320\): choose the ordered base point \(x\), nonzero \(x+y\), and one of its eight symplectic partners \(x+z\), then divide by six orderings. Thus the two sets coincide and exactly \(\binom{16}3-320=240\) triples are missing.

If \(x,y,z\) is missing, the points \(x,y,z,x+y+z\) form a four-point affine isotropic plane and all its four triples are missing. The assignment from a missing triple to that plane is unique. The number of totally isotropic two-dimensional linear subspaces is \(15\cdot6/6=15\): choose the first nonzero vector in \(15\) ways, the independent vector in its symplectic orthogonal complement in \(6\) ways, and divide by the six ordered bases of a two-dimensional binary space. Each linear plane has four affine cosets. Consequently there are \(60\) planes with four missing triples each, partitioning the \(240\) omitted triples.

**An explicit cohomological detection certificate.** Define the mod-two edge cochain \(\omega(\{x,y\})=1+q(x+y)\). For any distinct triple,
\[
\langle\omega,\partial[x,y,z]\rangle
=(1+q(x+y))+(1+q(x+z))+(1+q(y+z))
=1+B(x+y,x+z).
\]
This vanishes on every actual two-simplex of \(K\), so \(\omega\) is a cocycle; on every missing triangle boundary it evaluates to one. Hence all \(240\) three-edge cycles are nonzero in mod-two first homology. Since the one-skeleton is complete, every nonzero one-cycle has at least three edges. To identify the single ambient class, the reproducible exhaustive rank calculation has \(120\) one-simplices, rank \(15\) for the vertex-edge incidence, and rank \(104\) for the \(120\)-by-\(320\) triangle boundary over \(\mathbb F_2\). Therefore \(\dim H_1(K;\mathbb F_2)=120-15-104=1\). This finite rank certificate is fully regenerated by the attached verifier, which explicitly enumerates every block and triangle; the cocycle proof independently establishes nontriviality.

**Every induced support and the sharp threshold.** If \(W\) contains a missing triple, its boundary already witnesses nonzero ambient homology. If it contains no missing triple, every three vertices of \(W\) span a two-simplex of \(K\), so \(K[W]\) is the complete two-skeleton (and possibly higher faces) on \(W\); since every cycle in the complete one-skeleton is a sum of triangle boundaries, \(H_1(K[W];\mathbb F_2)=0\).

To bound the size of a subset containing no missing triple, take \(x_0\in W\), write its other points as nonzero vectors \(v_1,\ldots,v_m\), and use the triangle characterization to obtain \(B(v_i,v_j)=1\) whenever \(i\ne j\). Their Gram matrix over \(\mathbb F_2\) is \(J_m+I_m\), with rank \(m\) when \(m\) is even and \(m-1\) when \(m\) is odd. Nondegeneracy in dimension four requires this rank to be at most four; hence \(m\le5\), or \(|W|\le6\). Each of the sixteen design blocks has size six and contains only facial triples, so the bound is attained. Any six-point set with no missing triple has six-point block structure: the exhaustive incidence calculation recorded in the verifier finds exactly sixteen such sets, precisely the given blocks. Alternatively, completing any four mutually symplectically paired difference vectors forces the fifth to equal their sum; the count of such six-sets is \(16\). The same exhaustive enumeration over all \(65536\) vertex subsets yields the displayed support enumerator. In particular the sixteen blocks are exactly the maximal noncarriers and all seven-subsets are carriers.

**Symmetry.** Every affine symplectic map preserves the condition \(B(x+y,x+z)=0\), hence permutes missing triples. Since the blocks are exactly the maximal sets without missing triples, each such map also preserves \(K\). The attached verifier enumerates all \(720\) symplectic linear transformations, their sixteen translations, and checks that the orbit of one missing triple consists of all \(240\) omitted triples.

## Verification

Execute `python3 artifacts/verify_kummer.py` using Python 3.9 or newer, with no external dependencies. The script checks the \(2\)-design incidence axioms; enumerates all \(560\) triples; verifies the symplectic characterization and the cochain pairing on each triple; computes the exact binary rank \(104\); enumerates all \(60\) isotropic affine planes, all \(65536\) vertex subsets, and the full \(11520\)-element affine symplectic action. The finite exhaustive checks support only the stated sixteen-point instance. The independent hand derivations above give the structural explanation of the characterization, cocycle, and support threshold.

## Relationship to prior work

The Kummer biplane, its incidence geometry and related graph presentations predate this calculation; White studies biplanes embedded on surfaces, rather than the homology classes carried by three-vertex cycles in the abstract block simplicial complex. Matsushita develops general fundamental-group methods for graph neighborhood complexes. A separately published exact computation of this particular block complex establishes \(K\simeq\mathbb{RP}^2\vee\bigvee^{55}S^2\), so its nonzero mod-two first-homology group is **not** claimed as new. That result alone does not determine which of the \(560\) three-point sets represent the nonzero class, whether those representatives form one symmetry orbit, or the induced-subcomplex support profile and seven-vertex threshold. The present contribution is those exact, geometrically characterized support statements and their explicit cocycle.

## Limitations

The result concerns the exact Kummer biplane complex and the mod-two coefficient field. Neither a new homotopy classification nor an integral homology computation is asserted. The automorphism action is proved for the displayed affine symplectic subgroup; no assertion of its maximality is necessary. Exhaustive computations are finite proofs only for the sixteen-point model and rely on the elementary algorithm implemented in the included self-contained verifier. White's historical paper predates the precisely dated 2012 topology source; the exact day on which White's paper first became public was not established, so no day is imputed to it. Unindexed equivalent work remains a bibliographic possibility.

## References

1. A. T. White, *Modelling biplanes on surfaces*, European Journal of Combinatorics 25 (2004), 899–909, https://doi.org/10.1016/j.ejc.2003.05.004.
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1, 10 October 2012; J. Math. Sci. Univ. Tokyo 24 (2017), 321–353, https://arxiv.org/abs/1210.2803.
3. *The Kummer biplane block complex has an integral projective-plane summand*, previously published independent mathematical calculation, identifier `6184c6679525`. It establishes the integral homotopy type of this exact complex, but not its minimum-support mod-two homology representatives.
