# Independent mathematical audit

## correctness

PASS

The original is mathematically sound: forcing a cycle changes the cyclic-triangle expectation by k/4, and global reversal and relabeling leave just the adjacent-pair invariant quadratic mode, with the stated variance and coefficient. The repaired RESULT.md rederives this as background directly from Walsh coefficients. In its new claim for lengths k≥5, a proper subset of an underlying simple cycle cannot contain a cycle component; therefore a four-edge support on four vertices is impossible, and on five vertices the only contributing residual support is a four-edge path. A fixed oriented path extends to (n−5) falling (k−5) directed words; reversal contributes the same sign to its degree-four coefficient. Division by the triangle coefficient gives 1/[4(n−3)(n−4)] for every k≥5. The path products are mutually orthogonal, with (n) falling 5 over 2 such products. The residual on v≥6 vertices has O_k(n^v) possible supports with unnormalized coefficients O_k(n^(k−v)), giving normalized variance O_k(1) and zero residual for k=5. The five-vertex variance is exactly the triangle variance divided by (n−3)(n−4); Taylor expansion gives the positive coefficient 1/2 in the n^(−2) triangle correlation gap. For two lengths ≥5, the common first two components have variance Theta(n³) and the remaining cross-covariance is O(1), which gives the n^(−3) bound. All exact formulas are for n≥k; asymptotics fix lengths. The frozen code and its recorded finite checks were inspected, not executed, and are not certification of the new result.

## originality

PASS

Pass only for the delivered five-vertex refinement, not for the original exact covariance and common triangle mode as stand-alone novelty. The score-profile result already explicitly projects every centered cycle count to the stated triangle coefficient times the centered triangle count in a space containing triangles. This gives the exact covariance (the elementary triangle variance supplies the normalization) and, with the one-dimensional invariant quadratic subspace, the same quadratic projection. That is demonstrable mathematical coverage independent of chronology. Its inspected statement and proof give no higher-order variance or correlation estimate. The repaired result identifies and counts the first surviving motif for lengths ≥5, giving a common second component and sharper explicit rates not supplied by the score-profile result or the known length-four computation.

## value

PASS

The repaired result resolves the first non-triangle source of fluctuation for an entire natural family: the four-cycle rate does not describe any fixed longer length, and the five-vertex fluctuation cancels when comparing two longer lengths to each other. The positive universal coefficient and exact shared normalized correction are substantive information, not a looser rephrasing of the common triangle projection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
