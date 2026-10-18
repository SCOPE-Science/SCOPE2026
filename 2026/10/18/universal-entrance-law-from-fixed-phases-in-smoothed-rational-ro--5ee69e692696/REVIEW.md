# Review of the fixed-phase entrance law

## Correctness — PASS

A fixed interior interval \(K=[d,1/n-d]\) stays uniformly away from the discontinuity under the finite rotation itinerary. Its only two order-\(e^{-ad}\) errors are the positive and negative nearest-site corrections, with product \(e^{-a/n}\). The proof bounds all other visits and propagated corrections by \(O(ae^{-a/n})\), uniformly on \(K\), rather than relying on a shrinking neighborhood. The period-return is strictly increasing with derivative below one, has a unique fixed phase \(h+o(1/a)\), and maps the segment between this point and any fixed interior initial condition into itself. For the sign-adjusted exponential coordinate \(y_m\), the recurrence is \((y_{m+1}-y_m)/(a e^{-a/(2n)})=1-y_m^2+o(1)\) uniformly along every orbit time. Discrete Gronwall gives the complete \(\tanh\) limit, and strict threshold crossing gives the inverse hyperbolic tangent first-passage time. Numerical checks are diagnostic only. No claim is made outside the specified fixed-parameter regime.

## Originality — PASS under examined sources

The motivating paper [1] establishes rational-period attraction but not a sharp clock for an arbitrary fixed starting phase. The closest published quantitative result [2] obtains the half-grid correction and the local Floquet contraction gap, which motivate the clock but quantify the return displacement only in an exponentially shrinking neighborhood. Those statements do not imply a global-inside-the-bin displacement estimate, universal nonlinear entrance waveform, or first-passage law for initial phases separated from the half-grid by a fixed positive distance. The 2018 and 2024 game-map studies [3,4] address different dynamical outcomes; no equivalent full entrance profile was found in the actual searches. Mathematical priority remains uncertain because searches cannot prove absence, and the publicly available 2022 manuscript precursor was read, while version-specific differences in the final 2024 journal article remain a bibliographic risk.

## Value — PASS

A stable orbit's small multiplier gap does not quantify its capture time from macroscopic phases: the entire entrance trajectory may be nonlinear over most of its duration. The theorem solves that natural missing question at a physically specified tolerance \(\theta\), proving an unexpectedly universal \(\log\coth\)-shaped entrance profile, loss of the magnitude of initial-phase memory, and a sharp \(e^{a/(2n)}/a\) delay. This is distinct from a restatement of a local linearized contraction or from a routine fixed-point correction.

## Primary scientific context and limitations

[1] Bielawski et al., *Interval maps mimicking circle rotations*, arXiv:2411.01495v1, full HTML Sections 2–5.

[2] *Singular half-grid selection and exponentially weak attraction in rational EOS maps*, publicly available published-finding corpus mathematical research record (2026), proof section inspected.

[3] Chotibut et al., *Family of chaotic maps from game theory*, arXiv:1807.06831v1.

[4] Bielawski et al., *Unpredictable dynamics in congestion games: memory loss can prevent chaos*, arXiv:2201.10992 (2022), complete accessible manuscript inspected; journal successor *Memory loss can prevent chaos in games dynamics*, *Chaos* 34, 013146 (2024), DOI:10.1063/5.0184318.

Residual risk: An equivalent fixed-phase entrance asymptotic in unindexed smoothing or game-theory literature cannot be ruled out. The theorem does not address denominator-uniformity, basin-entry from another phase bin, or phases approaching boundaries with steepness.

Self-review: passed. Independent audit: not yet performed.
