# The Pappus induced-matching complex is 116 two-spheres, with no invariant homology

## Finding
Let \(P\) denote the eighteen-vertex Pappus graph and let \(\mathcal S(P)\) be the simplicial complex whose vertices are the edges of \(P\) and whose faces are *induced matchings*: for each face the induced subgraph of \(P\) on all selected edge endpoints consists of precisely the selected pairwise-disjoint edges. Equivalently, with \(L(P)\) the ordinary line graph and its graph square taken at distance at most two,
\[
\mathcal S(P)=\operatorname{Ind}(L(P)^2).
\]
Then, as an **integral homotopy equivalence**,
\[
\mathcal S(P)\simeq\bigvee^{116}S^2.
\]
In particular, \(\widetilde H_2(\mathcal S(P);\mathbb Z)\cong\mathbb Z^{116}\), and the other reduced integral homology groups vanish. Although its maximum simplex dimension is four, its homotopy is concentrated in dimension two.

More precisely, the full graph automorphism group has order \(216\). Its natural action on \(\widetilde H_2(\mathcal S(P);\mathbb Q)\) has the complete character-value distribution

| Character value | Number of automorphisms |
|---:|---:|
| \(116\) | 1 |
| \(8\) | 2 |
| \(5\) | 12 |
| \(2\) | 12 |
| \(-10\) | 18 |
| \(-1\) | 36 |
| \(0\) | 135 |

Consequently the symmetry-fixed rational subspace is zero:
\[
\widetilde H_2(\mathcal S(P);\mathbb Q)^{\operatorname{Aut}(P)}=0.
\]

## Assumptions and scope
Work with the fixed labeled graph \(V(P)=\{0,1,\ldots,17\}\). Form the undirected eighteen cyclic edges \(\{i,i+1\bmod 18\}\) and the distinct chord edges \(\{i,i+s_i\bmod18\}\), where \((s_0,\ldots,s_{17})\) repeats \((5,7,-7,7,-7,-5)\) three times. Deduplicate unordered edge pairs. This produces twenty-seven edges and three neighbors at every vertex. Sort these edges lexicographically, with labels \(0\) through \(26\). Thus the simplicial complex has exactly these twenty-seven labeled vertices. All matching and homotopy statements are for this fixed graph, not arbitrary cubic graphs.

Two edge-labels conflict when the corresponding graph edges share an endpoint or an endpoint of one is adjacent to an endpoint of the other. Consequently \(A\subseteq\{0,\ldots,26\}\) is a simplex if and only if no two selected edge-labels conflict. Every simplex is regarded as an ordinary unaugmented face for discrete Morse theory, so the empty simplex does not participate in the face-poset matching. Orient each nonempty simplex by increasing edge-label order.

## Proof
**1. Exhaustive face enumeration.** For each edge label \(j\), let \(C(j)\) be its exact set of conflicts and define \(E(j)=\{0,\ldots,26\}\setminus(C(j)\cup\{j\})\). Starting with the empty face and all candidate labels, enumerate by the recurrence: for each remaining candidate \(j\), append \(j\) to the face and recurse on candidates larger than \(j\) intersected with \(E(j)\). The increasing-index restriction produces each independent subset of the squared line graph exactly once, so this is a complete enumeration, not sampling. The counts by face cardinality \(0\) through \(5\) are exactly
\[
(1,27,189,387,135,27),
\]
for \(766\) faces including the empty one. An independent second method enumerates every \(k\)-edge choice for \(0\le k\le5\), tests pairwise distinct endpoints, and checks that the induced graph on the \(2k\) endpoints has exactly \(k\) edges. The independently obtained face set agrees exactly. Exhaustive checking of all six-edge choices finds none, so the list is complete in every dimension. The Euler check gives \(\widetilde\chi=116\).

**2. Discrete Morse matching.** Identify each face with its 27-bit integer mask. Begin with all \(765\) nonempty faces unmatched. For stages \(j=0,1,\ldots,26\), visit the currently unmatched masks in ascending integer order, pair a lower face \(F\) not containing \(j\) with \(F\cup\{j\}\) whenever that upper face is also currently unmatched and a valid simplex, then delete both partners before proceeding to the next stage. The recorded implementation groups pairs for each stage and confirms both partners still exist at deletion; since one partner has the \(j\)-bit and the other does not, no stage contains conflicting pairs. This yields exactly \(324\) matched pairs. The \(117\) critical cells comprise precisely one vertex and \(116\) triangles, with no cells in dimensions one, three, or four.

To check **acyclicity**, orient every codimension-one covering relation of the nonempty face poset from the larger face toward the smaller one, except reverse each of the \(324\) matched coverings. The program enumerates all \(2,214\) such covering incidences, constructs the directed graph on all \(765\) nonempty faces, and topologically sorts every vertex. The resulting topological order is an exhaustive certificate that this acyclic matching contains no closed gradient path. By the ordinary discrete Morse theorem, the simplicial complex is homotopy equivalent to a CW complex with one zero-cell, \(116\) two-cells, and no positive-dimensional cells in other degrees. Each two-cell therefore attaches to the single point by a constant map, proving
\[
\mathcal S(P)\simeq\bigvee^{116} S^2.
\]
There is no inference from finite-field homology to integral homotopy in this argument.

