# Sharp finite-census turning laws for random-placement species–area elasticity

## Finding

For a community with one singleton species and one species of abundance \(n\), place all individuals independently and uniformly in a study region. The local log–log exponent \(z(a)\) of expected richness as a function of relative sampled area \(0<a<1\) has the following complete classification: it is constant when \(n=1\), strictly decreasing when \(n=2\), and has exactly one stationary point when \(n\ge3\). In the last case the stationary point is a strict global minimum: \(z\) strictly decreases before it and strictly increases afterward. Its area is \(a_n=1-q_n\), where \(q_n\in(0,1)\) is the unique positive zero of \(P_n\) displayed below.

Among all communities with deterministic positive integer species abundances, the smallest total census that permits such a fall and then rise is four individuals. The vector \((1,3)\) attains that minimum census, with the exponent minimized at
\[
a_3=\frac{8-2\sqrt7}{3}=0.90283245929\ldots.
\]

## Assumptions and scope

The study region has area one and the subregion has relative area \(a\). Each of the \(n_i\ge1\) individuals of species \(i\), independently of the other individuals, is in the subregion with probability \(a\). Species abundances \(n_1,\ldots,n_s\), \(s\ge1\), are fixed. Under this classical model the expected richness and its local exponent are
\[
S(a)=\sum_{i=1}^s[1-(1-a)^{n_i}],\qquad z(a)=\frac{aS'(a)}{S(a)}.
\]
The exponent concerns expected, not realized, richness; it is not a fitted power-law slope over a finite area range.

For context, the complete-sampling derivative follows directly from the classical richness equation. If \(r_1\) and \(r_2\) are the numbers of singleton and doubleton species, then \(S(1)=s\), \(S'(1)=r_1\), and \(S''(1)=-2r_2\). Differentiating \(aS'/S\) and using continuity at \(a=1\) gives
\[
\lim_{a\uparrow1}z'(a)=\frac{r_1(s-r_1)-2sr_2}{s^2}.
\]
A strict sign implies the corresponding sign on a terminal interval, while a zero derivative at the boundary gives no sign conclusion by itself. This endpoint calculation is a corollary of the existing model, not a separate claim of originality, and does not count interior stationary points.

## Proof

**Complete classification for \((1,n)\).** Put \(q=1-a\) and \(G_n(q)=\sum_{j=0}^{n-1}q^j\). Factoring the richness polynomial gives \(S(a)=(1-q)(1+G_n(q))\), so
\[
z(a)=\frac{1+nq^{n-1}}{1+G_n(q)}.
\]
This is identically one for \(n=1\); for \(n=2\) the derivative of \((1+2q)/(2+q)\) with respect to \(q\) is \(3/(2+q)^2>0\), so the exponent strictly decreases with \(a\).

For \(n\ge3\), the quotient rule gives \(dz/dq=P_n(q)/(1+G_n(q))^2\), with
\[
P_n(q)=-\sum_{j=0}^{n-3}(j+1)q^j+(n-1)(2n-1)q^{n-2}
+n\sum_{j=1}^{n-2}(n-1-j)q^{n-2+j}.
\]
Indeed the numerator is \(n(n-1)q^{n-2}(1+G_n)-(1+nq^{n-1})G_n'\). The leading would-be term of degree \(2n-3\) cancels. The resulting coefficients are negative through degree \(n-3\) and positive from degree \(n-2\) through \(2n-4\). Also \(P_n(0)=-1\) and \(P_n(1)=n(n-1)(n+1)/2>0\). Descartes' rule and the intermediate value theorem give exactly one positive zero, in \((0,1)\); the sign is negative below it and positive above. Since \(dq/da=-1\), this yields precisely one strict minimum as claimed. In particular \(P_3(q)=3q^2+10q-1\), so \(q_3=(-5+2\sqrt7)/3\).

**Minimal census.** Among positive integer abundance partitions of at most three individuals, the only possibilities are all singletons, a single species, or the pair \((1,2)\). All-singleton exponents are constant, and the pair \((1,2)\) was handled above. For one species of abundance \(n\ge2\), the exponent is \(nq^{n-1}/G_n(q)\). Its derivative in \(q\) is positive on \((0,1)\) because the factor \((n-1)G_n-qG_n'=\sum_{j=0}^{n-1}(n-1-j)q^j\) is positive there. Thus it strictly decreases in area. The proven \((1,3)\) minimum establishes that four individuals suffice.

## Verification

The accompanying `verify_species_area.py` compares the derivative numerator with independent exact integer-polynomial differentiation for \(2\le n\le150\), checks the classical endpoint calculation on 19,607 abundance vectors, numerically brackets the root and samples the derivative sign for \(3\le n\le250\), and enumerates abundance partitions through total census three. It also compares numerical values at \(n=3\) with the exact radical derived above. The independent variable in the polynomial checks is \(q=1-a\). The universal claims follow from the analytic proof, not the finite checks.

## Relationship to prior work and limitations

He and Legendre (2002), Eq. (1), give the classical random-placement expected-richness formula for fixed individual abundances. Their Table 1 contains the most uneven abundance case, including the \((1,n)\) richness curve for two species. Neither that curve nor the routine terminal derivative calculation is asserted to be new. The contribution is the all-\(n\) interior turning classification of its local exponent and the sharp four-individual onset over all abundance partitions.

Qualitative changes of shape in log–log species–area curves are not claimed as new; see Tjørve et al. (2008) for related work on abundance and spatial distribution. Resultary record `03c33baca66d` examines a different two-species model with independent Poisson processes and can have two turns. Its random census and unbounded area variable do not give the deterministic finite-census result here. Coleman's earlier random-placement paper was not available for a complete statement-level comparison, so historical priority is not certified.

The interior turning count is proved only for the singleton/common family, not for general finite abundance vectors. Spatial clustering, gridded occupancy, finite-size specimens, and other sampling models can produce different conclusions. The theorem does not establish empirical detectability of the turn.

## References

- Coleman, B. D. (1981). *On random placement and species-area relations*. Mathematical Biosciences 54, 191–215. DOI: `10.1016/0025-5564(81)90086-9`.
- He, F. and Legendre, P. (2002). *Species diversity patterns derived from species–area models*. Ecology 83, 1185–1198. DOI: `10.1890/0012-9658(2002)083[1185:SDPDFS]2.0.CO;2`. [Author-hosted full text](https://sites.ualberta.ca/~fhe/He-publications/He_Legendre02.pdf).
- Tjørve, E., Kunin, W. E., Polce, C. and Calf Tjørve, K. M. (2008). *Species–area relationship: separating the effects of species abundance and spatial distribution*. Journal of Ecology 96, 1141–1151. DOI: `10.1111/j.1365-2745.2008.01433.x`.
