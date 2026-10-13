# Self-review

## Correctness
**PASS.** At fixed equal arm size \(m\), ARR is exactly \(d/m\) with \(d=c-t\), while RRR is \(d/c\). Thus the exact reversal criterion is immediate. Exhaustive enumeration of all positive-cell beneficial tables proves zero strict reversals through \(m=5\) and exactly two at \(m=6\). The displayed witness and persistent family are verified both algebraically and by the packaged exact-rational script, which returns `VERIFY_OK`.

Risk: the sharp cutoff changes if zero cells or unequal arm sizes are allowed.

## Originality
**PASS.** Cook and Sackett already give the formulas and show that equal RRR can correspond to very different ARR/NNT because baseline risks differ. Schechtman more broadly shows that absolute and relative effect measures can give different impressions, including ties under one measure split by another. Those results own the qualitative phenomenon. The accepted claim is narrower: the exact positive-cell equal-arm lattice boundary, the complete first reversal layer, and an all-larger-size integer family. Targeted published-result and web searches did not locate that theorem.

Risk: the result is elementary enough that an unindexed teaching problem or software test could contain the same small witness. Search failure is not proof of bibliographic uniqueness.

## Value
**PASS.** ARR/NNT and RRR are standard competing summaries of binary treatment benefit, and the literature emphasizes that they answer different clinical questions because RRR standardizes by baseline risk. The theorem isolates the smallest nondegenerate equal-arm trial in which that distinction changes the strict ordering of two treatments, rather than merely changing magnitudes or breaking a tie. The persistent family shows the disagreement is structural.

Self-review: passed. Independent audit: not yet performed.
