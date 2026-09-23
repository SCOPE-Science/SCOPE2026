# Independent three-axis audit — 2026-09-22

Review date (UTC): 2026-09-23. Reviewer: separate AI audit. Source tree: `5fcbf5488eba8670989586b38357acdf371237b5`, verified unchanged on current `main`.

## Correctness

I rebuilt the order-8 `Theta=(sigma,sigma,sigma)` search independently from the stated parametrization, with `sigma` the 7-cycle fixing the eighth point. The Latin row/column constraints give exactly 931 invariant labelled squares. I then independently classified those 931 squares under row/column/symbol isotopy with an explicit backtracking bijection test. The computation gives exactly 8 isotopy classes, with class sizes `49,294,294,98,49,49,49,49`; the intercalate buckets are `28:147, 21:588, 112:98, 7:98`. These reproduce the record's central numbers and independently verify the non-isotopy separation rather than merely replaying stored class labels. The fixed-point/orbit parametrization and centralizer order `7^3=343` are also correct.

## Originality

I searched the autotopism literature under equivalent terminology (autotopism, autoparatopism, cycle structure `(7,1)`, order-7 diagonal action, order-8 Latin squares). Falcón and related work classify possible cycle structures and earlier Gröbner-basis work counts squares related to autotopisms only through order 7; the Stones–Vojtěchovský–Wanless line determines existence/cycle-structure information, and public specified-autoparatopism data provide examples. I found no source reporting the order-8 diagonal `(7,1)^3` labelled count 931 together with the isotopy-class census 8. The record appropriately distinguishes existence results from the new per-symmetry census.

## Scientific value

The result converts a yes/no symmetry classification into a complete, replayable finite census with explicit representatives, class sizes, stabilizer orders, and non-isotopy witnesses. This is a useful refinement of published autotopism structure results and provides reusable benchmark data for Latin-square symmetry classification.

## Disposition

**PASSED unchanged.** All three axes pass.
