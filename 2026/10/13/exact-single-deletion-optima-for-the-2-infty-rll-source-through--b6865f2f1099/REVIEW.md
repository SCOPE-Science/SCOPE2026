# Review

## Correctness
PASS. The object and endpoint convention are stated explicitly. The finite verifier reconstructs every source set for \(2\le n\le11\), compares direct one-deletion-shadow disjointness with a separate longest-common-subsequence dynamic program on every pair, exhaustively enumerates all candidate subsets through the first impossible size, and rechecks the three length-eleven maxima. The decisive upper bound at \(n=11\) is exhaustive: all \(11628\) five-subsets fail. The published Theorem V.2 value \(823/105\) is independently re-evaluated from its formula.

## Originality
PASS. The closest primary source is Kulkarni--Kiyavash arXiv:1211.3128, whose Section V-A defines this constrained source and gives a general upper bound; it does not state the exact \((n,d)=(11,2)\) optimum or equality cases and explicitly leaves exact simplification of its RLL bounds outside its scope. The directly inspected Palunčić et al. article gives an asymptotic construction/decoder rather than a fixed-length extremal census. The Cheng--Ferreira--Broere and Bours works are construction-oriented and do not supply an implication-equivalent finite result in the inspected material. Targeted exact-parameter and alias searches found no published equality classification. Residual risk remains for an obscure or unindexed finite enumeration.

## Value
PASS. The case \(d=2\) is the first nontrivial regime of the cited RLL theorem, and \(n=11\) is the first length at which the exact optimum reaches four. The published bound there is only \(823/105\), hence the integer bound seven, so the exact value four closes a real finite gap rather than merely recomputing a known table. The three equality cases and their reversal structure provide a compact benchmark for constrained deletion-code algorithms.

Self-review: passed. Independent audit: not yet performed.
