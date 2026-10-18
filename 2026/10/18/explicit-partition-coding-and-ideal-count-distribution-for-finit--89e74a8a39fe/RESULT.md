# Explicit partition coding and ideal-count distribution for finite linear L-algebras

## Finding
For every integer \(n\geq 1\), there is an explicit, reversible, recursively computable bijection \(\Phi_n\) between the L-algebra operations whose induced order is the **fixed** chain \(L_n=\{x_0>x_1>\cdots>x_{n-1}\}\), with unit \(x_0\), and ordinary set partitions of \(\{1,\ldots,n-1\}\). Under this bijection, the number of **nonempty proper ideals** of the L-algebra is exactly the number of blocks of its partition. Consequently, for each \(0\leq k\leq n-1\), the number of these algebra operations with exactly \(k\) nonempty proper ideals is the Stirling number of the second kind \(\left\{\begin{smallmatrix}n-1\\k\end{smallmatrix}\right\}\). The empty partition and the one-element algebra correspond when \(n=1\). An order isomorphism of two such chains is forced to be the identity, so the same formula also counts their isomorphism classes.

This is a concrete partition-coding answer to the cardinality-consistent version of Problem 4.6 of Dietzel–Menchón–Vendramin [1], together with a refinement by the proper-ideal statistic. It does **not** assert a bijection with partitions of an \(n\)-element set, the wording printed in that problem: [1, Theorem 4.5] already proves there are \(B_{n-1}\), rather than \(B_n\), algebras.

## Assumptions and scope
An L-algebra \((X,\cdot,1)\) satisfies \(1\cdot y=y\), \(x\cdot1=x\cdot x=1\), the cycloid identity \((x\cdot y)\cdot(x\cdot z)=(y\cdot x)\cdot(y\cdot z)\), and the separation condition that \(x\cdot y=y\cdot x=1\) implies \(x=y\). The natural order is \(x\leq y\) precisely when \(x\cdot y=1\). The order is required to be the fixed total order above. We write a multiplication table entry as the index \(t\) of the element \(x_t\), and so \(x_0\) is the unit.

A non-unit element \(x_j\), \(j\geq1\), is *invariant* when \(x_i\cdot x_j=x_j\) for each \(i<j\). Ideals mean nonempty subsets satisfying all four axioms (I1)–(I4) of [2, Definition 1.3]. The whole algebra is an ideal, but is not counted as proper. The Stirling number is the number of partitions of an \((n-1)\)-element set into exactly \(k\) nonempty blocks, including the convention \(\left\{\begin{smallmatrix}0\\0\end{smallmatrix}\right\}=1\).

## Proof
**1. Published unique-extension lemma.** We use the actual full-strength [1, Proposition 4.4], not merely the Bell-number counting identity. Suppose an L-algebra on \(x_0>\cdots>x_{r-1}\) has smallest invariant element \(p\). To add \(z=x_r\), choose \(c<p\cdot x_{r-1}\) (where \(c=z\) is allowed). The unique extension with \(p\cdot z=c\) has \(z\cdot a=1\) for old \(a\); if \(c=z\), then every old \(a\) satisfies \(a\cdot z=z\); otherwise
\[
a\cdot z=\begin{cases}z,&a>p,\\(p\cdot a)\cdot c,&a\leq p.\end{cases}
\]
The previous table is unchanged. Existence, uniqueness, and satisfaction of the L identities are established by that proposition. Its Lemma 4.3 makes the successive values \(p\cdot x_j\) below a fixed smallest invariant \(p\) strictly decreasing in the chain order and distinct from the unit.

**2. Partition-to-algebra construction.** Let \(\Pi\) partition \(S_n=\{1,\ldots,n-1\}\). For \(n=1\), take the one-element algebra. Otherwise let \(B\) be the unique block containing \(n-1\), let \(C=S_n\setminus B\), and put \(m=|C|+1\). Delete \(B\), renumber the labels of \(C\) increasingly as \(1,\ldots,m-1\), and recursively decode the resulting partition to an L-algebra on \(x_0,\ldots,x_{m-1}\). First adjoin \(x_m\) as a new invariant by applying the extension lemma to the **old** smallest invariant with the choice \(c=x_m\). Then \(x_m\) becomes the smallest invariant of the enlarged algebra. In explicit table indices this means \(x_i\cdot x_m=x_m\) for every \(i<m\) and \(x_m\cdot x_i=x_0\) for every \(i\leq m\).

Next list \(B\setminus\{n-1\}=\{b_1<\cdots<b_t\}\); by construction \(t=n-m-1\) and \(1\leq b_j\leq m+j-1\). Successively adjoin the points \(x_{m+1},\ldots,x_{n-1}\), prescribing \(x_m\cdot x_{m+j}=x_{b_j}\). Each value is strictly below the preceding \(x_m\)-row value in the chain order, and is above the newly added point, so the lemma applies at every step. In every intermediate algebra \(x_m\) stays the smallest invariant element. Use the displayed table rule to fill each new column; no search or arbitrary tie-breaking is necessary.

