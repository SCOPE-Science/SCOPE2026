# Scientific review: multi-collector first-desynchronization theorem

## Correctness

**PASS.** The exact event is the first round in which the *counts* of distinct coupon types differ, not the first different coupon identities or the time of eventual collection completion. Conditional elimination of all-idle steps at a synchronized level gives the exact mixed-event joint mass. Expanding its finite product gives a uniform first-order local Rayleigh correction and Gaussian localization. Controlled Euler--Maclaurin summation gives the signed constant \(-1/(3q)\) in the mean for every fixed \(q\ge3\); the two-laggard probability follows by a distinct Gaussian weighted sum and has a positive \(d^{-1/2}\) leading term. All-error constants may depend on fixed \(q\), and the terminal all-tie atom is exponentially small. The exceptional \(q=2\) bridge representation follows by a binomial ratio and reflection. The submitted standard-library checker passed 3278 checks, including exact rational enumeration. This is supporting evidence, not a replacement for the infinite proof.

## Originality

**PASS (best-knowledge, subject to historical priority).** Long's May 2026 paper proves the \(q=2\) entrance law and Rayleigh limit, explicitly credited and not claimed as a new distribution. Krityakierne and Aek Thanatipanonda treat several collectors but their observable is the longest/shortest *completion time*, not first count desynchronization. Myers--Wilf work concerns two-player post-tie ballot outcomes. The result here allows at least two lagging collectors on the first unequal update and determines a new \(q\)-dependent order \(d^{-1/2}\) probability, plus a \(q\ge3\) mean correction that disappears at \(q=2\). Thus neither the higher-laggard event nor its constant is a two-player corollary. Targeted mathematical-record searches and the accessible prior research ledger returned no equivalent statement. Classical Gaussian summation and renewal methods provide ingredients but not identified prior coverage. An unindexed simultaneous-collector first-exit paper remains a nonzero risk; the search is not proof of novelty.

## Mathematical value

**PASS.** In a parallel multi-collector race, the first loss of equality of collection sizes is a natural stopping boundary: it determines where subsequent rank/ballot dynamics start. The theorem distinguishes two qualitatively different initial boundary geometries, showing that pairwise competition has zero constant mean bias, whereas each fixed \(q\ge3\) has negative bias \(-1/(3q)\) and a sharp rare multi-laggard probability. The exact joint finite distribution, local expansion, and entire family of constants allow accurate finite-size boundary initialization, beyond the leading Rayleigh scaling. This is more than a re-labeling of a known two-player probability and makes a specific structural prediction for the otherwise invisible multi-laggard channel.

## Closest literature and limits

The closest primary texts are Long (arXiv:2605.09641v1), Myers and Wilf (arXiv:math/0304229v1), and Krityakierne--Aek Thanatipanonda (arXiv:2211.04374). No claim is made for growing \(q\), nonuniform coupons, timing in raw rounds, or post-break winner probabilities. The result has no independent audit.

Self-review: passed. Independent audit: not yet performed.
