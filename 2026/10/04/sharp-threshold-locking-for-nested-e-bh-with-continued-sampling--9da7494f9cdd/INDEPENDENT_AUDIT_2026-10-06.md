# Independent mathematical audit

## correctness

PASS

If \(r\) old coordinates stay at least \(K/(\alpha r)\), the next \(r\)-th order statistic qualifies, so the new rejection count is at least \(r\) and its cutoff is no larger; every old rejection therefore persists. For sharpness, starting with exactly \(r\) coordinates at the old cutoff and outsiders zero, lowering one coordinate to any smaller value makes rank \(r\) fail, every lower rank fail because its threshold is strictly larger, and every higher rank fail at zero. The affine rule is predictable, stays above the lock pathwise, and has conditional expectation at most the current e-value. A fresh bounded replay independently checked persistence and the one-coordinate collapse for every \(2\le K\le8\) and all ranks.

## originality

PASS

Wang–Ramdas define base e-BH and its cutoff \(K/(\alpha k)\). Lin–Ma–Ren–Wei's current adaptive-data paper advertises nested e-BH rejection sets under conditionally valid e-increments and an e-PS sampling rule, but the accessible primary material does not state the coordinatewise persistence floor, the one-coordinate sharpness counterexample, or the affine lock-and-bet maximal-active-capital rule. Resultary search found no equivalent theorem. Full text of the very recent Lin et al. preprint was not materially available in this run, so that same-source overlap remains a named residual risk rather than negative novelty evidence.

## value

PASS

Nested discoveries are operationally important in continuing experiments. The theorem identifies exactly how much evidence may remain actively at risk after rejection while guaranteeing worst-case pathwise persistence, improving on the crude policy of freezing an entire rejected stream. The sharpness and capital interpretation make it a substantive design rule rather than a restatement of e-BH.

The dated certificate retains the supplied scientific assessment, sources and limitations.
