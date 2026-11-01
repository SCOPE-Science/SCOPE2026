# Nine three-spheres and the \(4\oplus5\) symmetry module of the folded five-cube

## Finding

Let \(E=\{x\in\mathbb F_2^5:\sum_i x_i=0\}\) and let \(G\) be the graph on these sixteen vertices in which \(x\sim y\) exactly when \(x+y\) has Hamming weight four. This is the **five-regular folded five-cube**, also called the five-regular Clebsch graph; it is **not** the ten-regular complementary graph sometimes called the Clebsch graph. Let \(X=\operatorname{Ind}(G)\) be its ordinary independence simplicial complex (faces are mutually nonadjacent vertex sets). Then

\[
 |X|\simeq\bigvee^{9}S^3.
\]

The full graph automorphism group is \(A=E\rtimes S_5\), where \(E\) acts by translation, and a permutation \(\pi\in S_5\) permutes coordinates. Define the four-dimensional standard rational \(S_5\)-module \(U=\mathbb Q^5/\mathbb Q(1,1,1,1,1)\), inflated to \(A\). Define the five-dimensional rational module \(W\) with basis \(e_1,\ldots,e_5\) and action

\[
 (a,\pi)e_i=(-1)^{a_{\pi(i)}}e_{\pi(i)}.
\]

Writing \(\operatorname{sgn}\) for the sign character of the coordinate-permutation quotient \(S_5\), there is an isomorphism of **rational** \(A\)-representations

\[
 \widetilde H_3(X;\mathbb Q)\cong
 (\operatorname{sgn}\otimes U)\oplus(\operatorname{sgn}\otimes W).
\]

Both displayed summands are irreducible over \(\mathbb Q\). Equivalently, for any \(a\in E\) and \(\pi\in S_5\), writing \(F(\pi)=\{i:\pi(i)=i\}\), the character is

\[
 \chi_3(a,\pi)=\operatorname{sgn}(\pi)
 \left( |F(\pi)|-1+\sum_{i\in F(\pi)}(-1)^{a_i}\right).
\]

The sole nonzero reduced integral homology group is \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^9\). The decomposition of its rationalization does **not** assert a corresponding direct-sum splitting of the integral \(A\)-lattice.

## Assumptions and scope

All vertex vectors have even parity; the graph is defined by Hamming distance **four**, not two. A \(k\)-simplex is a \((k+1)\)-element set of vertices with no distance-four pair. The automorphism convention is \((a,\pi):x\mapsto a+\pi(x)\). The claims concern this particular finite graph and its **ordinary** independence complex, not neighborhood, matching, or graph-Hom complexes and not a family of all folded cubes.

The group \(A\) has order \(16\cdot120=1920\). Translations and coordinate permutations give automorphisms. To see they are all, use vertex transitivity to fix the zero vertex. Its five neighbors correspond to the five weight-four vectors. Each remaining (distance-two) vertex is specified uniquely by the **pair** of neighbors it shares with zero, because the graph is strongly regular with parameters \((16,5,0,2)\). An automorphism fixing zero therefore injects into the permutations of those five neighbors, so its stabilizer has size at most \(120\). The exhibited subgroup reaches this bound.

## Proof

**1. Complete finite complex and acyclic reduction.** Index the even-parity five-bit vectors in increasing integer order. Enumerate all independent vertex masks by the recursion \(F(S)=F(S\setminus\{v\})\cup \{\{v\}\cup T:T\in F(S\setminus(\{v\}\cup N(v)))\}\). An independent bitmask recurrence provides a separate enumeration. Both yield \(393\) faces including the empty face and the nonempty face vector

\[
 (f_0,f_1,f_2,f_3,f_4)=(16,80,160,120,16).
\]

Match faces lexicographically by sweeping vertices in increasing index, pairing a currently unmatched face \(\sigma\) with \(\sigma\cup\{v\}\) whenever both are currently unmatched. The initial pair is the empty face and the first vertex; remove it from the augmented matching and retain the first vertex as a critical zero-cell. The algorithm yields \(191\) nonempty ordinary pairs and exactly nine further critical cells, all dimension three. The nine critical three-faces, recorded as hexadecimal vertex masks for the ascending vector order, are `0xf0, 0xf00, 0x3300, 0x5500, 0x6900, 0x9600, 0xaa00, 0xcc00, 0xf000`. For **all** \(1200\) nonempty codimension-one incidences, orient the Hasse edge upward if matched, downward otherwise. A complete topological sort visits all \(392\) nonempty faces, proving the matching is acyclic, without assuming that a failed cycle search establishes acyclicity. Discrete Morse theory therefore gives a CW space with one zero-cell and nine three-cells and no positive-dimensional cells otherwise. Every attaching map of a three-cell to a point is trivial; hence the stated integral wedge decomposition follows.

