# Independent mathematical audit

## correctness

PASS

The graph is the line graph of K_{m,n} with one vertex per board square. A chosen-edge set F is total dominating precisely when no selected edge is isolated in L(F) and not both sides contain unused vertices. Removing an essential edge either isolates another selected edge or creates unused row and column; this yields the three disjoint occupied-component regimes. Labelled exponential component enumeration gives the full coefficient-extraction polynomial. For n×n boards, the componentwise deficit 2n-|F| is at least two; equality requires one (n−1)-arm subdivided star plus one unused column, with 2n·n! orientations and label choices for n≥4. A deficit of 3 is impossible for n≥5 by the used-column bound. Independently brute-forced every selected-set mask on 2×2, 2×3, 3×3, 3×4, 4×4, reproducing polynomials (4z²), (3z²+2z³), (6z³+45z⁴), (4z³+93z⁴), and (80z⁴+96z⁵+192z⁶). The finite checks support but do not prove the infinite formula.

## originality

PASS

Howroyd's OEIS A384118 already gives the UNGRADED total for every rectangle, including 51, 368, 7310, and a m,n recurrence; the full three-variable cardinality polynomial, component classification, sharp upper total domination multiplicity and forbidden 2n−3 size are not stated there. Mertens computes ordinary domination rather than inclusion-minimal total domination; k-tuple total domination bounds are another parameter. Independent searches under line-graph edge domination, rook boards and minimal total domination returned no dominating weighted formula. The known ungraded table is expressly not claimed as new.

## value

PASS

The full size distribution and structure of inclusion-minimal (not minimum-size) total dominating sets on rectangular rook boards is a natural domination polynomial. It resolves every coefficient, including a surprising large-set cardinality gap, and counts extremal objects in a standard graph-product family; these are mathematically reusable invariants, not a table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
