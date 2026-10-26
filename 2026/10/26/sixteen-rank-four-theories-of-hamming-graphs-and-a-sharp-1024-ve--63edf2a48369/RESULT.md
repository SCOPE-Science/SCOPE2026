# Sixteen rank-four theories of Hamming graphs and a sharp 1024-vertex representative

## Finding

For integers \(d,e\ge 1\) and alphabet sizes \(q,r\ge 2\), let \(H(d,q)\) be the graph of all length-\(d\) words over a \(q\)-letter alphabet, adjacent exactly when their Hamming distance is one. Write \(\equiv_4\) for agreement on **every** first-order sentence of quantifier rank at most four in the pure adjacency-and-equality language. Then

\[
H(d,q)\equiv_4 H(e,r)
\iff
\min(q,4)=\min(r,4)\quad\text{and}\quad
\begin{cases}
\min(d,6)=\min(e,6),&q=r=2,\\
\min(d,5)=\min(e,5),&q,r\ge3.
\end{cases}
\]

Thus the family has exactly **16** rank-four theories: six at alphabet size two, five at alphabet size three, and five shared by every alphabet size at least four. Every class has a representative within the family on at most \(1024\) vertices. The bound is sharp: the last class has smallest representative \(H(5,4)\), with \(4^5=1024\) vertices.

## Assumptions and scope

The graph is finite, nonempty, undirected, simple, and has no named vertices, coordinate predicates, distance predicates, order or counting quantifiers. Quantifier rank means maximum nesting depth, not total number of quantified variables. In \(H(d,q)\), both parameters are positive integers with \(d\ge1\), \(q\ge2\), and the alphabet need not be a finite field.

## Proof

**1. Complete logical types.** For an ordered tuple \(\bar a\) of selected vertices, define \(T_0(\bar a)\) as the equality/adjacency diagram of its entries. Recursively put
\[
T_{s+1}(\bar a)=\bigl(T_0(\bar a),\{T_s(\bar a,x):x\in H(d,q)\}\bigr).
\]
By induction on formulas, equality of these objects is precisely agreement on all formulas of quantifier rank at most \(s\) with free tuple \(\bar a\). Equivalently, it is the standard back-and-forth characterization of an \(s\)-round Ehrenfeucht--Fraïssé game. The theorem concerns \(T_4(())\).

**2. Coordinate orbits.** The permutations of coordinates and independent permutations of the alphabet in each coordinate act by graph automorphisms. For three selected words, a coordinate is determined, up to these automorphisms, by the equality partition of the three symbols, encoded canonically as `000`, `001`, `010`, `011`, or `012`. The last pattern is absent when \(q=2\). Their multiplicities completely determine the ordered-triple orbit. Two selected words are similarly described by the number \(t\) of different coordinates, with \(d-t\) equal coordinates. This observation does **not** presume that graph automorphism orbits equal logical types: it only gives exhaustive representatives from which the logical types are evaluated.

**3. A finite rank-one reduction for triples.** The atomic diagram of a triple records each of its three pairwise Hamming distances clipped at two (zero is equality, one adjacency, and two means nonadjacency). For a further vertex \(x\), record its three Hamming distances to the triple, likewise clipped at two. Start from \((0,0,0)\). At each coordinate of pattern \(p\), add one of the three-bit difference vectors obtained by making \(x\)'s letter equal to a symbol already occurring in \(p\); when the alphabet has an unused fourth choice relative to the symbols of \(p\), also allow \((1,1,1)\). Clip each running coordinate at two. These 27 possible distance states, together with the old atomic diagram, exactly determine \(T_1\) of the triple.

For any starting state among these 27, the transition relation after \(c\) coordinates of pattern \(p\) is **unchanged** when \(c\) is replaced by \(c+1\) at the following thresholds:

| Alphabet | `000` | `001`/`010`/`011` | `012` |
| --- | ---: | ---: | ---: |
| \(q=2\) | 2 | 4 | impossible |
| \(q=3\) | 2 | 3 | 3 |
| \(q\ge4\) | 2 | 3 | 3 |

This is an exact finite transition identity, not a numerical extrapolation. The executable verifier checks each relation equality over **all 27 initial states** using exhaustive Boolean-state transitions. Transitions for distinct coordinate patterns commute because truncated coordinatewise addition is commutative. Hence \(T_1\) of triples depends only on the five multiplicities capped at their tabulated thresholds, for every number of coordinates. Moreover every alphabet \(q\ge4\) has exactly the same possible new-coordinate difference vectors at tuple length at most three.

