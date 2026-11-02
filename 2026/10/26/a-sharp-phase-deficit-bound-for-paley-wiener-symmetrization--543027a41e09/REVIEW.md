# Independent mathematical audit

## correctness

PASS

For W interval of length B, 0<BT<1 and centered I_T, the Fourier quadratic-form identity (Baeza–Guasch Lemma 2.1) gives a phase-deficit double integral with nonnegative factor |fhat(w)||fhat(e)|−Re[fhat(w) conjugate(fhat(e))]. The sinc kernel K_T(x)=T sinc(pi T x) is decreasing and >=T sinc(pi BT)>0 for |x|<=B. Thus concentration gain >=T sinc(pi BT)(||fhat||_1^2−|f(0)|^2). Opposite-phase packets of width epsilon at the two spectral ends have f(0)=0 and ratio tending to K_T(B), proving *sharp* uniform coefficient without finite equality attainment. The phase-distance inequality follows from inf_{|zeta|=1} ∫|fhat||u−zeta|²=2(A−|f(0)|) and A²−|f(0)|²>=A(A−|f(0)|). Independently verified algebra and packet limit. No claim at BT=1.

## originality

PASS

Best-of-knowledge PASS with close prior ingredients: Baeza–Guasch (2023/2026), Lemma 2.1 and Theorem 2.2 already establish exact fixed-modulus quadratic representation and qualitative nonnegative concentration difference. The inspected paper does not state the quantitative sharp lower constant tied to the central peak loss, or the weighted phase-distance inequality. Zelent 2026 studies global PSWF/observation-set stability and has different normalization and comparison objects. The new sharp coefficient is a short natural corollary of the old kernel identity, so originality is narrow; earlier implicit equivalent corollary is a real risk.

## value

PASS

A **sharp** quantitative stability modulus for constant spectral phase at fixed Fourier amplitude is a natural signal-concentration invariant, stronger than the original qualitative symmetrization inequality. It controls weighted Fourier-phase misalignment and is exact at every strict subcritical time–bandwidth pair, rather than being an arbitrary numerical inequality. The proof is elementary given the known kernel but identifies an optimal stability constant not present in inspected results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
