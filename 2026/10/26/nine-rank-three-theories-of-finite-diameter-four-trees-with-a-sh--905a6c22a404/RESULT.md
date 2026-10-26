# Nine rank-three theories of finite diameter-four trees, with a sharp ten-vertex kernel

## Finding

Let \(\mathscr T_4\) be the class of all finite simple undirected trees of graph diameter exactly four, viewed in the relational first-order language with equality and adjacency. Two graphs are \(\equiv_3\)-equivalent when they satisfy the same first-order sentences of quantifier rank at most three. Then

\[
|\mathscr T_4/\!\equiv_3|=9.
\]

Every \(T\in\mathscr T_4\) is \(\equiv_3\)-equivalent to a diameter-four tree on at most ten vertices. Ten is optimal: one of the nine classes has no representative on fewer than ten vertices. Thus checking an arbitrary rank-three sentence for satisfiability or validity **within this class** reduces to checking the nine listed representatives.

For a four-tuple \(m=(m_0,m_1,m_2,m_3)\), define \(T(m)\) to have a central vertex joined to \(m_t\) distinct branch vertices, each with exactly \(t\) additional pendant leaves, for \(t\in\{0,1,2,3\}\). The nine smallest representatives, recorded as \((|V|,m)\), are

\[
\begin{aligned}
 &(5,(0,2,0,0)),\ (6,(0,1,1,0)),\ (6,(1,2,0,0)),\\
 &(7,(0,0,2,0)),\ (7,(0,3,0,0)),\ (7,(1,1,1,0)),\\
 &(8,(0,2,1,0)),\ (9,(2,0,2,0)),\ (10,(0,0,3,0)).
\end{aligned}
\]

Each representative has diameter exactly four, and the nine are pairwise inequivalent at rank three. The last representative is the unique equivalence class whose minimum size is ten.

## Assumptions and scope

The signature has only the binary, symmetric, irreflexive adjacency relation and equality; there are **no** constants, colours, a named root, order, counting quantifiers, or distance predicate. The class contains all finite diameter-four trees, with arbitrary degrees and orders. The displayed lists classify equivalence of sentences, not isomorphism or tuple types. Rank three refers to nested quantifier depth, with unrestricted reuse of variables, connectives, and alternations.

## Proof

**1. Canonical reduction.** Every diameter-four tree has a unique center \(c\). Each neighbour \(b\) of \(c\) has \(t_b\ge0\) further neighbours, all pendant; at least two of the \(t_b\) are positive. Partition these branches into four categories \(t_b=0,1,2\) and \(t_b\ge3\). In the last category replace each branch by one containing exactly three pendant leaves. In each of the four categories retain at most three branches. Let \(m_t\in\{0,1,2,3\}\) denote the resulting multiplicities, with category \(t=3\) standing for all original counts at least three. This produces \(T(m)\) with \(m_1+m_2+m_3\ge2\).

Duplicator wins the three-round Ehrenfeucht–Fraïssé game on the original tree and \(T(m)\): she matches the unique centers, maps a newly visited branch to a fresh branch of the same category, maps subsequent vertices in an already visited branch consistently, and respects selected leaf identities. In three rounds, at most three distinct branches or three leaves of any one branch can be visited. Equality and adjacency of all selected vertices are preserved. Counts below three are exact on each side and counts at least three provide sufficient new branches or leaves. The game therefore proves \(T\equiv_3T(m)\). Truncation only deletes vertices, so \(|T(m)|\le |T|\).

There are exactly \(4^4-4-12=240\) admissible canonical vectors: four vectors have no positive branch, while twelve have exactly one positive branch. Thus the infinite problem is reduced **by proof** to a closed finite family, not by a sampling assumption.

