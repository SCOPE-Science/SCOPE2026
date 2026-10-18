# Independent mathematical audit

## correctness

PASS

For fixed even s≥4, γ in (d_s,δ_*), positivity of source spectral r_A^(m)(γ) gives a chain α_0,...,α_m with α_i≥d_s for i≥2 and all preceding α_i < u=(1−q)/2, q=(2^(s(1/s−h₂(γ)))−1)^(1/s). The cited Fagnani–Ravazzi transition inequality gives at most −η per middle transition with η=−d_s/2 log₂(1−q²)>0, while r_A^(2)≤1 and the final transition≤0. Thus r_A^(m)(γ)≤1−(m−3)η; m≥4+floor(1/η) contradicts r_A>0. Taylor expansion yields M_s(δ_*−Δ)∼(2 ln2/d_s)[s ln((1−δ_*)/δ_*)]^(−2/s) Δ^(−2/s). This is a sufficient round bound, not an optimum. Numeric checker only corroborates constants, not for-all-s proof. Critical source maximizing-chain hypothesis was quoted in source package but the full preprint could not be independently inspected in this execution; this reliance remains explicit.

## originality

PASS

Best-of-knowledge PASS, with a significant primary-access risk: Zhang arXiv:2610.01277 already proves qualitative convergence to the CSS GV target using a uniform negative transition gap; its accessible abstract does not assert an explicit dependence of accumulation rounds on Δ. The closed sufficient M_s and asymptotic Δ^(−2/s) dependence are a quantitative output, not merely changing symbols. Source Proposition 4.5 could contain a sharper explicit bound; its full text was not retrieved, so priority remains conditional on that comparison.

## value

PASS

PASS: the source poses qualitative threshold convergence but encoder size depends linearly on accumulation rounds; converting a target distance gap into explicit logarithmic-depth and linear-gate constants addresses a concrete resource question. The result does not purport to optimize required rounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
