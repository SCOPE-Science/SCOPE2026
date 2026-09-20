# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The proof was checked independently from the finite enumeration.

For \(H=G+\overline{K_m}\) at
\[
m=n-\max\{1,\delta(G)\}-1,
\]
the cross-edge imbalance formula
\[
\operatorname{imb}_H(va)=|d_G(v)-(\max\{1,\delta(G)\}+1)|
\]
is correct, while imbalances on edges inherited from \(G\) are unchanged. Writing
\[
A=\sum_v |d_G(v)-c|,\qquad
J=\sum_{uv\in E(G)}|d_G(u)-d_G(v)|,\qquad c=n-m,
\]
gives the exact total imbalance \(S=J+mA\).

The key estimates were stress-tested case by case. Every imbalance is at most \(m\) for \(n\ge5\). Also \(A\ge D\), where \(D\) is the largest positive imbalance: this is immediate for cross edges and follows from the triangle inequality for internal edges. Hence \(S\ge mD\). If \(D<m\), then \(S\ge D(D+1)\). If \(D=m\) is attained internally, then \(J\ge m\), again giving \(S\ge D(D+1)\). If \(D=m\) is attained only on a cross edge, the minimum-degree formulas show that for \(n\ge5\) this can occur only with \(m=D=1\); parity then gives \(S\ge2=D(D+1)\).

The auxiliary graphicality lemma was rederived directly from Erdős--Gallai. For a positive sequence of even sum \(S\), maximum \(D\), and \(S\ge D(D+1)\), the inequality
\[
\min\{k,d_i\}\ge (k/D)d_i
\]
for \(k\le D\), together with \(\sum_{i\le k}d_i\le kD\), proves every Erdős--Gallai inequality. For \(k>D\) the clique term alone suffices. The standard parity identity for graph irregularity supplies evenness.

The edge cases \(D=0\) and \(m=0\) are handled explicitly. The latter forces \(G=K_n\). Zero imbalance entries are harmless because they correspond to isolated vertices in a realization.

As supporting evidence, the standalone verifier exhaustively checked every unlabeled graph through order seven in the NetworkX graph atlas. All 34 order-five, 156 order-six, and 1044 order-seven graphs satisfy the theorem. Among the eleven order-four graphs, the unique failure is the known \(K_3\cup K_1\) example, with positive imbalance sequence \((2,2)\).

## Originality

PASS, to the best of our knowledge. The primary 2023 paper was inspected at Theorem 3.7 and the paragraph immediately following it. It proves the empty-join guarantee for
\[
m\ge n-\max\{1,\delta(G)\},
\]
exhibits \(K_3\cup K_1\) as a failure at one less, and explicitly asks whether such a failure can be constructed for arbitrary order.

Searches under the exact threshold expression, the terms `imbalance graphic`, `join`, `empty graph`, the Theorem 3.7 citation, and synonymous degree-sequence formulations located no later result answering this one-step boundary. The 2019 operations paper and the 2014 foundational paper were also checked at the level of their available statements and do not provide this theorem.

Two 2026 proofs of the Imbalance Conjecture were inspected in accessible full text. They concern graphs with strictly positive imbalance on every edge; they do not state the present join theorem, and their hypothesis does not apply in general because the empty join can contain zero-imbalance edges. A 2026 paper on regular blocks was also inspected; it settles the block-graph, line-graph-of-trees, and bicyclic questions from the 2023 paper but does not state this empty-join boundary result.

No specific inaccessible paper was found whose visible title, abstract, or theorem statement suggests coverage. Residual risk remains from unindexed work or terminology not captured by the searches.

## Value

PASS. The result directly resolves a concrete question left immediately after a published sufficient theorem. It shows that the known order-four obstruction is exceptional at the one-step-lower boundary: from order five onward the universal guarantee is strictly stronger than previously stated. The proof is not a finite extension but a general argument based on a reusable sufficient condition for graphical sequences.

The result is intentionally limited to a one-step improvement. It does not determine the minimum empty-join size for each graph or the optimal universal threshold under different parameterizations.

## Limitations

- Originality is asserted only to the best of our knowledge; unindexed parallel work remains possible.
- The new theorem improves the 2023 bound by one but does not characterize all smaller values of \(m\).
- The finite enumeration is corroborative only; correctness rests on the symbolic proof.
- The two 2026 Imbalance Conjecture preprints are recent and may receive revisions.
- Independent audit has not been performed.