The standalone `verify.py` constructs this exact matching from scratch and checks its global acyclicity. The exhaustive finite DAG check constitutes a finite certificate for the only nonstandard combinatorial step. It additionally compares both independent face-enumeration algorithms.

**2. Complete affine character.** Any graph automorphism permutes the simplicial vertex basis and acts on oriented simplices by the sign of the vertex permutation restricted to that simplex. For \(g=(a,\pi)\), its signed simplicial trace is computed *exactly* by enumerating all fixed independent faces and their orientation signs. Since the reduced homology is concentrated in degree three, reduced Lefschetz gives

\[
 \operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))
 =1-\sum_{\varnothing\ne\sigma\in X,\ g\sigma=\sigma}
 (-1)^{\dim\sigma}\operatorname{sgn}(g\mid\sigma).
\]

For all \(1920\) elements of \(A\), the checker confirms the right-hand side equals the displayed closed character formula. An **independent check** partitions the sixteen vertices into \(g\)-orbits and enumerates the independent unions of internally independent orbits; the associated independence polynomial at \(-1\) gives the same trace for every element. Thus the character identity is a completely verified finite statement, not an inferred extrapolation from sample symmetries. Its trace histogram is \((-5:20),(-3:60),(-1:884),(1:865),(3:80),(5:10),(9:1)\).

**3. Identifying the rational summands.** The character of \(\operatorname{sgn}\otimes U\) at \((a,\pi)\) is \(\operatorname{sgn}(\pi)(|F(\pi)|-1)\). The character of \(\operatorname{sgn}\otimes W\) is \(\operatorname{sgn}(\pi)\sum_{i\in F(\pi)}(-1)^{a_i}\). Their sum is the checked character. Maschke's theorem and equality of characters imply the rational module isomorphism. The first summand is the sign twist of the irreducible standard rational representation of \(S_5\); the second is irreducible because, upon restriction to the abelian normal subgroup \(E\), its five distinct nontrivial coordinate characters occur with multiplicity one and are permuted transitively by \(S_5\). Any nonzero invariant subspace therefore contains all five weights. The checker also verifies the translation-Fourier multiplicities \(4\) for the trivial character, \(1\) for each of the five coordinate characters, and \(0\) for the remaining ten. This identifies the two constituent families independently of the displayed closed formula.

## Verification

Run `python3 verify.py` with Python 3.10 or newer. It requires no third-party modules or external inputs. The program reconstructs the graph, all faces, both enumeration methods, matching and complete acyclic Hasse orientation; then evaluates all affine automorphisms by two character computations and exact translation-Fourier averages. Successful execution prints `RESULT_OK wedge_of_9_S3 and rational_H3=sign_tensor_standard4 plus sign_tensor_weight1_module5`. See `VERIFICATION.md` for the executed checks and their interpretation. Exhaustiveness relies on the explicit fixed sixteen-vertex definition, not on an assumption about an infinite family.

## Relationship to prior work

Egolf and Furst, *On the minimum number of distinct eigenvalues of triangle-free strongly regular graphs*, publicly posted 7 February 2025, examine the **same five-regular** Clebsch graph and its spectral and geometric constructions. Their Section 3 and Theorem 3.2 calculate a matrix minimum-eigenvalue invariant, not the topology of the independence complex or its homology representation. Schmidt's work on quantum automorphisms of folded cubes concerns a different type of invariant. Standard folded-cube descriptions and group order are known and not claimed as new.

Relevant published calculations concern the four-cube's independence complex, the Clebsch graph's **neighborhood complex**, and the Clebsch graph's **matching complex**. None of these computes or implies the claimed homotopy type or the full affine representation for this **ordinary independence complex**. The distinction is substantive: the four-cube has degree four, the folded five-cube has degree five; a neighborhood complex uses common neighbors, while a matching complex uses edge sets. Search and comparison cannot rule out an unindexed equivalent calculation.

## Limitations

Only the specific five-regular Clebsch graph is treated. The group-module decomposition is over \(\mathbb Q\), not a claimed direct decomposition over \(\mathbb Z\). The homotopy equivalence is ordinary, not equivariant. The executable supplies an exact finite verification, not an independently audited theorem or a proof of novel status against inaccessible literature. The earliest dated primary source is 2025-02-07; no publication priority is asserted for the result here.

## References

1. Emily Egolf and Veronika Furst, *On the minimum number of distinct eigenvalues of triangle-free strongly regular graphs*, arXiv:2502.05031v1 (publicly posted 2025-02-07), particularly Section 3 and Theorem 3.2. https://arxiv.org/abs/2502.05031
2. Simon Schmidt, *Quantum automorphisms of folded cube graphs*, *Annales de l'Institut Fourier* 70 (2020), 949–970, DOI 10.5802/aif.3328. https://archive.numdam.org/articles/10.5802/aif.3328/
3. Clebsch graph parameters and naming discussion, A. E. Brouwer graph tables (accessible mirror): https://jaanos.github.io/tables/graphs/Clebsch.html
