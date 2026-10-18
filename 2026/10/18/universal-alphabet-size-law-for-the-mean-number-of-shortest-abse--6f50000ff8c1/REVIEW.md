# Scientific review: exact mean shortest-absent-subsequence law for \(q\ge3\)

## Correctness — PASS

The proof fixes the ambient alphabet, including words with absent alphabet letters and the empty source. Greedy full-alphabet arch factorization establishes that an absent shortest target matches exactly one target symbol per complete arch and none in the terminal rest. Diagonal and off-diagonal transition series are derived by exhaustive combinatorial cases on the unique arch-terminal symbol; all unmarked-symbol requirements are enforced by inclusion–exclusion. Every complete word has a unique arch decomposition, and the all-ones eigenvector of the symmetric transition matrix yields the rational generating function. The ternary specialization follows by exact polynomial algebra. The simple positive dominant pole is proved using nonnegative, aperiodic arch-length support, not inferred from numerical coefficients.

Independent finite checks in `verify_qary_sas.py` directly reconstruct shortest absent subsequences for all source words through the stated bounds, enumerate transition arches, and verify the quintic recurrence through degree 35. The numerical growth constants are approximations to rigorously specified algebraic quantities.

## Originality — PASS, with residual risk

The closest primary reference, Kosche et al. (arXiv:2108.13968), develops structural and algorithmic tools for absent subsequences of *individual* words. Adamson et al. (arXiv:2407.18599) determine extremal counts conditioned on universality index, not the average over all fixed-length words. Manea et al. (arXiv:2504.21471) improve algorithms for enumerating absent subsequences of a supplied word, not all-word statistics. Accessible published research records and prior related results were compared for both direct statements and stronger implications. A previously known binary first-moment theorem is explicitly excluded from the new scope: here \(q\ge3\). There was no identified general formula implying the all-length ternary quintic or the stated full-alphabet generalization. An independently discovered equivalent enumeration in unindexed work remains possible.

## Mathematical value — PASS

The number of shortest absent subsequences is a natural size measure for a shortest missing-pattern set. Exact averages for full-length ensembles characterize typical enumeration output size, which is not determined by structural descriptions, an algorithm on one word, or extremal bounds alone. The first nonbinary instance gives a concrete five-term rational law and rigorous exponential mean-growth constant, while the general \(q\)-ary theorem covers all finite alphabets of size at least three, including the four-letter setting of sequence data. The additional distinct-terminal-letter transition creates a substantive case absent from the binary proof.

## Limits and closest coverage

The model is a fixed labeled alphabet with uniform host-word sampling; fixed-composition, nonuniform, dependent-source, and higher moment questions remain open here. The primary-source and published-record comparisons are not a proof of global bibliographic uniqueness. The checker supplies finite consistency only; the mathematical proof supplies the infinite result.

Self-review: passed. Independent audit: not yet performed.
