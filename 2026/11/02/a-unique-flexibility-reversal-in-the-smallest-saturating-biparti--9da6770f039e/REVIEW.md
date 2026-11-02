# Scientific review: smallest saturating-flexibility reversal

## Correctness — PASS

The precise model uses fixed flexible endpoints and independent edge indicators with probabilities \(p\) for inflexible–inflexible pairs and \(q\) when at least one endpoint is flexible. The proof represents every finite compatibility graph with its exact monomial probability, enumerates all 16 graph states on \(K_{2,2}\) and 512 on \(K_{3,3}\), and obtains exact expectation polynomial identities. A separate enumeration algorithm agrees on every graph's maximum matching. The resulting factors are \((q-p)(1-q)(2q^2-q+1)\) and \((q-p)P(p,q)\). Strict decrease of \(P\) follows from all 45 coefficients in the homogeneous simplex expansion of \(-P_q\): 43 positive and two zero, with strictly positive evaluation throughout the intended interior. The two boundary signs prove existence and uniqueness of the crossing, without extrapolating from numerical tests. The supplementary exact endpoint and rational-witness checks passed.

## Originality — PASS, qualified

The literature comparison separates model semantics and logical implications. Ameen–Sentenac–Yu (arXiv:2604.02295) use type-pair probabilities and large-market limits with random flexible types. Freund–Martin–Zhao (arXiv:2404.04709) consider additive flexibility effects and an explicit two-sided placement comparison; their \(2\times2\) and asymptotic statements do not imply a fixed-design saturating \(3\times3\) polynomial or unique crossover. The matching literature additionally contains exact finite-market results for other objectives, but no indexed equivalent or stronger theorem was identified through the recorded claim-level searches. No assumption of uniqueness follows from an unsuccessful index search. Residual priority risk: unindexed finite Bernoulli matching papers or unpublished formulas with an implicit saturation convention.

## Mathematical value — PASS

The exact first market size, continuous unique threshold for every baseline \(0<p<1\), and paradoxical edge-density reversal distinguish a genuine structural property of fixed-capacity matching from a routine coefficient table. In the saturated rule, concentrating both flexible vertices creates more potential high-probability edges, yet spreading them can create more matchable coverage. The theorem supplies a controlled baseline for choosing where to concentrate flexibility when a flexible–flexible interaction has no double benefit, and carefully distinguishes that design problem from additive-probability models.

## Scope and residual limitations

The theorem is confined to offline expected maximum-cardinality matching with independent Bernoulli edges, two predetermined flexible vertices and balanced \(2\times2\) or \(3\times3\) markets. No large-market, online, endogenous-flexibility, or general social-welfare inference is claimed. Primary-paper comparison remains qualified for undiscovered equivalent results.

Self-review: passed. Independent audit: not yet performed.
