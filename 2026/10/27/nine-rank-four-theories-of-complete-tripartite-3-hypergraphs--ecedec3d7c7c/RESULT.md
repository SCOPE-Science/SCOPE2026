# Nine rank-four theories of complete tripartite 3-hypergraphs

## Finding
Let \(H(a,b,c)\) be the complete \(3\)-uniform tripartite hypergraph with three nonempty, unlabelled parts of sizes \(a,b,c\ge1\). Its sole nonlogical relation is a symmetric ternary predicate \(E\), true exactly on triples with one vertex in each part; equality is available. Write \(\tau(a,b,c)\) for the increasing rearrangement of \((\min(a,3),\min(b,3),\min(c,3))\), and define \(\rho(2,3,3)=(2,2,3)\), while \(\rho\) fixes every other increasing triple in \(\{1,2,3\}^3\).

Then for every two positive triples \((a,b,c)\) and \((a',b',c')\),
\[
H(a,b,c)\equiv_4 H(a',b',c')\quad\Longleftrightarrow\quad
\rho(\tau(a,b,c))=\rho(\tau(a',b',c')).
\]
Here \(\equiv_4\) means agreement on **all** ordinary first-order sentences of quantifier rank at most four. Exactly nine theories occur, with unique lexicographically smallest part-size representatives
\[
(1,1,1),\ (1,1,2),\ (1,1,3),\ (1,2,2),\ (1,2,3),\ (1,3,3),\ (2,2,2),\ (2,2,3),\ (3,3,3).
\]
Every such hypergraph has a rank-four-equivalent member of the family on at most nine vertices, and nine is the optimal bound **within this family**. In particular, distinct vertex counts and different part-size multiplicities need not be detected: \(H(2,2,3)\equiv_4 H(2,3,3)\).

## Assumptions and scope
The universe is finite and nonempty. The three parts are all nonempty; parts are not named by predicates and are interchangeable. The ternary relation has no repeated-coordinate edges, is invariant under permutations of the three arguments, and contains every transversal triple. No graph adjacency, counting, arithmetic, order, constants, or part labels are in the signature. Quantifier rank counts nesting, rather than the number of quantifier occurrences. No assertion is made about arbitrary multipartite hypergraphs with more than three parts, incomplete hypergraphs, or other ranks.

## Proof
**1. Uniform reduction to twenty cases.** For any positive triple \(\mathbf n\), let \(\mathbf n^{[4]}\) be its coordinatewise truncation at four. Duplicator wins the four-round Ehrenfeucht--Fraïssé game between \(H(\mathbf n)\) and \(H(\mathbf n^{[4]})\). Match their three parts in the natural way. Whenever Spoiler repeats a previously selected vertex, repeat its mate. For a new vertex in a given part, select an unused vertex in the matching part. If the truncated part has fewer than four vertices, the two matching parts have the same size; otherwise each has at least four vertices and fewer than four total pairs have previously been selected. Thus the reply always exists. Equalities and the property that three selected vertices belong to three distinct parts are preserved, hence so is every atomic formula. Reordering the parts yields precisely the \(\binom{6}{3}=20\) nondecreasing triples with coordinates in \(\{1,2,3,4\}\). It suffices to classify these twenty structures.

**2. Exact finite rank-four recursion.** For a tuple \(\bar v\) in any finite ternary structure, let \(A(\bar v)\) be its complete atomic diagram: every equality comparison and every ternary-relation truth value on the tuple. Because the relation in this family is symmetric and irreflexive, it is sufficient to record equality for unordered pairs of tuple positions and \(E\) on unordered triples of **distinct** tuple positions; all other atomic instances are predetermined. Define recursively
\[
T_0(\bar v)=A(\bar v),\qquad
T_{r+1}(\bar v)=\left(A(\bar v),\{T_r(\bar v\mathbin{\frown}w):w\in V\}\right).
\]
By induction on \(r\), two tuples have equal \(T_r\) if and only if Duplicator can answer every next choice in either structure for \(r\) further rounds: the sets of extension types give exactly the back-and-forth condition, and \(T_0\) states atomic agreement. Consequently the empty-tuple \(T_4\) values classify all rank-four sentences. The code `verify_complete_tripartite.py` implements this complete recursion two independent ways: directly over every vertex, and using all orbit representatives obtained by tracking which vertices from each part have already appeared. The full-vertex version does not assume the orbit reduction. Each branch and each atom needed by the recursion is explicitly enumerated.

**3. Exhaustive twenty-case certificate.** The following table is the **complete** partition of the twenty truncated nondecreasing input triples computed by both implementations. Each row is one \(T_4\)-type; signatures from different rows are unequal.

| Rank-four type | All nondecreasing triples with parts at most four | Smallest triple |
| --- | --- | --- |
| 1 | \((1,1,1)\) | \((1,1,1)\) |
| 2 | \((1,1,2)\) | \((1,1,2)\) |
| 3 | \((1,1,3)\), \((1,1,4)\) | \((1,1,3)\) |
| 4 | \((1,2,2)\) | \((1,2,2)\) |
| 5 | \((1,2,3)\), \((1,2,4)\) | \((1,2,3)\) |
| 6 | \((1,3,3)\), \((1,3,4)\), \((1,4,4)\) | \((1,3,3)\) |
| 7 | \((2,2,2)\) | \((2,2,2)\) |
| 8 | \((2,2,3)\), \((2,2,4)\), \((2,3,3)\), \((2,3,4)\), \((2,4,4)\) | \((2,2,3)\) |
| 9 | \((3,3,3)\), \((3,3,4)\), \((3,4,4)\), \((4,4,4)\) | \((3,3,3)\) |

The table is equivalent to the stated \(\rho\circ\tau\) rule. For two arbitrary hypergraphs, the four-round reduction followed by the table proves equivalence in the same row and nonequivalence in different rows. This proves both directions for infinitely many part-size triples, without extrapolation from tested sizes.

**4. Sharp representative size.** The nine smallest triples in the table have respective vertex counts \(3,4,5,5,6,7,6,7,9\). Hence nine is a universal family-internal bound. A hypergraph in type 9 must have all three parts of size at least three, as shown by the table plus the uniform reduction, so no member of that type has fewer than nine vertices. This proves optimality.

## Verification
Run `python3 verify_complete_tripartite.py` from the directory containing the supplied script. The script first constructs all twenty truncated part-size triples, computes their complete rank-four Hintikka signatures by an orbit-compressed recursion and by a separate full-vertex recursion, and asserts that the resulting partitions coincide. It checks the nine explicit type rows, pairwise differentiation, and the sharp representative. Additional tests sample part sizes up to ten; they are consistency checks rather than the justification of the infinite theorem. Its recorded output is supplied in `verification_output.txt` and ends in `VERIFY_OK`. The all-size step is the uniform Duplicator strategy proved above, and the twenty-case step is an exhaustive finite proof via an openly specified decidable recursion.

## Relationship to prior work
The first-order and game-theoretic viewpoint is classical. Pikhurko, Veith, and Verbitsky (arXiv:math/0311041, especially Section 9) give general bounds on the first-order distinguishability and definability of uniform hypergraphs, but not an exact nine-type rank-four classification of these complete tripartite structures. Kiani and Saeedi Madani (arXiv:1402.2469) define complete multipartite hypergraphs and characterize algebraic properties of their edge ideals, not their bounded-depth logical theories.

Exact results for complete multipartite **graphs** work in a binary adjacency signature, in which belonging to the same part is quantifier-free definable. By contrast, the present signature contains **only** the ternary transversal-edge relation, and the loss of the binary part relation matters: the three-part profiles \((2,2,3)\) and \((2,3,3)\) have **distinct rank-four theories in the binary graph signature** yet the same rank-four theory in the ternary-only signature. To see the binary distinction, write \(F(x,y):=(x=y)\lor\neg A(x,y)\) for same-part membership in the complete multipartite graph. A rank-four sentence chooses two points \(x,y\) from distinct parts and, with two further nested existential quantifiers in **each of two separate conjuncts**, requires that each chosen part contain two further distinct points; it asserts that at least two parts have size at least three. This holds for \((2,3,3)\) but not \((2,2,3)\). In fact, in these tripartite hypergraphs same-part membership itself can be defined by the rank-one formula \(F(x,y):=\neg\exists z\,E(x,y,z)\): vertices from different parts admit a witness in the third nonempty part, while same-part pairs do not. This quantifier cost explains why translating a binary-graph rank-four distinction need not produce a ternary sentence of rank four. Thus the binary-graph results provide useful context but do not directly imply this nine-class classification or its nontrivial merger.

## Limitations
The claim is restricted to exactly three nonempty unlabelled parts and one symmetric ternary hyperedge relation. The finite twenty-case table is supported by two executable exact recursions; a handwritten closed-form family of all separating sentences is not supplied, although the recursion constructs characteristic formulas of rank four. No claim of independent external audit, exhaustive originality certification, or the absence of unpublished equivalents is made. A previously unindexed specialization of hypergraph Ehrenfeucht--Fraïssé theory remains a literature risk.

## References
1. Oleg Pikhurko, Helmut Veith, and Oleg Verbitsky, *The First Order Definability of Graphs: Upper Bounds for Quantifier Rank*, arXiv:math/0311041, first submitted 2003-11-04, especially Section 9 on uniform hypergraphs.
2. Dariush Kiani and Sara Saeedi Madani, *The Edge Ideals of Complete Multipartite Hypergraphs*, arXiv:1402.2469, first submitted 2014-02-11, especially Section 2 and Proposition 2.1.
3. Oleg Pikhurko and Oleg Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first submitted 2010-03-25.
