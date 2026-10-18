# Scientific review

## Correctness: PASS

The recurrence \(E(wc)=E(w)\cup E(w)c\) is exact, and the binary-tree encoding is injective. For each input word, the checker maintains the complete subsequence set, classifies Lyndon words by strict cyclic-rotation comparison, and counts new distinct Lyndon words once. Both next-letter branches are explored at every depth; the enumeration reaches all \(2^{20}\) length-twenty words. Expected maximum and optimizer counts are asserted for every length. A second implementation using greedy subsequence matching independently rechecks the entire domain through length fifteen and every claimed length-sixteen-to-twenty winner.

## Originality: PASS, with residual priority uncertainty

The original 2021 paper explicitly records the maximum-distinct-subsequence extremal quantity as open while determining its multiplicity-weighted and average analogues. The 2023 longest-Lyndon-subsequence paper addresses length optimization, and the standard OEIS sequence concerns contiguous factors. No implication yields this exact \(1\)-through-\(20\) table or optimizer classification. Searches did not locate an equivalent public result, but absence from searchable literature cannot establish universal priority.

## Mathematical value: PASS

The computed quantity is not a newly invented invariant: it is the precise maximum-distinct question expressly posed in the primary source. The classification settles twenty consecutive finite instances, including a million-word extremal case, and provides all witnesses and reproducible baseline data for a possible general theorem. It also concretely distinguishes the extremizers from those for the published total-with-multiplicity problem.

## Scope and residual risks

No assertion is made for length greater than twenty or for nonbinary alphabets. Exhaustive correctness is conditional only on the elementary verified program invariant and the ordinary execution of the provided standalone C++ source; independent external audit has not occurred. An unindexed equivalent computation is possible.

Self-review: passed. Independent audit: not yet performed.
