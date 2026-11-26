# Independent mathematical audit

## correctness

PASS

The stationary stochastic convolutions converge with bounded diffusivities and positive κ; differences under the same drivers decay at κ. Conditional on the whole telegraph path the coordinates are independent centered Gaussian processes. For t≥s their conditional autocovariances are e^(−κ(t−s))(D̄±δQ_s)/κ with Q the stationary exponential filter of S at rate 2κ. Averaging gives the stated isotropic covariance. The variance of Pθ given S is D̄/κ+(δ/κ)cos(2θ)Q_t. On the diagonals the conditional covariance at every pair of times is deterministic, proving the entire scalar OU law; off them the fourth cumulant is strictly positive. Independently of the density boundary argument, with m_h=E[Q^h] the stationary generator of (Q,S) gives m₁=0 and E[SQ^(h−1)]=m_h=(h−1)m_(h−2)/(h−1+γ/κ) for h≥2, by applying it to Q^h and S Q^(h−1). These compactly supported moments uniquely determine the symmetric beta density with shape ν=γ/(2κ) after mapping Q to (1+Q)/2. In particular m₂=κ/(κ+γ), m₄=3κ²/[(κ+γ)(3κ+γ)]. The Gaussian mixture gives the displayed characteristic function by the even moment series; the fourth, sixth and eighth cumulants are 3 times the variance, 15 times the third cumulant, and 105 times the fourth cumulant of the conditional variance. Thus they have exactly the stated values and signs. Wick's formula gives the positive diagonal square lag from the conditional cross-covariance (δ/κ)e^(−κ|t−s|)Q_min(t,s), while the conditional variances there are constant. This positive covariance of squares at zero linear cross-covariance precludes a joint Gaussian law. Conditional independence of the axis paths gives A(t)=−(δ/κ)^2G(t), G=E[Q_tQ₀]. E[S_tQ₀]=m₂e^(−2γt), and G'=2κ(E[S_tQ₀]−G), G(0)=m₂. Integrating gives the stated two exponentials or the repeated-root linear-times-exponential form; the lag is strictly positive before inserting the minus sign, by convolution with the positive sign correlation. At zero G'=0 and G''=−4κγG, yielding the inverse exactly, including κ=γ. The ordinary covariance fixes κ and D̄; δ² follows from A(0)<0, and relabeling ±S rules out identification of the sign. These are exact population identities, not finite-sample estimates or a formal certification.

## originality

PASS

Supported narrowly for the linked complementary-diffusivity result: exact Gaussian-process projection classification, positive dependence of the squared diagonal processes despite all-lag linear uncorrelatedness, and identification from a different observed cross-square lag on the axes. The exact model class and conditional-normal machinery are prior, and the stationary beta law of the latent filter is already covered exactly by the normalized harmonically confined run-and-tumble model. Novelty is not assigned to those ingredients or to Gaussian marginals hiding higher-order dependence in general.

## value

PASS

The recoverability of switching from low-order observations is the motivating question: all two-time covariances and both complete diagonal laws are indistinguishable from ordinary OU, and even the positive diagonal-square lag only carries the switching rate in an amplitude that also depends on the unknown contrast. The normalized curvature of the negative axis-square lag identifies the rate independently of that unknown amplitude and establishes a sharp failure at zero contrast. This is an exact information separation for natural observables, not a new general mixture theorem, a thermodynamic claim, or a guarantee about derivative estimation from finite data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
