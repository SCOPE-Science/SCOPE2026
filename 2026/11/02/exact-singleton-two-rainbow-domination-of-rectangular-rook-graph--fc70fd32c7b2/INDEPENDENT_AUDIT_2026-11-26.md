# Independent mathematical audit

## correctness

PASS

An empty row or column forces both colors on every perpendicular line, so weight below 2m implies every line is nonempty. Let (a,b,c) and (p,q,r) denote the numbers of lines with palette {1}, {2}, {1,2} among rows and columns, respectively. With a,p positive, the ap crossings must carry color 1, and they cover none of the both-color lines, so the number of 1s is at least ap+max(c,r). The always valid color-1 line-cover bound is max(a+c,p+r); use the symmetric bounds for 2. With both monochromatic crossing products positive, use ap>=a+p-1 and bq>=b+q-1 to get at least m+n-2+|c-r|. With only one positive product, the ordinary line-cover bound for the other color gives at least m+n-1 (depending on which monochromatic row/column count vanishes). With no positive product, either all lines in one direction are both-colored or all rows contain one color and all columns the other. This establishes the lower bound. Two colors per row attain 2m. For n=m or m+1 and m<=3, the two corner-adjacent arms work: their shared missing corner sees one color along each direction, as does the remaining empty subboard. For m>=4, the two disjoint cyclic diagonals in the (m-2)-square give both palettes there; the monochromatic-only row/column intersections of matching colors are exactly the other selected cells. Their weight plus the square weight is m+n-2. A separate mask-based exact search through the candidate minimum for nine dimension pairs, including (4,5), reproduced the predicted values. Scope: both dimensions at least two, colored vertices exempt, disjoint one-color classes, neither set-valued nor proper rainbow domination. The graph-isomorphism and support partition ensure the same minimum for dual-server domination; the finite replay is corroboration, not the lower-bound proof.

## originality

PASS

The supported contribution is the full rectangular dual-server formula, particularly the sharp near-square and intermediate-width lower bounds not supplied by ordinary 2-domination. The square value is an exact same-day overlap, not an independent priority claim, and the wide branch n>=2m as well as the m=2 slice follow from the known ordinary 2-domination bound and elementary placements. Inspected prior general results do not supply the complete rectangular formula.

## value

PASS

The formula answers a natural placement problem on the canonical two-dimensional complete-graph product. Its meaningful exact content is the singleton-color penalty and sharp transition at width m+2, including widths below the range where ordinary 2-domination suffices. The palette obstruction distinguishes the two parameters and covers an infinite family, rather than tabulating small boards or repeating only the square scalar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
