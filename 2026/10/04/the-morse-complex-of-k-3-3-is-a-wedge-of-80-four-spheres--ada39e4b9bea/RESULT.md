# The Morse complex of \(K_{3,3}\) is a wedge of \(80\) four-spheres
## Finding
For the complete bipartite graph \(K_{3,3}\), the Morse complex \(\mathcal M(K_{3,3})\) of acyclic discrete vector fields is homotopy equivalent to a wedge of exactly \(80\) four-spheres: \(\mathcal M(K_{3,3})\simeq\bigvee^{80}S^4\).

## Assumptions and scope
Let \(K_{3,3}\) have bipartition \(\{a_0,a_1,a_2\}\sqcup\{b_0,b_1,b_2\}\). A vertex of \(\mathcal M(K_{3,3})\) is a primitive discrete vector field, equivalently a choice of an endpoint as the tail of one edge. A simplex is a compatible collection of such choices in which no graph vertex is used twice as a tail and no closed \(V\)-path occurs. For a graph this is equivalently an orientation of a rooted spanning forest in which each non-root vertex points along the unique edge toward its component root.

The claim concerns the ordinary Morse complex of acyclic discrete vector fields, not the algebraic Morse chain complex of a chosen discrete Morse function and not graph-configuration-space Morse complexes.

## Proof
There are \(18\) primitive vector fields, two for each of the \(9\) edges. Encode each edge by one of three states: unused, oriented from the left part to the right part, or oriented from the right part to the left part. Exhausting all \(3^9=19683\) states and retaining exactly those with distinct tails and no directed cycle gives the nonempty face vector
\[
(18,126,432,729,486).
\]
This census has an independent closed check. A \(k\)-arrow acyclic vector field on a graph is a rooted spanning forest with \(k\) edges. The matrix-forest theorem therefore identifies the face numbers with the coefficients of \(\det(\lambda I+L)\). For \(K_{3,3}\), the Laplacian spectrum is \(0,6,3,3,3,3\), hence
\[
\det(\lambda I+L)=\lambda(\lambda+6)(\lambda+3)^4
=\lambda^6+18\lambda^5+126\lambda^4+432\lambda^3+729\lambda^2+486\lambda,
\]
which reproduces the face vector.

Order the \(18\) primitive vector fields lexicographically by edge and then by chosen tail. On the face poset, process these \(18\) vertices in that order and, at each stage, match every still-unmatched face \(\sigma\) not containing the current primitive vector field \(v\) with \(\sigma\cup\{v\}\) whenever that coface is still unmatched. The complete matching has \(855\) pairs. Exhaustive verification on all \(1791\) nonempty faces and all \(6894\) Hasse cover relations shows that reversing the matched cover relations produces an acyclic directed Hasse graph. The only critical faces are one \(0\)-simplex and exactly \(80\) \(4\)-simplices.

Forman's acyclic-matching theorem therefore gives a CW complex homotopy equivalent to \(\mathcal M(K_{3,3})\) with one \(0\)-cell, no cells in dimensions \(1,2,3\), and \(80\) cells in dimension \(4\). Every \(4\)-cell is attached to the single \(0\)-cell, so the CW complex is \(\bigvee^{80}S^4\).

## Verification
The standalone verifier `verify.py` reconstructs \(K_{3,3}\) from its definition, enumerates every one of the \(3^9\) edge states, checks the matrix-forest face count independently, reconstructs the sequential matching, and topologically sorts the fully oriented Hasse diagram to certify acyclicity. It also independently computes the augmented mod-\(2\) boundary ranks
\[
(1,17,109,323,406)
\]
and reduced mod-\(2\) Betti numbers
\[
(0,0,0,0,80),
\]
as a homological cross-check. Running the verifier prints `K33_MORSE_VERIFY_OK`.

## Relationship to prior work
Scoville and Zaremsky, arXiv:2004.10481, explicitly single out complete bipartite graphs as an example whose Morse-complex homotopy type was, to their knowledge, unknown; their result supplies connectivity bounds rather than an exact type. Their Example 4.6 states this for \(\mathcal M(K_{p,q})\), and their theorem implies simple connectivity for the present graph.

Donovan, Lin, and Scoville, arXiv:1909.11440, compute homotopy types for several graph families using domination and strong collapse, but the complete bipartite graph \(K_{3,3}\) is not among the families stated there. Donovan and Scoville, arXiv:2207.13780, treat paths, cycles, extended stars, and related matching complexes, again without an exact \(K_{3,3}\) calculation. Current semantic and exact-phrase searches for the claim and its standard aliases found no published result implying this \(80\)-sphere decomposition.

## Limitations
This is a single exact graph computation, not a formula for \(\mathcal M(K_{p,q})\) in general. The proof depends on a finite exhaustive acyclic-matching certificate, although the face census also has an independent matrix-forest derivation. The literature comparison cannot exclude a very recent, non-indexed, or differently phrased duplicate.

## References
1. N. A. Scoville and M. C. B. Zaremsky, “Higher connectivity of the Morse complex,” arXiv:2004.10481; later published in *Proceedings of the American Mathematical Society, Series B*.
2. C. Donovan, M. Lin, and N. A. Scoville, “On the homotopy and strong homotopy type of complexes of discrete Morse functions,” arXiv:1909.11440.
3. C. Donovan and N. A. Scoville, “Star clusters in the Matching, Morse, and Generalized Morse complex,” arXiv:2207.13780.
