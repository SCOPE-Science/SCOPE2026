# Normality and a Bell-number census for finite-agent someone-knows bundles

## Finding

Fix a nonempty set \(W\), a nonempty finite agent set \(A\), and equivalence relations \(R_a\subseteq W\times W\), one for each \(a\in A\). For \(X\subseteq W\), write
\[
K_a(X)=\{w\in W:[w]_{R_a}\subseteq X\},\qquad
S(X)=\bigcup_{a\in A}K_a(X),\qquad R_\cap=\bigcap_{a\in A}R_a.
\]
Then the following are equivalent:

1. \(S(X\cap Y)=S(X)\cap S(Y)\) for every two subsets \(X,Y\subseteq W\) (equivalently, the someone-knows bundle is a normal modal operator on this frame).
2. For every \(w\in W\), some \(a(w)\in A\) has \([w]_{R_{a(w)}}=\bigcap_{a\in A}[w]_{R_a}\).
3. For every \(X\subseteq W\), \(S(X)=\{w:[w]_{R_\cap}\subseteq X\}\); that is, someone-knows and distributed knowledge coincide on all valuations and under every modal nesting.

For exactly two agents, these conditions hold if and only if their two partitions have *laminar intersections*: whenever a block of one partition meets a block of the other, the two blocks are comparable by inclusion. On a fixed labeled set of \(n\ge1\) worlds, let \(a_n\) count **ordered pairs** of equivalence relations satisfying these conditions, and let \(B_m\) denote the \(m\)-th Bell number. With the auxiliary convention \(a_0=1\),
\[
a_n=\sum_{m=1}^n\binom{n-1}{m-1}(2B_m-1)a_{n-m},
\quad
\sum_{n\ge0}a_n\frac{z^n}{n!}
=\exp\!\left(2\exp(\exp z-1)-\exp z-1\right).
\]
In particular, \((a_1,\ldots,a_7)=(1,4,19,111,774,6229,56529)\). Three worlds are necessary and sufficient for failure of normality on a two-agent \(S5\) frame.

## Assumptions and scope

No finiteness assumption is imposed on \(W\) in the equivalence of conditions 1--3. The number of agents is finite and nonzero; each accessibility relation is an equivalence relation (\(S5\) semantics). Each atomic valuation is an arbitrary subset of \(W\). ``Normal'' means preservation of the top element and binary intersections on the full complex Boolean algebra \(\mathcal P(W)\), equivalently validity of the normal modal \(K\)-scheme under all valuations. Because each agent's successor class is nonempty and \(S(W)=W\), only binary-intersection preservation needs testing.

The enumerative formula concerns ordered *labeled* pairs of partitions of the same \(n\)-element set. It does not count pairs up to relabeling or up to exchange of agent identities. The empty labeled set occurs only as the combinatorial exponential-formula base case \(a_0=1\).

## Proof

**Step 1: the local minimum criterion.** Put \(C_a(w)=[w]_{R_a}\) and \(C_*(w)=\bigcap_{a\in A}C_a(w)\). Always \(S(X)\subseteq K_{R_\cap}(X)\), because \(C_*(w)\subseteq C_a(w)\). If condition 2 holds, then for any \(w\) and \(X\), the inclusion \(C_*(w)\subseteq X\) forces \(C_{a(w)}(w)\subseteq X\); hence \(K_{R_\cap}(X)\subseteq S(X)\). This proves 2 implies 3, and 3 implies 1 since an ordinary relational box preserves all intersections.

Conversely, suppose condition 1 holds. Fix \(w\). For every \(a\in A\), we have \(w\in S(C_a(w))\), witnessed by agent \(a\). Since \(A\) is finite, repeated binary-intersection preservation gives
\[
w\in S\!\left(\bigcap_{a\in A}C_a(w)\right)=S(C_*(w)).
\]
Thus some agent \(b\) satisfies \(C_b(w)\subseteq C_*(w)\). The reverse inclusion holds by definition; hence \(C_b(w)=C_*(w)\). This proves 1 implies 2. Since the equality \(S=K_{R_\cap}\) holds for *all* truth sets, induction on formulas also establishes preservation under arbitrary nesting and Boolean combinations of \(S\).

**Step 2: two-agent structure.** A partition block \(P\) and a partition block \(Q\) intersect precisely when there is \(w\in P\cap Q\), in which case \(P=C_1(w)\) and \(Q=C_2(w)\). The two-class intersection equals one of the two classes precisely when \(P\subseteq Q\) or \(Q\subseteq P\). This is exactly the asserted laminar-intersection condition.

