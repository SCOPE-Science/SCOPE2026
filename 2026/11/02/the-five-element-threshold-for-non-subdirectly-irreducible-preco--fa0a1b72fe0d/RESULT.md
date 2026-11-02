# The five-element threshold for non-subdirectly-irreducible preconditional chains

## Finding

Let \(C_n=\{0<1<\cdots<n-1\}\), with \(n\ge2\), and equip it with a preconditional \(\to\) satisfying the additional conditional-identity, semicomplementation, and double-negation-inflation axioms of an \(\mathsf F\)-algebra. Such an algebra is *subdirectly irreducible* (SI) when its congruences have a least nonidentity member.

**Theorem.** Every \(\mathsf F\)-expansion of \(C_2,C_3,C_4\) is SI. Among the six \(\mathsf F\)-expansions of \(C_5\), exactly two are not SI. Moreover, for every \(n\ge5\), there exists an \(\mathsf F\)-expansion of \(C_n\) that is not SI. Thus five is the sharp smallest nontrivial chain size where SI can fail, although every such expansion has the same negation as the Heyting chain.

## Assumptions and scope

The signature is \(\{\wedge,\vee,0,1,\to\}\). A preconditional obeys, for every \(a,b,c\),
\[
1\to a\le a,\quad a\wedge b\le a\to b,\quad a\to b\le a\to(a\wedge b),
\]
\[
a\to(b\wedge c)\le a\to b,\qquad a\to((a\wedge b)\to c)\le(a\wedge b)\to c.
\]
The stronger axioms are \(a\to a=1\), \(a\wedge(a\to0)=0\), and \(a\le(a\to0)\to0\). For \(C_n\), the symbols \(0\) and \(1\) in these axioms denote the least and greatest chain points, respectively. A congruence respects both lattice operations and the binary conditional. A nontrivial finite algebra is SI exactly when the intersection of all its nonidentity congruences is nonidentity.

## Proof

**Row form.** In a finite \(\mathsf F\)-chain, define \(q_a(b)=a\to b\). The first two axioms force \(q_{n-1}(b)=b\). Conditional identity, the consequent-monotonicity consequence of the preconditional axioms, and \(a\to b=a\to(a\wedge b)\) imply \(q_0(b)=n-1\), \(q_a(b)=n-1\) for \(b\ge a\), and \(q_a(0)=0\) for \(a>0\). The importation axiom makes each row idempotent on its image. Consequently, for internal \(a\), the map \(q_a\) is the ceiling to its fixed-point set \(S_a\cup\{n-1\}\), with \(S_a\subseteq\{0,\ldots,a-1\}\) and \(0\in S_a\). Importation between distinct rows is exactly \(S_a\subseteq S_{a+1}\). Conversely, every such nested system (with the full fixed-point set in the top row) satisfies the five axioms and the stronger axioms. This row characterization is also established in the prior finite-chain preconditional normal-form literature [3]. It can be verified directly: for every \(b\le a\), each value of \(q_b\) lies in \(S_b\cup\{n-1\}\subseteq S_a\cup\{n-1\}\), hence \(q_a(q_b(c))=q_b(c)\), proving importation. The other axioms follow from monotonic ceiling rows, the top identity row, and the designated endpoint values. The induced negation is \(\neg0=n-1\) and \(\neg a=0\) for all \(a>0\), so double negation inflation is automatic.

**Exhaustion through five elements.** The only choices for an internal fixed-point system on \(C_4\) are \(S_2=\{0,1\}\) and \(S_2=\{0\}\), while \(S_1=\{0\}\); on \(C_3\) only the Heyting operation occurs. Every lattice congruence of a finite chain is an interval partition. Encode such a partition by its *cut mask* \(m=\sum_{i=0}^{n-2}2^i\epsilon_i\), where \(\epsilon_i=1\) exactly when \(i\) and \(i+1\) belong to different blocks. The zero mask represents the universal congruence, and the mask \(2^{n-1}-1\) represents identity. Checking the conditional on the convex blocks yields the following complete congruence-mask sets:

For \(n=2\), there is one expansion with masks \(\{0,1\}\). For \(n=3\), there is one expansion with masks \(\{0,1,3\}\). For \(n=4\), the two choices \(S_2=\{0,1\}\) and \(S_2=\{0\}\) have masks \(\{0,1,3,7\}\) and \(\{0,1,5,7\}\), respectively. Each mask set has a least nonidentity congruence.

For \(n=5\), the six possibilities are exhausted by the following table; \(S_1=\{0\}\) and the top row are fixed. The entries in the last column are **all** congruence masks, not merely examples:

