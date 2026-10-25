# Scientific review: Sharp four-step loss of occupation-time universality in a sign-persistent walk

## Correctness — PASS
Exact conditioning on eight sign patterns gives the φ(q,v) law. Independent pair-difference symmetry proves probabilities 3/8, 1/8 and the relation t=3/8-v; cancellations eliminate auxiliary u. Reflection and normalization give all five masses. Exact endpoint cases q=0,1/2,1 and iid uniform/exponential magnitude laws are evaluated. A three-event disjointness argument and a log-uniform interpolation establish the sharp v range. The packaged stdlib checker passes 686 rational algebraic assertions; no finite check replaces the proof.

## Originality — PASS
The inspected full-text model paper proves universal survival and maximum-time laws but only reports numerical occupation-time nonuniversality in Section 6. Its assertion that the exponential law matches maximum-time statistics does not imply the one-scalar formula, sharp first horizon, or sharp range. A 2019 continuous-time run-and-tumble occupation law uses different sampling and dynamics. A 2021 permutation-generated walk concerns different increment dependence. published-finding corpus hits about four-step higher-order dependence affect Sparre-Andersen survival for non-iid signs, not this Markov-sign occupation-count classification. Priority remains uncertain for unindexed supplementary calculations.

## Value — PASS
The principal source explicitly identifies the nonuniversality of occupation time as a numerical observation and leaves its analysis open. A complete exact first-failure horizon, one-parameter law, complete exceptional-persistence classification and sharp attainable probability range answer a natural finite-step portion, rather than merely presenting a numerical counterexample.

## Sources and limitations
Source model: Lacroix-A-Chez-Toine and Mori, arXiv:2007.10969 (2020). Closest related discussions: Singh and Kundu, arXiv:1906.09442 (2019); Fang et al., DOI:10.1017/jpr.2021.14 (2021). The claim treats only 1–4 discrete observations, fair initial sign, and iid positive non-atomic magnitudes; it does not prove any infinite-horizon occupation law. Priority uncertainty remains for unindexed finite-horizon calculations. The package contains a reproducible exact-rational checker; computational checks are subordinate to the analytic proof.

Self-review: passed. Independent audit: not yet performed.
