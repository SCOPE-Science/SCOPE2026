# Independent mathematical audit

## correctness

PASS

For P~Dirichlet(γ/m)^m the specified singleton, doubleton and joint singleton/doubleton occupancy probabilities are exact beta-Dirichlet moments, giving Cov(A1,A2)=m²p1p2(Q_{m,n}-1) with a strictly positive prefactor. The gamma-ratio factorization isolates Q_infty,n=1+2(1-γ)/[n(n+γ-3)] and a uniform correction -C/m²≤h_n≤C/(mn). For fixed γ∈(0,1), this separates signs outside any fixed-width sqrt(m) critical window; there ∂_n logQ_infty≈-2A/n³ dominates ∂_n h_n=O(1/(mn²)), proving one unique real zero for large m. The uniform expansion yields r_m=sqrt(2(1-γ)m)+(3+2γ)/2+O(m^-1/2), and m logQ→2(1-γ)/c²-1 for n/sqrt(m)→c>0, all γ>0. Independent exact rational composition enumeration matched covariance formula for (m,n,γ)=(3,5,1/2),(4,6,3/4),(5,8,1/2), with covariances -103012/4782969, -48724571223/1644398379008, -28454423356832/1934051513671875. Independent 50-digit real roots for γ=.5 were 12.05034606,33.64158313,102.00621269 at m=100,1000,10000, showing offset toward 2. Finite checks are not the global asymptotic proof.

## originality

PASS

Huillet–Paroissin Theorem 2.1 contains the entire finite-Dirichlet joint species-frequency law; the exact moments and prefactor are therefore derived from known sampling distributions. The new claimed contribution is the large-support sign-change classification, uniqueness of the interpolated crossing, and O(1) correction under n~sqrt(m), which the inspected theorem does not state.

## value

PASS

Identifies a natural, previously unquantified qualitative change in dependence between singletons and doubletons in finite species sampling, with a sharp sqrt(m) critical curve and nontrivial O(1) shift. Such count covariance is directly relevant to diversity estimation and occupancy uncertainty, not a random table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