**Step 3: decomposition into join-components.** Consider the least equivalence relation containing both \(R_1\) and \(R_2\). Within one of its classes \(U\), examine the bipartite incidence graph of blocks of the two input partitions, joining two blocks if they intersect. Under the condition of Step 2, each intersecting pair is nested. If every incidence is equality, \(U\) is one common block. Otherwise take a strict inclusion, say \(P\subsetneq Q\). Every other block \(P'\) of the first partition intersecting \(Q\) must lie inside \(Q\): if \(Q\subseteq P'\), then \(P'\) would meet the distinct block \(P\), impossible. No block of the second partition other than \(Q\) can meet any \(P'\subseteq Q\). Hence \(Q=U\), the second partition is indiscrete on \(U\), and the first is a nontrivial arbitrary partition of \(U\). The symmetric strict-inclusion case interchanges the agents. Conversely, any of these configurations has laminar intersections. The join-components are uniquely determined, so there is no overcounting.

On a fixed \(m\)-element component, there is one common-block configuration, \(B_m-1\) configurations with the first partition indiscrete and the second nontrivial, and \(B_m-1\) in the reverse orientation. Thus the exact component weight is \(c_m=2B_m-1\). The component containing a distinguished label has \(\binom{n-1}{m-1}\) choices of its remaining labels, \(c_m\) internal configurations, and \(a_{n-m}\) configurations on the complement. Summing over \(m\) proves the recurrence. By the labeled exponential formula,
\[
\sum_{n\ge0}a_n\frac{z^n}{n!}
=\exp\left(\sum_{m\ge1}(2B_m-1)\frac{z^m}{m!}\right).
\]
The standard Bell-number identity \(\sum_{m\ge0}B_m z^m/m!=\exp(\exp z-1)\) yields the displayed generating function.

**Step 4: sharp first counterexample.** Every pair of partitions on one or two points has comparable blocks whenever they meet. On \(W=\{1,2,3\}\), take \(P=\{\{1,2\},\{3\}\}\) and \(Q=\{\{1\},\{2,3\}\}\). At \(w=2\), put \(X=\{1,2\}\) and \(Y=\{2,3\}\). Then \(w\in S(X)\cap S(Y)\), but \(w\notin S(X\cap Y)\), proving the bound is sharp.

## Verification

The accompanying standard-library Python program `verify.py` independently generates all set partitions on up to six labels, checks the laminar criterion against the local-minimum criterion for every ordered pair, and confirms the counts \(1,4,19,111,774,6229\) for sizes one through six. For two agents with up to four worlds, it additionally tests binary-intersection preservation under **all** pairs of truth-set valuations, and checks the collapse to the intersection relation on every subset whenever the criterion holds. For three agents with up to four worlds, it tests the analogous criterion under every pair of valuations. The program checks 44,168 two-agent partition-pairs and 931,396 valuation-pairs in total and finishes with `VERIFY_OK`. It also evaluates the symbolic recurrence through eight worlds. These finite checks test the proof but do not replace the all-size combinatorial argument or the arbitrary-\(W\) local-minimum proof.

Reproduce with `python3 verify.py` from this directory; no external packages are needed.

## Relationship to prior work

Ding and Yang, *A General Theory of Propositional Modal Bundled Modalities* (arXiv:2603.26268, first submitted 27 March 2026), give a semantic and axiomatic treatment of the someone-knows bundle on \(S5\) frames. Ågotnes and Wáng, *Somebody Knows* (KR 2021), establish its failure of full conjunctive closure on the class of all multi-agent frames, and provide neighborhood semantics and completeness results. Ding, Liu and Wang (2023) likewise study weakly aggregative someone-knows logic and hypergraph semantics. None of the inspected parts states the exact per-frame collapse criterion together with the ordered labeled-frame census. This is a **relative literature assessment**, not a proof that an equivalent formulation is absent from all prior publications. Earlier results on nesting of block structures provide nearby combinatorial language but not this explicit epistemic enumeration in the inspected sections.

## Limitations

The finite number of agents is essential for the implication from binary-intersection preservation to attainment of a minimum local information class. For infinitely many agents a decreasing family of classes can be closed under finite intersections without containing its intersection. The exact census applies to two agents and labeled finite worlds; no formula for an arbitrary number of agents and no unlabeled isomorphism census is asserted. Published equivalences under other terminologies, especially neighborhood filter theory and partition-incidence enumerations, remain a literature risk.

## References

1. Yifeng Ding and Yuanzhe Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268v2 (2026), Section 5.1 and Theorem 5.6; https://arxiv.org/abs/2603.26268 . First version 27 March 2026.
2. Thomas Ågotnes and Yì N. Wáng, *Somebody Knows*, Proceedings KR 2021, pp. 2–11, DOI:10.24963/kr.2021/1; https://proceedings.kr.org/2021/1/kr2021-0001-agotnes-et-al.pdf .
3. Yifeng Ding, Jixin Liu and Yanjing Wang, *Someone knows that local reasoning on hypergraphs is a weakly aggregative modal logic*, Synthese 201:46 (2023), DOI:10.1007/s11229-022-04032-y.
4. M. Anagnostopoulou-Merkouri, R. A. Bailey and P. J. Cameron, *Permutation groups, partition lattices, and block structures*, Forum of Mathematics, Sigma 13 (2025), Section 2.4, DOI:10.1017/fms.2025.10126.
