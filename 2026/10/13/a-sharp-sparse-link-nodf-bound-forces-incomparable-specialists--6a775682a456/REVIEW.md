# Self-review

## Correctness — PASS
The fixed link count and absence of zero columns force total column-degree excess two; hence every candidate has either one degree-three column or exactly two degree-two columns. In the first type the column contribution is \(n-1\), and the row contribution is at most \(5/2\), strictly below the proposed maximum for \(n\ge4\). For distinct degree-two columns meeting in one row, the column contribution is at most \(2(n-2)\) and the row contribution at most two, with equality forcing all singleton columns onto the common row. If the degree-two columns share two rows, the third nonisolated row forces a strict gap. The equality structure, Ferrers comparison, and labeled count are explicit. Two independent exact scorers agree on every one of 63,906 exhaustive small matrices; this is not substituted for the universal proof.

Residual C risk: the theorem applies to classical unequal-degree-pair NODF with both guilds counted and positive degrees; changing the metric or constraint changes the problem.

## Originality — PASS
The original NODF paper defines the metric, the detailed analytical study characterizes its zero and one values, and later fixed-size/fixed-link ecological optimizations use heuristics without a guarantee of exact global maxima. Targeted literature and mathematical database searches for exact three-guild sparse bounds, Ferrers comparison, tree extremizers, and explicit fixed-connectance equalities produced no covering result. The nearest already-known size-only extremum does not constrain link count and has Ferrers maximizers, whereas the new optimum at the prescribed sparse link count is necessarily non-Ferrers. Thus the new statement is not implied by that earlier theorem.

Residual O risk: an obscure table of tiny matrices or code test may reproduce an instance of the optimizer; no independently validated uniqueness claim is asserted.

## Value — PASS
Normalization by the maximum NODF attainable at the same network dimensions and link count is an established ecological practice, but current algorithms do not certify that maximum in general. This is an exact, closed-form benchmark for the sparsest connected-link regime at a fixed three-species guild. More importantly, it shows that the configuration maximizing a widely used nestedness score necessarily contains incomparable specialist neighborhoods, rather than the Ferrers arrangement normally associated with strict nestedness. The positive gap \((n-3)/K\) quantifies this diagnostic discrepancy and holds for all \(n\ge4\).

Self-review: passed. Independent audit: not yet performed.
