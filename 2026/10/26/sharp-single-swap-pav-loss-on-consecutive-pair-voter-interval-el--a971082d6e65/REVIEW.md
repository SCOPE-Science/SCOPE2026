# Scientific review

## Correctness

PASS. The exact score identity \(\operatorname{PAV}(W)=2k-a(W)/2\) follows from two approval incidences per candidate and the harmonic discount of \(1/2\) at exactly the doubly represented voters. Nonimproving swaps force the forbidden adjacency patterns proved in RESULT.md. Counting surplus zeros against singleton one-runs then proves the sharp upper bound \(a(W)\le\lfloor k/3\rfloor\). The explicit binary-word family attains it and is locally optimal by a neighbor-by-neighbor run-count argument. The integer checker exhausts all committees for \(k\le10\); its finite scope is not used as proof for all \(k\).

## Originality

PASS on the inspected literature and research-record comparisons, with historical-priority reservations. The main 2026 voter-interval results concern global exact optimization; the 2026 local PAV efficiency result gives a general tight \(2/3\) bound from a non-path approval construction, not an exact restricted \(11/12\) bound. The 2024 local-search paper concerns trajectory length, and the 2026 Pareto-committee reconfiguration result addresses a different objective. Searches for binary-word and path-graph equivalences did not reveal a dominating result. An earlier result phrased as fixed-cardinality path energy or local graph-edge penalty remains possible.

## Value

PASS. The bound gives the **exact finite-size quality** of swap-local PAV on a canonical, polynomial-time-solvable VI domain; the sharp \(11/12\) quality ceiling and linear additive gap show that exact tractability does not make simple improving swaps globally sufficient. The theorem is structural and quantified for every committee size rather than a single negative example.

## Limitations

No guarantee is claimed for general VI elections, other scoring sequences, or weighted approval profiles. No independent historical-priority certification has been carried out.

Self-review: passed. Independent audit: not yet performed.
