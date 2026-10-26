# Self-review

## Correctness — PASS
The complete coefficient identity is derived from explicitly defined finite-state continuations for every integer \(r\ge1\), rather than extrapolated from samples. The arch-count equivalence, boundary cases, cancellation at \(u=1\), and strict rate comparison are independently reconstructed in the proof. The standard-library verification program checks both the defining subsequence condition and independent count recurrences for specified finite ranges.

## Originality — PASS, with residual risks
The closest works are Adamson et al., *k-Universality of Regular Languages* (arXiv:2311.10658v1), which provides counting procedures for arbitrary automata; Adamson, *Ranking and Unranking k-subsequence universal words* (arXiv:2304.04583v1), which treats unrestricted enumeration; Barker et al. (arXiv:2003.04629v1), which provides the arch framework; and a previously published unconstrained binary closed-form expression. None of the inspected relevant results gives the uniform zero-run-bound rational series or proves the rate reversal. The possibility of an equivalent expression elsewhere remains a literature risk.

## Mathematical value — PASS
The formula yields, simultaneously for every zero-run ceiling and length, the exact counting distribution of the index on a natural regular language. The nonmonotonic constraint effect gives a structural conclusion not supplied by the mere computability of regular-language counts. It provides exact benchmarks for constrained words in a subsequence-based coverage model, while not claiming a larger-alphabet classification.

## Limitations
The underlying alphabet is binary, only zero-runs are constrained, and the rate limit is for fixed run ceiling. Independent mathematical auditing and exhaustive scholarly verification are outstanding.

Self-review: passed. Independent audit: not yet performed.
