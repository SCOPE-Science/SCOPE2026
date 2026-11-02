# Scientific review

## Correctness — PASS

The fixed-weight-one pool is bijective with weak compositions of the pool size into \(n\) marker positions. Literal reads yield precisely the adjacent sums \(y_j=x_j+x_{j+1}\), with the all-zero-read multiplicity determined by total pool size. The alternating kernel is exhaustive. Its sum vanishes exactly at even strand lengths, yielding the parity distinction. Canonical representatives of even-length fibers have minimum odd coordinate zero, and a shifted stars-and-bars count gives every exact fiber multiplicity. The constructive maximum and threshold are sharp, including the boundaries \(k=0\) and \(n=2\). The standalone literal-read enumeration checks all 63 prescribed finite cases, but only the proof establishes the infinite statements.

## Originality — PASS (qualified)

The nearest direct model is Yehezkeally–Marcovich–Yaakobi's 2021 multi-strand substring-profile work (arXiv:2108.11725), whose accessible definitions, bounds and constructions were examined. It does not state a one-marker, longest-proper-read exact fiber spectrum or finite-parameter optimal codebook count. The 2022 generalized study (arXiv:2210.04471) likewise treats rate and repeat-free families. The 2023 random-source threshold paper (arXiv:2305.05820) uses a Bernoulli sequence ensemble and logarithmic read lengths. The 2024 constant-weight multi-strand result (arXiv:2411.03776) studies compositions of prefixes and suffixes of all lengths and uniqueness modulo reversal, a different channel. A further single-string multispectrum paper (arXiv:1804.04548) and pooled prefix/suffix composition paper (arXiv:2110.02352) do not imply these counts as stated. Search comparisons of statement, alias, stronger coverage and table quantities found no controlling exact theorem. Residual risk: an equivalent path-incidence fiber enumeration may be hidden in earlier mathematical literature; novelty is not established by search absence alone.

## Mathematical value — PASS

The longest proper read is the maximal informative but nontrivial read length, and the one-marker restriction is a natural sparse-source benchmark for joint decoding. Unlike an isolated small calculation, the result gives a sharp complete parity transition, all fiber-size multiplicities, a maximal inverse-list bound and the exact maximum zero-error code size for every positive strand length and pool size. It quantifies how information is lost through pooling despite nearly full-length observations; for even length the number of distinguishable pools is asymptotically one polynomial degree below the number of possible pools. These are natural finite-parameter invariants of the specified observation channel, not arbitrarily selected data points.

## Scope and limitations

Noiseless oriented string reads with multiplicities; strand weight one; no claims about shorter reads, errors, different alphabets, or unlabeled read orientation. Prior-work matching is qualified by the possibility of an unindexed equivalent graph-incidence statement. The verification program is exhaustive only in its finite parameter range, and mathematical proof is required for all lengths.

Self-review: passed. Independent audit: not yet performed.
