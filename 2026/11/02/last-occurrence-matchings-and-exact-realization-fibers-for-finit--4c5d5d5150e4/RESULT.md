# Last-occurrence matchings and exact realization fibers for finite flat Heyting–Lewis chains

## Finding

Fix an integer \(n\ge1\) and the ordered set \(C_n=\{0<1<\cdots<n-1\}\). Write \(U_a=\{a,\ldots,n-1\}\) for \(0\le a<n\), and \(U_n=\varnothing\); these are all the upsets of \(C_n\). For every binary relation \(R\subseteq C_n\times C_n\), let \(J_R\) be the **flat strict-implication** operation defined by
\[
J_R(A,B)=\bigl\{i\in C_n:\ \forall j\ge i,\ R[j]\subseteq A\Longrightarrow R[j]\subseteq B\bigr\},
\]
where \(R[j]=\{t:jRt\}\).

Define \(\mu_R(j)=\min R[j]\) for nonempty rows, with a special empty-row symbol otherwise. For each \(t\in C_n\), put
\[
\ell_t(R)=\max\bigl\{j:\ R[j]\ne\varnothing,\ \mu_R(j)=t\bigr\},
\qquad\max\varnothing=-1.
\]
The nonnegative values of the vector \(\ell(R)\) are pairwise distinct. In fact,
\[
\boxed{J_R(U_a,U_b)=U_{1+\max\{\ell_t(R):a\le t<b\}}}
\qquad(0\le a,b\le n),
\]
with an empty maximum equal to \(-1\), including the case \(a\ge b\). Conversely, **every** vector \(\ell\in\{-1,0,\ldots,n-1\}^n\) whose nonnegative entries are distinct occurs. Two relations induce exactly the same strict-implication operation if and only if their \(\ell\)-vectors agree.

Thus the number of distinct flat strict-implication operations on the fixed \((n+1)\)-element Heyting algebra of chain upsets is
\[
\boxed{T_n=\sum_{k=0}^{n}\binom nk^{\!2}k!},
\]
with \(T_1,T_2,T_3,T_4,T_5=2,7,34,209,1546\). The count is that of partial bijections between two distinguished copies of \(C_n\), not the count \(2^{n^2}\) of underlying binary relations.

Each operation has a **unique inclusion-least representing relation**
\[
\widehat R_{\ell}=\bigl\{(\ell_t,t):\ell_t\ge0\bigr\}.
\]
Moreover, its exact number of representing relations can be read from \(\ell\). Put \(w_t=2^{n-1-t}\), and \(I=\{\ell_t:\ell_t\ge0\}\). Then
\[
\boxed{
\#\{R:\ell(R)=\ell\}=
\left(\prod_{t:\ell_t\ge0}w_t\right)
\left(\prod_{j\in C_n\setminus I}\left(1+\sum_{t:\ell_t>j}w_t\right)\right).
}
\]
In particular these exact fiber sizes sum to \(2^{n^2}\) over all partial-injection vectors \(\ell\).

## Assumptions and scope

All statements hold for **every integer** \(n\ge1\), with the chain order, its labelled worlds and the entire Heyting algebra of upsets fixed. Every binary relation \(R\subseteq C_n^2\) is allowed, including relations with empty rows, loops and arbitrary successor sets. There are no additional transitivity, reflexivity, or S4-like restrictions. The operation is the flat interpretation of the binary Lewis-style strict implication, not the ordinary intuitionistic Heyting implication, sharp-frame semantics, or a preconditional in a different algebraic language.

This is a classification of the flat-frame-induced operations on the specified upset algebra. It does not assert that every abstract Lewisian Heyting-algebra expansion of that Heyting reduct arises from a binary relation on this particular frame.

## Proof

**Row reduction.** For every nonempty subset \(S\subseteq C_n\), \(S\subseteq U_a\) if and only if \(\min S\ge a\). For an empty \(S\), inclusion into every upset is true. Hence a row \(R[j]\) violates the implication \(R[j]\subseteq U_a\Rightarrow R[j]\subseteq U_b\) precisely when \(a<b\), the row is nonempty, and \(a\le\mu_R(j)<b\). Therefore \(i\in J_R(U_a,U_b)\) if and only if there is no such violating row indexed by \(j\ge i\). If \(d\) is the largest violating row index, or \(-1\) when no violating row exists, this is equivalent to \(i>d\), proving the displayed operation formula with \(d=\max\{\ell_t:a\le t<b\}\).

**Injective last-occurrence encoding and recovery.** A row has at most one minimum. Consequently distinct targets \(t\) cannot have the same nonnegative last-occurrence index. For every \(t<n\), the single adjacent-upset value
\[
J_R(U_t,U_{t+1})=U_{\ell_t(R)+1}
\]
recovers \(\ell_t(R)\) exactly, because the upsets \(U_0,\ldots,U_n\) are distinct. Thus identical operations yield identical vectors, while the row formula gives the converse.

