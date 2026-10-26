# Nine rank-three theories of mixed Hamming graphs

## Finding

For every finite nonempty sequence \(\mathbf q=(q_1,\ldots,q_d)\) of integers \(q_i\ge2\), let
\[
G(\mathbf q)=K_{q_1}\square\cdots\square K_{q_d}.
\]
Its vertices are coordinate strings and two distinct vertices are adjacent exactly when they disagree in one coordinate. The language has equality and one undirected adjacency relation, with no named vertices, coordinates, or factor predicates. Write \(G\equiv_3H\) when \(G\) and \(H\) satisfy the same first-order sentences of quantifier rank at most three.

**Theorem.** There are exactly **nine** \(\equiv_3\)-classes among all \(G(\mathbf q)\). They are specified by the following mutually exclusive conditions, where a *binary factor* has size two and a *nonbinary factor* has size at least three.

| Class | Conditions | Smallest product representative | Number of vertices |
| --- | --- | --- | ---: |
| 1 | \(d=1\), binary | \(K_2\) | 2 |
| 2 | \(d=1\), nonbinary | \(K_3\) | 3 |
| 3 | \(d=2\), both binary | \(K_2\square K_2\) | 4 |
| 4 | \(d=2\), exactly one binary | \(K_2\square K_3\) | 6 |
| 5 | \(d=3\), all binary | \(K_2\square K_2\square K_2\) | 8 |
| 6 | \(d=2\), both nonbinary | \(K_3\square K_3\) | 9 |
| 7 | \(d\ge3\), both binary and nonbinary factors present | \(K_2\square K_2\square K_3\) | 12 |
| 8 | \(d\ge4\), all binary | \(K_2\square K_2\square K_2\square K_2\) | 16 |
| 9 | \(d\ge3\), all nonbinary | \(K_3\square K_3\square K_3\) | 27 |

Therefore every graph in the family has a rank-three equivalent member on at most **27 vertices**, and no smaller bound works within this family. In particular the nonisomorphic graphs \(K_2\square K_2\square K_3\) and \(K_2\square K_3\square K_3\) are rank-three equivalent.

## Assumptions and scope

All graphs are finite, nonempty, simple, and undirected. Each Cartesian factor has at least two vertices; no factors of order one are retained. Factors may have unequal orders. The theorem concerns unrestricted first-order sentences of *quantifier rank* at most three, not three-variable logic, counting logic, or theories with named coordinate relations. The sharp 27-vertex bound is internal to the specified family, not a universal minimum among arbitrary finite graphs.

## Proof

**1. Complete rank-three invariant.** For an ordered pair \((x,y)\), record its atomic equality/adjacency relation and the set of all atomic diagrams realized by \((x,y,z)\) as \(z\) ranges over the graph. This is exactly its one-round extension type: with one move remaining, the two pointed structures are equivalent precisely when these sets agree. With two remaining moves after selecting \(x\), its type is the set of the resulting ordered-pair extension types, along with the trivial atomic type of the singleton. Coordinatewise permutations act transitively on the vertices of each product. Consequently its empty-tuple rank-three type is determined exactly by the **set of realized ordered-pair extension types**. This is the standard three-move back-and-forth recursion and applies to either starting structure.

For \(x\ne y\), the diagrams with \(z=x\) or \(z=y\) are already specified by equality and whether \(x\) and \(y\) are adjacent. Among third vertices distinct from both, only four adjacency patterns are possible, indexed by whether \(z\) is adjacent to both, exactly one, or neither of \(x,y\). The two patterns adjacent to exactly one have the same positive/zero status by the coordinate symmetry interchanging \(x\) and \(y\). Thus the positive/zero statuses of three counts—\(11\), \(10\), and \(00\)—determine the complete extension type. The diagonal pair \(x=y\) is governed by the existence of a vertex nonadjacent to \(x\).

**2. Exact extension counts.** Put \(N=\prod_iq_i\) and \(\Delta=\sum_i(q_i-1)\). Every vertex has degree \(\Delta\). For distinct vertices, the following table gives, in order, the number of third vertices adjacent to both, to \(x\) but not \(y\), and to neither. All counted third vertices are distinct from \(x,y\).

| Pair type | \(11\) | \(10\) | \(00\) |
| --- | ---: | ---: | ---: |
| Adjacent; differing coordinate \(i\) | \(q_i-2\) | \(\Delta-1-(q_i-2)\) | \(N-2\Delta+q_i-2\) |
| Hamming distance two | \(2\) | \(\Delta-2\) | \(N-2\Delta\) |
| Hamming distance at least three | \(0\) | \(\Delta\) | \(N-2-2\Delta\) |

Indeed, adjacent vertices have \(q_i-2\) common neighbors, obtained by changing their differing coordinate to a third symbol. Two vertices at distance two have exactly two common neighbors, obtained by correcting either differing coordinate; vertices at greater distance have none. Subtracting these overlaps from the two degree-\(\Delta\) neighborhoods yields the other columns. The diagonal pair admits a distinct nonneighbor precisely when \(N-1-\Delta>0\).

**3. Complete sign analysis.** Let \(F=N-2\Delta\). For \(d=1\), the graph is complete and the only variation is whether \(q_1-2\) vanishes. For \(d=2\), writing the factor sizes as \(a,b\),
\[
F=(a-2)(b-2),\qquad \Delta-2=a+b-4.
\]
These identities give exactly the three two-factor classes in the table, according as zero, one, or two factors are nonbinary. The diagonal nonneighbor condition holds for every \(d\ge2\).