| \(S_2\) | \(S_3\) | All congruence masks | SI? |
|---|---|---|---|
| \(\{0,1\}\) | \(\{0,1,2\}\) | 0, 1, 3, 7, 15 | yes |
| \(\{0,1\}\) | \(\{0,1\}\) | 0, 1, 3, 11, 15 | yes |
| \(\{0\}\) | \(\{0,1,2\}\) | 0, 1, 5, 7, 13, 15 | no |
| \(\{0\}\) | \(\{0,1\}\) | 0, 1, 15 | yes |
| \(\{0\}\) | \(\{0,2\}\) | 0, 1, 5, 13, 15 | yes |
| \(\{0\}\) | \(\{0\}\) | 0, 1, 9, 11, 13, 15 | no |

For a family of interval partitions, taking the intersection of equivalence relations corresponds to the bitwise OR of their cut masks. In exactly the third and sixth rows, the OR of all nonidentity masks is 15, so their meet is identity and the algebra is not SI. In the other four rows that OR is not 15, so there is a least nonidentity congruence. Each table row is obtained by testing the sixteen convex partitions; the standalone checker independently performs that exhaustive comparison, rather than inferring untested congruences from sample partitions.

**Every larger chain has a failure.** For every \(n\ge5\), take the Heyting implication on \(C_n\) except change the single entry \(2\to1\) from \(1\) to \(n-1\). Equivalently, take \(S_1=\{0\}\), \(S_2=\{0\}\), and \(S_a=\{0,\ldots,a-1\}\) for all \(a\ge3\) (including the top row). These fixed-point sets are nested, hence this is an \(\mathsf F\)-preconditional by the row form.

Let \(\theta_1\) identify only the adjacent pair \(1,2\), and let \(\theta_{n-2}\) identify only \(n-2,n-1\); every other point is a singleton. Both are interval-partition lattice congruences. To check the conditional for \(\theta_1\), observe that antecedent rows 1 and 2 are identical and that, on consequents 1 and 2, every earlier row has identical output while every row with antecedent at least 3 outputs respectively 1 and 2. To check \(\theta_{n-2}\), rows \(n-2\) and \(n-1\) agree on all smaller consequents and yield values in the merged top pair on the last two consequents; every other row sends both last two consequents to top. Thus both are genuine nonidentity proper algebra congruences. Because \(1<n-2\) for \(n\ge5\), they identify disjoint adjacent pairs and intersect only at identity. No least nonidentity congruence exists. This proves the asserted sharp threshold and the infinite family. \(\square\)

## Verification

Run `python3 checker.py` using Python 3.9 or later. The checker enumerates every candidate row table satisfying the independently derived endpoint and monotonicity restrictions on chains of sizes 2 through 5; it then tests *all five original preconditional axioms* and all three stronger axioms literally. For each surviving table, it enumerates all interval partitions and tests conditional compatibility on every ordered input pair. The outputs are respectively \(1,1,2,6\) valid algebras and \(1,1,2,4\) SI algebras. It also validates the explicit infinite-family construction on sizes 5 through 12 and checks both exhibited one-pair congruences. These finite tests corroborate the proof; they are not offered as a proof for unbounded \(n\).

## Relationship to prior work

Chen [1] introduces the \(\mathsf K/\mathsf T/\mathsf F\) algebraic hierarchy and establishes completeness and finite model properties. Holliday [2] introduces preconditionals. The prior finite-chain classification [3] already proves the fixed-point normal form, coincidence of \(\mathsf T\) and \(\mathsf F\) on chains, and their factorial enumeration; **none of these is claimed as novel here**. The present statement concerns the congruence-theoretic property of subdirect irreducibility and its sharp first failure. The inspected chain-classification texts do not determine the congruence masks, the two five-element non-SI cases, or the all-sizes obstruction. Standard facts about convex lattice congruences and subdirect irreducibility are used, not claimed as new.

## Limitations

This theorem applies only to the \(\mathsf F\) algebraic signature with its conditional retained, not to the negation reduct, arbitrary bounded lattices, or all \(\mathsf K\)-algebras. It is not a complete formula for the number of SI expansions at every size, and no complexity consequence is established. The literature comparison cannot rule out earlier equivalent results under a different designation for these operations. Independent verification outside the reported elementary proof and finite checker remains to be performed.

## References

[1] Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221, first posted 2026-07-22.

[2] Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296, first posted 2024-02-03.

[3] *Fixed-point normal form for finite-chain preconditionals*, published research record SCOPE-20261004-3d55c0067825, 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-fixed-point-normal-form-for-finite-chain-preconditionals--3d55c0067825.

[4] *Factorial classification of preconditionals on finite chains*, published research record SCOPE-20261004-cbc434a2c6a0, 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-factorial-classification-of-preconditionals-on-finite-chains--cbc434a2c6a0.
