# Partial-matching normal forms for flat Heyting-Lewis implication on finite chains
## Finding

For every integer \(n\ge1\), the distinct flat Heyting-Lewis strict-implication operations induced by arbitrary binary relations on the \(n\)-world chain are in canonical bijection with partial injections from the \(n\) threshold labels to the \(n\) world positions. Each semantic equivalence class has **one and only one** relation with the fewest arrows; that relation is the graph of its partial injection. In particular, there are exactly
\[
N_n=\sum_{k=0}^{n}\binom{n}{k}^{2}k!
\]
different operations, with \(\binom nk^2k!\) of minimum relation size \(k\). Since the underlying finite Heyting chain has no nontrivial automorphism, this is also the number of isomorphism types of the corresponding expansions of that fixed Heyting reduct.

The first six values, for \(n=1,\ldots,6\), are \(2,7,34,209,1546,13327\). These numbers already occur in classical combinatorics as counts of partial injections (OEIS A002720); the mathematical assertion here is the **semantic correspondence, its unique sparsest frame representation, and its exact redundancy fibres**, not the invention of the numerical sequence.

## Assumptions and scope

Fix \(W_n=\{0,1,\ldots,n-1\}\) ordered by its usual total order, and write \(U_p=\{p,p+1,\ldots,n-1\}\) for \(0\le p\le n\), so \(U_n=\varnothing\). The Heyting algebra of upsets has precisely these \(n+1\) elements. A relation \(R\subseteq W_n\times W_n\) is **completely arbitrary**: no reflexivity, transitivity, seriality, or upward-flatness is assumed. Write \(R[j]=\{v:jRv\}\) and interpret strict implication by de Groot–Litak's flat clause:
\[
J_R(A,B)=\{i\in W_n:\forall j\ge i,\, (R[j]\subseteq A\Rightarrow R[j]\subseteq B)\}.
\]
For each source row set
\[
r_j=\begin{cases}\min R[j],&R[j]\ne\varnothing,\\n,&R[j]=\varnothing,\end{cases}
\qquad
\ell_p=\max\{j\in W_n:r_j=p\}\quad(0\le p<n),
\]
where a maximum of an empty set is \(-1\). Put \(S=\{p<n:\ell_p\ge0\}\) and \(k=|S|\). The map \(\ell:S\to W_n\) is injective, because a single row has only one minimum. We call \(\ell\) the last-occurrence partial injection.

## Proof

**Step 1 — complete semantic formula.** For any row and any upset \(U_p\), the inclusion \(R[j]\subseteq U_p\) holds exactly when \(r_j\ge p\), including the empty-row case \(r_j=n\). Thus if \(p\ge q\), the conditional \(R[j]\subseteq U_p\Rightarrow R[j]\subseteq U_q\) always holds. If \(p<q\), it fails precisely at those rows with \(p\le r_j<q\). Hence
\[
J_R(U_p,U_q)=
\begin{cases}
U_0,&p\ge q,\\
U_{1+\max\{\ell_s:p\le s<q\}},&p<q,
\end{cases}
\]
with \(\max\varnothing=-1\). This expression includes boundary cases \(p=0\), \(q=n\), empty rows, and an absent label; the output threshold lies in \(\{0,\ldots,n\}\).

**Step 2 — completeness and separation of the invariant.** Step 1 shows that the operation depends only on \(\ell\). Conversely the adjacent input \(J_R(U_p,U_{p+1})=U_{1+\ell_p}\) recovers each \(\ell_p\) from the operation, including \(\ell_p=-1\). Thus two relations induce equal operations if and only if their last-occurrence partial injections are identical.

**Step 3 — every partial injection occurs and has a unique sparsest representative.** Given any partial injection \(f:S\to W_n\), define \(R_f=\{(f(p),p):p\in S\}\). Distinct values \(f(p)\) occupy distinct source rows, so its last-occurrence vector is exactly \(f\), and by Step 2 it realizes one operation. Conversely any relation realizing the same operation must have a row whose minimum is \(p\) at the last-occurrence index \(f(p)\), for every \(p\in S\). These are \(k\) different nonempty rows, hence at least \(k\) arrows. If it has exactly \(k\) arrows, every arrow must lie in one of those prescribed rows, and the only possible target at that row is its prescribed minimum \(p\). Therefore it is exactly \(R_f\). Existence and **uniqueness** of the minimum-arrow representative both follow.

