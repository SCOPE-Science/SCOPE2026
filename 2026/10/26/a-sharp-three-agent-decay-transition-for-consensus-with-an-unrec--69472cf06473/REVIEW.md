# Review of the three-agent adaptive-confidence decay theorem

## Correctness — PASS

The exact K3 effective-path operator has positive gap recurrences u_next=(u+2v)/6 and v_next=(2u+v)/6. Consequently both active edges remain active for every pre-activation step and the outer gap is D/2^t. The inactive outer confidence is c0 delta^t; the strict inequality crosses precisely when (2 delta)^t>D/c0. This proves the global sector dichotomy including equality delta=1/2; the left stationary vector (2,3,2)/7 and the (-1/6)-mode give limiting / exact consensus expressions. The two-agent case is impossible by direct one-step averaging or frozen disagreement. Executed exact-rational 72-family/15-step trajectory checks with a separate step function; these supplement but do not replace proof. Scope includes K3, ordered initial opinions, homogeneous c0, gamma in (0,1], delta in (0,1).

The exact-rational script executes successfully on 72 admissible parameter families across 15 steps each. The analytic proof separately handles infinitely many steps, the strict-equality boundaries, and the two-node minimality argument. No numerical extrapolation is used as a proof.

## Originality — PASS (with residual uncertainty)

The 2023 primary manuscript and 2025 expanded paper introduce exactly this model and report numerical same-limit nonreceptiveness, but their general edge limits and stabilization results do not quantify the exact three-agent first activation or sharp half-threshold. The related 2024 thesis discusses mediator nodes as a future direction. Comparisons to alternative rewiring BCMs and distinct mathematical research records show nonimplication, rather than simple keyword mismatch; publication priority remains non-exhaustively checked.

The nearest primary literature is Li, Luo, and Porter, arXiv:2303.07563 (March 14, 2023), DOI 10.1137/23M1558951 (journal 2025), and the 2024 thesis of Grace Li. The mathematical comparison is to the *actual implication*: their general confidence-limit/stabilization theorems and large-network numerical observation do not fix the active-set outcome in the initial three-agent path sector or imply the sharp \(1/2\) decay boundary. In a different 2021/2023 study, Kan, Feng, and Porter analyze rewiring rather than exponentially decaying thresholds. Published research records with related bounded-confidence and fading-consensus terminology do not assert this theorem. Full publication-priority uniqueness is not certified.

## Value — PASS

The source specifically highlights unreceptive dyads agreeing via intermediaries as a striking limitation of inferring social receptiveness from opinion clusters, and its 2024 extended discussion invites mediator analysis. The theorem identifies the minimal mediator network and an exact structural phase boundary separating asymptotic agreement with permanently vanishing trust from finite-time agreement with full trust, including strict timing and a positive-volume regime. It is a new quantitative answer to a motivated gap, not just a normalization or numerical curiosity.

## Limitations and closest sources

Only homogeneous initial confidence on a complete three-agent physical graph, an initially ordered effective path, and strict synchronous adaptive-confidence averaging are established. One must not universalize \(1/2\) to heterogeneous networks or asynchronous systems. The original qualitative phenomenon belongs to Li, Luo, and Porter; the new contribution is the quantified exact phase transition, finite activation and minimality classification. The work awaits independent audit.

Self-review: passed. Independent audit: not yet performed.
