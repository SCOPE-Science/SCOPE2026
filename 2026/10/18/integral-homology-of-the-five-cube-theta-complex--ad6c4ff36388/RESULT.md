# Integral homology of the five-cube theta complex

## Finding

Let \(Q_5\) denote the ordinary graph of the five-dimensional cube, with \(32\) vertices, and let \(\operatorname{Cube}(5,1)\) be the hypergraph whose hyperedges are the graph edges of \(Q_5\). Then its theta complex has the complete reduced **integral** homology groups
\[
\widetilde H_i\bigl(\Theta(\operatorname{Cube}(5,1));\mathbb Z\bigr)
\cong\begin{cases}
\mathbb Z^{10},&i=22,\\
\mathbb Z,&i=24,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, every integral homology group is torsion-free. More strongly, the ordinary independence complex of the same graph admits an explicit acyclic discrete-Morse matching with precisely **one critical vertex, one critical 5-simplex and ten critical 7-simplices**. It follows that
\[
\widetilde H_i(\operatorname{Ind}(Q_5);\mathbb Z)
\cong\begin{cases}
\mathbb Z,&i=5,\\
\mathbb Z^{10},&i=7,\\
0,&\text{otherwise}.
\end{cases}
\]
The result does not assert a complete homotopy type or sphere-wedge decomposition for either complex.

## Assumptions and scope

Write \(V=\{0,1,\ldots,31\}\) for the cube vertices, regarding each integer as a binary string of length five. Join \(u\) to \(v\) precisely when their binary strings differ in one coordinate. Define \(K=\operatorname{Ind}(Q_5)\) to consist of vertex subsets containing no cube edge. Define \(\Theta=\Theta(\operatorname{Cube}(5,1))\) to consist of subsets \(\sigma\subseteq V\) disjoint from at least one edge of \(Q_5\). All homology groups are simplicial, reduced where indicated, with coefficients in \(\mathbb Z\); \(\operatorname{Ind}(Q_5)\) and \(\Theta\) use their usual nonaugmented geometric realizations. This is a theorem about this specified finite complex, not all dimensions of cubes.

## Proof

**Step 1: Complete finite face enumeration.** Represent a subset \(\sigma\subseteq V\) by its \(32\)-bit integer characteristic mask. For each integer vertex \(v\), its graph-neighborhood mask is
\[
N(v)=\bigvee_{j=0}^{4}2^{\,v\operatorname{xor}2^j}.
\]
Starting with all \(32\) vertices eligible and the empty chosen set, recursively take each least eligible vertex, forbid its graph-neighbors, and recurse on the remaining eligible vertices. This enumerates every independent subset once, including the empty set. The exact counts by cardinality \(0,1,\ldots,16\) are
\[
(1,32,416,2880,11760,29856,48960,54304,44240,29920,17952,9088,3672,1120,240,32,2).
\]
The total is \(254475\) masks. A separate deletion/closed-neighborhood polynomial recurrence yields the identical sequence; see `VERIFY_Q5.py`.

**Step 2: Construct the acyclic matching.** Work in the face poset of the nonempty simplices of \(K\). Order the potential matching vertices so that the even-Hamming-weight cube vertices occur in increasing numerical order first, followed by the odd-Hamming-weight vertices in increasing numerical order. At each vertex \(v\), among faces not matched at an earlier step, pair every face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) if both faces remain available. The two faces differ by exactly one vertex. At any one stage the matching pairs are disjoint, since the lower face lacks \(v\) and the upper face contains \(v\). Thus the construction is well-defined, without reliance on iteration order within a stage. Exactly \(127231\) pairs are formed. Exactly twelve critical faces remain: one of dimension zero, one of dimension five, and ten of dimension seven. Their full bitmasks appear in `critical_faces.json` and are rechecked in `VERIFY_Q5.py`.

