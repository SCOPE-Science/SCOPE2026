# Independent mathematical audit

## correctness

PASS

Independently expanded the exact polynomial using a+b=−√3 and ab=−3(1+√3)/2. The residual after subtracting A(z−aμ)²(z−bμ)² from Kz⁴−(z−μ)⁴ is (10+6√3)μ³(z−μ), which integrates to zero. Equality for nonzero f requires μ≠0 and the two root values, with the mean forcing mass α=(a−1)/(a−b) on the b root; the reverse construction works. For a normalized input, nearest-root error e satisfies E|e|⁴≤D/A and E|e|²≤4D/(Ad²μ²) when μ≠0. The mean of e is dμ(t−α), where t is the measurable selected-root mass, so D≥Ad⁴μ⁴δ²/4. If D<A/16, the triangle inequality forces |μ|>1/(2M); otherwise δ≤α supplies the other lower-bound branch, including zero mean. For the upper bound shift both roots by d(t−α) to give mean one and denominator E|g|⁴≥1; the exact squared remainder is bounded by Ad⁴(1+|t−α|)²|t−α|². Approximate the infimum over t to get C*. The separate numerical arithmetic gives c=0.07659598858 and C*=502.99071645. The two-atom formula was also reconstructed: the centered output is (x−y)(1−p,−p), and the weighted dual fourth power of the difference functional is (p^(−1/3)+(1−p)^(−1/3))³, yielding the stated two-atom check and the quadratic sharp order near α. For uniform n the grid of event masses and the polynomial for α give the claimed finite gap; for a rational root the cleared polynomial forces 3 to divide the denominator, after which the leading term alone has 3-adic valuation three. These are arbitrary-space estimates, including the trivial space, not inferences from sampling. The two norm/equality criteria are correct; they need not be interpreted as suggesting a space with δ=0 but no α event: the range of a probability measure is compact by separating its countable atoms from the divisible nonatomic part (a compact subset-sum set plus a closed interval). Algebra is replayable from RESULT.md lines 37–75; the supplied verify.py was inspected but not run.

## originality

PASS

Pass for the dimension-free, two-sided quantitative deficit across arbitrary probability spaces. Credit the unrestricted sharp constant, Bernoulli model, and exact norms in known finite-uniform cases. No verified stronger statement supplies the weighted-arbitrary-space quadratic gap or its explicit uniform constants. The exact remainder is a mechanism for the estimate; this is not a separate priority ruling for every ingredient or for unrestricted extremizers.

## value

PASS

The estimate turns the unobtainability of a particular Bernoulli mass into a quantitative loss in the operator norm on an arbitrary fixed space. It gives the matching exponent in both directions, applies to nonuniform measures without dimension assumptions, and explains arithmetic gaps for uniform finite spaces. The usefulness is in the fixed-measure stability theorem, not a new calculation of the known unrestricted constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
