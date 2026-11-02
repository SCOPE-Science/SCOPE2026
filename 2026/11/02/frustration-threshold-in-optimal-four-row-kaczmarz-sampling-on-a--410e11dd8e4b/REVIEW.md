# Self-review

## Correctness

**PASS.** The exact unit-row Kaczmarz contraction identity reduces the problem to a diagonal majorant semidefinite program. The two explicit primal matrices have positive-semidefinite reversal blocks, while the collinear and planar correlation matrices give matching dual values. Complementary slackness recovers every diagonal majorant coordinate from a unit dual vector, establishing uniqueness for all \(t>0\), including \(t=1/3\). The explicit example and implicit-function argument confirm that the assumptions are realizable. The bundled verifier corroborates the certificates and actual one-step contraction numerically. The uniform proof is algebraic and does not rely on finite enumeration.

## Originality

**PASS, qualified.** Needell–Srebro–Ward establish the weighted Kaczmarz framework, and Agaskar–Wang–Lu investigate general row-probability optimization and exact mean-square behavior. Laurent–Mascarin–Telen characterize the underlying cycle elliptope geometrically, but do not present this Kaczmarz one-step signed-inverse-Gram allocation and its exact universal breakpoint in their examined statements. A previously identified inverse-positive coordinate-sampling theorem is inapplicable: a negative sign around the four-cycle cannot be removed by row sign switching. The complete text of Agaskar–Wang–Lu was inaccessible, so specialized prior coverage is a genuine residual risk rather than disproved novelty.

## Value

**PASS.** The result turns a four-variable semidefinite sampling problem into a closed optimal probability rule for a family of normalized linear systems with one frustrated conditional-correlation cycle. It characterizes a universal \(1/3\) transition in the rank of an optimal dual certificate, gives exact contraction and uniqueness, and distinguishes effects invisible in sign-balanced inverse-Gram sampling. The family is motivated by Kaczmarz importance-sampling design, not an arbitrary numerical instance.

## Limits and literature

The problem is one-step fixed-distribution minimax squared-error contraction, not an exact multistep error exponent. The diagonal entries are constrained by actual unit-row Gram realizability, for which the text gives an existence proof. Existing general SDP and elliptope formulations remain credited. An inaccessible specialized source is identified transparently, and independent audit is still needed.

Self-review: passed. Independent audit: not yet performed.
