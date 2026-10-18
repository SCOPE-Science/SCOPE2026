# Scientific review: exact dyadic Rudin–Shapiro attractor profile

## Correctness — PASS

The verified theorem is exactly \(\gamma(R_{128}),\gamma(R_{256}),\gamma(R_{512}),\gamma(R_{1024})=(10,11,12,12)\), with the binary sequence, indexing, and attractor notion defined in `RESULT.md`. The full factor-coverage hypergraphs are recomputed from every distinct substring of the four words; their inclusion-minimal constraints have sizes \(48,64,80,96\). The displayed position sets hit each constraint. Integral incidence-dual subfamilies of sizes \(9,10,22,24\), with respective weights \(1,1,1/2,1/2\), give certified lower bounds \(9,10,11,12\). For the first three lengths an exhaustive *exact-cover equality argument* eliminates every possible matching-size hitting set, using respectively \(30,2566,1316\) distinct search states, thereby raising each integer bound by one. No step relies on a floating-point solver conclusion, and the result claims only these finite lengths.

Residual correctness risk is implementation error in a finite checker, mitigated by two independent ways to generate the binary word, regeneration and equality-checking of the entire minimal-coverage antichain, exact integer arithmetic and explicit source code. No external independent audit has occurred.

## Originality — PASS, subject to stated access risk

The closest identified record, `2026/9/8/SCOPE079`, reports exact dyadic Rudin–Shapiro minima through length \(64\) and only upper bounds \(12,13,15,16\) for the four lengths settled here. Therefore its *accessible stated claims* do not imply the new exact profile. Schaeffer and Shallit (arXiv:2012.06840) establish automatic-sequence algorithms and bounds but no Rudin–Shapiro numerical profile; Banbara et al. (arXiv:2602.16152) treat Fibonacci and period-doubling words; Faro et al. (arXiv:2610.10950) treat Thue–Morse rather than Rudin–Shapiro. The complete latest Thue–Morse manuscript and directly relevant older papers' accessible sections were inspected, and published-finding corpus searches were run using the sequence, dyadic parameters, and equivalent factor-covering formulation.

The complete underlying `SCOPE079` artifact was inaccessible: its summary was read but not treated as whole-document proof of absence. Unindexed tables, earlier enumerations, or inaccessible supplementary data remain genuine originality risks. No independent novelty certification is asserted.

## Value — PASS

The four tested lengths are not arbitrarily selected: they are precisely the next four dyadic Rudin–Shapiro prefixes after the previously published exact run through length \(64\). These lengths already have identified benchmark upper bounds. Resolving all four rather than extending a single arbitrary finite sample produces a useful sequence-family calibration of the exact attractor number, improves the stated bounds by \(2,2,3,4\), and detects the first observed plateau at the final two lengths in this range. Explicit witnesses and concise exact integer exclusion certificates permit independent reuse without proprietary solvers. The result is a finite benchmark, not an unsupported asymptotic theorem.

## Limitations and closest literature

Only the four stated dyadic prefixes are classified; optimal-attractor multiplicities, other lengths, and the asymptotic growth of Rudin–Shapiro attractors remain undetermined here. Related full papers were inspected where accessible. The closest prior benchmark was available only as a published searchable summary, so originality must be assessed with that specific access limitation in mind. Proof and verification are self-contained; external independent audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
