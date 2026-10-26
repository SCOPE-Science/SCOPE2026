# Thirty-three rank-four theories and a sharp fifteen-vertex kernel for pentagon blow-ups

## Finding

Let \(G(a,b,c,d,e)\), for positive integers \(a,b,c,d,e\), be the finite simple undirected graph obtained from a five-cycle by replacing successive vertices by independent sets of the indicated sizes and replacing each cycle edge by a complete bipartite graph. Work in the first-order language with equality and **only** the undirected adjacency predicate \(E\): the five parts and their cyclic order are not named.

**Theorem.** The family \(\mathcal B=\{G(a,b,c,d,e):a,b,c,d,e\geq1\}\) has exactly \(33\) equivalence classes under agreement on every first-order sentence of quantifier rank at most \(4\). Every such class has a representative on at most \(15\) vertices, and this uniform bound is optimal. In fact, exactly one class requires \(15\) vertices; it is represented by \(G(3,3,3,3,3)\). For every positive size vector \(\mathbf s\),

\[
G(\mathbf s)\equiv_4 G(\min(3,s_1),\ldots,\min(3,s_5)).
\]

The sizes of the smallest representatives for the \(33\) classes have frequency distribution \(5:1,\ 6:1,\ 7:3,\ 8:4,\ 9:7,\ 10:7,\ 11:6,\ 12:2,\ 13:1,\ 15:1\). The attached `c5_class_table.csv` supplies the exact class of each of the \(1024\) vectors from \(\{1,2,3,4\}^5\), including all shortest representatives.

## Assumptions and scope

Only **nonempty** independent clone parts are allowed. No vertex colours, part names, orientation, order relation, or counting quantifier is available. A quantifier-rank-four theory means the set of all ordinary first-order sentences of rank at most four in the binary adjacency language, with arbitrary reuse of variables and Boolean connectives.

Cyclic permutations and reversals of the size vector yield isomorphic graphs, but rank-four equivalence is substantially coarser than isomorphism: the census is taken over all \(1024\) ordered clipped vectors rather than assuming any orbit quotient in the final answer. The result does not concern general triangle-free graphs, graphs with empty parts, or iterated blow-ups whose substituted pieces contain edges.

## Proof

**Step 1 (a uniform finite reduction).** For any two positive size vectors \(\mathbf s,\mathbf t\) with \(\min(s_i,4)=\min(t_i,4)\) for each part index \(i\), Duplicator wins the four-move Ehrenfeucht–Fraïssé game on \(G(\mathbf s)\) and \(G(\mathbf t)\). After each move, retain the property that selected vertices correspond partwise and that selected distinct clones correspond injectively within each part. If Spoiler repeats a selected vertex, repeat its mate. If Spoiler chooses a new vertex in part \(i\), fewer than four vertices have been selected before this move. If the part has fewer than four elements, both corresponding part sizes are equal, so an unused mate exists; otherwise each has at least four elements, and again an unused mate exists. Because edge incidence depends only on whether the two parts are consecutive, all equalities and adjacency relations between selected vertices are preserved. Thus

\[
G(\mathbf s)\equiv_4 G(\min(4,s_1),\ldots,\min(4,s_5)).
\]

**Step 2 (exact logical-type recurrence).** For a graph and an ordered tuple \(\bar v\), let \(A(\bar v)\) be its complete atomic diagram (all equalities and adjacency facts, positive or negative). Define recursively

\[
T_0(G,\bar v)=A(\bar v),\qquad
T_{r+1}(G,\bar v)=\bigl(A(\bar v),\{T_r(G,\bar v w):w\in V(G)\}\bigr).
\]

By induction on formulas, equality of these types is equivalent to agreement on all first-order formulas of quantifier rank at most \(r\) at the indicated tuple. The inductive step handles existential quantifiers via the displayed set of extension types; universal quantifiers follow by negation, and Boolean combinations follow componentwise. In particular, equality of \(T_4(G,())\) is equivalent to four-round equivalence.

For a pentagon blow-up, represent each chosen vertex by a pair \((i,j)\), where \(i\in\{0,1,2,3,4\}\) is its clone part and \(j\) indexes its occurrence among distinct already selected vertices of that part. A next move is, up to an automorphism fixing the selected tuple, either the repetition of one already selected vertex or the first unused clone in one of the five parts having spare capacity. These are **all** orbits of the stabilizer on possible next moves: permutations of still-unused clones within each independent part act transitively. Consequently the recursion above is exactly evaluated by the finite quotient recurrence in `verify_c5.py`, without considering all labelled vertices or omitting any possible logical move.

