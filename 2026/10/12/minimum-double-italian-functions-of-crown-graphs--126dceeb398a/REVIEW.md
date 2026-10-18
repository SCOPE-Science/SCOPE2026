# Independent mathematical audit

## correctness

PASS

With X=sum x_i and Y=sum y_i, f(N[a_i])>=3 for x_i<=1 is x_i+Y-y_i>=3 and similarly y_i+X-x_i>=3 for y_i<=1. If total <=5 the lighter side X<=2 has zero coordinates, and opposite inequalities make Y exceed available weight, ruling out <6. At weight 6, X=2 case is impossible: either two 1 entries imply Y>=n+2>4, or one 2 entry forces all other y_i>=1 and n=4,5 distinguished coordinate fails; similarly X<=1 impossible. Thus X=Y=3. If x_i or y_i <=1 the paired inequalities force equality; if both >=2, side totals force equality of final coordinate. Conversely copied composition totals 3 satisfy all; weak compositions of 3 into n parts count C(n+2,3).

## originality

PASS

No prior mathematical result located implying the all-parameter family-specific theorem; best-of-knowledge, with residual indexed/access limitations.

## value

PASS

The missing perfect matching makes a crown a natural one-edge-per-vertex perturbation of a solved complete multipartite family. Equality forces a nontrivial synchronization of labels on omitted matched endpoints and completely counts optimum functions; a precise natural equality invariant, not an arbitrary graph slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
