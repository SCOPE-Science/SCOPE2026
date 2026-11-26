# Independent mathematical audit

## correctness

PASS

Checked the exact continuous affine projector and all asymptotic claims. Centering the last coordinate diagonalizes the affine moment Gram matrix: the tangential variances are 1/d, and the last variance is v_d/d with v_d=1−d m_d²>0; the beta law of Y_d² gives the stated gamma-function mean. The resulting kernel row has norm equal to its absolute integral (test the row sign), and continuity plus full support allow the supremum over all locations, including the boundary. The normalized Gaussian representation yields the joint tangential/axial limit (G₁,|G₂|) a.s. and in L¹ by the uniform second moments. The coefficients of the kernel row divided by sqrt(d) converge uniformly in latitude, so the absolute-expectation convergence is uniform. For monotonicity, for Y=|G₂|−μ, differentiate H(r)=E|G₁+rY| to get H−rH′=μ A(r) and H′/μ=∫₀ʳ E[Y² exp(−s²Y²/2)]ds. With C=v−E[Y⁴]/6, the polynomial C−2v² is increasing for 7/11<μ²<2/3 and is 5/363 at the lower endpoint. On 0<r≤1 the exponential lower bound yields H′/μ≥rC; on r≥1 it gives H′/μ≥C, while the density of Y is at most μ and hence A(r)≤2/r. Both ranges give H′>μv²rA. Under r=t/(v sqrt(1−t²)) this is exactly vF′(t)>0. Endpoint continuity gives the unique limiting maximum; the centered-half-normal positive tail gives the pole constant, numerically 1.32815206218154 by an independent scalar quadrature. Uniform convergence and the strict gap away from t=1 prove both directions of the near-norming classification. The packaged script was inspected, not executed.

## originality

PASS

The supported distinct claim is the uniform high-dimensional profile for the exact continuous affine projector with normalized hemispherical surface measure, including its strict limiting latitude order, sharp constant, and characterization of all near-norming locations. The closest inspected same-domain result is a fixed-dimension exact calculation, while the closest high-dimensional indexed analogue uses the positive orthant. The primary full-sphere and weighted-ball hyperinterpolation results concern a different limit and operator. None of these inspected results yields the stated half-normal profile and its monotonicity.

## value

PASS

The Lebesgue constant measures amplification by a concrete affine fit, and symmetry alone no longer makes evaluation rows equivalent on a hemisphere. The uniform profile identifies both the sharp growth constant and where arbitrarily nearly worst amplification can occur. Distinguishing asymptotic polar localization from fixed-dimensional maximizing locations is substantive, particularly given the exact equatorial result in dimension three.

The dated certificate retains the supplied scientific assessment, sources and limitations.