**4. A finite rank-two reduction for pairs.** When a third word is chosen, coordinates where the old pair agrees split between patterns `000` and `001`; coordinates where it differs split among `010`, `011`, `012`, with `012` forbidden for binary alphabets. If child classes have rank-one caps \(c_1,\dots,c_b\), the set of their capped multiplicity vectors obtainable from a parent count \(N\) depends only on \(\min(N,\sum_i c_i)\): below the sum the total determines the possibilities, and at or above the sum at least one child is saturated and can absorb every extra coordinate. Conversely every vector with a saturated child can be so lifted.

It follows that the exact \(T_2\) of a pair at Hamming distance \(t\) depends only on
\[
\begin{cases}
\bigl(\min(d-t,6),\min(t,8)\bigr),&q=2,\\
\bigl(\min(d-t,5),\min(t,9)\bigr),&q\ge3.
\end{cases}
\]
These vectors also recover the old pair atomic diagram, since the distance is distinguished as zero, one, or at least two.

**5. Infinite stabilization and exhaustive finite boundary.** Every Hamming graph is vertex-transitive, so \(T_4(())\) is determined by the set of \(T_2\) types of ordered pairs (equivalently the unique \(T_3\) vertex type). For \(d\ge14\), the set of capped pair-count vectors in step 4 is independent of \(d\): the two caps add to fourteen in both alphabet regimes. Thus the dimension need only be checked through fourteen, and the alphabet only through representatives two, three and four.

The exact finite logical-type computation in `verify.py` exhausts all \(42\) parameter cases \(q\in\{2,3,4\}\), \(1\le d\le14\). It compares the full nested logical-type objects rather than truncated hashes. Its output gives six distinct types for \(q=2\), stabilizing at \(d=6\); five for \(q=3\) and five for \(q\ge4\), both stabilizing at \(d=5\); and **no coincidences between these three alphabet regimes**. By the previous paragraphs, these 42 checks entail the asserted classification for all infinitely many parameters.

**6. Sharpness.** The sixteen exact logical types have their smallest parameter representatives at \((q,d)=(2,1),\dots,(2,6)\), \((3,1),\dots,(3,5)\), and \((4,1),\dots,(4,5)\). The largest corresponding vertex count is \(4^5=1024\). Every other member in the last logical class has alphabet at least four and dimension at least five, so it has at least \(1024\) vertices. This proves optimality within the Hamming graph family.

## Verification

Run `python3 verify.py` using standard-library Python. The program checks the critical 27-state transition-cap identities, enumerates all 42 finite-boundary logical profiles with exact nested type comparison, and compares its results against a **separate graph-level quantifier-rank recursion** on nine explicitly enumerated small Hamming graphs (81 ordered equivalence comparisons). `verification_output.txt` is the recorded output and finishes with `VERIFY_OK`. The program uses SHA-256 *only to display abbreviated identifiers* for exact objects; no proof or comparison rests on a hash collision assumption.

## Relationship to prior work

The Hamming graph construction and its coordinate automorphisms are classical; Jones (2010, §2) states the full wreath-product symmetry, but studies regular surface embeddings rather than quantifier-rank equivalence. Pikhurko and Verbitsky (2010/2011, §§1,3--4) describe first-order graph logical depth and Ehrenfeucht games, but not this Hamming-parameter classification. Benediktsson, Macpherson and Adler (2020, §4, especially Theorems 4.6--4.8) determine adjacency-neighborhood VC-dimension and VC-density for Hamming graphs, a distinct invariant that does not imply the sixteen rank-four logical classes or the 1024-vertex bound. An earlier separate result on binary hypercubes establishes the \(q=2\) subcase; the new content here is the full two-parameter classification, including the ternary-versus-larger-alphabet separation and the new, different dimension stabilization threshold.

## Limitations

The theorem is only about first-order **quantifier rank four** and only within the indicated Hamming-graph family. It does not classify quantifier rank five, counting logic, arbitrary induced subgraphs, or structures with named coordinates. The finite computations alone do not establish the infinite assertion: the transition-cap and pair-splitting reductions above are essential. A plausible residual originality risk is an equivalent unindexed logical classification, although none emerged in the literature comparisons described in `REVIEW.md`.

## References

1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (first public preprint March 25, 2010); *Contemporary Mathematics* 558 (2011), 129--180. https://arxiv.org/abs/1003.4865
2. G. A. Jones, *Classification and Galois conjugacy of Hamming maps*, arXiv:1006.0516 (first public preprint June 2, 2010), §2. https://arxiv.org/abs/1006.0516
3. B. G. Benediktsson, D. Macpherson and I. Adler, *Vapnik--Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (first public preprint July 31, 2020), §4. https://arxiv.org/abs/2007.16042
4. A. E. Brouwer, *Hamming graphs*, distance-regular graph reference page. https://aeb.win.tue.nl/drg/graphs/Hamming.html
