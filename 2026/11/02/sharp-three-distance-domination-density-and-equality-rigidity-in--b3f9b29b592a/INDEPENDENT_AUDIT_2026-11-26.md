# Independent mathematical audit

## correctness

PASS

Cartesian product distance is horizontal distance plus the change of row. At n>=7 the allowed offsets are exactly same-row ±3 and other-row ±2; the center itself is allowed only because selected vertices are exempt. Consecutive six-column states of every admissible cyclic word form a closed walk, and shift overlap reconstructs the labeled word from its walk; center weights count every selected vertex once. An independent exhaustive reproduction read the frozen potential as data, rebuilt all 15,376 arcs on 4,096 states from seven-mask windows, verified every nonnegative slack and reproduced all entries in 18 simultaneous relaxations. For each of the 3,583 tight arcs I used return-path reachability, not the supplied SCC program, to check it is cyclic iff it is one of the 14 arcs of the stated two disjoint seven-cycles. The telescoped slack gives |D|>=ceil(3n/7), and equality in 7|D|=3n forces only those cyclic arcs. Traversing either cycle with a fixed labeled origin gives seven distinct words, and the row-swapped family is disjoint. A separate primal BFS and subset enumeration agreed at n=7,8,9: (minimum,count)=(3,14),(4,36),(5,72); BFS neighborhoods were checked also at n=10. In the open ladder an existing distance-three witness has horizontal displacement <=3 and retains its exact distance on wrapping when n>=7. Restricting a periodic optimum and filling both boundary strips of three columns costs at most 12 extra vertices and retains all interior witnesses; this proves the stated density limit.

## originality

PASS

Exact-distance domination and the strip-state method are prior. The distinct supported claim is the sharp coefficient 3/7 per column, the two-periodic-pattern families exhausting equality at all multiples of seven, and the matching open-ladder density. Inspected literature and matched indexed results concern different invariants or domains.

## value

PASS

Fixed-height two is a natural strip version of exact-distance grid domination. The exact density gives an asymptotic benchmark, and the complete labeled rigidity at the optimal periodic orders is a distinct structural result, not just a numerical minimum at one circumference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
