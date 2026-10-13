# Conditional L1 precedence is exactly mean order under arbitrary dependence
## Finding
For every jointly distributed pair of integrable real random variables \(X,Y\), the conditional \(\mathcal L_1\) precedence relation introduced by Ghosh and Nanda coincides exactly with mean order, without any independence assumption:
\[
X\le_{{\mathrm{{cp-}}\mathcal L_1}}Y
\quad\Longleftrightarrow\quad
\mathbb E X\le\mathbb E Y.
\]
Thus the relation is unchanged by any alteration of the dependence structure that preserves the marginal means. In particular,
\[
X=_{\mathrm{{cp-}}\mathcal L_1}Y
\quad\Longleftrightarrow\quad
\mathbb E X=\mathbb E Y.
\]

## Assumptions and scope
Assume only that \(X\) and \(Y\) are real-valued random variables on a common probability space with \(\mathbb E|X|<\infty\) and \(\mathbb E|Y|<\infty\). No independence, continuity, discreteness, density, or copula assumption is used.

The source defines conditional \(\mathcal L_1\) precedence by comparing
\[
\mathbb E(Y-X\mid X<Y)\Pr(X<Y)
\]
with
\[
\mathbb E(X-Y\mid X>Y)\Pr(X>Y).
\]
When a conditioning event has probability zero, the corresponding product is understood through its canonical unconditional form, \(\mathbb E[(Y-X)\mathbf 1_{{\{X<Y\}}}]\) or \(\mathbb E[(X-Y)\mathbf 1_{{\{X>Y\}}}]\). This agrees with the displayed product whenever the conditioning event has positive probability and extends it without ambiguity to degenerate boundary cases.

## Proof
Set
\[
A=\mathbb E[(Y-X)\mathbf 1_{{\{X<Y\}}}],
\qquad
B=\mathbb E[(X-Y)\mathbf 1_{{\{X>Y\}}}].
\]
Integrability of \(X\) and \(Y\) makes both quantities finite. The defining relation is exactly \(A\ge B\). Since \(Y-X=0\) on \(\{X=Y\}\),
\[
\begin{{aligned}}
A-B
&=\mathbb E[(Y-X)\mathbf 1_{{\{X<Y\}}}]
  +\mathbb E[(Y-X)\mathbf 1_{{\{X>Y\}}}]\\
&=\mathbb E(Y-X).
\end{{aligned}}
\]
Therefore
\[
A\ge B
\quad\Longleftrightarrow\quad
\mathbb E(Y-X)\ge0
\quad\Longleftrightarrow\quad
\mathbb E X\le\mathbb E Y.
\]
No step uses independence. Reversing \(X\) and \(Y\) shows that both precedence directions hold exactly when \(\mathbb E X=\mathbb E Y\). Because the right-hand criterion depends only on the two marginal means, the relation is invariant under every coupling of fixed integrable marginals.

## Verification
The proof is an identity, not an inference from numerical experiments. Its only decomposition is the partition of the sample space into \(\{X<Y\}\), \(\{X=Y\}\), and \(\{X>Y\}\), with the middle term vanishing pointwise. The finite-first-moment assumption guarantees that all positive-part expectations used above are finite.

A boundary check is also immediate: if one strict-comparison event has probability zero, the associated truncated expectation is zero, and the same identity still proves the equivalence. No finite enumeration, asymptotic approximation, or external computational certificate is needed.

## Relationship to prior work
Ghosh and Nanda define conditional \(\mathcal L_1\) precedence in Section 2 of arXiv:2103.01650 and state in Theorem 2.1 that it agrees with mean order when \(X\) and \(Y\) are independent. Immediately afterward they describe the dependent case as an improvement over mean order because it is intended to use dependence. The identity above shows that the independence restriction is unnecessary and that the claimed dependence sensitivity is absent for this particular order.

The same source also introduces a different bounded-distance order, conditional \(K^*\) precedence. The present result does not collapse that second order: its nonlinear weight prevents the signed positive- and negative-part contributions from recombining into \(\mathbb E(Y-X)\).

Targeted searches for the exact unconditional equivalence, coupling invariance, an erratum, and a correction to Theorem 2.1 located the original article and its publication metadata but no prior statement of this strengthening. Semantic-database searches likewise returned no covering finding. This is evidence against overlap, not a proof that no unindexed observation exists.

## Limitations
The result concerns only the conditional \(\mathcal L_1\) precedence relation defined by the source. It makes no claim about stochastic precedence, conditional \(K^*\) precedence, usual stochastic order, likelihood-ratio order, or other dependence-sensitive comparisons.

The originality check cannot exclude an unpublished note, private communication, or unindexed corrigendum containing the same one-line identity. The mathematical claim itself does not depend on any literature-search assumption.

## References
1. S. Ghosh and A. K. Nanda, “Conditional Precedence Orders for Stochastic Comparison of Random Variables,” arXiv:2103.01650v1, first posted 2021-03-02.
2. S. Ghosh and A. K. Nanda, “Conditional precedence orders for stochastic comparison of random variables,” *Statistics & Probability Letters* 193 (2023), 109702. DOI: 10.1016/j.spl.2022.109702.
