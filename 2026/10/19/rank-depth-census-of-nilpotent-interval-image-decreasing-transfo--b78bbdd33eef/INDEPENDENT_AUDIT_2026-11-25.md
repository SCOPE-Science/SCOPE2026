# Independent mathematical audit

## correctness

PASS

The order and interval constraints give binary increments starting from f(1)=1. The first increment must be zero, since otherwise 2 is fixed; if it is zero, every i>1 descends. Monotonicity makes the orbit of n determine the least zero-power. Restricting a rank-r map to [r] gives a zero-root map, of rank s and depth h-1; its extensions of the required rank choose r-s increments in n-r positions. For the support, put m=n-r. The descending orbit has positive steps with total n-1, initially m and thereafter nonincreasing and at most m. Conversely, choose a nonincreasing list of h-1 positive summands of r-1 bounded by m. On consecutive orbit anchors the required change in the defect i-f(i) lies between zero and their separation, so interpolation by binary increments is possible; on the final interval up from 1 it is forced to increase by one at each point. The resulting map has precisely this orbit. At depth r all steps after the first are one, forcing all but one of the rank increments; the remaining increment has n-r choices. At depth two the restriction to [r] is constant, giving the binomial count and the displayed formal series by summation, with the n=1 term removed. Rank one and n=2 are included. The finite check was independently reconstructed by enumerating all regressive full maps through n=8, filtering the stated domain conditions, and composing the actual maps; all rank/depth cells agreed. This is corroboration only. The proof is replayable at RESULT.md §§1–5; the frozen checker.py and VERIFICATION.md were inspected, not executed.

## originality

PASS

The supported distinction is the full zero-root interval-image subset census, including its exact joint support and endpoint multiplicities. The prior rank count, general Catalan-monoid stabilization census, partial-map nilpotent counts, and classical Fibonacci enumeration are not themselves new here. The strongest general Catalan census aggregates together several subclasses, without a restriction variable that selects this subset. The different n-r upper-boundary count and the rank-dependent lower boundary require additional information. No stronger covering result was established in the checked statements.

## value

PASS

The invariant tracks the collapse dynamics of every nilpotent in a natural path-transformation monoid. The complete joint census and the interpolation proof of exactly which rank-depth pairs occur go beyond the known ambient size and generating ranks. The shallow-depth binomial and Fibonacci laws provide a precise comparison with the whole nilpotent class; the value is the map interpretation and rank refinement, not the Fibonacci numbers alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