**2. Complete logical types.** For an ordered tuple \(\bar a\), let \(H_0(\bar a)\) be its complete atomic diagram of equalities and adjacencies, and recursively let
\[
H_{r+1}(\bar a)=\{H_r(\bar a,b):b\in V(T)\}.
\]
The standard Ehrenfeucht–Fraïssé/Hintikka recursion gives \(T\equiv_3T'\) exactly when \(H_3^T(())=H_3^{T'}(())\). The included program computes this recursion twice, with logically independent representations. A compact method records, for each vertex \(x\), the possible adjacency diagrams of triples \((x,y,z)\) as \(y,z\) vary; the independent method constructs literal atomic diagrams before forming three nested sets. The two agree on every one of the 240 canonical trees.

The computed partition has exactly nine distinct types. Taking the least order in each type yields the displayed nine representatives, with minimal orders \(5,6,6,7,7,7,8,9,10\). The smallest order of any canonical representative of the last type is ten. If an arbitrary tree with that type were smaller, the reduction in Step 1 would produce an equally typed canonical tree no larger, contradicting the exhaustive minimum. Hence the ten-vertex bound is sharp.

**3. Independent game cross-check.** A literal three-round Spoiler/Duplicator minimax routine, distinct from both signature implementations, tests every ordered pair among the nine representatives. It finds Duplicator wins exactly the nine diagonal matches. This checks the sharp class separation without relying on the hashed representation of the signatures.

## Verification

Execute `python3 verify_diam4.py` in the directory containing the supplied files. It uses Python's standard library only. The output `verification_output.txt` was produced from that program and ends with `VERIFY_OK`. The program iterates over all 240 canonical vectors; compares two complete three-round logical invariants; verifies nine types and minimal orders; and checks 81 independently evaluated three-round games. The reduction in Step 1, not the finite computation, is what extends the calculation to **every** finite diameter-four tree.

## Relationship to prior work

The Ehrenfeucht–Fraïssé correspondence and finite-type recursion are classical (see Libkin, *Elements of Finite Model Theory*, chapter 3). Bohman, Frieze, Łuczak, Pikhurko, Smyth, Spencer and Verbitsky study the quantifier depth needed to **define individual trees** and asymptotic worst-case depth under degree restrictions; their results concern another invariant and do not state the exact nine-class quotient or sharp ten-vertex witness for diameter-four trees. Existing rank-three classifications for star forests and linear forests concern, respectively, disjoint unions of stars and degree-at-most-two forests; those classes do not contain arbitrary diameter-four trees with branching. Heuter (1991) characterizes first-order definable languages of finite **ordered ranked labelled** trees using successor relations and star-free expressions, not this unlabelled pure-adjacency diameter-four rank-three quotient. No claim is made that general finite-tree logical-depth bounds are new here.

## Limitations

The count and bound concern **only** trees of diameter exactly four and sentences of quantifier rank at most three. This does not classify all trees, rank four, two-variable logic, or the quantifier depth of defining a particular tree among arbitrary graphs. The mathematical derivation of the 240-instance reduction and the independently specified finite recursion are both necessary to the proof. Independent scholarly audit and exhaustive inspection of all unindexed literature have not been performed.

## References

1. T. Bohman, A. Frieze, T. Łuczak, O. Pikhurko, C. Smyth, J. Spencer and O. Verbitsky, *First-Order Definability of Trees and Sparse Random Graphs*, Combinatorics, Probability and Computing **16** (2007), 375–400, https://doi.org/10.1017/S0963548306008376 (first online 23 January 2007).
2. L. Libkin, *Elements of Finite Model Theory*, Springer, chapter 3, https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf (accessible 2012 version).
3. E. S. Wolk, *The comparability graph of a tree*, Proceedings of the American Mathematical Society **13** (1962), 789–795, https://doi.org/10.1090/S0002-9939-1962-0172273-0 (structural background only).
4. U. Heuter, *First-order properties of trees, star-free expressions, and aperiodicity*, Informatique théorique et Applications **25** (1991), 125–146, https://www.numdam.org/item/ITA_1991__25_2_125_0/ (comparison in a different signature).
