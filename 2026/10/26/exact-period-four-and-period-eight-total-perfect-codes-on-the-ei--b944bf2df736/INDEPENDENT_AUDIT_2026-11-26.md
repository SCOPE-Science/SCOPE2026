# Independent mathematical audit

## correctness

PASS

For t>=3 the four neighbors are distinct, and at column j the exact-one equation determines bit i of the next column to be 1 minus bit i of the preceding column and the two vertical neighbor bits of the current one. Thus the binary-successor condition gives a partial function on exactly 256^2 ordered column pairs. Closure after t updates is necessary and sufficient for the cyclic equations, with no overcount: fixing the distinguished j=0 fixes the initial ordered pair (column -1, column 0), and conversely that state determines every labeled column. I independently computed candidates coordinatewise and deleted zero-indegree states iteratively. This cannot delete any cycle; any surviving vertex must have an incoming edge from the survivor set. In a finite graph with at most one outgoing edge per vertex this forces all surviving indegrees and outdegrees to be one, so the survivors are disjoint cycles. Of 65,536 states, 1,156 have a defined successor; the 144 survivors give four length-four and sixteen length-eight cycles with the same minima as the frozen certificate. Shortest cycle length in this graph equals least translation period of the associated code. Each length-l cycle contributes l distinct states fixed by the t-fold map when l divides t, none otherwise. Hence the exact labeled census is 16 times the indicator of 4|t plus 128 times the indicator of 8|t (which includes the sixteen least-four patterns when 8|t). This exhaustive finite quotient covers every t; no extrapolation in t is needed.

## originality

PASS

The supported distinct finding is the unrestricted labeled census and least-period structure at width eight. The closest accessible primary results classify or guarantee parallel codes and explicitly stop short of the unrestricted width-eight case. The independent census even gives mixed-direction induced matchings, so the parallel classification cannot include all the counted patterns. The 2026 Wehrmann–Koster paper is a material unresolved priority risk, not evidence of coverage or of absence; the originality assessment does not assert first resolution of the existence slice over all literature.

## value

PASS

Width eight is the next natural width after the documented width-three-through-seven cases of the toroidal existence question. Beyond deciding existence, the census gives a uniform least-period bound and the exact labeled number for an infinite family, including patterns with both matching directions that a parallel-code theory does not see. The exact count and forced periods are useful benchmarks for wider toroidal tilings, rather than a database recomputation or an arbitrary one-off size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
