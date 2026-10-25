# Independent mathematical audit

## correctness

PASS

For U=(0..q-1)^m and V=(q-1..0)^m, greedy minimum block counts are 1+d+e and 1+a+e. Hence a word w is common iff d+e<=m-1 and a+e<=m-1; this implies length<=2m-1, attained by alternating extremal letters. Any equality neighbor can be split by another symbol without changing either budget. For unequal neighboring symbols, if both budgets are free, suitable two appended extreme letters spend one ascent and one descent. In the only-one-budget-free case (d=m-1>a), the nonexistence of an ascent-only insertion forces first minimum, last maximum, every ascent of unit height and every descent full maximum-to-minimum; telescoping implies a=(q-1)(d+1)>d, contradiction. Symmetry handles the other direction. Thus shorter common words can be extended; maximal iff longest length 2m-1 with a=d=m-1, e=0. The q-state weighted transfer matrix yields exact counts; constant-term extraction at q=3 gives C=binom(2m+2,m+1)-2binom(2m,m)+binom(2m-2,m-1). An independent exhaustive implementation reconstructed both subsequence sets and insertion-maximality for all q=2..4, m=1..3, with exact formula agreement for q=3; these finite checks only corroborate the all-q proof.

## originality

PASS

Best-of-knowledge comparison of the exact claim against named closely related published results, semantic Resultary search and inspected primary scientific material; unsuccessful retrieval is not treated as evidence of absence.

## value

PASS

All-size collapse of maximal to longest subsequences in a natural reversed-periodic family gives an exact constructive benchmark for maximal-subsequence enumeration; the ternary exponential-count closed form and transfer-matrix representation add nontrivial structure beyond a known integer sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
