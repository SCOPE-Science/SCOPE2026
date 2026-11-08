# Independent mathematical audit

## correctness

PASS

For Cartesian metric d((a,j),(b,h))=|j-h|+1_{a!=b}, a radius-r source fills exactly the at-most (2r-1) full columns c-r+1..c+r-1 and may cover its single row at the two tips. If I_r are full-column intervals, L=sum|I_r|<=sum_{r=1}^{k-1}(2r-1)=(k-1)^2; overlap redundancy W=L-|union I_r|. For every unfilled column x, the end/start multiplicities a_x,b_x and possible one radius-zero source must cover m different rows. Charging (a_x-1)_++(b_x-1)_+ to adjacent filled columns gives sum R_x<=W (two-sided charge cannot collide except at a singleton covered by only the one r=1 interval). Thus holes cost >=1 overlap unit if m>=4 and all but possibly one if m=3. This proves n<=(k-1)^2 or (k-1)^2+1, respectively, with the k=2 n<=1 exception for m=3. Consecutive odd-length full interval tilings and explicit 5-column row1/r2 at col2, row2/r1 at col5, row3/r0 at col4 witness equality. Source-column clipping proves all shorter path orders. Independent bitmask dynamic search checked exact burning numbers for m=3,n=1..9; m=4,n=1..8; m=5,n=1..5, agreeing with formula. Finite checks are not the infinite proof.

## originality

PASS

Best-of-knowledge qualified: the final statement is not shown to be equivalent to, an implication of, or covered by the materially inspected prior primary statements. General background and known subcases are credited explicitly; inaccessible plausible primary literature is a documented priority risk, not automatic scientific failure.

## value

PASS

A complete exact infinite two-parameter graph-burning classification closes the one-round ambiguity of the known general Cartesian-product bound for all nonsquare path orders. The abrupt m=3 versus m>=4 extra burnable column is a mathematically motivated extremal boundary, not a routine parameter substitution or finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