**3. Algebra-to-partition inverse.** Given a linear L-algebra of size \(n>1\), let \(m\) be the largest index of a non-unit invariant element (the smallest such element in the chain order). Such an element exists because \(x_1\) is invariant. Restrict the table to the top \(m\) points \(x_0,\ldots,x_{m-1}\), a subalgebra by [1, Theorem 4.5, proof]. Form the set of distinct output indices
\[
 A=\{a_j:x_m\cdot x_j=x_{a_j},\ m<j<n\}\subseteq\{1,\ldots,n-2\}.
\]
By the strictness and extension lemmas in [1], these indices are strictly increasing as \(j\) increases and \(|A|=n-m-1\). Set \(B=A\cup\{n-1\}\) and \(C=S_n\setminus B\); then \(|C|=m-1\). Recursively encode the restricted top algebra on \(\{1,\ldots,m-1\}\), relabel its partition blocks increasingly onto \(C\), and append block \(B\). This defines \(\Phi_n\).

**4. Inverseness.** By [1, Theorem 4.5, proof], every linear L-algebra is uniquely determined by the triple consisting of its smallest invariant index \(m\), the restricted top algebra, and the set \(A\) above. The partition operation in step 2 uses the unique block \(B\) containing the maximum label, with \(A=B\setminus\{n-1\}\); its other blocks are the recursively coded top algebra on \(C\). These constructions undo each other by induction on \(n\). In particular no two partition inputs produce the same operation table, and every allowed table occurs. There is no claim of an unproved direct classification beyond the unique-extension and decomposition statements of [1].

**5. Proper-ideal statistic.** In the construction, existing invariants in the top subalgebra remain invariant after adding lower points because invariance only tests elements higher in the total order. The new point \(x_m\) is invariant, and all lower points subsequently adjoined are non-invariant, because \(x_m\) remains the smallest invariant [1, Theorem 4.5, proof]. Thus the number of non-unit invariants increases by exactly one when block \(B\) is appended. By induction it equals the number of blocks of \(\Pi\). Independently, [2, Theorem 4.3 and Corollary 4.4] prove that the proper nonempty ideals are precisely \(\uparrow x_{j-1}\) for invariant \(x_j\), \(1\leq j<n\); this is a bijection between proper ideals and non-unit invariants. Hence the block statistic equals the proper-ideal count. The exact Stirling distribution follows from the proven bijection and the definition of the Stirling numbers.

## Verification
Run `python3 verify.py` from the package directory. It generates every partition on \(n-1\) points and checks both coding directions, injectivity, the L identities, the invariant/block count, and the Stirling distribution, for \(1\leq n\leq8\). It independently enumerates all multiplication tables satisfying the raw identities for \(1\leq n\leq5\) and compares the complete sets. For \(1\leq n\leq6\), it also directly checks all four ideal axioms for each nonempty proper subset and matches the ideal count to the block count. The resulting total numbers for \(n=1,\ldots,8\) are \(1,1,2,5,15,52,203,877\), and the checker prints `VERIFY_OK`.

Finite checks corroborate but do not prove the universal assertion. That proof is the induction using [1, Proposition 4.4 and Theorem 4.5] and [2, Theorem 4.3] above.

## Relationship to prior work
[1, Theorem 4.5] already gives \(B_{n-1}\) total linear L-algebras and a bijective **decomposition into a smaller algebra and a subset**; that theorem and its unique-extension lemma are indispensable prior ingredients, not new discoveries. [1, Problem 4.6] asks for an explicit partition bijection; the printed ambient set has one extra element compared with its own Bell-number theorem, so the result here uses \(n-1\) partition labels. [2, Theorem 4.3] already classifies ideals by invariant elements. The contribution here is a fully specified **mutually inverse canonical partition coding** realizing [1]'s combinatorial request, together with the induced **exact Stirling law for the number of nonempty proper ideals** from [2]. Neither claimed part is the general Bell-number count or the known ideal characterization by itself.

A further closely related source is Rump [3], which advertises a recursive treatment of noetherian linear KL-algebras and prime factorization. Its abstract and bibliographic record, but not its full text, could be inspected. A potentially equivalent encoding in that source remains an acknowledged originality risk.

## Limitations
The fixed-chain and finite hypotheses are essential to the construction. The one-element case uses the empty partition and zero proper nonempty ideals. The published Problem 4.6 as printed asks for partitions of \(n\) labels; this cardinality-inconsistent literal statement is not solved. The Stirling refinement uses the later ideal theorem [2] and is not independent of that known result. No independent external audit or broad machine formalization has been performed. Prior literature could contain equivalent coding or a stronger enumerator under different terminology.

## References
[1] C. Dietzel, P. Menchón, and L. Vendramin, *On the enumeration of finite L-algebras*, arXiv:2206.04955 (first publicly posted 2022-06-10); *Mathematics of Computation* 92 (2023), 1363–1381, doi:10.1090/mcom/3814, especially Proposition 4.4, Theorem 4.5, and Problem 4.6.

[2] S. Properzi and Y. Qin, *L-algebras and their ideals: from simplicity to semidirect products*, arXiv:2512.08579 (first publicly posted 2025-12-09), especially Definition 1.3, Theorem 4.3, and Corollary 4.4.

[3] W. Rump, *Linear L-Algebras and Prime Factorization*, *Studia Logica* 111 (2023), 57–82, doi:10.1007/s11225-022-10018-1 (abstract and publisher bibliographic record inspected only).
