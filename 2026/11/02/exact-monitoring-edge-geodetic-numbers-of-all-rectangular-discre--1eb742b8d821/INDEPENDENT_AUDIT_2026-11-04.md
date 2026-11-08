# Independent mathematical audit

## correctness

PASS

A forced edge must occur on every shortest path between a selected pair. Cartesian coordinate-interleaving shows only same-fiber pairs can force edges, so every C_m fiber needs 3 monitors (all vertices if m=3,4). For m<=n, selecting R+floor(mj/n) in column j gives exactly 3n points. The row maximum circular gap is <=ceil(floor((m-1)/3)*n/m)+1<n/2 for n>=13; the 36 smaller dimension pairs leave exactly (5,6),(7,8), for which RESULT.md supplies explicit 3-per-column arrays with row and column gaps strictly below half-cycle. Thus every edge is forced and 3n meets the fiber lower bound. Independent newly written checker examined 1,235 5<=m<=30, m<=n<=64 pairs and all 36 arithmetic cases. These checks corroborate the all-dimensional inequality, not replace it.

## originality

PASS

Haslegrave proved the product fiber theorem, the general 3 max(m,n) lower bound and the square-torus case, but no arbitrary rectangular matching construction. Dev et al. established the individual cycle values; these are explicitly inherited. The 2024 product-networks article accessible abstract covers several non-Cartesian products and cannot alone establish complete full-text noncoverage. Searches of other toroidal invariants/Resultary gave no covering claim, not priority certification.

## value

PASS

This exactly resolves the natural extremal monitoring number of every unweighted rectangular torus, with a stretched explicit optimal placement for arbitrary aspect ratios; the sharp value and constructions are useful beyond the previously settled square network and trivial factors, not an artificial parameter choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