**Step 4 — enumeration and isomorphisms.** Choose \(k\) threshold labels and \(k\) distinct world positions and biject them: \(\binom nk\binom nk k!=\binom nk^2 k!\) choices. Summing over \(k\) counts all distinct operations. A finite totally ordered Heyting algebra admits only the identity order automorphism; an isomorphism of full expansions must preserve its Heyting order. Hence distinct operations are not isomorphic as expansions of this fixed reduct.

**Step 5 — exact fibres among all raw relations.** Fix \(f:S\to W_n\). At a prescribed final row \(j=f(p)\), the relation's row can contain \(p\) and any subset of strictly greater targets, so there are \(2^{n-1-p}\) choices. At every other row \(j\), either the row is empty (one choice) or its minimum is some \(p\in S\) with \(f(p)>j\). No label absent from \(S\), or used at or after its final occurrence, is allowed. For a specified such \(p\), there are \(2^{n-1-p}\) choices of the row. The row choices are independent, giving exactly
\[
F_n(f)=\prod_{p\in S}2^{n-1-p}
\prod_{j\notin f(S)}\left(1+\sum_{p\in S:\,f(p)>j}2^{n-1-p}\right).
\]
All factors are positive integers, and summing these fibres over all partial injections partitions the \(2^{n^2}\) raw binary relations.

## Verification

Two executable Python 3 programs accompany this result. Run `python3 verify.py` and `python3 verify_all_relations.py` with the standard library only. The first enumerates every upward-flat row-threshold relation through \(n=6\) (\(117649\) relations at \(n=6\)), checks the direct operator semantics against the closed formula, checks injectivity, rank counts, and upward-flat fibre multiplicities, and prints `VERIFY_OK`. The second enumerates all \(2^{n^2}\) unrestricted binary relations for \(n=1,2,3,4\) (\(65536\) at \(n=4\)), checks unique edge-minimality and the unrestricted fibre count, and prints `RAW_VERIFY_OK`. The proofs above establish the statements for **all** \(n\), not merely these finite test sizes.

## Relationship to prior work

The relational clause and preservation of complex algebras under target-upward closure are established in de Groot and Litak (2026), Definition 3.1, Definition 3.5 and Proposition 3.10. Their Remark 3.8 identifies the broader difficulty of recovering economical relational presentations from algebras. The present result solves this natural representation and equivalence problem completely on chain carriers, including a unique edge-minimizer and exact relation-to-operation fibre sizes. This is not a claim of general finite-poset duality or of a classification of all abstract Heyting-Lewis expansions.

Alizadeh and Joharizadeh (2015) study algorithms for counting **all** weak Heyting expansions of finite distributive lattices. On a chain the present flat operations satisfy the sharp distributivity identity automatically, and so belong to that broader weak-Heyting setting. Their accessible abstract does not establish the chain-specific partial-injection or unique-minimal-relation result; the unavailable full paper remains a literature risk. The resulting numerical sequence and rank coefficients coincide with well-known partial-permutation/rook-matching counts (OEIS A002720 and A144084); the correspondence to the 2026 flat semantics and edge-minimality are the proposed contribution.

## Limitations

This classifies only operators *realized by the specified flat relational semantics on finite nonempty chains*; it does not classify all weak Heyting or Lewisian Heyting algebra expansions on a chain, all preorder carriers, or all formulas and deductive extensions of the logic. The formula for exact fibres counts labeled raw relations; the isomorphism count concerns algebras with the chain Heyting reduct. Finite checks are corroboration, not infinite proofs. The inaccessible full text of the 2015 counting article leaves residual risk of unnoticed equivalent specialization; the known rook-counting sequence by itself is not a new numerical discovery.

## References

- Jim de Groot and Tadeusz Litak, *Relational Semantics for Flat Heyting-Lewis Logic*, arXiv:2603.28402v1 (first public 2026-03-30), updated v2 (2026-06-30), EPTCS 447 (2026), 445–463, DOI:10.4204/EPTCS.447.25. https://arxiv.org/html/2603.28402v2
- Majid Alizadeh and Nima Joharizadeh, *Counting weak Heyting algebras on finite distributive lattices*, Logic Journal of the IGPL 23 (2015), 247–258, DOI:10.1093/jigpal/jzu033 (abstract inspected; full text not obtained).
- OEIS A002720, *Number of partial permutations of an n-set*. https://oeis.org/A002720
- OEIS A144084, *Number of partial bijections of height k of an n-element set*. https://oeis.org/A144084