Let \(\ell\) be any vector with distinct nonnegative entries. Define \(\widehat R_{\ell}\) to have precisely the edges \((\ell_t,t)\) for the present targets. Its row at \(\ell_t\) is the singleton \(\{t\}\), and every other row is empty. Hence \(\ell(\widehat R_{\ell})=\ell\), proving surjectivity. Counting domain size \(k\), its choice of \(k\) targets, choice of \(k\) distinct row indices, and bijections between them gives \(\binom nk^2k!\); summing over \(0\le k\le n\) proves the census.

**Least representative.** If \(\ell_t(R)=j\ge0\), then \(\mu_R(j)=t\), so \((j,t)\in R\). Therefore \(\widehat R_{\ell}\subseteq R\) for every relation representing \(\ell\). The canonical relation itself represents \(\ell\), so it is the unique least element of the realization fiber under inclusion. In particular it has exactly as many edges as the size of the partial injection's domain.

**Exact fibers.** Suppose \(\ell_t=j\ge0\). At this forced row index \(j\), the row must have minimum \(t\), and may independently include any target strictly larger than \(t\). There are \(w_t=2^{n-1-t}\) possibilities. These forced indices are disjoint. At any non-forced index \(j\notin I\), the row may be empty (one possibility) or may have minimum \(t\) only when its designated last occurrence is strictly later, \(\ell_t>j\). In the latter case there are \(w_t\) row subsets with minimum \(t\). Those cases are disjoint over \(t\) and independent across row indices, giving the product formula. Conversely, all such row choices preserve the intended last-occurrence vector; no other choices can do so. Every binary relation has exactly one vector, so summing the fibers recovers \(2^{n^2}\).

## Verification

The included standalone Python program `checker.py` independently computes the operation from the original row-inclusion semantic clause for **every** binary relation on chains of sizes \(1,2,3,4\), i.e. \(2+16+512+65{,}536=66{,}066\) relations. It separately compares the adjacent-upset reconstruction and all \((n+1)^2\) operation values with the claimed formula; it checks the number and injectivity of signatures, all exact fiber sizes, and the total fiber mass. The observed operation counts are \(2,7,34,209\), with all tests passing. The universal theorem rests on the preceding argument, not on exhaustive finite experiments.

Reproduce with standard Python 3, without third-party packages: `python checker.py`. The checker prints `ALL_CHECKS_OK` on successful completion.

## Relationship to prior work

De Groot and Litak, *Relational Semantics for Flat Heyting-Lewis Logic* (arXiv:2603.28402, first posted March 30, 2026), introduce the exact flat operation in Definition 3.1/3.5 and show in Proposition 3.10 that upward-closing individual successor rows preserves the complex algebra. On chains this already implies that the *minimum* of a nonempty row is the relevant rowwise invariant. The new step here is identifying precisely which of those row minima survive the universal quantification over later rows: one **last occurrence per target**. This produces the operation-level bijection with partial injections, a canonical least representing frame, and exact full realization-fiber counts; none is asserted in that paper's inspected Sections 3–5 or appendix.

The published *Bell-number census for the S4-like finite-chain flat frames* counts relations satisfying two extra frame axioms and explicitly restricts to that class; it does not enumerate induced operations over **all** unrestricted flat relations or describe their exact fibers. Published chain-frame maxima classifications for other modal interaction conditions and finite-chain preconditional classifications study different semantics and are not implication-equivalent to this theorem. The numerical sequence \(T_n\) is the previously known partial-permutation sequence OEIS A002720; its independent combinatorial enumeration is **not** claimed as a novel sequence identity. The proposed scientific contribution is the semantic identification and fiber classification.

## Limitations

The quotient is taken on a fixed labelled finite chain. Different underlying intuitionistic posets, additional frame axioms, or sharp strict-implication semantics are not classified. The oldest possible equivalent semantic classification in the broader Lewisian-algebra literature has not been ruled out conclusively. No statement about independent validation or mathematical priority beyond the inspected literature is made.

## References

1. J. de Groot and T. Litak, *Relational Semantics for Flat Heyting-Lewis Logic*, arXiv:2603.28402 (March 30, 2026), also Electronic Proceedings in Theoretical Computer Science 447 (2026), doi:10.4204/EPTCS.447.25; Sections 3.1–3.3, especially Definition 3.5 and Proposition 3.10.
2. T. Litak and A. Visser, *Lewis meets Brouwer: Constructive strict implication*, Indagationes Mathematicae 29 (2018), 36–90, doi:10.1016/j.indag.2017.10.003. Different strict-implication setting; consulted for background and priority risk.
3. *Bell-number census for the S4-like finite-chain flat frames*, published mathematical finding at https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-bell-number-census-for-the-s4-like-finite-chain-flat-frames--6ab97388fd68; restricted-frame comparison.
4. *Maxima normal form and exact census for chain birelational relations*, published mathematical finding at https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-maxima-normal-form-and-exact-census-for-chain-birelational-relat--f1e0f9b64170; different frame conditions and semantic operator.
5. OEIS A002720, partial permutations, https://oeis.org/A002720; independently known combinatorial count, not a source for the semantic theorem.
