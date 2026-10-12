# Self-review

## Correctness
**PASS.** The standard inequality \(h\le g\) is reconstructed directly from the definitions. If the common total is below nine, then \(g\le2\), leaving no possible opposite strict order among admissible \((h,g)\) pairs. At total nine, three papers force \(g=3\), so four papers are necessary; the two index classes at four papers are solved completely and give exactly fifteen reversals. The positive-citation variant is likewise solved exactly at totals nine and ten. The packaged verifier returns `VERIFY_OK` and independently replays the finite boundary calculations.

Risk: a modified \(g\)-index that extends beyond the number of published papers is a different object and is outside the claim.

## Originality
**PASS.** Hirsch and Egghe own the two indices; empirical work already establishes that their researcher rankings can differ, and recent mathematical work proves ordering relations such as \(h\le g\) in a formal citation-vector setting. The accepted claim is narrower: both the number of papers and total citations are held fixed, and the exact smallest citation budget, smallest paper count, complete first strict-reversal layer, and positive-citation variant are determined. Exact-vector and equal-resource searches did not locate those statements.

Risk: a recent mathematical paper contains small illustrative citation vectors whose table entries were not fully exposed in the text extraction, and an unindexed exercise or software test could contain an isolated witness. No checked source stated the minimality or full first-layer classification.

## Value
**PASS.** The \(h\)- and \(g\)-indices are established research-evaluation measures that weight citation concentration differently. Fixing publication count and total citations removes two obvious scale effects and asks when distribution alone can overturn a ranking. The exact nine-citation threshold gives a smallest interpretable benchmark, while the ten-citation positive variant handles the common convention of listing only cited papers.

Self-review: passed. Independent audit: not yet performed.
