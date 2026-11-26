# Independent mathematical audit

## correctness

PASS

Left multiplication preserves Hamming distance and reduces the centers to e and sigma. Complementing the balls gives n!-2D_n+Q(sigma), where Q counts derangements also avoiding the moved edges of sigma. Prescribing one moved edge leaves n-2 disjoint forbidden diagonal cells on n-1 rows, so U=D_(n-1)+D_(n-2). Prescribing two distinct edges leaves respectively n-2, n-3 or n-4 such cells according to the number of symbols in their union, giving the common upper bound V=D_(n-2)+2D_(n-3)+D_(n-4). A transposition uses only two edges with overlap D_(n-2), giving the claimed value. Any other nonidentity type moves at least three points; Bonferroni for those three events bounds Q by D_n-3U+3V, below the transposition value by at least D_(n-1)-D_(n-2)-6D_(n-3)-3D_(n-4). This is 1, 20, 161 for n=5,6,7 and by recurrence (n-3)D_(n-2)+(n-8)D_(n-3)-3D_(n-4)>0 for n>=8. Thus equality is possible only for a transposition. An independent direct enumeration of survivors agreeing in both balls counted every relative cycle type for n=3 through 8: maxima 3, 10, 56, 358, 2612, 21514, including exactly the stated small-length exceptions.

## originality

PASS

The prescribed distance-two count and known finite maxima are prior coverage. The supported distinct claim is the uniform strict classification over all distinct centers along the unbounded diagonal r=n-1, not a new count at prescribed distance two or a determination of the conjecture at arbitrary radius. The closest accessible reconstruction source proves fixed small radii and tabulates further lengths; that evidence does not give the infinite strict diagonal conclusion.

## value

PASS

This treats a natural extremal boundary of an existing permutation reconstruction conjecture at every length, not just a finite extension of its tables. The strict equality-case classification and sharp n=3,4 behavior say which center geometries create the worst ambiguity; the short forbidden-position comparison replaces a length-by-length maximization over cycle types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
