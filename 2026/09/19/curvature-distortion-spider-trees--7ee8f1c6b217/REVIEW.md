# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof is a direct reduction of the finite-tree fixed-point theorem
for LLY curvature-distortion. On each degree-two arm, zero curvature forces
\(x_j^2=x_{j-1}x_{j+1}\), hence a geometric progression. The center equation
then reduces every long arm to
\[
s=\rho^{\ell-1}(\rho+1).
\]
Summing the center-incident weights gives the stated scalar equation. Its
left-hand side is continuous and strictly decreasing in \(s\), is at least one
at \(s=d\), and tends to zero, so the scalar solution is unique. The constructed
weights satisfy the complete fixed-point system; Xia's uniqueness and optimality
theorem therefore identifies them as the canonical optimal weights.

The ordering of arm contributions is strict in arm length, which proves both
the distortion formula and strict monotonicity under arm lengthening. The two
closed-form extremizers follow by solving the scalar equation for the one-long-arm
and all-equal-arm patterns.

A standalone numerical verifier independently checks the displayed weights
against the nonlinear fixed-point map on 660 deterministic test cases, including
mixed arm lengths and the two extremal families. The largest observed residual
is \(3.638\times10^{-12}\). The finite checks support but do not replace the
proof.

## Originality

**PASS, to the best of our knowledge.** The most relevant source is Qing Xia,
arXiv:2609.12125v2. Its current 27-page full text was inspected. Section 4.2
records two explicit finite-tree families: double stars and a symmetric
three-center tree; Section 4.3 proves suppression monotonicity and gives
\(ST_{2,1}\) as a strict example. Full-text searches for `spider` and
`subdivid` returned no match. The present one-long-arm formula contains
\(ST_{2,1}\) as its smallest nontrivial special case but extends it to arbitrary
arm length and degree, while the general theorem treats every finite spider.

Searches for `curvature-distortion` together with `spider`, `starlike tree`,
`subdivided star`, and `uniform subdivision`, and searches for weighted
Lin--Lu--Yau curvature on spider/starlike trees, did not locate an equivalent
distortion formula or stronger result.

The nearest older weighted-tree literature addresses a different optimization
target. Bai--Hua (arXiv:2604.22449) studies constant-curvature discrete Einstein
metrics via a Perron eigenvector; its accessible full text contains no `spider`,
`starlike`, or `subdivid` match. Lin--Liu (arXiv:2603.10479) studies prescribed
curvature flow. Those results do not imply the minimum multiplicative edge-weight
spread for nonnegative curvature.

Residual risk remains because the curvature-distortion invariant is extremely
recent, so parallel work may not yet be indexed, and an equivalent consequence
could be phrased only through nonlinear tree weights rather than spider
terminology. No inaccessible paper was identified whose known statement
materially suggests coverage of the result.

## Value

**PASS.** The result solves the new invariant on a standard infinite tree family
with arbitrary arm lengths, reduces an edge-dimensional nonlinear fixed point to
one scalar equation, and gives the entire canonical optimal weight explicitly.
The extremal law shows that degree-two subdivisions can amplify distortion from
the star value \(1\) to \((d-1)^{L-1}\) while the number of branch vertices
remains exactly one. This gives a quantitative and exponentially sharp refinement
of the source paper's qualitative suppression monotonicity on spiders.

## Limitations

- The theorem is restricted to finite spider trees and the fixed-combinatorial-distance weighted LLY convention.
- Arbitrary mixed arm lengths are characterized by a unique scalar equation rather than elementary radicals.
- The invariant and its literature are very recent; unindexed parallel work remains a residual originality risk.
- Numerical verification is finite and is not a substitute for the proof.
- Independent audit has not been performed.