For \(d\ge3\), \(F\ge2\), with equality exactly when \(d=3\) and every factor is binary. To see this, start with three binary factors, where \(N=8\), \(\Delta=3\), and \(F=2\). Increasing one factor by one raises \(F\) by the product of the remaining factor sizes minus two, which is at least two. Adding a factor of size \(s\ge2\) raises \(F\) by \((s-1)(N-2)>0\). Consequently all adjacent-pair \(00\) counts and all distance-two \(00\) counts are positive, and the distance-at-least-three \(00\) count is zero exactly for the binary three-cube. Adjacent pairs have common neighbors exactly in the nonbinary directions; all their \(10\) counts are positive for \(d\ge2\). At distance two the \(10\) count is positive except in the binary square; at distance at least three it is always positive.

A distance-at-least-three pair exists exactly when \(d\ge3\). Its \(00\) flag, the existence of binary/nonbinary edge directions, and the two-factor boundary flags now give precisely the four classes with \(d\ge3\) shown above. Together with the one- and two-factor cases, this yields nine pair-extension signature sets. They are pairwise distinct: completeness distinguishes one-factor cases; the common-neighbor flag distinguishes a binary from a nonbinary direction; the distance-two \(10\)/\(00\) flags separate the two-factor cases; and for higher dimensions the presence of distance-at-least-three pairs and their \(00\) flag isolates the binary three-cube. When both factor types occur, the set contains both edge-direction profiles; this distinguishes it from all-binary or all-nonbinary cases. Hence, by step 1, the nine signatures are exactly the rank-three equivalence classes.

For complete transparency, write \(E_{abc}\) for an *adjacent* pair having positivity flags \((11,10,00)=(a,b,c)\), and \(N_{abc}\) for a *nonadjacent distinct* pair. The full sets of distinct-pair profiles in class order are:

| Class | Realized ordered-pair profiles (excluding the diagonal) |
| --- | --- |
| 1 | \(E_{000}\) |
| 2 | \(E_{100}\) |
| 3 | \(E_{010},N_{100}\) |
| 4 | \(E_{010},E_{111},N_{110}\) |
| 5 | \(E_{011},N_{111},N_{010}\) |
| 6 | \(E_{111},N_{111}\) |
| 7 | \(E_{011},E_{111},N_{111},N_{011}\) |
| 8 | \(E_{011},N_{111},N_{011}\) |
| 9 | \(E_{111},N_{111},N_{011}\) |

The diagonal extension type has a distinct nonneighbor in classes 3–9 but not in classes 1–2. This explicit table also verifies pairwise distinctness without any appeal to computation.

To see directly that every distinct signature can be separated by rank-three sentences, describe a particular ordered-pair type by a conjunction of its atomic pair relation and, for each of the four possible third-vertex adjacency patterns, an existential or negated existential statement for a distinct third vertex. Prefixing with \(\exists x\exists y\) yields rank at most three. Any pair-extension type present in only one signature provides a separating sentence.

**4. Sharp representatives.** Minimizing the product \(\prod_iq_i\) subject to each of the nine class conditions gives respectively \(2,3,4,6,8,9,12,16,27\), attained by the listed products. Distinct classes cannot share a representative by step 3, so the largest of these minima, 27, is the sharp internal kernel size.

## Verification

The standalone program `verify_mixed_hamming_rank3.py` independently enumerates all vertices of small products and constructs the full atomic diagram set of every triple \((x,y,z)\) with a fixed first vertex. Vertex transitivity makes one fixed first vertex sufficient. It compares those directly enumerated three-round signatures to a separately implemented closed-form positive/zero profile. It also checks the nine class representatives and symbolically verifies the parameter classification across 6,434 tuples of factor sizes. Run:

```text
python3 verify_mixed_hamming_rank3.py
```

The expected run output is embedded in `verification_output.txt`. The infinite conclusion is established by the proof above; neither finitely many examples nor the code are a substitute for the inequalities in step 3.

## Relationship to prior work

Cartesian products of complete graphs and their combinatorics are classical. Jacobson, Niedermaier, and Reiner analyze their critical groups. Klavžar and Peterin study their embedding and subgraph characterization. Fisher and Isaak's accessible full text, including its principal theorem and final product-graph discussion, determines distinguishing colorings and automorphism-related invariants for products of two cliques; it does not state a first-order rank-three classification. Those properties do not imply the present logical equivalence result. A separate recorded rank-four classification for equal-size Hamming factors only covers the homogeneous subfamily; a separate rank-all-depth classification for products of exactly two cliques only covers \(d=2\). Neither statement by itself determines what happens with arbitrarily many *unequal* factors, particularly the mixed binary/nonbinary class and its sharp 12-vertex representative.

## Limitations

No claim is made about ranks four and above for arbitrary mixed factors, about counting or variable-bounded logics, or about arbitrary graph products. The novelty comparison is based on inspected accessible material and searched research records, not a proof that unindexed literature contains no equivalent theorem. The full text of two older graph-theoretic articles was not accessible for line-by-line comparison; their visible abstracts concern different invariants. Independent scientific validation has not been performed.

## References

1. B. Jacobson, A. Niedermaier, and V. Reiner, *Critical groups for complete multipartite graphs and Cartesian products of complete graphs*, Journal of Graph Theory 44 (2003), 231–250, DOI:10.1002/jgt.10139 (first verified online 2003-10-01).
2. S. Klavžar and I. Peterin, *Characterizing subgraphs of Hamming graphs*, Journal of Graph Theory 49 (2005), 302–312, DOI:10.1002/jgt.20084 (first online 2005-04-08).
3. M. J. Fisher and G. Isaak, *Distinguishing colorings of Cartesian products of complete graphs*, arXiv:math/0607465 (submitted 2006-07-19), full HTML at https://arxiv.org/html/math/0607465v1.
