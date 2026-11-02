# Mathematical assessment

## Correctness — PASS

The first step and two adaptive coefficients were reconstructed from Zeng--Han--Su--Xie, Algorithm 3 and equation (17). Rotating each independent Gaussian sketch gives the exact identities \(\alpha_1=1/Y\), \(\beta_1=(t/r)ZU/Y\), with \(Y\sim\chi^2_{n-1}\). A second independent first-sketch ratio \(t/r=\|G_\perp\|/|G_0|\) explains why every absolute moment of order at least one of the momentum coefficient diverges. The gamma-integral calculation verifies the finite fractional moments, and an orthogonal projection identity shows bounded iterate errors. The included verifier replays the published coefficient formula and compares it with these identities; numerical evidence is not substituted for the infinite-dimensional or moment proofs.

## Originality — PASS (best-knowledge assessment)

Zeng--Han--Su--Xie supply the adaptive method and its projection interpretation, which is cited, but the inspected full text did not exhibit a distribution or infinite-first-absolute-moment theorem for its adaptively chosen momentum under independent Gaussian sketches. The deterministic Polyak heavy-ball method of Goujaud--Taylor--Dieuleveut and constant-momentum stochastic schemes of Loizou--Richtárik do not imply that formula for these random ASHBM coefficients. Relevant mathematical-record and historical-claim searches did not find a dominating or equivalent result. The Gaussian integral identities themselves are classical and are not asserted novel. Equivalent statements under another parameterization, or work not found by these searches, remain residual priority risks.

## Mathematical value — PASS

The adaptive method's step and momentum parameters form a small random least-squares system; conditionally nearly collinear directions generate potentially very large coefficients. The theorem gives the exact dimension threshold for step-size moments and the stronger dimension-independent divergence of the momentum's first absolute moment. This matters for interpreting moment-based diagnostics and numerical conditioning: a bounded, strictly improving iterate coexists with raw coefficients whose expectations are undefined. The exact uncancelled/projected formulas identify the cancellation mechanism and a geometrically expressed alternative. The result does not prove a particular floating-point failure probability.

## Closest literature and limitations

Closest algorithm: Zeng et al., arXiv:2305.05482, Algorithm 3, equation (17), Section 5. Broader context: Goujaud et al., arXiv:2210.06367; Loizou and Richtárik, arXiv:1712.09677. The claim is limited to exactly two iterations of the identity problem with independent Gaussian rank-one sketches and exact arithmetic. Generic numerical consequences and independent priority verification remain open.

Self-review: passed. Independent audit: not yet performed.
