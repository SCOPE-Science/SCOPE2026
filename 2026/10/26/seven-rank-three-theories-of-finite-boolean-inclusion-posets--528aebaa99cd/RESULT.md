# Seven rank-three theories of finite Boolean inclusion posets

## Finding
For each integer \(n\ge0\), let \(P_n=(\mathcal P([n]),\subseteq)\) be the finite Boolean lattice regarded **only as a poset** in the relational language \(\{\subseteq\}\). Then for all \(m,n\ge0\),
\[
P_n\equiv_3 P_m\quad\Longleftrightarrow\quad\min(n,6)=\min(m,6).
\]
Thus this family has exactly seven first-order theories at quantifier rank three. The smallest order-poset representative of the final class has \(2^6=64\) vertices; the bound is sharp within the family. If only nontrivial Boolean lattices with \(n\ge1\) are admitted, there are six classes. Here \(\equiv_3\) means agreement on every first-order sentence whose quantifier nesting depth is at most three, with no functions, constants, counting quantifiers, or named bottom/top elements.

## Assumptions and scope
The empty ground set is allowed; its powerset poset has one vertex. Quantifier-free formulas compare selected subsets by the single binary relation \(\subseteq\), together with equality (which is equivalent to mutual inclusion on this class). The result is *not* a rank-three statement in the richer Boolean-algebra language \(\{0,1,\wedge,\vee,\neg\}\). Finite Boolean inclusion posets are invariant under permutation of their ground atoms.

## Proof
**The finite-type recursion.** Given an ordered tuple \(\bar X=(X_1,\ldots,X_k)\) in \(P_n\), define its Venn vector \(c=(c_s:s\in\{0,1\}^k)\) by \(c_s=|\{a\in[n]:a\in X_i\ \text{iff}\ s_i=1\text{ for all }i\}|\). This vector is a complete orbit invariant under permutations of ground atoms. In particular, \(X_i\subseteq X_j\) holds exactly when every cell with \(s_i=1,s_j=0\) has size zero.

Define the complete quantifier-rank-\(r\) tuple type \(T_r(c)\) recursively. Its rank-zero part \(A(c)\) is the \(k\times k\) matrix of these inclusion facts. Set \(T_0(c)=A(c)\). For \(r\ge1\), set
\[
T_r(c)=\bigl(A(c),\ \{T_{r-1}(c\mathbin{\Vert_a}):0\le a_s\le c_s\text{ for every }s\}\bigr),
\]
where \(c\mathbin{\Vert_a}\) is the vector obtained by replacing each old cell of size \(c_s\) by the two cells of sizes \(c_s-a_s\) (outside a new set) and \(a_s\) (inside it). Sets in this recurrence remove duplicate types, since a quantified formula asks whether *some* successor realizes a type, not how many successors do. The induction that this is exactly the finite Hintikka type is standard: every rank-\(r\) formula is a Boolean combination of rank-zero atoms and existential rank-\((r-1)\) formulas after putting it in a suitable normal form. Thus two structures have the same rank-\(r\) sentences exactly when the two empty-tuple types \(T_r((n))\) and \(T_r((m))\) agree. Every step is finite and explicit.

The accompanying complete executable `verify.py` implements this recursion, **without imposing any bound on potential next chosen subsets**, for every \(0\le n\le9\) at rank three. It returns seven distinct empty-tuple types at \(n=0,1,2,3,4,5,6\), and the same type for \(n=6,7,8,9\). This gives exact separation of all seven classes, and shows that \(P_6\equiv_3P_8\). A separate brute-force implementation, selecting actual subsets of the ground set rather than orbit vectors, independently obtains the same equivalence pattern through \(n=7\). These finite computations are exhaustive for their explicitly stated finite ranges, but do not purport to prove an infinite theorem on their own.

**Uniform upper bound for the infinite tail.** We show that \(P_n\equiv_q P_m\) whenever \(n,m\ge2^q\), for every integer \(q\ge0\). In the \(q\)-round Ehrenfeucht--Fraisse game, after \(j\) rounds the paired selected subsets partition each ground set into corresponding Venn cells. Maintain: in each pair of cells, their sizes either coincide, or both are at least \(2^{q-j}\). Initially there is only one cell, so this holds. For the next move put \(t=2^{q-j-1}\). If the two old cell sizes agree, Duplicator copies the proposed split sizes. Otherwise each is at least \(2t\). If a split piece on Spoiler's side has fewer than \(t\) elements, match its size exactly and assign the remaining elements to the other piece (which then has at least \(t\) elements). If both pieces have at least \(t\) elements, split the counterpart into two pieces both of size at least \(t\). The invariant persists in every new cell. After all \(q\) moves the threshold is one: corresponding cells are simultaneously empty or nonempty. Hence all inclusion comparisons between selected subsets agree, so Duplicator wins.

With \(q=3\), all \(P_n\) with \(n\ge8\) are equivalent. The exact recursion already gives \(P_6\equiv_3P_8\), so transitivity places every \(n\ge6\) in one class. The six earlier sizes have distinct finite Hintikka types. This proves the displayed iff, including the sharp representative bound.

## Verification
Run `python3 verify.py` with the Python standard library. It computes the complete Venn-orbit rank-three types through \(n=9\), the rank-two types through \(n=8\), and independent direct quantifier-type profiles for actual subsets through \(n=7\). It also checks 4,404 bounded instances of the one-cell splitting condition used in the symbolic game proof. The recorded output `verification_output.txt` ends in `VERIFY_OK`; it reports 25,090 memoized Venn states and 82 distinct type records in the rank-three run. The numerical type IDs are just deterministic internal labels, not mathematical invariants; their equality classes are. The infinite tail is justified by the written game strategy, not finite extrapolation.

## Relationship to prior work
Kuncak and Rinard (arXiv:cs/0407045, §§4.2 and 6) study quantifier elimination for Boolean algebras of sets and develop cardinality/Venn-cell methods. Their language has Boolean-algebra operations, constants, and in its larger formulation cardinality constraints; their inspected discussion does not give the exact rank-three equivalence classes for *only* the inclusion relation. A published rank-\(q\) theorem for finite Boolean algebras in the full operation language gives the larger threshold \(2^q\) atoms, hence eight for rank three. Forgetting operations makes the language weaker: equivalence in the full language implies equivalence in the inclusion reduct, but inequivalence in the full language does **not** imply inequivalence in the reduct. Thus its threshold eight cannot give the sharp threshold six claimed here. Searches for the inclusion-poset aliases did not locate a dominating theorem. General Ehrenfeucht--Fraisse and finite-type methods are standard and are not claimed as new.

## Limitations
The result concerns the one-family exact rank-three profile in pure first-order inclusion order. It does not establish optimal rank bounds in enriched lattice or set-operation signatures, nor claim an independent literature certification. The new part is the exact sharp six-atom boundary and complete seven-class census in the weak signature, not the general Venn-game technique. It is possible that a prior solution exists in unindexed order-theory or finite-model-theory exercises. The complete finite certificate is finite; the infinite conclusion additionally requires the explicitly proved cell-splitting lemma.

## References
1. Viktor Kuncak and Martin Rinard, “The First-Order Theory of Sets with Cardinality Constraints is Decidable,” MIT CSAIL Technical Report 958 (July 2004), arXiv:cs/0407045, first public arXiv posting 17 July 2004; https://arxiv.org/abs/cs/0407045.
2. “Sharp \(2^q\) atom-visibility threshold for finite Boolean algebras,” published published-finding corpus research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-2-q-atom-visibility-threshold-for-finite-boolean-algebras--938cb5f89dc7.
