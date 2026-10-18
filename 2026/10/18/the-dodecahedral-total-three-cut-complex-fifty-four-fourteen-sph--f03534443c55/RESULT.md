# The dodecahedral total three-cut complex: fifty-four fourteen-spheres and its full symmetry character

## Finding

Let \(D=GP(10,2)\) be the twenty-vertex dodecahedral graph. The **total three-cut complex** \(X=\Delta^t_3(D)\) has one facet \(V(D)\setminus I\) for each independent triple \(I\) of vertices. Then its integral homotopy type is

\[
X\simeq\bigvee^{54}S^{14}.
\]

The complex is pure of dimension \(16\), but its nonzero reduced integral homology is \(\widetilde H_{14}(X;\mathbb Z)\cong\mathbb Z^{54}\). Consequently it is not shellable.

Its full group of graph automorphisms has order \(120\). The following table specifies the **entire rational homology character**, with every element of a given order having the displayed trace on \(\widetilde H_{14}(X;\mathbb Q)\):

| Element order | Number of elements | Character value |
| --- | ---: | ---: |
| 1 | 1 | 54 |
| 2 | 31 | 6 |
| 3 | 20 | 0 |
| 5 | 24 | -1 |
| 6 | 20 | 0 |
| 10 | 24 | 1 |

Thus the space of rational homology classes fixed by all automorphisms has dimension exactly \(2\). The unique nonidentity central automorphism is an antipodal involution; its \(+1\) and \(-1\) eigenspaces have dimensions \(30\) and \(24\), respectively.

## Assumptions and scope

The graph has vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/10\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). Every graph is simple and unweighted. A triple is independent precisely when none of its three unordered pairs is an edge; the total cut complex uses **independent triples**, not all disconnected triples. The simplicial complexes include the empty face. Integral homology is reduced except where specified.

The group action is the natural action of all vertex permutations preserving the graph edges. Its character is computed over \(\mathbb Q\); no equivariant homotopy classification or full integral module decomposition is asserted.

## Proof

**1. Alexander-dual model.** Let \(K=X^\vee\) be the combinatorial Alexander dual on the same twenty-vertex set. By the definition of a total cut complex,

\[
K=\{T\subseteq V(D):\alpha(D[T])\le2\},
\]

where \(\alpha\) is the independence number. This equivalence follows because a set lies outside \(X\) precisely when its complement contains no independent triple. The dodecahedron graph is triangle-free. The six-vertex Ramsey theorem \(R(3,3)=6\) implies that every six-vertex induced subgraph contains an independent triple; therefore \(K\) has no faces of cardinality at least six.

A complete independent-triple test on all vertex subsets of sizes at most six gives the augmented face counts for cardinalities zero through five:

\[
(1,20,190,480,375,12).
\]

In particular there are exactly \(660\) independent triples. The supplied standard-library program `verify_dodeca_total3.py` enumerates these faces afresh from the thirty graph edges and checks all counts.

**2. Integral boundary computation.** Orient every nonempty face by ascending vertex label. In dimensions one through four, the boundary matrices of \(K\) have the following exact ranks:

\[
\bigl(\operatorname{rk}\partial_1,\operatorname{rk}\partial_2,
\operatorname{rk}\partial_3,\operatorname{rk}\partial_4\bigr)
=(19,171,309,12).
\]

Crucially, *every nonzero Smith factor is one*. This is not inferred from ranks modulo finitely many primes. The program performs a deterministic reduction over \(\mathbb Z\): it selects entries equal to \(+1\) or \(-1\), clears their rows and columns by **unimodular integer operations**, removes each unit block, and verifies that the entire remaining matrix is zero. It obtains respectively \(19\), \(171\), \(309\), and \(12\) unit blocks, with zero remainder in each boundary matrix. Each recorded pivot therefore contributes a unit Smith factor; no nonunit invariant factor remains.

The integral homology calculation is consequently exact. In degree three, \(\operatorname{rk}\ker\partial_3=375-309=66\) and \(\operatorname{rk}\operatorname{im}\partial_4=12\), so

\[
\widetilde H_3(K;\mathbb Z)=\mathbb Z^{54},
\qquad\widetilde H_j(K;\mathbb Z)=0\text{ for }j\ne3.
\]

