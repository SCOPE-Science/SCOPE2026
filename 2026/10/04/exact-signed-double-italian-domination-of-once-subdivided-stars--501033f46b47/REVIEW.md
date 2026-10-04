# Review of Exact signed double Italian domination of once-subdivided stars

## Correctness
PASS. The leaf and support constraints are reduced exactly to feasible two-vertex arm states for each center label. For positive center labels, an arm with support \(-1\) has minimum weight \(1\), while any arm whose support is not \(-1\) costs at least one extra unit and can contribute at most four additional units to the support sum. This converts the center closed-neighborhood condition into sharp lower bounds for center labels \(1,2,3\). A center labeled \(-1\) makes every arm cost at least \(2\). Comparing the four cases proves the value, and equality forces the claimed two arm states and exact number of exceptional arms. Direct brute force for \(q=4,5\) and exact dynamic programming through \(q=60\) agree with both the value and count.

## Originality
PASS. The primary 2023 paper itself introduces the exact family \(T_{4k}\) but uses it only as a witness construction, proving \(\gamma_{sdI}(T_{4k})\le5k+1\) while showing the signed double Roman number is larger. Its exact-family results concern paths, stars, and cycles, while the double-star section gives lower bounds. Targeted semantic and exact-phrase searches found no equality for \(T_{4k}\), no all-\(q\) once-subdivided-star formula, and no minimum-function count. A later survey likewise summarizes paths, stars, and cycles as the exact named families.

## Value
PASS. The result closes the exact value on the very family chosen by the defining paper to demonstrate strict separation from signed double Roman domination. It converts a one-sided construction into an equality theorem, extends it to every arm count, and identifies every optimizer with a residue-class-sensitive count. That is a natural structural completion of an explicit literature construction rather than an arbitrary new slice.

Same-model review: passed. Independent audit: not yet performed.
