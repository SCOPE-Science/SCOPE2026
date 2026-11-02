# Exact size enumerator and maximal faces of binary diameter-two anticodes

## Finding

For every integer \(n\geq3\), let \(\mathcal A_n\) be the collection of all (including empty) subsets \(S\subseteq\{0,1\}^n\) with \(d_H(x,y)\leq2\) for every \(x,y\in S\). Write \(F_n(z)=\sum_{S\in\mathcal A_n}z^{|S|}\). Then

\[
\begin{aligned}
F_n(z)={}&1+2^n z+2^{n-1}\left(n+\binom n2\right)z^2\\
&+2^n\left(\binom n2+\binom n3\right)z^3
+2^n\sum_{j=4}^{n+1}\binom{n+1}{j}z^j\\
&+2^{n-2}\left(\binom n2+\binom n3\right)z^4.
\end{aligned}
\]

The complete number of binary diameter-at-most-two anticodes is therefore

\[
|\mathcal A_n|=1+2^{2n+1}+2^{n-2}\left(\binom n3-\binom n2-6n-4\right)
=2\cdot4^n\bigl(1+o(1)\bigr).
\]

The inclusion-maximal members of \(\mathcal A_n\) are exactly the following three classes: radius-one Hamming balls; four-point coordinate squares; and four-point affine even-parity planes supported on three coordinates. The three classes have respectively \(2^n\), \(2^{n-2}\binom n2\), and \(2^{n-2}\binom n3\) distinct members. Their cardinality enumerator is

\[
M_n(z)=2^n z^{n+1}+2^{n-2}\left(\binom n2+\binom n3\right)z^4.
\]

Every anticode with at least four elements belongs to a **unique** inclusion-maximal anticode. (Small anticodes need not have unique maximal extensions.)

## Assumptions and scope

Vectors are in the binary cube \(V=\mathbb F_2^n\), with addition componentwise modulo two and Hamming distance the number of unequal coordinates. Let \(e_i\) denote the \(i\)-th standard unit vector, and let \(B(c)=\{c\}\cup\{c+e_i:1\leq i\leq n\}\). For \(i<j\) define a coordinate square \(F(a;i,j)=\{a,a+e_i,a+e_j,a+e_i+e_j\}\). For \(i<j<k\), define a parity plane \(P(a;i,j,k)=\{a,a+e_i+e_j,a+e_i+e_k,a+e_j+e_k\}\). All these sets have pairwise distance at most two. The symbols \(F\) and \(P\) denote subsets, not a particular choice of base vertex \(a\). Different base vertices can describe the same set. Every anticode means diameter **at most** two (not necessarily exactly two). All displayed counts concern subsets of a labelled coordinate cube and do not identify symmetry-related subsets.

## Proof

**Classification.** Let \(S\) be a nonempty anticode. Translate by any \(x\in S\) so that \(0\in S\). Every nonzero element then has support of size one or two. The two-element supports form an intersecting family \(E\) of graph edges on the coordinate set, since disjoint supports would give Hamming distance four. A family of pairwise intersecting two-element subsets is either a star (all edges share a coordinate) or a triangle; with only one edge the star case is handled separately.

If \(E\) is empty, all members are \(0\) and unit vectors, hence \(S\subseteq B(0)\). If \(E\) consists of the single edge \(\{i,j\}\), then any singleton support must be \(\{i\}\) or \(\{j\}\), hence \(S\subseteq F(0;i,j)\). If \(E\) is a star with at least two edges, every permissible singleton support must be its common center \(i\); each member is either \(0\), \(e_i\), or \(e_i+e_j\), so \(S\subseteq B(e_i)\). Finally, if \(E\) is a triangle on \(\{i,j,k\}\), no singleton support meets all three edges, so \(S\subseteq P(0;i,j,k)\). Thus every anticode is contained in a member of one of the three stated classes.

**Maximality and distinctness.** Each \(B(c)\) is maximal for \(n\geq3\). Translate \(c\) to zero: a candidate outside \(B(0)\) within distance at most two of \(0\) must have weight two, but it then has distance three from some \(e_k\) outside its two-coordinate support. A square \(F(a;i,j)\) is maximal because any vector differing from \(a\) outside coordinates \(i,j\) has distance at least three from one of its four corners; all vectors supported entirely within these two coordinates are already in the square. A parity plane \(P(a;i,j,k)\) is maximal since an odd-parity triple has distance three from one of its four even-parity triples, and any nonzero coordinate outside the triple similarly forces distance at least three from one of those four triples. Thus the three classes list **all** inclusion-maximal anticodes.

A ball \(B(c)\) has \(n+1\) vertices, and distinct centers give distinct balls: the center is the unique vertex adjacent by cube edges to the other \(n\) vertices for \(n\geq3\). Coordinate squares are determined uniquely by their two varying coordinate directions and fixed values in the other \(n-2\) coordinates, giving \(2^{n-2}\binom n2\) squares. Parity planes are determined uniquely by their three varying coordinates, the fixed \(n-3\) coordinates, and one of two parity classes, giving \(2^{n-2}\binom n3\) planes. The classes are disjoint: the cube-edge graph on a square is a four-cycle, on a parity plane has no edges, and on a ball is a star.

