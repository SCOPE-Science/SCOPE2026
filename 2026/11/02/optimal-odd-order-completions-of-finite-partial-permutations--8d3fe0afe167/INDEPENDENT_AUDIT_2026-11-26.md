# Independent mathematical audit

## correctness

PASS

A prescribed directed cycle is immutable, so any even one prevents every completion. Otherwise, on the original carrier the only free arrows send path ends bijectively to path starts. A component cycle is admissible exactly when it contains an odd number of odd-size paths, including an unassigned singleton as one such path. If a>=1, delete even-size paths from their cycles to get an odd-cycle permutation of the a labelled odd-size paths. Reinsertion in fixed label order has exactly a,a+1,...,a+b-1 choices and is reversible. The classical EGF C(x)=sqrt((1+x)/(1-x)) gives the stated double factorials; the mixed EGF follows by substituting x/(1-y), or by exponentiating the cycle sum 1/2 times log((1-y+x)/(1-y-x)). For a=b=0 the empty component permutation is unique, including for an empty carrier. For a=0<b, all cycles on the original carrier would be even; a fixed new vertex is the sole odd component and forces one cycle containing every path. Ordering the b paths after that vertex gives exactly b! possibilities. The notes and supplied checker were inspected but not run. Separate bounded enumeration of component permutations with a+b<=7 and fixed-label repair cases b=1..6 corroborates the counts; the bijection proves the theorem.

## originality

PASS

Best of current knowledge for the joint sharp carrier-size and mixed labelled completion classification. The all-odd-cycle counts are explicitly classical. The closest inspected extension result gives existence but not a shared single-vertex optimum or exact mixed multiplicities, and the closest inspected indexed exponent result fixes the carrier and restricts to powers of 3.

## value

PASS

Optimal carrier enlargement is a natural question for the cited extension problem. The result explains when a single new point repairs arbitrarily many even-sized paths, and exactly which component orders and how many labelled completions occur. This provides a usable sharp parity-profile invariant beyond mere existence or recomputing the all-odd baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
