# Same-model scientific review

## Correctness — PASS
The proof derives the exact optimizing center from concavity of the square root of the reflected-overlap area, then identifies the optimizer as the intersection of \(2n\) regular unit disks. For each disk intersection, the globally active ray constraint is the farthest center; a quadratic equation supplies its radial function and its elementary area integral. The strict inequality follows from an explicit generating-vertex witness, while two even Taylor series establish the exact asymptotic coefficients. A standalone verifier independently imposes all disk constraints and reports `VERIFY_OK`; this finite check is only diagnostic.

## Originality — PASS, with residual historical risk
Harrell's 2000 paper concerns total area minimization at fixed width; Groemer–Wallen (2001) use a diameter-area split and Jin–Guo (2011) use Minkowski dilation. Known exact Kovner–Besicovitch values for **straight regular polygons** do not imply the present formula for **curved regular Reuleaux odd-gons**. An earlier outer Estermann formula for regular Reuleaux polygons optimizes symmetric **supersets**, not subsets; earlier isotropic second moments likewise do not imply reflected-overlap area. The Reuleaux triangle is already an acknowledged benchmark. Besicovitch (1951) remains an incompletely accessible historical priority source. For Jin (2016), a later full paper by Guo and Jin (2017) explicitly identifies the relevant functional as the Lu–Pan boundary-perimeter asymmetry, not the inner-area fraction; direct 2016 full-text comparison remains unavailable.

## Value — PASS
The Kovner–Besicovitch area fraction is a geometrically natural affine-invariant descriptor of central symmetry. The theorem supplies its exact value simultaneously for every odd regular Reuleaux order, an explicit attaining inner body, and an expansion quantifying how central symmetry increases toward the disk. The broader family-level exact characterization is substantive even without classifying irregular Reuleaux polygons or providing downstream general inequalities.

## Limits
Only regular Euclidean Reuleaux odd-gons are covered; uniqueness of maximizing center and rank-order monotonicity are not proved. Finite numerical verification is not a substitute for the analytic argument. Full comparison with Besicovitch (1951), direct inspection of Jin (2016), and independent validation remain unresolved.

Same-model review: passed. Independent audit: not yet performed.
