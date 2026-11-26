# Independent mathematical audit

## correctness

PASS

Zero infected mobility preserves each infection-coordinate support, and nonnegative solutions are bounded by the conserved mass. At equilibrium all infection fluxes vanish separately; connected susceptible diffusion then gives S=s·1, so every positive infected cell has risk s and the remaining mass is N−ks. Differentiating V=½∑S_j²+∑r_vI_v gives the negative sum of the graph energy and ∑β_v I_v(S_j−r_v)²; the zero set consists exactly of equilibria. LaSalle and the strictly ordered equilibrium values F(r)=Nr−kr²/2 on r≤N/k give approach to a single admissible risk level. At a higher limit, a positive minimum-risk seed would eventually grow at a strictly positive uniform per-capita rate, contradicting bounded mass. In off-risk, susceptible, tied-risk order the Jacobian has diagonal blocks diag(β_v(r−r_v)), M, and 0. Connectedness and positive endemic mass make M negative definite. The full kernel is freely supported on the tied infected coordinates and has dimension equal to the algebraic zero multiplicity; intersecting with the mass tangent removes exactly one such direction and preserves all nonzero eigenvalues. A small feasible perturbation seeding an absent lower-risk cell selects its lower stratum and confirms instability on the actual simplex. At c≤r_min, V−V(E₀) has a strict minimum on the mass simplex, including equality c=r_min, so attraction also gives Lyapunov stability. The claim for multiple equal minimum-risk seeds is convergence in distance to a face, not convergence of the individual shares. The frozen exact two-patch checker was inspected rather than run; its finite cases do not establish the all-graph argument.

## originality

PASS

The distinct result supported by the comparison is the exact two-strain, zero-infected-mobility finite-patch classification: all risk-tied simplices, full-trajectory seeded-face selection and the full mass-tangent spectrum. The qualitative selection mechanism has a significant single-strain PDE precedent and is not credited as new in general.

## value

PASS

At the exact zero-mobility boundary, accessibility and stability change qualitatively: a lower-risk but unseeded coordinate can give an unstable invasion mode without defeating the higher-risk state within its invariant support. Linking all equilibrium compositions and their tangent spectra to global selection for every feasible initial condition resolves a substantive regime left open in the initiating model and deals explicitly with ties and the nonhyperbolic extinction threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
