# Independent mathematical audit

## correctness

PASS

For m=∫F finite and R₀=∫A>1 the constant equilibrium and exact perturbation equation yield H=A/R₀−(R₀−1)F/m and Δ=1−Ĥ. For σ≥0, g=e^(−σa)F is integrable, decreasing and distributionally convex since F′=−K is nondecreasing. Both g and its right derivative tend to zero at infinity, so g(a)=∫(u−a)_+dg′(u). Tonelli gives ∫u² dg′(u)=2∫g<∞, justifying the cosine transform identity with nonnegative integrand (1−cos(ωu))/ω² after integration. The normalized positive A term has real part strictly less than one except at z=0: for σ>0 the maximal weight is attained only at a=0, and for nonzero ω on the axis it is attained only on a null set. At z=0, Δ=R₀−1>0. This establishes strict positivity of the determinant's real part throughout the claimed half-plane. With an exponential moment, monotonicity bounds e^(ηa)F(a) for a≥1 by e^η∫_(a−1)^a e^(ηs)F(s)ds; thus A=βF also has an exponential moment. For bounded real parts the exponentially weighted kernels range over a compact L¹ set, so Riemann–Lebesgue decay is uniform there; large positive real parts give small transform directly by domination. Compactness on the remaining bounded rectangle extends nonvanishing to Re z≥−δ for a sufficiently small δ>0. The weighted causal Wiener criterion then gives an inverse identity plus an L¹(e^(δa)da) resolvent. Splitting at t=0, each G in {H,F,A} contributes a past forcing bounded in weighted sup norm by ||G||_(1,δ)||history||_∞. Causal convolutions have the same operator bound on future perturbations, and the weighted norm of a product is at most the product of weighted norms. The resulting resolvent fixed-point map on a ball of radius proportional to the history size is a contraction for small compatible histories; it gives exponential incidence decay. No decay of the entire past in the unweighted history norm is asserted. The uniform-duration illustration is Uniform[0,T], as confirmed by the supplied cosine check, not a uniform distribution starting at a positive age.

## originality

PASS

The closest inspected paper has the identical renewal model and determinant, but its checked analysis does not state this profile-uniform sufficient condition. Earlier constant-transmission results give stronger convergence for a special model, not this quantifier. The Fourier positivity argument for decreasing convex integrable kernels and the causal resolvent method are classical techniques; the supported contribution is the exact application to the endemic determinant for every admissible nonnegative age profile, and the local incidence consequence with light tails. Unavailable sources are reported as limits, not negative evidence.

## value

PASS

A single test on the shape of the survival law replaces a separate search for characteristic roots for each admissible age profile. It gives an analytic boundary for classical endemic Hopf behavior in the same model studied via specific bifurcation examples, and separates the root exclusion from the stronger incidence convergence available only with a tail hypothesis. This usefulness does not depend on a new Fourier or Wiener theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
