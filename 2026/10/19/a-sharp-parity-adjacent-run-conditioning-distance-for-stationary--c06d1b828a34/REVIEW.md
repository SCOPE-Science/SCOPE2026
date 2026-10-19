# Scientific review

## Correctness — PASS

The stationary binary-chain endpoint weights yield the exact finite affine likelihood ratio between joint occupancy and adjacent even/odd total-run events. Normalizing this ratio gives an exact total-variation identity in terms of the even-conditioned mean absolute deviation. The conditional even-run occupancy distribution is an explicitly tilted product of two binomial-composition counts; strict concavity and the explicit adjacent ratio prove a local Gaussian limit with uniform integrability, giving the claimed coefficient. All limits use the correct centered mean and allow arbitrary integer \(s_n\) with \(s_n/n\to\rho\) in the open interior. The two finite equality curves follow from factoring the affine slope. The accompanying executable reproduces 281 exact/numerical checks. The bounds are not asserted to be uniform at parameter boundaries.

## Originality — PASS, with substantial residual risk

A published 2016 conditional Markov-run formula explicitly covers the **finite** starting identity, so that identity is not asserted to be new. The assessed result is the sharp scaled total-variation comparison across parity-adjacent *total-run* conditioning, including explicit Gaussian coefficient and exact two-curve degeneracy. Inspected sources on Markov-binomial approximation and conditional runs do not state this sharp comparison. A 2004 paper on the joint laws of ones and success runs gives Gaussian approximations and could implicitly contain it; only its abstract was accessible. This is a documented unresolved priority risk, not an independent novelty certification. The scientific value and priority claims are confined accordingly.

## Mathematical value — PASS

The two conditional occupancy laws are natural alternatives in exact binary-runs tests, and a leading-order total-variation distance directly quantifies statistical discriminability lost when neighboring even and odd run counts are pooled. The theorem identifies an exact degeneracy phase diagram with two distinct mechanisms (symbol symmetry and lack of temporal dependence) and a sharp nonzero separation coefficient everywhere else. It gives a complete natural fixed-density parameter classification; the new asymptotic requires a conditional local-limit argument beyond the established finite tables.

## Closest literature and limitations

Corzo–Vergara (2016), equations (2.4)–(2.5), implies the finite likelihood ratio, and Savelyev–Balakin (2004) provides an earlier joint-distribution framework with unavailable full text. Xia–Zhang (2010) treats unconditioned Markov-binomial approximation. The present result does not treat transition probabilities or run densities tending to their boundaries. Full-source priority risk persists for the 2004 paper.

Self-review: passed. Independent audit: not yet performed.
