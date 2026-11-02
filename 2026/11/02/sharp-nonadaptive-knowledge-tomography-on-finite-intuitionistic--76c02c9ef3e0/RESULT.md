# Sharp nonadaptive knowledge tomography on finite intuitionistic S5 frames

## Finding

**Theorem (sharp nonadaptive knowledge tomography).** Let \((W,\leq)\) be a known nonempty finite poset, let \(C_1,\ldots,C_c\) be the nonempty connected components of its *undirected comparability graph*, and let \(R\) be an unknown equivalence relation on \(W\) satisfying triangle confluence
\[
w\leq v\ \land\ vRu\quad\Longrightarrow\quad wRu.
\]
A query selects, **before any answers are seen**, an upward-closed atomic truth set \(X\subseteq W\) and receives the truth set of the one-step knowledge formula \(Kp\) at **every labelled world**, namely
\[
L_R(X)=\{w\in W:[w]_R\subseteq X\}.
\]
The exact smallest number of such fixed queries that determines \(R\) for **every** admissible \(R\) is
\[
\boxed{q(W,\leq)=c-1.}
\]
For \(c=1\), the sole admissible relation is universal, so no query is needed. For a discrete \(n\)-world intuitionistic order, this becomes \(q=n-1\). The result is a fixed, nonadaptive query theorem; no optimality claim for adaptive experiments is made.

## Assumptions and scope

World labels and the intuitionistic order are known, with \(1\leq |W|<\infty\). Only the accessibility relation of **one named agent** is unknown. The relation is S5 (reflexive, transitive, symmetric), and obeys the displayed triangle-confluence condition. For each experiment, a fresh atomic proposition can be assigned any persistent/upward-closed truth set, and the *complete labelled* output of the corresponding atomic knowledge formula is observed without noise. Queries are fixed simultaneously. No other modal, negated, compound, or oracle queries are allowed. The comparability graph has an undirected edge between distinct comparable worlds. Its connected components \(C_i\) may have arbitrary finite poset shapes and sizes.

## Proof

**1. Reduction to arbitrary partitions of comparability components.** If \(w\leq v\), reflexivity gives \(vRv\), hence confluence gives \(wRv\). Thus each pair of comparable worlds is \(R\)-equivalent. By symmetry/transitivity every comparability component \(C_i\) is contained in one \(R\)-class. Conversely, any partition of the \(c\) components into larger blocks induces an equivalence relation obeying triangle confluence: when \(w\leq v\), they belong to the same component and hence the same equivalence class, so \(vRu\) entails \(wRu\). Therefore the admissible relations correspond bijectively to the set partitions of \(\{1,\ldots,c\}\).

**2. A determining collection of \(c-1\) queries.** Number the components arbitrarily, and for each integer \(1\leq j<c\) query
\[
X_j=C_1\cup\cdots\cup C_j.
\]
Each \(X_j\) is upward closed (indeed both upward and downward closed), since comparable worlds lie in the same component. Put \(X_0=\varnothing\) and \(Y_j=L_R(X_j)\), with \(Y_0=\varnothing\). The family \(Y_j\) is increasing. Each \(R\)-class is a union of indexed components; denote its largest component index by \(m(B)\). This class first appears in the outputs at \(Y_{m(B)}\). Since there is exactly one component with index \(j\), there is **at most one class** with \(m(B)=j\). Hence, for every \(1\leq j<c\), the nonempty difference \(Y_j\setminus Y_{j-1}\) is exactly one \(R\)-class; empty differences correspond to no such class. The final remaining class is \(W\setminus Y_{c-1}\) (the class containing \(C_c\)), which is always nonempty. These classes recover \(R\) uniquely. When \(c=1\), the universal relation is already known.

