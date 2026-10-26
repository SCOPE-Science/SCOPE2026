# Mathematical review

## Correctness — PASS

The renewal equation for the number of steps after the latest reset yields the exact transform \(F(s+\lambda(1-z))/(sF(s))\). A genuine iid-wait CTRW must instead have a geometric Montroll–Weiss factor; their equality forces \(1/F\) to be affine on overlapping intervals and hence \(F(s)=1/(s+r)\). The unique inverse waiting law has finite density \(\lambda e^{-(\lambda+r)t}\) and mass \(r/(\lambda+r)\) at infinity. An independent matrix-generator implementation checks the one-time and two-time identities. The covariance and time-average proofs explicitly distinguish stopped and regenerative paths. The evidence is analytic, not an inference from finite tests.

## Originality — PASS (best-knowledge)

Colantoni–Pagnini's general reset-count representation and index-dependent coefficients, Godrèche–Luck's cumulative dressed event count, Bodrova–Sokolov's power-law displacement laws, and Stojkoski et al.'s two-time correlation calculations are all acknowledged and compared at the statement level. The new conjunction is an if-and-only-if criterion for *ordinary iid-renewal spatial-marginal surrogates*, uniqueness of its necessarily defective law, and a sharp trajectory distinction. Relevant public research records and accessible antecedent claims were searched; this does not certify worldwide priority. A general renewal factorization or transform-rigidity theorem not examined could subsume the criterion.

## Value — PASS

The result answers when a widely used marginal CTRW representation may legitimately be promoted to a genuine iid-wait renewal model, and shows that doing so at positive Poisson-reset rate sacrifices long-time transport along individual trajectories. It is a structural limit and identifiability boundary, not a small numerical gain or a restatement of the reset renewal equation. The no-reset endpoint and the requirement that infinite waits be admitted are explicit.

## Scope and risk

Only symmetric nearest-neighbor jumps with a Poisson underlying clock, ordinary nondelayed wait-first renewal surrogates, and all-time spatial-marginal equality are classified. The general result for non-Poisson underlying clocks remains open here. The earlier two-time resetting-covariance mechanism is not independently novel; it provides an explicit consequence. Literature-wide priority is unverified.

Self-review: passed. Independent audit: not yet performed.
