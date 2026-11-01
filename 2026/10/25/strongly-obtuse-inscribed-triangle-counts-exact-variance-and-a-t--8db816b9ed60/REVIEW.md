# Independent mathematical audit

## correctness

PASS

For iid uniform points on unit circle and b=1−α/π strictly between 0 and 1/2, cyclic spacings of one triangle are Dirichlet(1,1,1). The long gap >1−b is unique, giving exact count A_n=Σ_i binom(m_i(b),2) and probability p=3b². Conditioning on a pair at minor normalized gap s gives q(s)=(2b−s)1_{s<b}, hence E q²=14b³/3 and pair-sharing covariance ζ=14b³/3−9b⁴. Distinct triples sharing 0 or 1 vertices have zero covariance, so exact variance =p(1−p)C(n,3)+2ζ C(n,2)C(n−2,2). The first Hoeffding projection vanishes by rotational invariance, and the Fourier eigenvalues of centered second projection are λ_k=b sin(2πkb)/(πk)+(1−cos(2πkb))/(2π²k²). Canonical third-order remainder has O(n³) variance. Pair-sum CLT plus square-summable truncation gives (A−EA)/n² ⇒ Σ λ_k(E_k−1), whose variance ζ/2. λ_1>0 and some large k with sin(2πkb)<0 force a two-sided full R support for every strict b; b=1/2 has nonnegative λ_k only. Independent deterministic sample counts matched direct enumeration at n=7,11 for three b and Fourier partial sums to 25,000 terms matched ζ/2 within 1e-6.

## originality

PASS

Existing bivariate simplicial depth results include the right-angle endpoint α=π/2 and standard degenerate U-statistic methods. The surviving strict α>π/2 law has a different one-parameter geometry: an exact finite covariance, explicit signed Fourier spectrum and full two-sided support, not obtained by complementing the known endpoint. The 2013 polygon paper treats maxima of perimeter/area, not counts of angles crossing a prescribed threshold. Older 1989/2020 endpoint full texts remain a historical-priority risk.

## value

PASS

Counting all strongly obtuse inscribed triangles is a natural dependent geometric U-statistic for cyclic samples. Exact finite variance, an explicit complete infinite eigenvalue spectrum and a sharp all-strict-cutoff support dichotomy are substantive structure absent from the single-triple probability. The 120° exact rational special case is a motivated benchmark, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
