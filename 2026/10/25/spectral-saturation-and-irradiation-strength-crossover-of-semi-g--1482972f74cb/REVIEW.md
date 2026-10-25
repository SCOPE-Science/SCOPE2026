# Scientific review: spectral saturation of planetary inversion depth

## Correctness — PASS

The mathematical statement concerns the precisely normalized multiband extension of the constant-thermal-opacity Eddington profile, not arbitrary radiative transfer. Differentiating the stated temperature formula gives \(4(T_s^4)'=3T_{\mathrm{int}}^4+s(Q-P)\) without a missing coefficient. In the ratio \(P/(B/s+Q)\), every exponent in the numerator is strictly greater than \(\sqrt3\) and every nonconstant exponent in the denominator is smaller. Its strict decay proves the unique-root and sign-transition theorem at all permissible finite band counts. The positive region of \(P-Q\) has strictly negative derivative, supporting the intensity monotonicity and linear onset. Distinct rate ordering makes the mixed-band zero \(P=Q\) transverse, validating the finite saturation depth and first-order correction; absence of a low band gives the leading smallest-high-rate exponential and logarithmic law. Direct substitution gives the exact two-band crossover, and its endpoint expansions follow by monotone inversion. Conditions \(T_{\mathrm{int}}>0\), positive weights, fixed opacities and \(s>s_c\) are essential and are retained throughout.

The included `check.py` ran successfully from this package's source, with 5,000 derivative comparisons, 3,000 randomized shape classifications and 1,000 two-band crossover comparisons. Those finite checks are consistency evidence, not the proof of universal claims.

## Originality — PASS, with residual historical-priority risk

Guillot (2010, Equation 27) already supplies the one-visible-band profile. Parmentier and Guillot (2013, Section 3.8 and Equation 98) already explicitly supply linear superposition for multiple visible bands. Tokarev (2011, Theorem 7) already covers the general one-zero bound for sign-separated Laplace transforms. None of these three ingredients is claimed to be original in isolation. Heng et al. (2011) derive different cloud/scattering corrections and inversion conditions, not the same fixed-thermal-opacity spectral scaling problem.

The particular contribution assessed here is the **joint, sharp radiation-intensity phase diagram for minimum depth**, the dichotomy between finite strong-irradiation saturation and logarithmic deepening, the quantitative leading corrections, and the exact weak-transparent-band crossover equation. The inspected source sections did not state that combined profile-location classification. Published broad zero-count statements directly imply the uniqueness ingredient, not by themselves the location asymptotics or band-weight crossover. Specialized literature and broader algebraic comparisons could still contain equivalent consequences; this has not been independently excluded. No originality assertion rests solely on the absence of keyword matches.

## Mathematical value — PASS

The source spectral model is used to interpret physically meaningful hot-Jupiter thermal inversions. A sharp diagnostic is useful: changing only stellar absorption-band multiplicities and overall flux cannot create several temperature extrema under the shared grey thermal closure. More importantly, a deep-penetrating visible band, even one with small but nonzero flux weight, changes the strong-irradiation scaling of inversion depth from unbounded logarithmic growth to finite saturation. The crossover law quantifies precisely when the weak band becomes dynamically important. The result is a natural parameter classification of an established radiative-transfer approximation, rather than an arbitrary numerical example, and provides a limiting benchmark for broader atmosphere models.

## Closest sources, assumptions and risks

- Guillot (2010), arXiv:1006.4702v1, Section 2.4 and Equation 27: original single-beam temperature formula and inversion mechanism.
- Parmentier and Guillot (2013), arXiv:1311.6597v1, Section 3.8 and Equation 98: already-known arbitrary visible-band superposition, but with additional non-grey thermal behavior.
- Heng et al. (2011), arXiv:1107.1390, abstract and Sections 1–2: cloud/haze, scattering and collision-induced absorption modify inversion conditions.
- Tokarev (2011), DOI:10.1017/S144678871100156X, Theorem 7/Remark 8: existing general one-zero Laplace-transform principle.

The proof does not cover spectral weights dependent on irradiation, feedback of atmospheric chemistry on opacities, multiple infrared thermal opacities, clouds or transport. No observational or independent validation is claimed. Exact historical priority, including possible implications of general exponential-polynomial results, remains open to external comparison.

Self-review: passed. Independent audit: not yet performed.
