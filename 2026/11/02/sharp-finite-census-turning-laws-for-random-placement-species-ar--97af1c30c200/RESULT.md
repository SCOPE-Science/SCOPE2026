# Sharp finite-census turning laws for random-placement species–area elasticity

## Finding

For a community of \(s\ge1\) species with positive integer abundances \(n_1,\ldots,n_s\), independently and uniformly placed in a unit study region, let \(S(a)\) be expected richness in a subregion with area fraction \(a\), and let \(z(a)=d\log S(a)/d\log a\) be its instantaneous species–area exponent. Let \(r_1\) and \(r_2\) denote the numbers of singleton and doubleton species. The derivative of this exponent near complete sampling obeys the exact identity

\[
\lim_{a\uparrow1}z'(a)=\frac{r_1(s-r_1)-2sr_2}{s^2}.
\]

Consequently a strictly positive (respectively negative) right-hand expression forces the local log–log exponent to increase (respectively decrease) throughout some terminal area interval. No sign conclusion is asserted at equality.

For the particularly natural *one singleton and one common species* abundance vector \((1,n)\), the complete shape is sharp for all integers \(n\ge1\): \(z\equiv1\) when \(n=1\), \(z\) strictly decreases for \(n=2\), and for every \(n\ge3\) there is **exactly one** stationary point in \((0,1)\), a strict global minimum; the exponent decreases before it and increases after it. In the latter case the unique minimum is \(a_n=1-q_n\), where \(q_n\in(0,1)\) is the unique positive zero of the explicit polynomial \(P_n\) below. Thus **four individuals**, in abundance pattern \((1,3)\), are necessary and sufficient for a random-placement community to have a log–log species–area exponent that first falls and then rises as sampling area grows. This is minimal across all positive integer abundance partitions, not merely two-species communities.

For \(n=3\), the minimum is located exactly at
\[
 a_3=\frac{8-2\sqrt 7}{3}=0.90283245929\ldots.
\]

## Assumptions and scope

