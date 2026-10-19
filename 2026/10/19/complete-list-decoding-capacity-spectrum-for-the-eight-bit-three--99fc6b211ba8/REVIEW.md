# Scientific review

## Correctness — PASS
The complete finite theorem is established by an exact rational dual upper envelope and explicit binary codebooks attaining the integer part at every allowance from \(1\) through \(93\). The \(L=0\) and \(L\ge93\) endpoints follow from existence of deletion outputs and a complete incidence count. The standalone verifier reconstructs the incidence relation directly and checks all lower and upper certificates using exact fractions. No finite-to-infinite extrapolation is used: the only unbounded parameter is list size, with a proved saturation cutoff.

## Originality — PASS
Lin (arXiv:2609.26650v1) studies exactly the same list-deletion model, but the inspected eight-page paper proves asymptotic bounds and common-subsequence estimates rather than the explicit eight-bit complete list-size profile. Kiah--Wei--Zeng (arXiv:2609.21395v1) concerns fixed-list insertion/deletion rate bounds, while Yasunaga (2024) develops general error-correction bounds. The closest previously recorded finite instances address other block/deletion parameters. Searches across the named formulation and its equivalent hypergraph/incidence-packing and list-decoding formulations found no directly covering theorem. The Kiah--Wei--Zeng primary text was inspected, including its finite-length bound in Theorem 23; that general inequality does not give the complete exact eight-bit list-size profile. Unindexed tables remain a residual risk, not a certified absence.

## Value — PASS
The list allowance is an intrinsic coding parameter, so classifying all \(L\ge0\) at one nontrivial finite block length is a natural complete benchmark, rather than an arbitrary isolated slice. The six changing optimal affine dual bounds expose a concrete discrete packing phase diagram, including nonintegral rational upper bounds and saturation at \(L=93\). All \(93\) intermediate optima have inspectable witnesses, making the classification reusable for testing future finite-block bounds and code-search methods.

## Limitations and comparisons
The certificate applies only to eight-bit binary words and exactly three deletions. It does not imply a longer-block or asymptotic theorem, nor does it claim a complete classification of all optimal codebooks. Earlier unindexed exhaustive enumerations or finite tables could still overlap. The public certificate relies on no unprovided optimizer, external log, or hidden data.

Self-review: passed. Independent audit: not yet performed.
