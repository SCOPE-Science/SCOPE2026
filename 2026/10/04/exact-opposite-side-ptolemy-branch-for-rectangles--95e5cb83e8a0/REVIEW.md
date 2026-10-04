# Same-model review

## Correctness
PASS. The coordinate reduction is exact. With bottom and top half-lengths \(a,b\), midpoint offset \(h\), \(p_0=a+b\), and \(q=a-b\), the Ptolemy ratio has the displayed closed form. The first monotonicity follows from
\[
\Phi_h(q)^2-(q^2+H^2-h^2)^2=4H^2h^2,
\]
which makes the numerator nonincreasing in \(q^2\). The second reduction is monotone in \(v^2\), and the final one-variable function is increasing in \(u\). Equality conditions propagate to \(a=b=L/4\) and \(h=L/2\). The comparison with the full rectangle lower candidates is exact.

## Originality
PASS with residual historical-access risk. Harmaala--Klén publish the same numerical value as one lower-bound configuration, but their result does not imply the sharp upper bound or equality classification for the full opposite-side branch. Their global rectangle upper bound is strictly coarser. Finch explicitly labels his global rectangle formula nonrigorous and says that many configurations remain to be ruled out; he does not state this branch theorem. Targeted published-finding searches for opposite-side, parallel-segment, and exact-formula aliases found no covering statement. The unpublished 1996 Seittenranta licentiate thesis cited by Harmaala--Klén was not materially inspected.

## Value
PASS. The result gives a natural complete classification of a whole side-occupancy branch in an explicit open rectangle maximization problem. It identifies the exact role of Harmaala--Klén's third parallelogram lower-bound configuration and proves that this branch is never globally extremal, thereby removing an infinite family of candidate configurations rather than merely checking isolated parameters.

Same-model review: passed. Independent audit: not yet performed.