**Step 3 (exhaustive finite calculation and sharpness).** Evaluate this recurrence for every size vector in \(\{1,2,3,4\}^5\), identifying two vectors precisely when their empty-tuple type signatures agree. The finite computation returns \(33\) distinct signatures across \(1024\) vectors. Comparison with their coordinatewise three-clipped vectors establishes, for every one of these \(1024\) vectors, equality of rank-four types. Combining this finite identity with Step 1 proves the displayed three-clone reduction for **every** positive size vector.

The exact minimum total order in each signature class is then computed, not inferred from symmetry. Its maximum is \(15\); the unique class attaining this maximum comprises exactly the \(32\) clipped vectors with every coordinate equal to \(3\) or \(4\). Every original graph in that signature class must have all five part sizes at least \(3\), and thus at least \(15\) vertices. Conversely, \(G(3,3,3,3,3)\) has \(15\) vertices and belongs to that class, proving sharpness.

## Verification

Run `python verify_c5.py` using the Python standard library. The program generates `c5_class_table.csv` (all \(1024\) clipped vectors) and prints the exact list of \(33\) shortest representatives and its frequency distribution. The included `verify_c5_output.txt` records a successful run and the expected output.

For a separate direct-state-space cross-check, the program also constructs **all** \(243\) fully labelled graphs with part sizes in \(\{1,2,3\}^5\), computes four-round types by a second recursion that visits every vertex individually without quotienting by twin classes, and compares all \(29403\) pairs of those graphs against the quotient classification. The two partitions agree exactly. This finite oracle is a cross-check; the infinite-universe assertion follows from Step 1 and the exact recurrence, not from an unproved extrapolation.

## Relationship to prior work

Pentagon blow-ups are a natural family in extremal graph theory. Hatami, Hladký, Král', Norine and Razborov (first publicly available 8 February 2011) studied pentagon counts in triangle-free graphs, defined independent-set blow-ups in their Section 2.3, and characterized the extremal balanced cases. Their flag-algebra *types* count labelled subgraph configurations and are not the first-order quantifier-rank types classified here. Balogh, Hu, Lidický and Pfender (2014) studied inducibility and **iterated** pentagon blow-ups, not rank-four elementary equivalence. Brown and Hoshino (2007) gave complete Ehrenfeucht–Fraïssé results for paths and unblown cycles, not variable-size pentagon blow-ups. These works give motivation and methodological context but do not state the \(33\)-class or optimal \(15\)-vertex result.

The logical recurrence in Step 2 is standard finite model theory; no novelty is claimed for it or for the elementary four-pebble clipping lemma individually. The claimed contribution is the full exact classification and unexpected further collapse from the provable four-clone truncation to the sharp three-clone representatives, including the optimal extremal class.

## Limitations

Originality was assessed against the primary works above, publicly searchable literature and indexed mathematical-result records; inaccessible or unindexed publications could still contain an equivalent classification. The theorem is specific to nonempty independent-set blow-ups of the simple five-cycle, ordinary first-order logic, pure graph adjacency, and quantifier rank four. It makes no claim about quantifier rank five or higher, colour-named parts, or unrestricted graph substitution. The calculation is exhaustive over the finite reduced domain by a mathematically justified reduction.

## References

1. H. Hatami, J. Hladký, D. Král', S. Norine, A. Razborov, *On the Number of Pentagons in Triangle-Free Graphs*, arXiv:1102.1634 (first posted 2011-02-08), J. Combin. Theory Ser. A **120** (2013), 722–732. https://arxiv.org/html/1102.1634v4
2. J. Balogh, P. Hu, B. Lidický, F. Pfender, *Maximum density of an induced 5-cycle is achieved by an iterated blow-up of a 5-cycle*, arXiv:1411.4645 (first posted 2014-11-17), European J. Combin. **52** (2016), 47–58. https://arxiv.org/html/1411.4645v1
3. J. Brown, R. Hoshino, *The Ehrenfeucht-Fraïssé Game for Paths and Cycles*, Ars Combinatoria **83** (2007), 193–212. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
