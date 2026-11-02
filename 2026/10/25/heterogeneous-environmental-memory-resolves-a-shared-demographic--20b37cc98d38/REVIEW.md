# Independent mathematical audit

## correctness

PASS

Eliminating E_i yields stable AR2 with coefficients s_i=λ+α_i and t_i=λα_i. Yule–Walker gives r_i=γ_i(1)/γ_i(0)=s_i/(1+t_i), q_i=γ_i(2)/γ_i(0)=s_i r_i-t_i. Inverting t_i=(r_i²−q_i)/(1−r_i²), s_i=r_i(1+t_i) recovers unordered poles including double roots. Distinct α1 and α2 make the intersection singleton {λ}. The exact variance γ_i(0)=σ_i²(1+λα_i)/[(1−λ²)(1−α_i²)(1−λα_i)] and cross C=τ(1−λ²α1α2)/[(1−α1α2)(1−λ²)(1−λα1)(1−λα2)] recover all covariance parameters, with denominators positive. With equal α, commuting linear filters make an exact full-law swap, even with cross correlation. For insufficient lag0,1+C data, perturb λ and solve α_i=(r_i−λ)/(1−r_i λ) while continuously resetting variances/τ, retaining Σ positive definite locally. Independent rational inversions and 250-term causal impulse convolution confirmed both cross and autocovariance identities; this finite check is not the proof.

## originality

PASS

AR2 pole recovery and pole-order exchangeability are classical; the 2015 enhanced Moran-effect study covers spatially varying environmental autocorrelation in population synchrony. The submitted theorem instead characterizes full structural parameter identification by intersecting two site-specific pole multisets and determines a lag-minimal moment set and all-lag obstruction. No prior exact theorem for this named combination was identified, but the classical algebra may be repackaged in systems-identification terminology.

## value

PASS

Disentangling demographic persistence from autocorrelated environmental forcing is a motivated ecological inference problem. The theorem supplies an exact observational sufficiency/impossibility dichotomy, including equal-colour nonidentifiability even with all-time data, and a sharp limited moment measurement protocol. Although the inversion uses classical AR2 algebra, the contrast between two heterogeneous sites and same-colour sites is a concrete useful structural boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