**Step 3: Certify acyclicity, not merely critical counts.** Give each matched pair \((\sigma,\tau)\) a vertex in an auxiliary directed graph. For every facet \(\sigma'\neq\sigma\) of \(\tau\) that occurs as the *lower* simplex in another matched pair, insert an arc from \((\sigma,\tau)\) to that other pair. This directed graph encodes precisely the possible nonconstant alternating Forman gradient paths. It has exactly \(127231\) vertices and \(99497\) arcs. Kahn topological elimination removes all \(127231\) vertices. Hence the directed graph has no cycles and the matching is acyclic. The included standalone verifier constructs the complete graph and performs this elimination, with no probability, timeout inference or sampling.

**Step 4: Integral homology by discrete Morse theory.** A finite acyclic simplicial matching gives a CW complex homotopy equivalent to \(K\) with precisely one cell for each critical simplex. Its nonzero cell dimensions are \(0,5,7\). The cellular differential lowers dimension by one, so all differentials are zero *integrally*. It follows that \(K\) has the displayed reduced integral homology, with no possible hidden torsion.

**Step 5: Integral Alexander duality.** For a hypergraph \(\mathcal H\), the theta complex is the simplicial Alexander dual of \(\operatorname{Ind}(\mathcal H)\): a set belongs to theta exactly when its complement contains a hyperedge. For the present \(32\)-element vertex set, combinatorial Alexander duality over integers gives
\[
\widetilde H_i(\Theta;\mathbb Z)\cong
\widetilde H^{29-i}(K;\mathbb Z).
\]
The integral cohomology groups of \(K\) follow from its torsion-free cellular cochain complex: \(\mathbb Z\) in degree \(5\), \(\mathbb Z^{10}\) in degree \(7\), and zero elsewhere. Therefore theta has \(\mathbb Z^{10}\) in degree \(22\) and \(\mathbb Z\) in degree \(24\), as claimed.

## Verification

Run `python3 VERIFY_Q5.py` in a directory containing the extracted artifact files (Python 3 standard library only). The program independently checks the complete face count, the exact critical cell masks, the disjoint matching coverage identity, all possible gradient transitions, acyclicity by a full topological ordering, and face counts from an independent recursive polynomial. It also checks the reduced Euler characteristic \(-11\), which agrees with \((-1)^{22}10+(-1)^{24}1=11\) for theta after the parity relation between dual complexes (the independence complex has reduced Euler characteristic \(-11\)). The finite checks concern every face of the exact finite domain, not a sample or asymptotic extrapolation.

## Relationship to prior work

Conant and Thistlethwaite introduced the theta complex and proved the Alexander-duality identification. In Section 5.2, Theorem 5, their calculation of \(\Theta(\operatorname{Cube}(5,1))\) gives rational Betti numbers \(10\) in degree \(22\) and \(1\) in degree \(24\), while explicitly leaving its **integer homology** unresolved. The new conclusion is the exact torsion-free integral result and the complete acyclic matching proving it; the two rational ranks and the Alexander-duality equivalence themselves are not new. Their Theorem 3 also identifies the theta complex, up to homotopy, with the simplicial space of satisfiable four-conjunctive-normal-form formulae in at most five variables. Related general work on the independence complexes of planar and cylindrical grids concerns different graph families; it does not supply this exact integral calculation. The ordinary five-cube must not be confused with its sixteen-vertex folded quotient (the Clebsch graph) or the sixteen-vertex four-cube.

## Limitations

The perfect matching determines integral homology and a small CW model, but not the attaching maps of the ten critical seven-cells to the five-skeleton. In particular a wedge of spheres is **not** claimed. This is one specified cubical parameter, not a general result for \(\operatorname{Cube}(n,k)\). Exact acyclicity relies on replay of a finite, fully specified deterministic computation rather than a closed symbolic counting argument.

## References

1. James Conant and Oliver Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739 (first public 5 August 2008; revised 23 August 2010). Proposition 1, Theorem 1, Theorem 3, Section 5.2 and Theorem 5. https://arxiv.org/html/0808.0739v2
2. Kengo Okura, *Simple Homotopy Types of Independence Complexes of Graphs involving Grid Graphs*, arXiv:1908.09356v1 (2019), introduction and Theorems 1.1–1.3. https://arxiv.org/html/1908.09356v1
3. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145 (discrete-Morse matching and CW-cell theorem).
