# Integral homology of the five-cube theta complex

## Finding

Let \(Q_5\) be the graph on the \(32\) binary words of length five, with adjacent words differing in one coordinate, and let \(I=\operatorname{Ind}(Q_5)\) be its simplicial complex of independent vertex sets. Let \(\Theta=\Theta(\operatorname{Cube}(5,1))\) denote the hypergraph theta complex associated with the edges of the five-dimensional cube. Then

\[
\widetilde H_i(I;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=5,\\
\mathbb Z^{10},&i=7,\\
0,&\text{otherwise},
\end{cases}
\qquad
\widetilde H_i(\Theta;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{10},&i=22,\\
\mathbb Z,&i=24,\\
0,&\text{otherwise}.
\end{cases}
\]

The integral statement for the theta complex removes the coefficient uncertainty left in the published rational computation. The theorem claims **integral homology**, not a wedge-of-spheres homotopy equivalence.

## Assumptions and scope

All complexes are finite abstract simplicial complexes and all groups use ordinary reduced integral homology. Encode the cube vertices as integers \(0,1,\ldots,31\), with the binary Hamming-neighbor relation \(u\sim v\) exactly when \(u\oplus v\) is a power of two. The \(32\) hypergraph vertices of \(\operatorname{Cube}(5,1)\) are these cube vertices and its hyperedges are the \(80\) cube edges. By the definition of the theta complex, \(\Theta\) is the combinatorial Alexander dual of \(I\), with respect to these same \(32\) vertices.

## Proof

**1. Complete finite face set.** An independent set is a bit mask \(s\) with no adjacent selected graph vertices. The attached standard-library-only verifier recursively considers the \(32\) graph vertices, either selecting an unblocked vertex and blocking its five neighbors, or omitting that vertex. Induction on the recursion index proves that every independent subset occurs exactly once, and that no non-independent subset occurs. The resulting face set contains \(254{,}475\) faces including the empty face, and \(254{,}474\) nonempty faces. The nonempty face counts, in dimensions \(0\) through \(15\), are

\[
(32,416,2880,11760,29856,48960,54304,44240,29920,17952,9088,3672,1120,240,32,2).
\]

**2. Explicit discrete-Morse matching.** Exclude the empty face. Order the \(32\) cube vertices by the parity of the number of ones in their binary labels (even parity first), breaking ties by the integer label. For each vertex \(v\), while considering only faces not already matched, pair every lower face \(s\) that omits \(v\) with the higher face \(s\cup\{v\}\), provided both are still unmatched. Remove each such pair before proceeding to the next pivot. Since distinct lower faces at the same stage have different mates, these pairs form a genuine partial matching of codimension-one face incidences.

The attached verifier constructs this matching from the complete face list and finds exactly \(127{,}231\) disjoint pairs. The unpaired faces have dimensions

\[
\{0:1,\;5:1,\;7:10\}.
\]

For an independent, exhaustive acyclicity check, take the entire Hasse graph of the poset of **all nonempty faces**, orient each matched covering edge upward and each other covering edge downward. This directed graph has \(254{,}474\) vertices and \(1{,}844{,}864\) edges. The included program explicitly constructs every indegree and runs Kahn's topological-sort algorithm, updating every oriented covering edge exactly once. It visits all \(254{,}474\) faces and finishes with all indegrees zero. A finite directed graph is acyclic if and only if this process visits every vertex. Hence the stated matching is acyclic; this is an exhaustive finite check, not a sample of cycles.

**3. Integral cellular homology.** The acyclic-matching theorem of discrete Morse theory gives a CW complex homotopy equivalent to \(I\), having exactly one \(0\)-cell, one \(5\)-cell, ten \(7\)-cells, and no other cells. Because there are no cells in dimensions \(1\), \(4\), or \(6\), all cellular boundary homomorphisms vanish integrally. Thus \(\widetilde H_5(I;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_7(I;\mathbb Z)\cong\mathbb Z^{10}\), with all other reduced homology groups zero. No assumption about attaching maps is needed for this homology conclusion.

**4. Integral Alexander duality.** By combinatorial Alexander duality on a \(32\)-element ground set,

\[
\widetilde H_i(\Theta;\mathbb Z)
\cong \widetilde H^{32-i-3}(I;\mathbb Z).
\]

The integral cohomology of \(I\) is free of rank one in degree \(5\) and rank ten in degree \(7\), and zero otherwise, by the universal coefficient theorem and the free integral homology just proved. Substituting these degrees yields the asserted theta-complex homology in degrees \(24\) and \(22\), with no other nonzero reduced groups.

## Verification

Run the included file `verify_q5.py` using `python -I verify_q5.py` (Python standard library only). It enumerates the **entire** face set, verifies independence directly, records face counts, constructs every matched pair, tests that no face belongs to two pairs, computes all oriented face-poset covering edges, and topologically sorts the resulting directed graph. The recorded `verify_output.txt` ends with `VERIFY_OK` and gives the critical-face masks, matching-stage counts, and total Hasse-edge count. An additional clean replay produced byte-identical output. These are exact integer and bit-mask computations, without floating-point tolerances or probabilistic steps.

The face-vector reduced Euler characteristic is \(-11\), consistent with one degree-five and ten degree-seven homology generators. The dual theta-complex reduced Euler characteristic is \(11\), agreeing with the previously computed rational Betti numbers.

## Relationship to prior work

Conant and Thistlethwaite introduced the theta construction and explicitly tabulated the rational groups for \(\Theta(\operatorname{Cube}(5,1))\): rank ten in degree \(22\), rank one in degree \(24\), and no other positive rational homology. Their treatment states that the integer homology of this example is unknown. Here the groups are determined integrally, ruling out torsion in every degree. This is not a claim of novelty for the rational Betti numbers, the Alexander-duality definition, or the discrete-Morse theorem.

Nilakantan and Shukla studied independence complexes of a different, explicitly defined family of circulant-neighborhood regular bipartite graphs. Their degree-five, sixteen-per-side graph has pairs of same-side vertices sharing four neighbors, whereas same-side vertices of \(Q_5\) share either zero or two; that graph family therefore does not identify this case. Other known computations for lower-dimensional cube graphs do not imply the present five-dimensional result.

## Limitations

A Morse CW model having cells only in dimensions \(0\), \(5\), and \(7\) determines integral homology, **not** the attaching maps of the \(7\)-cells into the \(5\)-skeleton. In particular, no equivalence of \(I\) or \(\Theta\) to a wedge of spheres is claimed. The finite certificate depends on the correctness of the provided exhaustive code and has not undergone independent mathematical auditing. A previously unlocated stronger homotopy theorem could imply the result.

## References

1. James Conant and Oliver Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739, first publicly posted 2008-08-05. Sections 2 and 5.2, including Theorem 5 and the note on unknown integral homology. https://arxiv.org/abs/0808.0739
2. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145. The acyclic discrete-Morse matching theorem.
3. Nandini Nilakantan and Samir Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789, first publicly posted 2017-09-14. Section 1 (the graph-family definition), Sections 2–3 (matching framework). https://arxiv.org/abs/1709.04789
