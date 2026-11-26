# Independent mathematical audit

## correctness

PASS

The claimed depth counts the first equality of consecutive synchronous partitions, starting at round zero with one uniquely marked corner. The degree deficit first becomes available at round one; applying the Laplacian k times uses k additional rounds. Its separated path resolvent satisfies both endpoints (after removing the common prefactor, the left endpoint equation reduces to (1-r^q)/(1-r)) and the interior recurrence for z=-r/(1-r)^2. The change of parameter preserves order of vanishing. The cross-multiplied numerator is anti-reciprocal in degree m+n-1; the R initial zero coefficients force all coefficients to vanish except in the four expressly handled small cases. At a primitive q-th root, the reflected-position amplitudes have distinct cosine factors on the near half of the path, so a nonzero difference of reflection types has least period q. Thus the shorter and longer path differences cannot cancel unless both vanish; for squares, coefficient multiplicities distinguish unordered pairs of reflection types. A root-distance d at most R gives a shortest-walk count binom(d,i) with just the swap ambiguity. An unequal swap cannot preserve both rectangle reflection types because it would require i+j=m-1=n-1. Outside radius R, only the far-far position in a reflection orbit remains, modulo swap on a square. The reflected witness in the final column has distances R and greater than R, is indistinguishable before R, and splits at R. Direct small-case refinement gives round depths 1, 2, 2, 3 for (2,2), (2,3), (3,3), (3,4); in the last case round two leaves only the doubletons {(0,3),(2,3)} and {(2,1),(2,2)}, both split by their neighbors in round three. An independent in-memory implementation using retained vertex color and sorted neighbor colors checked depth and orbit partition on 63 pairs, 2<=m<=10 and m<=n<=12. The supplied direct/algebra scripts and recorded outputs were inspected, not executed. The bounded replay corroborates the finite cases; the proof establishes the universal depth.

## originality

PASS

Pass concerns the exact first stabilization round for the single-corner initialization. The stable singleton/swap partition is supported here but is not a distinct contribution: same-object catalogue records already give that partition, and the frozen result acknowledges overlap on eventual orbits. The closest quantitative catalogue result is for uniform initialization and differs in actual value. No inspected same-object statement gives the marked stopping time or makes it an immediate corollary. This is a bounded source comparison, not a priority determination.

## value

PASS

A single initial marker is a natural individualization of rectangular grids. The exact synchronous depth explains when boundary information and the marker together finish refinement, rather than simply giving eventual identifiability or an order-of-growth bound. The reflected far-column pair certifies a sharp obstruction, and the even/odd short-side dependence is useful when comparing refinement depths across initializations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
