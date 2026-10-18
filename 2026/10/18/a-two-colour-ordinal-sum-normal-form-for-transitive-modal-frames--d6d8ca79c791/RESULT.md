# A two-colour ordinal-sum normal form for transitive modal frames on rooted forks

## Finding

For each integer \(k\ge1\), let \(F_k=\{o\}\sqcup L\) be the intuitionistic poset with least world \(o\) and \(k\) labelled, pairwise incomparable maximal worlds \(L\). Consider a binary modal relation \(R\) that is **transitive but not necessarily reflexive** and obeys both Fischer--Servi-style confluence laws:

\[
(x\le x'\land xRy)\Longrightarrow(\exists y'\ge y)\,x'Ry',
\qquad
(xRy\land y\le y')\Longrightarrow(\exists x'\ge x)\,x'Ry'.
\]

Put \(S=\{s\in L:oRs\}\), \(B=\{b\in L:bRo\}\), and let \(c\) be the truth value of \(oRo\). Then precisely the following possibilities occur.

**Ordinary case.** The sets \(S,B\) are disjoint. With \(M=L\setminus(S\cup B)\), the restricted leaf relation is uniquely the *ordinal sum* \(B\oplus T\oplus S\): every edge goes from an earlier nonempty block to a later one; each of \(B\) and \(S\) is internally a complete reflexive relation; \(T\) is an arbitrary transitive relation on \(M\), including possible nonreflexive points. The root has only its prescribed edges \(o\to S\), \(B\to o\), and optional loop \(o\to o\). If \(c=0\), all these choices are valid. If \(c=1\), the following additional, necessary-and-sufficient conditions hold:

* \(S,B\ne\varnothing\): no condition on \(T\).
* \(S\ne\varnothing=B\): every column of \(T\) is nonempty.
* \(B\ne\varnothing=S\): every row of \(T\) is nonempty.
* \(S=B=\varnothing\): every row and every column of \(T\) is nonempty.

For the empty middle set, these row/column conditions are vacuous.

**Exceptional case.** Exactly one further relation exists: \(R=F_k\times F_k\), for which \(c=1\) and \(S=B=L\). There is no such exceptional relation with \(c=0\).

Write \(t_j\) for the number of all transitive binary relations on a labelled \(j\)-set, \(r_j\) for those having no empty row, and \(b_j\) for those having neither empty rows nor empty columns; put \(t_0=r_0=b_0=1\). If \(N_k^{(c)}\) counts the above frames by whether \(oRo\) holds, the complete exact census is

\[
N_k^{(0)}=\sum_{j=0}^{k}\binom{k}{j}2^{k-j}t_j,
\]
\[
N_k^{(1)}=b_k+2\sum_{j=0}^{k-1}\binom{k}{j}r_j
 +\sum_{j=0}^{k-2}\binom{k}{j}(2^{k-j}-2)t_j+1.
\]

The second final sum is empty for \(k=1\). In particular the exact pairs \((N_k^{(0)},N_k^{(1)})\) for \(k=1,2,3,4\) are \((4,4),(25,13),(281,98),(5754,1428)\), with totals \(8,38,379,7182\). The root-irreflexive count has the exponential generating function \(e^{2z}T(z)\), where \(T(z)=\sum_{j\ge0}t_jz^j/j!\).

## Assumptions and scope

The intuitionistic order is exactly one bottom element below \(k\) incomparable leaves, with no fallible worlds. Modal arrows may include or omit loops at any vertex, and **only** transitivity (not reflexivity, seriality, symmetry, or antisymmetry) is required. Confluence is quantified over all worlds as displayed above. The result concerns labelled frames and an exact structural count, not isomorphism classes or a completeness theorem for the entire intuitionistic modal logic. Its natural semantic setting is the transitive two-confluence finite-frame semantics associated with intuitionistic \(\mathsf{K4}\), rather than the reflexive \(\mathsf{S4}\) subclass.

An ordinal sum here means that all ordered pairs from an earlier block to any later block are present, none in reverse, and all internal pairs in each of the distinguished blocks \(B,S\) are present. The middle block carries exactly its freely selected transitive relation. When a distinguished block is empty, it is omitted.

## Proof

**1. Restrictions imposed by the two confluence laws.** Let \(T=R\cap(L\times L)\). The sole nontrivial intuitionistic comparisons are \(o\le a\) for \(a\in L\). Apply forth-up to \(oRs\), \(o\le a\). Because \(s\) is maximal, its only intuitionistic extension is itself; hence \(aTs\) for every \(a\in L\) and every \(s\in S\). Dually, apply back-up to \(bRo\), \(o\le a\). Since \(b\) is maximal, \(bTa\) for every \(a\in L\), \(b\in B\). Conversely, the confluence instances with leaf targets or sources follow from these properties; the only remaining nontrivial cases are the instances with \(oRo\), treated in step 3.

**2. Exactly two disjoint extremal classes, or complete collapse.** Define the universal-target and universal-source sets of the transitive relation \(T\) by

\[
U=\{s\in L:(\forall a\in L)\,aTs\},\qquad
V=\{b\in L:(\forall a\in L)\,bTa\}.
\]

By step 1, \(S\subseteq U\) and \(B\subseteq V\). If \(S\ne\varnothing\), choose \(s\in S\). For any \(u\in U\), \(sTu\), so transitivity of \(R\) through \(oRs\) gives \(oRu\); thus \(U=S\). Similarly, if \(B\ne\varnothing\), any \(v\in V\) satisfies \(vTb\) for \(b\in B\), whence \(vRo\) and \(V=B\). A nonempty \(U\) or \(V\) is a complete reflexive equivalence class. If \(U\cap V\ne\varnothing\), choose \(u\) in the intersection; for all \(a,d\in L\), \(aTuTd\), so \(T=L\times L\) and \(U=V=L\). Therefore, if \(S\cap B\ne\varnothing\), \(T\) is complete and \(S=B=L\); transitivity along \(o\to s\to o\) forces \(oRo\). This is precisely the exceptional complete relation.

