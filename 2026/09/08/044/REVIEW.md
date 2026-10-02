# Review status

Independent audit date: 2026-09-30 UTC.

Disposition: **passed**.

Correctness: PASS. A fresh enumeration using an independent connected-graph atlas gives exactly 6, 21, and 112 isomorphism types on 4, 5, and 6 vertices. Recomputing clique vectors and the Steinberg denominator for every graph gives finite/subexponential/exponential counts 1/2/3, 1/2/18, and 1/3/108. Independent root calculations reproduce the golden ratio as the minimum exponential rate in every stratum with witness multiplicities 1, 2, and 3; every other exponential row has rate at least 2. The displayed factorizations explain the equality cases exactly.

Originality: PASS. Terragni proves general monotonicity and a universal Coxeter growth lower bound, not the per-graph right-angled census. Later work on RACG growth polynomials studies broad algebraic families rather than this 139-row exact small-graph classification. Resultary shows a later 2026-09-09 record extending a complete RACG table through seven vertices; because it postdates this 2026-09-08 record, it is downstream coverage rather than prior coverage and does not retroactively defeat originality.

Scientific value: PASS. The complete 139-type exact table is a natural finite classification of the smallest connected defining graphs, and the exact golden-ratio minimizers plus a gap to 2 give a clean structural benchmark. The table is reusable for testing growth-series software and for checking conjectures about small RACG growth behavior.

Evidence: `INDEPENDENT_AUDIT_2026-09-30.md` and `INDEPENDENT_AUDIT_2026-09-30.json`.
