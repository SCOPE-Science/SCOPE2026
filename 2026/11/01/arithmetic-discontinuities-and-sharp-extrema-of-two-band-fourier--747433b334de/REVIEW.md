# Independent mathematical audit

## correctness

PASS

The normalized measure and the even absolute value give 1/π on the positive half-period. Factoring the polynomial and replacing (2 sin(t/2))⁻¹ by t⁻¹ on [1/N,π] change the norm by O(1), as does discarding t≤1/N. After u=Nt the difference between m_N/N and fixed α changes the numerator by at most 2u/N, hence its weighted integral also by O(1). The Cesàro mean M of F_α(u)=4|sin(u/2)cos(αu/2)| exists (irrational continuous torus flow, or rational periodicity). For G(R)=∫₀ᴿ(F_α−M)=o(R), integration by parts gives G(R)/R and ∫₁ᴿG(u)/u²=o(log R) by an ε-bound on the tail, proving C=M/π without a Diophantine or uniform rate. The torus product gives 16/π³; absolute cosine-series convergence lets one average termwise, and the resonances n=pℓ, m=qℓ with mean cos²=1/2 give exactly the factor 2 and sign (−1)^(qℓ) in the series. For even q each positive summand is strictly dominated by its (3,2) counterpart unless (p,q)=(3,2); for odd q the positive alternating deficit is less than 1/105 away from (2,1), whose deficit exceeds 1/45−1/945. This gives uniqueness against the generic irrational value as well. Substitution x=cos v gives ∫₀^π|sin v cos 2v|dv=(4√2−2)/3. For (3,2), use symmetry about π/2, split at π/6 on the first half, and use primitive cos(v)/2−cos(5v)/10; this gives (6√3−4)/5. The multiplier 4/π² produces both claimed closed forms. Rational corrections have magnitude O(q⁻⁴), so they vanish along rational approximations to an irrational, and the dense irrational values witness a discontinuity at each rational. Scope is exactly fixed slopes, equal unit-weight blocks and continuous normalized circle measure; the passage saying ‘positive-frequency’ includes frequency zero by the explicit polynomial and has no mathematical effect.

## originality

PASS

General truncated Fourier-transform norm estimates and almost-periodic jump means already give the method and, after recentering the two bands, the existence and implicit mean formula. The distinct supported result is the explicit arithmetic evaluation for every slope, its nonzero parity corrections and continuity classification, and the exact unique global extrema. Related two-aperture singular-value constants have a genuinely different averaging problem and parity, not an equivalent arithmetic law.

## value

PASS

The equal two-band family is a natural first departure from the classical single block and has only one normalized separation parameter. The explicit law shows exactly when separating the bands changes the leading constant, how the sign and decay depend on reduced arithmetic data, and where the two extreme projection costs occur over a continuum of slopes. It is a complete comparison in this family, not merely another use of an almost-periodic existence theorem or a finite numerical census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