**3. Matching lower bound, even for queries that split comparability components.** Assume \(c\geq2\), and fix any \(q<c-1\) upward-closed query sets \(X_1,\ldots,X_q\). Define
\[
Z_j=\{i\in\{1,\ldots,c\}:C_i\not\subseteq X_j\}.
\]
Form a real \((q+1)\times c\) matrix whose first \(q\) rows are the incidence vectors of \(Z_1,\ldots,Z_q\), and whose last row is all ones. Since \(q+1<c\), it has a nonzero real kernel vector \(v=(v_1,\ldots,v_c)\). The last row forces \(\sum_i v_i=0\). Consequently the disjoint sign supports
\[
B=\{i:v_i>0\},\qquad D=\{i:v_i<0\}
\]
are both nonempty. For each \(j\), the vanishing of the corresponding row gives
\[
\sum_{i\in B\cap Z_j}v_i
=\sum_{i\in D\cap Z_j}(-v_i).
\]
All terms on both sides are strictly positive when present. Therefore \(B\cap Z_j=\varnothing\) if and only if \(D\cap Z_j=\varnothing\). Equivalently, the unions of components indexed by \(B\) and \(D\) are either **both wholly contained** in \(X_j\) or **both not wholly contained** in \(X_j\).

Now compare two partitions of the components: one has separate blocks \(B\) and \(D\), and the other replaces these by the single block \(B\cup D\); every remaining component index is a singleton block in both. These yield two distinct admissible S5 relations. For every chosen query, the two separate blocks are present in the knowledge output exactly when the merged block is present, and then their union is the same. All other blocks have identical behavior. Thus all \(q\) complete worldwise outputs coincide for these distinct relations. No \(q<c-1\) fixed queries can identify every admissible relation. Together with Step 2 this proves the theorem. \(\square\)

## Verification

The standalone standard-library program `checker.py` independently enumerates all partitions of each discrete carrier of size one through six and checks that the proposed prefix queries distinguish every partition. For sizes one through five it exhaustively tests **all** query collections of smaller size (including empty and full subsets) and confirms none distinguishes every partition. It also constructs admissible component-union relations on several non-discrete partial orders, checks triangle confluence directly, and checks unique recovery from persistent prefix queries. Execution prints `ALL_CHECKS_OK`. Finite enumeration is corroboration; the proof above supplies the arbitrary-finite-poset result.

## Relationship to prior work

Zenger's 2026 *Intuitionistic Common Knowledge* defines persistent valuations, triangle-confluent epistemic frames, and S5 equivalence relations, and explicitly observes that comparable worlds in S5 frames share modal successors (Definitions 2.4–2.6; discussion around Lemma 2.11). This theorem uses that semantic framework but asks a separate **experimental identifiability** question with a restricted observation language; it does not claim a new characterization of S5 or triangle confluence.

The map \(X\mapsto L_R(X)\) is the established **Pawlak lower approximation** or equivalence-partition interior operator. The known operator definition alone does not give the sharp finite *number of preselected complete-output evaluations* required to reconstruct an unknown partition; the lower bound here rests on the sign-support kernel argument. Other semantic learning models using unrestricted formulas, arbitrary relation oracles, membership/equivalence queries, or adaptive choices have different information content and need not obey this bound.

## Limitations

Only **nonadaptive** atomic observations with complete labelled outputs are covered. Adaptive observations, restricted observer locations, observational noise, multiple unknown agents queried jointly, unlabelled carriers, infinite world sets, or additional modal connectives may have different complexities. Although a statement-equivalent theorem was not found in the inspected sources, a general result in rough-set identification, partition learning or topology determination could subsume this theorem. Historical priority has not been independently certified. The computational checks do not constitute an infinite proof and are not an independent audit.

## References

1. Lukas Zenger, *Intuitionistic Common Knowledge*, arXiv:2605.00523v1, first publicly posted 2026-05-01, https://arxiv.org/html/2605.00523 (especially §2.2 and the S5 discussion).
2. Zdzisław I. Pawlak, *Rough Sets*, International Journal of Computer & Information Sciences **11** (1982), 341–356. This is the classical source for rough-set approximation operators.
3. *A Landscape and Implementation Framework for Probabilistic Rough Sets Using ProbLog*, Information Sciences (2022), DOI:10.1016/j.ins.2021.12.062 (Definitions 2.1–2.2 give the general lower-approximation semantics).
