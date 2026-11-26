# Independent mathematical audit

## correctness

PASS

The complete corrected RESULT.md under repairs/4 gives the formulas for fixed d≥3. The coprime generators a and da+b ensure cofiniteness and the least positive generator is a. Vandermonde bounds the total represented binomial value by the binomial at the total index cost, proving the lower bound c_d n^(1/d). To check the upper bound independently, if k is the largest admissible index, the bounds for the binomial product put c_d n^(1/d) in [k−d+1,k+1). Pascal's identity bounds the remainder r by O_d((n+1)^((d−1)/d)), with r<n. Since (r+1)^(1/d)/(n+1)^(1/d)≤1/2 for all sufficiently large n, strong induction first gives a global bound A_d(n+1)^(1/d) (cover bounded n by the unit coin). Applying that bound only to the first remainder gives O_d((n+1)^η_d), including n=0. In residue br the binomial value has form r+ja with j≥0, by coprimality and nonnegativity; index below d only adds multiples of a. The least residue element is br+a times the index-cost envelope above br, i.e. w_r=br+a min_j(μ_d(r+ja)+bj). Every j gives the same required lower bound and j=0 gives the upper bound uniformly in b, whether or not it minimizes. Counting individual residue gaps gives the Apéry max-minus-a and sum identities. Taking r=a−1 for the lower maximum and bounding monotonically for the upper, and using integral comparison for the genus sum, gives both constants and O_d(a^(1+η_d)); all estimates include a≥2 and the residue r=0. The frozen script was inspected (it tests finite residue minima), not executed.

## originality

PASS

The original's assertion of a new quadratic refinement is not passed: the precise degree-two powers and coefficients already follow from Hashuga–Herbine–Jensen's bounds and exact Apéry formulas. The repaired contribution is the uniform expansion for every fixed d≥3. The closest general coin, Apéry, and binomial Frobenius results inspected do not supply this higher-degree mixed-family statement.

## value

PASS

For higher degrees the quantitative binomial cost estimate and control of every residue lift establish explicit leading constants for two natural semigroup invariants, extending the quadratic problem and remaining informative after subtraction even when b grows without bound. This is not a new claim about the covered quadratic case or a table of small semigroups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
