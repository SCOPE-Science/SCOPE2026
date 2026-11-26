# Independent mathematical audit

## correctness

PASS

Ranking independent chord endpoints generates each perfect matching with the same multiplicity. The crossing counts within disjoint groups are independent and their sum is pointwise bounded by the full count. On isolation the two arcs have independent uniform submatchings. Their crossing-count sum is bounded by the (n−1)-chord law, itself strictly smaller in increasing-test expectation because the extra chord crosses a specified existing chord with probability 1/3. Summing positive isolation-event weights gives the result, including n=2 and empty arcs. This is size bias, not conditioning on I_n>0. The replacement checker ran successfully for every designated pair and every relevant threshold at n=2..6 (python /workspace/repairs/2/verify.py); it is finite corroboration. The uploaded checker was inspected, not executed.

## originality

PASS

For the corrected claim the substantive step is stochastic domination at every split, not the arc formula, crossing pmf, mixed moment, or simple-chord case. No inspected antecedent gives this stochastic comparison for all isolated chords.

## value

PASS

The stochastic order controls all crossing thresholds at once and identifies a uniform upper bound even at each nontrivial arc split. Neither a negative covariance nor a simple-chord Palm identity answers this dependence question for the full isolate count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
