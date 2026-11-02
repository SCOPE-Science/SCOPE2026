# Six sharp four-round theories of binary hypercube graphs

## Finding

Let \(Q_d\), for an integer \(d\ge1\), be the simple graph on \(\{0,1\}^d\), with two words adjacent exactly when their Hamming distance is one. Work in first-order logic with equality and one binary adjacency predicate, with no named coordinates, constants, or distance predicates. For all \(d,e\ge1\),

\[
Q_d\equiv_4 Q_e\quad\Longleftrightarrow\quad
(d=e<6)\ \text{or}\ (d,e\ge6).
\]

Thus this natural family has exactly six distinct quantifier-rank-four theories, represented by \(Q_1,Q_2,Q_3,Q_4,Q_5,Q_6\). Every member has a rank-four equivalent representative with at most \(64\) vertices, and no smaller bound works within the family.

## Assumptions and scope

The equivalence \(\equiv_4\) means agreement on **all** first-order graph sentences of quantifier rank at most four, not merely existential sentences or induced subgraph patterns. Dimensions are positive integers. The graph relation is symmetric and irreflexive. Both repeated choices and mixed quantifier patterns are included in the four-move Ehrenfeucht--Fraïssé characterization.

## Proof

**1. Exact atomic diagrams and tuple types.** For distances \(u\ge0\), put \(s(u)=0\) if \(u=0\), \(s(u)=1\) if \(u=1\), and \(s(u)=2\) if \(u\ge2\). These statuses encode all equality and adjacency atoms. For an ordered tuple of length four, its complete atomic diagram is the six statuses of its pairwise distances, in the fixed pair order \((12,13,23,14,24,34)\).

For any ordered triple \((x,y,z)\) of vertices, a cube automorphism moves \(x\) to the zero word. Let \(c_{ab}\) count coordinates in which \((y,z)=(a,b)\), with \(a,b\in\{0,1\}\). These four nonnegative counts sum to \(d\) and classify the triple up to cube automorphisms. The distances among the original three vertices are

\[
D_{12}=c_{10}+c_{11},\quad D_{13}=c_{01}+c_{11},\quad D_{23}=c_{01}+c_{10}.
\]

Any fourth vertex \(w\) is specified, for the purpose of the three distances to \(x,y,z\), by four integers \(t_{ab}\in[0,c_{ab}]\), where \(t_{ab}\) counts its one-bits within the corresponding coordinate class. If \(T=\sum_{a,b}t_{ab}\), then

\[
D_{14}=T,\quad D_{24}=D_{12}+T-2(t_{10}+t_{11}),\quad
D_{34}=D_{13}+T-2(t_{01}+t_{11}).
\]

Let \(\mathcal T_3(c)\) be the exact **set** of resulting six-status atomic diagrams, over all the indicated integer choices. For a pair whose Hamming distance is \(h\), let

\[
\mathcal T_2(d,h)=\bigl\{\mathcal T_3(d-h-a,a,h-b,b):
0\le a\le d-h,\ 0\le b\le h\bigr\}.
\]

Finally define \(\mathcal T_1(d)=\{\mathcal T_2(d,h):0\le h\le d\}\). By downward induction on the remaining number of moves, \(\mathcal T_3\), \(\mathcal T_2\), and \(\mathcal T_1\) are precisely complete extension types for three, two, and one moves of the four-round game. The empty-tuple type is determined by \(\mathcal T_1(d)\), because \(Q_d\) is vertex-transitive. Therefore

\[
Q_d\equiv_4 Q_e\quad\Longleftrightarrow\quad
\mathcal T_1(d)=\mathcal T_1(e).
\]

All sets above are sets of **types**, not multiplicity multisets; ordinary first-order logic has no counting quantifier. Equal chosen vertices remain included because \(h=0\) and the integer splitting ranges are not restricted to distinct choices.

**2. Four-coordinate saturation for triples.** Define \(\widehat c_{ab}=\min(c_{ab},4)\). Then

\[
\mathcal T_3(c)=\mathcal T_3(\widehat c).
\]

For one direction, take any fourth word in the larger cube. In each coordinate class containing more than four positions, retain exactly four, including up to two positions where the fourth word has bit zero and up to two where it has bit one; fill remaining retained positions arbitrarily. This preserves, truncated at two, both the number of mismatches to bit zero and the number to bit one in that class. Hence it preserves the statuses of the three distances from the fourth word to the original three. Distances among the original three also retain their statuses, because a class of size greater than four is reduced only to size four.