**3. Full symmetry character.** Enumerate all graph automorphisms as bijections of the eighteen labeled vertices, preserving adjacency and nonadjacency on every vertex pair. Recursive backtracking explores all consistent partial bijections; it finds exactly \(216\) complete automorphisms. Every such bijection induces a permutation of the twenty-seven lexicographically indexed graph edges and hence of the \(766\) simplicial faces. If \(g\) is such an automorphism, compute the reduced signed simplicial Lefschetz number directly as
\[
\widetilde L(g)=-1+\sum_{\substack{\varnothing\ne F\in\mathcal S(P)\\gF=F}}(-1)^{|F|-1}\operatorname{sgn}(g|_F),
\]
where \(\operatorname{sgn}(g|_F)\) is the parity of the induced permutation of the increasingly oriented face. The initial \(-1\) is the contribution from the augmented degree-minus-one chain of the empty face; it is necessary for *reduced* homology. The Hopf trace identity and the just-proved concentration in degree two yield
\[
\widetilde L(g)=\operatorname{tr}\bigl(g\mid\widetilde H_2(\mathcal S(P);\mathbb Q)\bigr).
\]
Exhaustive evaluation across all \(216\) automorphisms gives the table in the Finding. The value at the identity is \(116\), agreeing with the integral sphere count. Averaging the character gives
\[
\frac{116+2(8)+12(5)+12(2)+18(-10)+36(-1)+135(0)}{216}=0.
\]
By the rational character projection formula, this is the dimension of the full-automorphism invariant subspace, proving the last assertion.

## Verification
Run `python3 verify_pappus_strong_matching.py` with a Python version supporting `int.bit_count` (Python 3.8+ with the method available, normally Python 3.10 or later). The verifier uses only the standard library and independently reconstructs the LCF graph, all face sets by two algorithms, nonexistence of size-six induced matchings, every proposed paired incidence, the complete directed Hasse graph and its acyclic topological sort, and the complete graph automorphism group and signed character. On successful execution it prints `VERIFY_OK` and the complete deterministic count summary; `verification_output.txt` contains a previously reproduced output transcript. The small exact computation enumerates all relevant finite objects and uses no timeouts or statistical sampling.

## Relationship to prior work
The classical graph-theoretic induced matching is discussed by Joos, Rautenbach and Sasse (first public arXiv version December 4, 2013); their main result is a size bound for induced matchings in cubic graphs, not a homotopy or symmetry classification of the simplicial complex of **all** induced matchings. Kozlov's March 28, 2005 article (primary MSC 57Q10) supplies older simple-homotopy methodology for graph-related simplicial complexes, but no Pappus induced-matching calculation.

The previously published integral homotopy calculation for the **ordinary matching complex** of the same Pappus graph concerns \(\operatorname{Ind}(L(P))\), in which selected graph edges need only be endpoint-disjoint. That complex has forty five-dimensional spheres; it is strictly different from the present \(\operatorname{Ind}(L(P)^2)\). Likewise, the ordinary vertex-independence complex of \(P\) uses the original eighteen vertices, rather than the twenty-seven graph edges, and cannot imply the present result. Previous examples of strong-matching complexes on other cubic graphs do not determine the topology or rational automorphism character of the Pappus instance. No stronger covering theorem was found in the searched sources, but indexing gaps remain possible.

## Limitations
This is a single finite labeled graph, even though it is a canonical cubic symmetric incidence graph. Its full integral homotopy type and *rational* automorphism character are determined; no integral decomposition of the graph-automorphism module is claimed. The graph-edge-based definition matters: a complex built from arbitrary vertex subsets inducing degree at most one is not the same construction. Computations are exact and exhaustive for the stated finite domain but do not imply an infinite-family classification. Novelty cannot be proved solely by unsuccessful literature search; an unindexed prior treatment remains a residual risk. No independent mathematical audit has been performed.

## References
1. Dmitry N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613, first public version 2005-03-28, primary MSC 57Q10. https://arxiv.org/abs/math/0503613
2. Felix Joos, Dieter Rautenbach, Thomas Sasse, *Induced Matchings in Subcubic Graphs*, arXiv:1312.1110, first public version 2013-12-04. https://arxiv.org/abs/1312.1110
3. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
4. *Integral homotopy type of the Pappus graph matching complex*, published research record (2026): https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-pappus-graph-matching-complex--db6c6c11f317
5. *Pappus Graph*, Wolfram MathWorld, for the graph name and LCF edge specification. https://mathworld.wolfram.com/PappusGraph.html