Distinct balls intersect in at most two vertices: their centers have distance one, two, or at least three. Neither a square nor a parity plane is contained in any ball. A square cannot be contained in a ball because its cube-edge graph has a four-cycle while a ball's cube-edge graph is a star. A parity plane cannot be contained in a ball because its four even-parity triples lack a common Hamming-distance-one neighbor. Finally, two distinct four-point members intersect in at most three points simply because their entire vertex sets are distinct. Hence **any two distinct maximal anticodes meet in at most three vertices**, proving unique extension for every anticode of size at least four.

**Counting faces of size at least four.** A maximal ball contributes \(\binom{n+1}{j}\) subsets of size \(j\). By the uniqueness just proved, none of these subsets is counted through another ball or four-point maximal set. At \(j=4\), each four-point coordinate square and each four-point parity plane contributes exactly one additional anticode. No four-point maximal class contributes when \(j>4\). This gives the last two terms of \(F_n(z)\).

**Counting faces of size at most three.** There is one empty set and \(2^n\) singleton sets. Every cube vertex has \(n+\binom n2\) distinct neighbors at Hamming distance one or two, so there are \(2^{n-1}(n+\binom n2)\) admissible unordered pairs. For an admissible triple containing a specified vertex \(0\), the other two supports can consist of two distinct singletons (\(\binom n2\) choices), one singleton contained in one doubleton (\(2\binom n2\) choices), or two intersecting doubletons (\(3\binom n3\) choices). Thus there are \(3(\binom n2+\binom n3)\) admissible triples through a fixed vertex, and double-counting across the three vertices of every triple gives \(2^n(\binom n2+\binom n3)\). These counts establish the polynomial.

**Total.** Set \(z=1\), use \(\sum_{j=4}^{n+1}\binom{n+1}{j}=2^{n+1}-1-(n+1)-\binom{n+1}{2}-\binom{n+1}{3}\), and simplify with Pascal's identity. The stated closed total follows. Its correction to \(2^{2n+1}\) is of order \(n^3 2^n\), which is negligible relative to \(4^n\).

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It separately enumerates maximal cliques in the graph on the \(2^n\) cube vertices with edges between distinct vertices at Hamming distance at most two (Bron–Kerbosch with a pivot), and verifies that those cliques are exactly the three explicit maximal classes for each \(3\leq n\leq7\). It separately checks the uniqueness of maximal extension for size-at-least-four faces and their claimed coefficients. For \(n=3,4\) it exhaustively tests all \(2^{2^n}\) subsets for the diameter constraint and compares the full coefficients. Observed independent coefficients are \((1,8,24,32,16)\) for \(n=3\) and \((1,16,80,160,120,16)\) for \(n=4\). These tests are finite checks of the proof; the infinite-family statement follows from the symbolic arguments above.

Run using `python3 verify.py`.

## Relationship to prior work

Horlemann and Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces* (arXiv:2610.31618v1, first posted 2026-10-22), prove a general bound for diameter two of \(2^{\Theta(n)}\) in the binary case (Proposition 3.4); their displayed exact formula concerns diameter one. The present statement supplies the exact diameter-two size enumerator, total count, and maximal-subset classification in the binary case. The classical extremal diameter-two bound \(n+1\) (Kleitman's diameter theorem) is assumed as background but not needed for this proof.

Bukh and Saatashvili (arXiv:2507.10828) study maximal fixed-diameter sets in Hamming cubes, proving bounds for their size and structure rather than this all-cardinality polynomial. Adamaszek and Adams (arXiv:2103.01040) determine the homotopy type of the scale-two Vietoris–Rips complex of the cube; a homotopy type does not specify its face counts. Briggs, Feng, and Wells (arXiv:2408.01288) study rigid facets and general scales, including extremal constructions, but do not state this complete scale-two face enumerator. The current formula is equivalently the face-generating polynomial (including the empty face) of \(\operatorname{VR}(Q_n;2)\), and also the clique polynomial of the square of the binary hypercube.

## Limitations

The result is restricted to the binary alphabet, inclusive diameter at most two, and dimensions \(n\geq3\). It is not an exact enumerator for larger diameters or nonbinary Hamming spaces. It counts subsets with coordinate labels fixed, not orbits under the hypercube automorphism group. The prior-art comparison supports an originality assessment but does not establish historical uniqueness; overlooked equivalent formulas under coding-theory, distance-graph, or simplicial-face terminology remain possible. No independent mathematical audit is claimed.

## References

1. A.-L. Horlemann and A. Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces*, arXiv:2610.31618v1 (2026), Proposition 3.4.
2. B. Bukh and N. Saatashvili, *Maximal sets of a given diameter in Hamming cubes*, arXiv:2507.10828 (2025).
3. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (2021), Theorem 1.
4. J. Briggs, Z. Feng, and C. Wells, *Facets in the Vietoris–Rips complexes of hypercubes*, arXiv:2408.01288 (2024).