Torsion cannot occur, because the boundary images are primitive sublattices, as witnessed by the unit Smith forms. Independent modular reductions at primes \(2,3,5,7\) agree, but are corroborations rather than the integral proof.

**3. From dual homology to homotopy.** Combinatorial Alexander duality on twenty vertices gives

\[
\widetilde H_j(X;\mathbb Z)\cong\widetilde H^{17-j}(K;\mathbb Z).
\]

The integral universal coefficient theorem and the free homology just established show that the only nonzero reduced group of \(X\) is \(\mathbb Z^{54}\) in degree fourteen.

Because every induced six-vertex subgraph of \(D\) contains an independent triple, \(X\) contains the full thirteen-skeleton of the nineteen-simplex. It is therefore at least twelve-connected. The vanishing of \(H_{13}(X;\mathbb Z)\), together with the Hurewicz isomorphism in degree thirteen, implies \(\pi_{13}(X)=0\); hence \(X\) is thirteen-connected. Applying Hurewicz once more gives \(\pi_{14}(X)\cong H_{14}(X;\mathbb Z)=\mathbb Z^{54}\). Choose sphere maps representing a basis and form a map from \(\bigvee^{54}S^{14}\) to \(X\). It induces an integral homology isomorphism, so the homology Whitehead theorem makes it a homotopy equivalence. The conclusion is a homotopy classification, not merely a Betti-number computation.

Since \(X\) has facets of size seventeen, its dimension is sixteen. A pure shellable complex is either contractible or a wedge of spheres in its top dimension; neither possibility matches this nontrivial degree-fourteen homology. Therefore \(X\) is not shellable.

**4. Complete homology character.** An exhaustive adjacency-preserving permutation backtrack enumerates exactly \(120\) automorphisms. For each automorphism, every setwise fixed simplex of \(X\) is a union of its vertex cycles. The induced signed orientation and the alternating trace of these simplices give the reduced Lefschetz number. Since reduced homology is concentrated in even degree fourteen, this is precisely the trace on \(\widetilde H_{14}(X;\mathbb Q)\). The direct calculation gives the table in the Finding section for **every** automorphism, not selected representatives.

For an independent check, the program computes signed fixed-face traces on the smaller Alexander dual \(K\) and applies the orientation sign in equivariant combinatorial Alexander duality. Both implementations agree for all \(120\) elements. Averaging the table gives invariant dimension \((54+31\cdot6+24\cdot(-1)+24\cdot1)/120=2\). Enumerating central elements yields exactly the identity and a fixed-point-free involution; its trace six gives the stated eigenspace dimensions.

## Verification

Run `python3 verify_dodeca_total3.py` using Python 3 with its standard library only. The expected exact output is embedded in `verification_output.txt`. The program regenerates the graph, simplices, four integral unimodular reductions, four independent finite-field rank checks, full automorphism set and both signed character evaluations. Its final line is `VERIFICATION_COMPLETE`. No external data or opaque numerical package is required to reproduce the calculations.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced total cut complexes and proved structural results for chordal graphs, cycles, complete multipartite graphs and grids [1]. The graph \(D\) is neither chordal nor a cycle nor a member of their explicitly classified complete multipartite or grid families. Their full-text definitions and family theorems do not supply this dodecahedral classification or its complete symmetry character.

The companion work [2] studies **ordinary** cut complexes, whose facets complement disconnected vertex sets. The ordinary three-cut complex and total three-cut complex differ here: a disconnected triple containing one edge is included only in the ordinary construction. Results about ordinary cut complexes therefore do not imply the stated homotopy or character for the total three-cut complex.

Additional comparisons included published homotopy calculations for other graph complexes associated with the dodecahedron and for total cut complexes of other cubic graphs. The operators, graph parameters and relevant dimensions differ. No equivalent dodecahedral total-three-cut statement was identified in the sources searched; that negative search is not a proof of global originality.

## Limitations

The theorem is specific to \(GP(10,2)\) and to independent triples. It does not classify total cut complexes of arbitrary cubic or girth-five graphs, integral representation lattices beyond the displayed ranks and central involution eigenspaces, or the equivariant homotopy type. Possible unindexed or differently phrased prior treatments remain an originality risk. The mathematical verification reported here is not an independent external audit.

## References

[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first public version September 27, 2022, https://arxiv.org/abs/2209.13503.

[2] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public version April 26, 2023, https://arxiv.org/abs/2304.13675.
