# Review: post-SDPI relay counterexample family

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The capacity calculation was checked independently from the proposed characterization. A block-Markov partial-decode-forward construction achieves one noiseless bit through the direct coordinate plus any relay-path rate below \(\min(C_1,C_2)\). The two cutset terms are bounded by \(1+C_1\) and \(1+C_2\), respectively, giving the exact capacity \(1+\min(C_1,C_2)\).

For the proposed characterization, the decode-forward term is at most \(C_1\). Shiu's common relaxation of the two compress-forward terms depends only on the factorization
\[
P_{A,B,X_r}W_1(Y_r|A)W_2(Z|X_r)P_{\widehat Y_r|Y_r,X_r},
\]
not on the numerical value \(1/4\). Its relaxed objective and constraint therefore remain
\[
H(B|X_r)+I(A;\widehat Y_r|B,X_r)
\]
and
\[
I(\widehat Y_r;Y_r|B,X_r)\le I(X_r;B,Z).
\]
Conditioning on \((B,X_r)\) preserves the Markov chain \(A\to Y_r\to\widehat Y_r\) with first channel \(W_1\). Applying the input-free post-processing coefficient pointwise and averaging yields
\[
I(A;\widehat Y_r|B,X_r)\le\eta I(Y_r;\widehat Y_r|B,X_r).
\]
The resulting upper bound
\[
H(B)-(1-\eta)I(B;X_r)+\eta I(X_r;Z|B)\le1+\eta C_2
\]
was checked for hidden dependence assumptions; none are needed beyond the stated channel factorization. Because \(C_1\le1\), the same bound dominates the decode-forward term.

For BSC links, the specialization \(C_i=1-h_2(\delta_i)\) and \(\eta=(1-2\delta_1)^2\) gives the stated wedge. On \(0<\delta_1\le\delta_2<1/2\), monotonicity of BSC capacity gives \(C_2\le C_1\), so the certified gap reduces exactly to
\[
[1-(1-2\delta_1)^2]C_2
=4\delta_1(1-\delta_1)(1-h_2(\delta_2))>0.
\]
The finite artifact checks representative values and a grid but is not used as a substitute for the proof.

Boundary cases were stress-tested. At \(\delta_1=0\), \(\eta=1\) and the strict gap disappears; at \(\delta_2=1/2\), \(C_2=0\) and the relay path carries no information. These agree with the theorem's strict hypotheses.

## Originality

**PASS, to the best of our knowledge.**

The full text of Shiu, arXiv:2609.18727, was inspected. It gives one explicit channel with both noisy links equal to \(\operatorname{BSC}(1/4)\), proves an achievable rate \(2-h_2(1/4)\), and upper-bounds the proposed three-scheme expression using the BSC post-processing coefficient. It does not state the arbitrary-\(W_1,W_2\) criterion \(\min(C_1,C_2)>\eta C_2\), the two-parameter BSC region, or the conclusion that every nondegenerate symmetric BSC crossover is a counterexample.

The full arXiv text of Ponniah, arXiv:2609.15709, was inspected for the claimed three-scheme characterization and its role for partial decode-forward. The established orthogonal-sender capacity result of El Gamal--Zahedi (2005) was also checked; that literature supplies the true-capacity side but predates, and therefore does not address, the 2026 proposed characterization or its post-SDPI failure mechanism.

Targeted searches used the source title, Ponniah's title, "relay channel" with "post-SDPI" or "strong data processing", BSC crossover generalizations, partial decode-forward, and orthogonal sender components. No prior statement of this family criterion or the explicit BSC wedge was located. Repository searches for relay-channel, SDPI, Ponniah, Shiu, and equivalent counterexample terminology found no existing SCOPE result covering the claim.

No inaccessible paper was identified that is specifically more likely than the recent-source risk to contain the same theorem. The principal residual risk is temporal: the motivating counterexample is a very recent preprint, so an unindexed independent note or a subsequent revision could contain the same generalization.

The novelty claim is deliberately narrow. The capacity of orthogonal sender-component relay channels, partial decode-forward, post-SDPI, and the BSC contraction coefficient are prior results. The claimed contribution is the general post-SDPI separation criterion for Ponniah's proposed expression and its explicit continuum of BSC counterexamples.

## Value

**PASS.**

A single numerical counterexample establishes falsity, but it does not explain how robust the failure is. The theorem isolates a simple mechanism: the true relay path is limited by \(\min(C_1,C_2)\), whereas the relaxed compress-forward terms are limited by \(\eta C_2\). This produces a channel-independent sufficient condition and shows that the failure occupies a nontrivial parameter region rather than an isolated point.

For BSC links the consequence is especially transparent: every \(0<\delta_1\le\delta_2<1/2\) fails the proposed characterization. The symmetric one-parameter family alone gives infinitely many explicit counterexamples, and \(\delta=1/8\) provides a larger certified numerical gap than the motivating \(\delta=1/4\) example.

The result does not repair or replace a general relay-channel capacity theorem. Its value is diagnostic and structural: it characterizes a broad class on which the specific proposed three-scheme formula is necessarily too small.

## Verification state

- review_type: `same_model_review`
- independent: `false`
- same_model_review_status: `passed`
- independent_audit_status: `not_performed`
