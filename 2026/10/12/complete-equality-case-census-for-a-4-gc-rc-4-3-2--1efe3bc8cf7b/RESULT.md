# Complete equality-case census for \(A_{4}^{GC,RC}(4,3,2)\)
## Finding
Let the DNA alphabet be \(\{A,C,G,T\}\), with Watson--Crick complement \(A\leftrightarrow T\) and \(C\leftrightarrow G\). For a word \(x=x_1x_2x_3x_4\), let \(x^{RC}\) be its reverse complement. Consider codes \(C\) consisting only of length-four words of GC-content exactly \(2\), subject to
\[
H(x,y)\ge 3\quad(x\ne y),\qquad H(x,y^{RC})\ge 3\quad(x,y\in C).
\]
The known optimum is \(A_{4}^{GC,RC}(4,3,2)=6\). There are exactly \(512\) labeled maximum codes of size \(6\).

Every maximum code has the same distance structure. Each codeword satisfies \(H(x,x^{RC})=4\). Among the \(15\) unordered pairs of distinct codewords, exactly three pairs have both \(H(x,y)=4\) and \(H(x,y^{RC})=4\); these three pairs form a perfect matching on the six codewords. For each of the other twelve pairs, both distances are exactly \(3\).

Under the explicit \(64\)-element symmetry subgroup obtained by combining coordinate permutations that commute with coordinate reversal and alphabet permutations that commute with Watson--Crick complement, the \(512\) maxima split into exactly \(14\) orbits: twelve of size \(32\) and two of size \(64\). The corresponding stabilizer orders are \(2\) and \(1\), respectively.
## Assumptions and scope
The finding uses the standard Hamming-distance and reverse-complement constraints for DNA codes with constant GC-content. The alphabet and complement map are fixed as above, and GC-content counts positions occupied by \(C\) or \(G\). The symmetry statement is only for the explicit \(64\)-element subgroup described above; it does not assert that this subgroup is the full automorphism group of the constrained code space.

The published optimum \(6\) is prior work. The new content is the complete labeled equality-case census, the universal perfect-matching distance structure, and the orbit decomposition under the stated subgroup.
## Proof
First restrict to words of length four and GC-content two that individually satisfy the self reverse-complement constraint \(H(x,x^{RC})\ge3\). Exactly \(72\) words remain. Form a graph on these \(72\) vertices, joining distinct words \(x,y\) exactly when both \(H(x,y)\ge3\) and \(H(x,y^{RC})\ge3\). A code satisfying the stated constraints is exactly a clique in this graph.

The supplied verifier constructs all vertices and all \(1168\) compatibility edges directly from the definitions. A complete Bron--Kerbosch recursion enumerates every maximal clique. Its maximal-clique size histogram is
\[
2:64,\qquad 4:640,\qquad 5:1024,\qquad 6:512.
\]
Thus the graph maximum clique size is \(6\), and exactly \(512\) labeled six-cliques attain it. As an independent enumeration path, a separate increasing-order clique recursion enumerates all six-cliques and again obtains exactly \(512\), with the same set of six-cliques.

For each of the \(512\) maxima, the verifier recomputes all self and pairwise direct/reverse-complement distances. It verifies that every self reverse-complement distance is \(4\); that exactly three unordered pairs simultaneously have direct and reverse-complement distance \(4\); that these three pairs are identical for the two distance tests and form a perfect matching; and that every other unordered pair has both distances equal to \(3\).

For the symmetry statement, coordinate reversal is the involution \((1\ 4)(2\ 3)\). Its centralizer in the coordinate permutation group has order \(8\). The Watson--Crick complement is the alphabet involution \((A\ T)(C\ G)\), whose centralizer in the alphabet permutation group also has order \(8\); because the GC-content is exactly half the word length, all eight such alphabet permutations preserve GC-content two. The resulting direct action has \(64\) elements. The verifier applies every group element to every maximum code, checks closure in the set of maxima, and computes orbit sizes \(32\) repeated twelve times and \(64\) repeated twice.
## Verification
Run `python verify.py`. A successful replay prints a line beginning `VERIFY_OK` and reports `eligible_vertices=72`, `edges=1168`, `maximal_cliques=2240`, `maximum=6`, `labeled_maxima=512`, `group_size=64`, `orbits=14`, and `orbit_sizes=32x12,64x2`. The packaged `verification_output.txt` is the output of a fresh replay of the packaged verifier.
## Relationship to prior work
King defines \(A_{4}^{GC,RC}(n,d,w)\) using exactly the constant-GC, Hamming-distance, and reverse-complement constraints used here. His Table 1 records the exact value \(A_{4}^{GC,RC}(4,3,2)=6\), with optimality certified by the paper's upper-bound machinery. The same paper is construction- and bound-focused and does not give an equality-case census for this parameter. Aboluion, Smith, and Perkins later study linear, additive, coset, and shortening constructions under the same types of constraints and describe obtaining many best codes, but their published abstract does not state the \(512\)-extremizer census, the universal matching structure, or the orbit decomposition claimed here.

Targeted searches for the exact parameter, the number \(512\), equality cases, and symmetry/orbit classifications did not locate a published statement implying this classification. This is evidence of non-coverage, not a proof that no unindexed enumeration exists.
## Limitations
The result is finite and parameter-specific: it concerns only length \(4\), GC-content \(2\), and threshold \(3\). It does not classify larger parameters, thermodynamic constraints beyond GC-content, or the full automorphism group of the compatibility graph. The originality assessment retains a residual risk of an obscure or unindexed finite census.
## References
1. O. D. King, “Bounds for DNA codes with constant GC-content,” arXiv:math/0306197v1, first public 2003-06-12; Electronic Journal of Combinatorics 10 (2003), R33, DOI 10.37236/1726.
2. N. Aboluion, D. Smith, and S. Perkins, “Linear and nonlinear constructions of DNA codes with Hamming distance d, constant GC-content and a reverse-complement constraint,” Discrete Mathematics 312 (2012), 1062–1075, DOI 10.1016/j.disc.2011.11.021.
