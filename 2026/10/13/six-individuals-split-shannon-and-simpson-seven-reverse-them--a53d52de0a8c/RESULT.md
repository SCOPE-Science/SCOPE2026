# Six individuals split Shannon and Simpson; seven reverse them

## Finding

For each integer census size \(N\ge2\), consider all unordered profiles of positive integer species abundances \(n_1,\ldots,n_s\) with \(\sum_i n_i=N\). Write \(p_i=n_i/N\) and use Shannon diversity \(H=-\sum_i p_i\ln p_i\) and finite-sample Simpson diversity
\[
D=1-\frac{\sum_i n_i(n_i-1)}{N(N-1)}.
\]
For \(2\le N\le5\) their weak orderings are identical. The first disagreements occur at \(N=6\): Simpson ties exactly two pairs that Shannon separates, namely \((4,1,1)\) versus \((3,3)\), and \((3,1,1,1)\) versus \((2,2,2)\). Shannon ranks the first profile higher in each. There are no opposite strict rankings through \(N=6\).

At \(N=7\), the first strict reversals occur, and the complete strict-reversal list is \((5,1,1)\) versus \((4,3)\), and \((4,1,1,1)\) versus \((3,2,2)\). Shannon again ranks the first profile higher in each, but Simpson ranks it lower.

## Assumptions and scope

Only equal-census comparisons are made. Richness may vary between profiles, and zero-abundance species are omitted. The stated Simpson diversity is undefined at \(N=1\), where there is only one profile and no comparison between different profiles; the theorem does not assign a value there. For \(N\ge2\) the population Gini–Simpson index \(1-\sum_i p_i^2\) differs from \(D\) by the positive scale factor \((N-1)/N\), so gives exactly the same within-census rankings. Changing the Shannon logarithm base to any other base greater than one also preserves the rankings.

## Proof

For a partition \(a\) of \(N\), put \(P(a)=\prod_{n\in a}n^n\) and \(C(a)=\sum_{n\in a}n(n-1)\), counting repeated parts with multiplicity. At fixed \(N\), both diversities are decreasing transforms of the corresponding integer keys: \(H(a)=\ln N-N^{-1}\ln P(a)\), and \(D(a)=1-C(a)/[N(N-1)]\). Thus mismatches are precisely the unordered pairs whose key-comparison signs differ, and strict reversals are the pairs whose signs are nonzero and opposite.

To enumerate, generate partitions as nonincreasing sequences by choosing their first part in \(\{1,\ldots,N\}\), then recursively choosing the next part no larger than the previous one or the remaining total, stopping exactly at remainder zero. Compute the two integer keys and compare each unordered pair once. The exhaustive counts are:

| \(N\) | partitions | order mismatches | strict reversals |
|---:|---:|---:|---:|
| 2 | 2 | 0 | 0 |
| 3 | 3 | 0 | 0 |
| 4 | 5 | 0 | 0 |
| 5 | 7 | 0 | 0 |
| 6 | 11 | 2 | 0 |
| 7 | 15 | 4 | 2 |

At \(N=6\) the two listed pairs have \((P,C)\) equal to \((256,12),(729,12)\) and \((27,6),(64,6)\), respectively. At \(N=7\) the two listed strict pairs have \((P,C)\) equal to \((3125,20),(6912,18)\) and \((256,12),(432,10)\), respectively. For those two strict pairs the Simpson scores are \(11/21<4/7\) and \(5/7<16/21\), respectively. These witnesses exhaust the corresponding counts.

## Verification

Run `python3 verify_shannon_simpson_minimal_reversal.py` using standard Python 3. It independently generates partitions both by recursion and by sorting and deduplicating all compositions. It verifies the full comparison counts with exact integers and the witness Simpson scores with exact rationals. The first line is `VERIFY_OK`. The proof's exact keys verify the signs of the two six-individual witnesses; the program counts all six-individual mismatches and verifies the complete seven-individual strict layer.

## Relationship to prior work

Simpson [1] introduced the concentration-based index. Tóthmérész [2] discusses noncomparability under diversity profiles and gives a size-100 example of opposite Shannon and Simpson rankings. The question here is not whether such reversals can occur in general, but their minimum equal integer census size and the full lists at the first disagreement and first reversal.

## Limitations

The result classifies exact abundance profiles, not sampling uncertainty, detectability, spatial structure or taxonomic relatedness. The threshold is not a sample-size recommendation. Earlier examples or small tables outside the sources inspected may exist.

## References

1. E. H. Simpson, “Measurement of Diversity,” *Nature* 163, 688 (1949), DOI: 10.1038/163688a0.
2. B. Tóthmérész, “Comparison of different methods for diversity ordering,” *Journal of Vegetation Science* 6(2), 283–290 (1995), DOI: 10.2307/3236223.
