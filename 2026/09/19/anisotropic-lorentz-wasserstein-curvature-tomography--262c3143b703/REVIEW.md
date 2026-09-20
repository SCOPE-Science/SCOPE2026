# Review — Anisotropic Lorentz–Wasserstein curvature tomography

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The main expansion is a direct consequence of the two uniform endpoint estimates in Braun--Li, but with the isotropic averaging step removed.

For the lower bound, the source and target laws are defined from the same probability measure on the transverse unit ball and related by parallel transport. The identity coupling in transverse coordinates is therefore an exact coupling of the two prescribed marginals. Its transverse displacement is zero, so it satisfies the hypothesis of Braun--Li's lower time-separation estimate. Integrating gives the second-order term \(-\frac12\delta\varepsilon^2 a_{ij}M_\mu^{ij}\).

For the upper bound, Braun--Li's uniform time-separation estimate applies to arbitrary pairs of points in the two transverse balls under \(\varepsilon=o(\delta^{5/2})\). The nonpositive displacement term can be discarded. What remains at second order depends only on the first endpoint. Hence integration against any coupling depends only on its first marginal and gives exactly the same contraction \(a_{ij}M_\mu^{ij}\). The error terms are uniform in the endpoints and therefore remain uniform after integration against an arbitrary probability law. Supremizing over chronological couplings produces the matching upper bound.

No density, symmetry, centering, or smoothness of \(\mu\) is used. Atomic two-point laws are legitimate because the Lorentz--Wasserstein definition only requires probability marginals and, for sufficiently small parameters in the stated regime, the two compact supports are uniformly chronologically ordered.

The fixed-direction tomography formula was checked by polarization: probes along \(e_i\) give \(a_{ii}\), while probes along \((e_i+e_j)/\sqrt2\) give \((a_{ii}+2a_{ij}+a_{jj})/2\). There are \(n(n+1)/2\) entries, equal to the dimension of \(\operatorname{Sym}(n)\).

For the full-tensor statement, rank-one probe data provide \(R(u,v,v,u)\) for every timelike-spacelike orthogonal pair, up to the fixed sign convention. If the difference of two algebraic curvature tensors has all these measurements zero, then for timelike \(v\) it has \(S(z,v,v,z)=0\) for arbitrary \(z\), since the component of \(z\) parallel to \(v\) drops out. Polynomial continuation in \(v\) makes this identity valid for every \(v\), and the standard polarization of sectional curvature gives \(S=0\). Thus the probe functionals span the dual of the algebraic-curvature-tensor space, whose dimension is \(m^2(m^2-1)/12\); a basis-sized finite subfamily exists and no smaller family of scalar linear measurements can be injective on that vector space.

Consistency checks against the isotropic unit-ball moment \(I/(n+2)\), flat spacetime, constant sectional curvature, and random symmetric-matrix polarization all agree with the formulas.

## Originality

The primary source arXiv:2609.18664 was inspected at its Fermi expansion, its Euclidean-ball second-moment contraction, and the lower and upper time-separation estimates used in the proof. Braun--Li explicitly show that the isotropic ball average converts \(a_{ij}w^iw^j\) into \(\operatorname{Ric}(v,v)\), but their stated coarse-curvature theorem uses the weighted/uniform spacelike-ball law. Their paper does not state the arbitrary matched-law contraction, rank-one sectional-curvature recovery, finite tidal-operator tomography, or full Riemann-tensor tomography.

The closest independent Lorentzian construction found is Barton--Borza--Roehrig, arXiv:2606.04910. Their continuum proof likewise contains a pointwise curvature quadratic form before integration, but their probability measures are symmetric causal-diamond measures and their continuum/discrete curvature results recover Ricci curvature. No tensor-tomography statement was located.

A broader neighboring result is Ketterer--Mondino, arXiv:1610.03339 / Adv. Math. 329 (2018), which characterizes Riemannian sectional and intermediate Ricci curvature bounds using entropy along Wasserstein geodesics. That is a different transport observable and does not cover the present Lorentzian Ollivier-type matched-slice expansion.

Targeted literature searches using “Lorentz-Wasserstein” together with “anisotropic”, “second moment”, “sectional curvature”, “Jacobi operator”, “tidal curvature”, “Riemann tensor”, and “tomography”, as well as analogous searches with “Ollivier-Ricci”, did not locate the stated theorem or its finite reconstruction consequences. The current SCOPE archive was searched directly by timelike, Lorentz--Wasserstein, Ollivier--Ricci, curvature-tensor, Jacobi/tidal, and sectional-curvature terminology and showed no overlap.

The main residual originality risk is that both Lorentzian Ollivier--Ricci papers are recent and their proofs already expose the unaveraged curvature quadratic form; an unindexed note or an unstated observation by the authors could therefore contain a closely related anisotropic consequence. Originality is only to the best of our knowledge.

## Value

The result changes the information content of the new timelike Ollivier--Ricci construction. With an isotropic transverse law the observable sees only the trace \(\operatorname{Ric}(v,v)\); with a controlled anisotropic law the same observable becomes a linear sensor for the complete tidal operator \(A_v\). A concrete set of \(n(n+1)/2\) two-point probes recovers that operator exactly at leading order.

Varying the timelike direction upgrades the construction further: the resulting timelike sectional-curvature measurements separate algebraic curvature tensors, so a finite linearly minimal set of \(m^2(m^2-1)/12\) scalar probe limits determines the entire Riemann tensor at a point. In four-dimensional spacetime this number is 20. This supplies a direct curvature-tomography interpretation of Lorentz--Wasserstein measurements rather than only a Ricci estimator.

## Limitations

The theorem is local and asymptotic, and it inherits the restrictive scale condition \(\varepsilon=o(\delta^{5/2})\) from the presently available uniform upper estimate. It does not establish a discrete causal-set anisotropic estimator or its convergence, nor does it analyze statistical noise, finite-scale bias, or numerical conditioning. The full-curvature finite family is existential rather than an optimized canonical design. Individual rank-one probes reduce at leading order to the classical sectional-curvature term in the second variation of time separation; the substantive contribution is the arbitrary matched-law Lorentz--Wasserstein contraction and its transport-tomography synthesis. Recent parallel work remains a meaningful originality risk.
