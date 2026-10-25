# The cap complex of the quaternary projective plane is a wedge of 750 three-spheres

## Finding

Let \(P=\operatorname{PG}(2,\mathbb F_4)\), whose 21 vertices are its projective points. Let \(\mathcal A(P)\) be the simplicial complex whose faces are all sets of distinct projective points containing no collinear triple (the *cap complex*). Then
\[
\boxed{\mathcal A(P)\simeq\bigvee^{750}S^3.}
\]
In particular, its reduced integral homology is \(\widetilde H_3(\mathcal A(P);\mathbb Z)\cong\mathbb Z^{750}\) and vanishes in every other degree; the claim includes absence of integral torsion. The complex has face vector \((21,210,1120,2520,1008,168)\) in dimensions zero through five.

## Assumptions and scope

The field \(\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)\) has elements \(0,1,\omega,\omega+1\). A projective point is an equivalence class of nonzero triples under scalar multiplication, represented uniquely by the triple whose first nonzero entry is 1. Thus there are 21 points. A projective line is the zero set of a nonzero linear form, likewise represented by a normalized nonzero coefficient triple. Three points are collinear if they lie on one projective line. The claim concerns precisely this finite abstract simplicial complex, not arbitrary projective planes or all extension fields.

## Proof

Represent \(\mathbb F_4\) using the integer labels \(0,1,2,3\), where \(2=\omega\) and \(3=\omega+1\); addition is bitwise exclusive-or, and multiplication is reduction modulo \(\omega^2+\omega+1\). Normalize every nonzero vector of \(\mathbb F_4^3\) as above. Enumerate the 21 normalized point vectors, and use the 21 normalized nonzero covectors to enumerate the 21 projective lines. Each line contains five points; every pair of points belongs to exactly one line. Consequently there are \(21\binom{5}{3}=210\) distinct forbidden collinear triples.

Now enumerate every \(k\)-element subset of the 21 vertices for \(1\le k\le7\). Retain it if and only if none of its triples is forbidden. The exact face counts in cardinalities one through seven are
\[
(21,210,1120,2520,1008,168,0).
\]
Since the no-collinear-triple condition is hereditary, no face of cardinality at least eight exists. These 5047 nonempty faces exhaust the complex. The 168 six-point facets are its hyperovals; the maximal cap size six is consistent with the classical finite-geometric literature.

We next construct an explicit matching on the Hasse diagram of the nonempty face poset. Temporarily adjoin the empty face. Starting with every face unpaired, visit vertices \(v=0,1,\ldots,20\) in the fixed lexicographic enumeration of projective-point triples. For each still-unpaired face \(F\) not containing \(v\), pair it with \(F\cup\{v\}\) if the latter is also a still-unpaired face. At any fixed vertex, such pairs are disjoint, so the internal enumeration order is immaterial. This matches 2149 pairs among the 5048 faces including the empty face. The only unmatched faces are 750 four-element faces (dimension three). The empty face is paired with the first vertex. Discarding that pair and the empty face gives an ordinary matching of 2148 pairs on the 5047 nonempty faces; its critical cells are one vertex and precisely 750 three-dimensional simplices.

It remains to establish *acyclicity*, which is essential: a face count or homology rank alone would not prove the homotopy classification. Orient each unmatched face inclusion \(F\subset G\) of codimension one from \(G\) down to \(F\), and each matched face inclusion upward. There are exactly 19908 directed incidences among 5047 nonempty faces. The standalone program `VERIFY.py` constructs the full directed incidence graph and uses a complete indegree-zero topological sort to verify that all 5047 vertices are processed. Thus the matching is acyclic, by exhaustive verification of the explicitly defined finite graph. The script checks all 5047 vertices, every codimension-one incidence, and the complete matching, not a sample.

Forman's discrete Morse theorem therefore supplies a CW model with exactly one zero-cell, exactly 750 three-cells, and no cells in other positive dimensions. Every three-cell attaches to the zero-cell, so this CW model is a wedge of 750 three-spheres. This proves the claim, including all integral homology statements.

## Verification

`VERIFY.py` is self-contained and requires only Python's standard library. Running `python3 VERIFY.py` exhaustively reconstructs the 21 projective points and 21 lines, checks 210 forbidden triples, tests all subsets through cardinality seven, builds the greedy discrete Morse matching, and confirms that its directed Hasse graph is acyclic. The checked output is embedded as `VERIFY.txt`: `VERIFY_OK`, with 5047 nonempty cells, 2148 matching pairs, one critical vertex, 750 critical three-cells and a 5047-vertex topological sort. The Euler characteristic is independently checked as \(-749=1-750\). No finite experiment is extrapolated to an infinite statement: the theorem's domain is this explicitly enumerated finite complex.

## Relationship to prior work

Hernando and McGuire, *Proof of a Conjecture of Segre and Bartocci on Monomial Hyperovals in Projective Planes* (2010 preprint), treat the finite-geometry of maximal no-three-collinear sets and monomial hyperovals. Bamberg, Glasby, Popiel and Praeger, *Generalised quadrangles and transitive pseudo-hyperovals* (2014 preprint), discuss the regular hyperoval in \(\operatorname{PG}(2,4)\). *Large caps in projective space \(\operatorname{PG}(r,4)\)* (2015) studies cap constructions, completeness and associated codes and gives six as the maximum cap size in the plane. These accessible results provide geometric context and do not state a homotopy classification of the simplicial complex of **all** caps. Knowing the maximum size and the number of hyperovals does not imply the acyclic matching or the integral homotopy type established here.

## Limitations

The statement is for \(\operatorname{PG}(2,\mathbb F_4)\) alone. It does not classify cap complexes in other finite planes, group actions on the homology, or maps under field extensions. The proof is constructive and exhaustively finite, but depends on correct implementation of the specified field operations, face enumeration and acyclicity check. The cited 2015 paper was only partially accessible through indexed section text; a direct full-document fetch failed. No independent scientific audit is claimed, and unindexed coverage cannot be excluded absolutely.

## References

1. Fernando Hernando and Gary McGuire, *Proof of a Conjecture of Segre and Bartocci on Monomial Hyperovals in Projective Planes*, arXiv:1010.3965v1 (first public 2010-10-19), Sections 1–2. https://arxiv.org/html/1010.3965v1
2. John Bamberg, Stephen P. Glasby, Tomasz Popiel and Cheryl E. Praeger, *Generalised quadrangles and transitive pseudo-hyperovals*, arXiv:1406.6445v1 (first public 2014-06-25), Introduction and Proposition 1.2. https://arxiv.org/abs/1406.6445
3. *Large caps in projective space \(\operatorname{PG}(r,4)\)*, *Finite Fields and Their Applications* 35 (2015), 231–246, DOI:10.1016/j.ffa.2015.04.006. Available indexed sections and abstract inspected; full text not established as accessible in this run.
4. Robin Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145, discrete Morse theorem.
