# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The Richardson coefficients are the Lagrange weights for extrapolation from the geometric nodes \(r^{-2k}\) to zero. Their signs alternate, while after multiplication by the trapezoidal mesh factor their absolute magnitudes satisfy
\[
\frac{A_{k+1}}{A_k}
=\frac1r\frac{r^{2k+2}(r^{2(d-k)}-1)}{r^{2k+2}-1}
>r-r^{-1}>1.
\]
Every collected quadrature weight is therefore an alternating tail ending in its largest positive term, which proves strict positivity. The exact maximum follows because newly introduced finest-grid nodes contain only the last term, whereas all older-node tails are positive and smaller. Constant exactness then gives \(\sum |w_i|=b-a\), which is also the universal lower bound for any constant-exact rule. Standard Euler--Maclaurin cancellation gives polynomial exactness through degree \(2d+1\).

The symbolic argument was stress-tested on endpoints, nodes first appearing at every possible level, arbitrary base subdivision counts, and the limiting cases \(d=0\) and \(r=2\). Exact rational verification over 60 parameter combinations checks all sample weights, moment exactness, normalization, and the tail-ratio inequality.

## Originality

**PASS, to the best of our knowledge, with material historical-equivalence uncertainty.** Positivity of the dyadic \(r=2\) Romberg rule is classical and is explicitly excluded from the novelty claim. Welsch (1966) gives positive classical Romberg weights with the familiar approximately 0.484 to 1.4524 normalized range, and Camargo's modern treatment gives another proof for the classical dyadic family.

Farzi (2014) was checked at the relevant positivity section. It permits general division sequences, but its stated positivity results distinguish the dyadic Romberg sequence, selected prefixes of the alternating Bauer sequence, and the nonpositive Bulirsch case. The checked text does not state that every pure geometric integer sequence \(s,sr,sr^2,\ldots\) is positive for all \(r\ge3\). Sidi (1997) treats generalized Richardson extrapolation on geometric points and generalized Romberg applications, but the accessible material checked did not state this final-sample positivity theorem. General quadrature-weight positivity criteria such as Sottas--Wanner are acknowledged as background.

Searches covered generalized Romberg, Richardson integration, positive extrapolation weights, geometric division sequences, Bauer and Bulirsch sequences, and synonymous equidistant quadrature formulations. No checked source stated the all-integer-refinement theorem, the exact maximum-weight product for this family, or the sharp sample-noise consequence. The main remaining risk is older generalized-extrapolation literature, especially books and theorem-level material not fully searchable online, where an equivalent special case may appear under division-sequence notation.

## Value

**PASS.** The result identifies a simple infinite family of arbitrarily high-order, nested, equally spaced quadrature rules whose final weights remain positive for every integer refinement factor, rather than only the familiar dyadic case. Positivity immediately turns the collected quadrature into an optimally conditioned linear functional for bounded absolute sample noise, and the exact maximum-weight product gives a concise local-weight scale. The proof also explains why alternating Richardson coefficients do not imply negative final sample weights.

## Scientific limitations

The theorem is restricted to integer-ratio nested uniform trapezoidal grids and exact final rule aggregation. It does not control intermediate cancellation in a floating-point Richardson tableau, nonnested or arbitrary division sequences, rational extrapolation, or stochastic/relative noise. Larger refinement factors have a substantially larger sampling cost at fixed depth, and no efficiency dominance is claimed. Historical equivalence in older extrapolation literature remains possible.