Suppose instead \(S\cap B=\varnothing\). The universal-row and universal-column properties force every arrow from \(B\) to every point of \(M\cup S\), and every arrow from \(M\cup B\) into \(S\), as well as all internal arrows of \(B,S\). There are no arrows from \(M\) to \(B\): otherwise some \(mTb\) with \(b\in B=V\) implies \(mTa\) for all leaves \(a\), yielding \(m\in V=B\), a contradiction. There are no arrows from \(S\) to \(M\) by the dual argument. No arrows go from \(S\) to \(B\) because that would force their universal classes to coincide. Thus the leaf relation is exactly \(B\oplus T|_M\oplus S\), with unrestricted transitive middle relation.

**3. The root-loop dichotomy.** All nontrivial transitivity cases involving the root are already ensured by the ordinal sum except the possibility that a path \(o\to s\to o\) might force \(oRo\); disjointness of \(S,B\) prevents that path. If \(oRo\) is absent, the confluence instances not settled in step 1 have false antecedent, so every ordinary construction works. If \(oRo\) holds, forth-up applied to \(oRo\) and \(o\le a\) requires **some** outgoing \(R\)-edge from every leaf \(a\); back-up applied to \(oRo\) and \(o\le a\) requires **some** incoming edge to every leaf \(a\). These two requirements are sufficient too, by the explicit root/leaf order. In the ordinal-sum construction, \(S\ne\varnothing\) guarantees all leaf rows nonempty and \(B\ne\varnothing\) guarantees all leaf columns nonempty. If either distinguished set is absent, only the corresponding rows or columns of the middle relation can be empty. This gives the four stated conditions. Conversely these conditions make every confluence instance valid, completing sufficiency.

**4. Exact counts.** Fix \(j=|M|\). Choose \(M\) in \(\binom{k}{j}\) ways, assign each remaining label independently to \(S\) or \(B\) in \(2^{k-j}\) ways, and put any of the \(t_j\) transitive relations on \(M\). The classification makes this a bijection for \(c=0\), giving \(N_k^{(0)}\).

For \(c=1\), if both distinguished sets are empty, there are exactly \(b_k\) choices. If exactly one is nonempty, there are two choices for its role and \(\binom{k}{j}\) choices for the middle set, whose row-complete or column-complete relations are equinumerous by taking converses; there are \(r_j\) such relations. If both sets are nonempty and disjoint, there are \(2^{k-j}-2\) assignments of the labels outside \(M\), followed by \(t_j\) choices. Finally add the one complete exceptional relation. This yields \(N_k^{(1)}\). Standard exponential generating function multiplication gives the stated root-irreflexive expression. No asymptotic claim is required.

## Verification

Run `python verify_fork_ik4.py` with Python 3 and its standard library. It checks **the original quantified confluence axioms** and transitivity against the proposed normal form on every binary relation over the rooted forks with \(k=1,2,3\) leaves: respectively \(16,512,65536\) candidate relations. It compares the root-loop split with the independently computed enumerative formulas. For \(k=4\), it exhaustively enumerates all \(2^{16}=65536\) leaf matrices, classifies the transitive ones, and verifies the exact weighted count and formula. All assertions passed. Finite enumeration is evidence for the small counts, not a substitute for the all-\(k\) proof.

## Relationship to prior work

Girlando, Kuznets, Marin and Straßburger (2026, arXiv:2609.24922) establish decision procedures and the finite-model property for \(\mathsf{IS4}\) and \(\mathsf{IK4}\). Their published abstract is the recent impetus for studying the transitive two-confluence semantics at the first branching intuitionistic order. Balbiani, Diéguez, Fernández-Duque and McLean (2024, arXiv:2403.00201, especially Definitions 7--8) give the exact two confluence laws and distinguish the reflexive \(\mathsf{IS4}\) frames from related classes. These sources do not, in the inspected material, state the rooted-fork transitive normal form or its root-loop census. Earlier published chain-frame enumerations concern a totally ordered intuitionistic order, not this branching fork. OEIS A006905 tabulates the unrestricted transitive-relation counts \(t_j\), which are inputs here rather than new results; OEIS A306445 concerns a different set-family enumeration with a different sequence of counts.

## Limitations

The full text of arXiv:2609.24922 was not available in the accessible retrieval channels; its metadata and abstract, not its complete proofs, were examined. The full 2024 primary paper was inspected at the semantic definitions and later discussion, but unindexed equivalent treatments of the fork census remain possible. The result does not count isomorphism classes, does not characterize formula validity on all frames, and assumes exactly the displayed two confluence laws. The computer enumeration does not prove the infinite family theorem on its own.

## References

1. M. Girlando, R. Kuznets, S. Marin, L. Straßburger, *A decision procedure for intuitionistic modal logic IS4 (and IK4)*, arXiv:2609.24922, first posted 2026-09-21.
2. P. Balbiani, M. Diéguez, D. Fernández-Duque, B. McLean, *Constructive S4 modal logics with the finite birelational frame property*, arXiv:2403.00201, first posted 2024-03-01, especially Definitions 7--8.
3. OEIS A006905, *Number of transitive relations on a labelled set*; OEIS A306445, *Number of collections of subsets closed under union and intersection* (distinct comparison sequence).