Conversely, start from a fourth word in the truncated cube. If it has distance at most one from at least one of the original three words, fill every restored coordinate by matching that near word. All such near words agree in every truncated class of size four: two near words have mutual distance at most two, whereas differing in such a class would already give distance four. The distances to near words remain at most one, with their exact original values, and all other distances can only increase from at least two. If there is no near word, fill the restored coordinates arbitrarily; all three distances remain at least two. Thus each atomic four-tuple diagram lifts. This proves the claimed saturation identity.

**3. Eight-coordinate saturation for pairs.** Given a pair at distance \(h\), its coordinates split into groups of sizes \(h\) and \(d-h\). Adding a third word partitions each of these groups into two cells. For a group of size \(n\), the set of possible pairs \((\min(a,4),\min(n-a,4))\), as \(a\) ranges from zero to \(n\), depends only on \(\min(n,8)\): the possibilities stabilize when \(n\ge8\). Step 2 therefore implies that \(\mathcal T_2(d,h)\) depends only on

\[
(\min(h,8),\min(d-h,8)).
\]

For every \(d\ge16\), the set of these ordered capped pairs as \(h\) ranges over \(0,\ldots,d\) is exactly

\[
\{(j,8):0\le j\le7\}\ \cup\ \{(8,8)\}\ \cup\
\{(8,j):0\le j\le7\}.
\]

Hence \(\mathcal T_1(d)=\mathcal T_1(16)\) for **every** integer \(d\ge16\). This is the symbolic infinite-stabilization step.

**4. Finite exact boundary.** The bundled `verify_cube_rank4.py` enumerates all four-tuples' atomic-extension types using the integer ranges in Step 1, for every dimension from one through sixteen. It calculates the exact partition

\[
\{1\},\{2\},\{3\},\{4\},\{5\},\{6,7,8,9,10,11,12,13,14,15,16\}.
\]

The verifier performs set construction and exact integer comparison, not sampling. An independent implementation over all actual graph vertices reproduces the computed four-round root types for dimensions one through five. Steps 2 and 3 extend the last class to every larger dimension. The first five singleton classes cannot be represented by smaller-dimension cubes because their complete root types differ; the last class has smallest representative \(Q_6\), containing \(2^6=64\) vertices. This proves both the equivalence criterion and the sharp representative bound.

## Verification

Run `python3 verify_cube_rank4.py` in a directory containing that file. The program has no third-party dependencies; its exact recorded output is `verify_cube_rank4_output.txt`. It enumerates all integer four-tuple extension possibilities through dimension sixteen, checks all pairwise class distinctions and tail agreements, and independently checks actual graph tuple recursion through dimension five. The infinite conclusion additionally uses the two proved saturation lemmas; numerical runs alone do not prove stabilization past the finite range.

## Relationship to prior work

Pikhurko and Verbitsky's survey of logical graph complexity (first publicly available in March 2010; arXiv:1003.4865) gives the Ehrenfeucht-game characterization and general graph-definability machinery but does not state an exact rank-four hypercube-dimension partition. Goldwasser and Hansen's open-access work on inducibility in hypercubes (first published November 2023; DOI:10.1002/jgt.23053) treats cube configurations and their densities, not bounded-rank elementary equivalence. The present theorem specializes the general game machinery to this family and determines the exact six classes. An earlier rank-three classification of binary Hamming powers does not determine the rank-four types, and its single-radius specialization leaves the present threshold unresolved.

## Limitations

The result is for plain graph adjacency and equality only, at quantifier rank four. It does not claim a general quantifier-rank formula, a classification with named coordinate predicates, or a classification of hypercubes with counting quantifiers. Priority relative to unindexed historical literature is not independently certified; the finite calculations are reproducible, while the infinite conclusion requires the mathematical lemmas above. Independent mathematical validation has not been performed.

## References

1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (initial arXiv posting 25 March 2010), especially §§1--3. https://arxiv.org/abs/1003.4865.
2. J. Goldwasser and R. Hansen, *Inducibility in the hypercube*, Journal of Graph Theory 105 (2024), 501--522 (first published online 9 November 2023), DOI:10.1002/jgt.23053. https://doi.org/10.1002/jgt.23053.
