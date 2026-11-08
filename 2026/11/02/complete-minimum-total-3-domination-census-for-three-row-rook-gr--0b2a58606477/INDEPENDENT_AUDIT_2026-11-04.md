# Independent mathematical audit

## correctness

PASS

For x_ij∈{0,1}, open selected neighbors at (i,j) are exactly r_i+c_j−2x_ij. If some row has two selected cells their two columns must be fully selected, and every other column nonempty. At 6,7,8,9-cell thresholds these constraints classify optima: n2 all cells; n3 two full columns and one double; n4 two full and same-row singles; n>=5 three full or one full+three doubles with missing-row permutation; additionally n5 two full+three same-row singles. Counts: 1,9,18,160, and binom(n,3)+n(n−1)(n−2)(n−3) for n>=6; gamma values 6,8,8,9. Independent direct adjacency-bitmask enumeration of all subsets of sizes 1 through the proposed optimum for n2..6 (187573 examined) agreed. Full proof uses row-rigidity, not bounded enumeration.

## originality

PASS

The scalar n>=5 minimum 9 was proved by Bermudo–Sánchez–Sigarreta (2017) and is not new. Carballosa–Wisby (2020/2022) give product lower bounds and square cases but not an optimizer census. The full three-row extremizer families, n5 special class, and exact quartic labeled count are not implied by these scalar bounds. Historic unindexed minimum-set enumeration remains possible.

## value

PASS

A natural complete classification of all optimal configurations in the canonical line graph L(K_{3,n}), including a 5-column exceptional family and count needed for extremal sampling/reliability polynomials. It is more than repeating the known scalar gamma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