Fix a measurable study region of area one and a subregion of relative area \(0<a<1\). For each \(i\), the \(n_i\) distinct individuals of species \(i\) have independent uniformly distributed locations; each is included in the subregion with probability \(a\). Total abundances are deterministic positive integers. No spatial dependence, species interaction or immigration is assumed. Expected observed species richness is
\[
 S(a)=\sum_{i=1}^{s}\bigl[1-(1-a)^{n_i}\bigr]>0,
 \qquad z(a)=\frac{aS'(a)}{S(a)}.
\]

The terminal derivative is the one-sided limit from \(a<1\); in the proof the polynomials extend continuously to \(a=1\). The theorem concerns the *local exponent*, not the first derivative of richness on ordinary linear axes or any fitted power-law slope over a finite observation window.

## Proof

**Universal terminal law.** Put \(q=1-a\). Differentiation gives
\[
 S(1)=s,\qquad S'(1)=r_1,\qquad S''(1)=-2r_2.
\]

The third identity holds because only abundance-two terms contribute nontrivially to the second derivative at \(q=0\). Since
\[
 z'(a)=\frac{S'(a)}{S(a)}+
  \frac{a S''(a)}{S(a)}-
  \frac{a S'(a)^2}{S(a)^2},
\]
substitution at \(a=1\) proves the stated exact identity. Polynomials have continuous derivatives at \(a=1\), so any strict terminal sign persists on a sufficiently small nonempty interval immediately below one. The equality case is intentionally left unclassified by this first-order law.

**Two-species global classification.** For abundances \((1,n)\), set \(G_n(q)=\sum_{j=0}^{n-1}q^j\). The exact identity \(S(a)=(1-q)(1+G_n(q))\) yields
\[
 z(a)=\frac{1+nq^{n-1}}{1+G_n(q)},\qquad q=1-a.
\]
For \(n=1\), the exponent is identically one. For \(n=2\), \(z=(1+2q)/(2+q)\), strictly increasing as a function of \(q\), hence strictly decreasing as a function of area.

For every integer \(n\ge3\), differentiation with respect to \(q\) gives
\[
 \frac{dz}{dq}=\frac{P_n(q)}{(1+G_n(q))^2},
\]
where
\[
 P_n(q)= -\sum_{j=0}^{n-3}(j+1)q^j
 +(n-1)(2n-1)q^{n-2}
 +n\sum_{j=1}^{n-2}(n-1-j)q^{n-2+j}.
\]
The coefficient list of \(P_n\), in increasing powers of \(q\), has negative coefficients in degrees \(0,\ldots,n-3\), then positive coefficients in degrees \(n-2,\ldots,2n-4\). Thus there is exactly one sign change. Moreover
\[
 P_n(0)=-1<0,\qquad P_n(1)=\frac{n(n-1)(n+1)}2>0.
\]
By Descartes' rule of signs (counted with multiplicity), \(P_n\) has at most one positive real zero, and the intermediate value theorem supplies one in \((0,1)\). Because the denominator above is strictly positive, \(z\) increases with \(q\) beyond that root and decreases with \(q\) below it. Since \(dq/da=-1\), \(z\) strictly decreases with area until the unique point \(a_n=1-q_n\) and strictly increases thereafter. It is therefore the unique strict global minimum. For \(n=3\), \(P_3(q)=3q^2+10q-1\), yielding the exact displayed value of \(a_3\).

**Sharp minimum number of individuals.** Every total abundance \(\sum_i n_i\le3\) belongs, up to permuting species, to one of the single-species cases \((1),(2),(3)\), all-singleton cases \((1,1),(1,1,1)\), or the case \((1,2)\). All-singleton abundances yield \(z\equiv1\). The case \((1,2)\) is strictly decreasing by the formula above. For one species with \(n\ge2\),
\[
 z(a)=\frac{nq^{n-1}}{G_n(q)}.
\]
Its derivative with respect to \(q\) is positive on \((0,1)\), since
\[
 (n-1)G_n(q)-qG_n'(q)
 =\sum_{j=0}^{n-1}(n-1-j)q^j>0.
\]
Hence every one-species exponent strictly decreases with area. No community containing at most three individuals can exhibit the stated fall-then-rise. The verified \((1,3)\) construction contains four individuals and exhibits exactly that behavior, proving minimality.

## Verification

Run `python3 verify_species_area.py` using Python 3.10 or later; it has no third-party dependencies. Its exact integer-polynomial tests compare the closed formula for \(P_n\) with independently differentiated numerators for \(2\le n\le150\); it checks the singleton/doubleton endpoint identities in 19,607 finite abundance vectors; it numerically brackets a unique stationary location for \(3\le n\le250\); and it independently enumerates all integer abundance partitions with at most three individuals. The tests are finite checks of the derived identities and examples, **not a substitute for the all-integer analytical proof**. For the \((1,3)\) example, the critical quadratic and its exact radical root are verified directly.

## Relationship to prior work

The finite random-placement expected-richness equation is classical; He and Legendre (2002), Eq. (1), explicitly write it for arbitrary fixed species abundances, and their Table 1 already contains the *most uneven* special-abundance curve, including the two-species \((1,n)\) curve before differentiation. This prior formula is not claimed as new. Coleman (1981) is an earlier source of random-placement species–area relations. Tjørve, Kunin, Polce and Calf Tjørve (2008) explicitly examine nonmonotonic log–log species–area shapes from uneven occurrence and spatial patterns in a related gridded occupancy model, so qualitative reversals of curvature are **not** claimed as new either. The contribution here is the exact fixed-individual-count terminal sign law, all-\(n\) uniqueness of the one-common-species elasticity minimum, and its sharp four-individual onset. A separate two-species Poisson-placement calculation also has log–log slope turnings, but its unbounded independent abundance counts and two-turning structure do not imply this finite-census theorem.

The closest older Coleman full text was not obtainable for complete comparison. In particular, the broader random-placement literature might contain an equivalent or stronger result; that priority risk remains. No claim of globally established originality is made beyond the stated inspected comparisons.

## Limitations

The result concerns expected richness, not an individual realized sample. Spatial clustering, fixed occupied grid cells, finite-size specimen geometry, nonuniform species-location distributions, and alternative observation procedures can change the shape. The terminal derivative identity does not classify the equality case, and the complete interior turning count is proved only for the indicated two-species family, not all finite communities. The proof does not establish empirical detectability of the narrow late-area increase or global historical priority.

## References

1. Coleman, B. D. (1981). *On random placement and species-area relations*. Mathematical Biosciences 54, 191–215. DOI: `10.1016/0025-5564(81)90086-9`. Earlier model source; original complete text inaccessible for this comparison.
2. He, F. and Legendre, P. (2002). *Species diversity patterns derived from species–area models*. Ecology 83, 1185–1198. DOI: `10.1890/0012-9658(2002)083[1185:SDPDFS]2.0.CO;2`. Available author-hosted full text: https://sites.ualberta.ca/~fhe/He-publications/He_Legendre02.pdf. First public publisher date verified as 2002-05-01.
3. Tjørve, E., Kunin, W. E., Polce, C. and Calf Tjørve, K. M. (2008). *Species–area relationship: separating the effects of species abundance and spatial distribution*. Journal of Ecology 96, 1141–1151. DOI: `10.1111/j.1365-2745.2008.01433.x`. Publisher-hosted full HTML examined.
