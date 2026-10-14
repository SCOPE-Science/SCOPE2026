# Independent mathematical audit

## correctness

PASS

Reconstructed gamma=0 coefficients directly from Exner–Pekař Sec. IV end/Appendix A: P6=72ℓ^6(c−1)² sin(kl1)sin(kl2)sin(kl3), P4=12ℓ^4(c−1)(c+1)B4, Pc=−16ℓ²(c+1)[3k²ℓ²(c−1)−(c+1)](sin(kl2)+sin(kl3)), with c=cos(πt/3). On t_m√m→τ and k=k_m+x/m, c−1=−π²τ²/(18m)+o(1/m), sin(kl1)=εl1x/m+O(m^-3), B4(k_m)=4ε sin(a_m+b_m). Dividing the exact secular equation by m³ gives an affine x-equation proportional to [π⁴ℓ²τ²/(24l1)] εx sin a sin b−ε sin(a+b)+(sin a+sin b)cosθ; k²P2 and k² sinθ Ps are lower order, uniformly in θ on bounded x. Nonresonance sin a sin b≠0 makes the derivative nonzero, yielding a unique local root and uniform x_m→x∞. Since (k_m+x/m)²−k_m²→2πx/l1, the asserted translated energy profile and limiting width W∞=96/(π³ℓ²τ²)| (sin a+sin b)/(sin a sin b)| follow. Independently checked leading coefficient ratios in SymPy and evaluated exact secular equations for m=121,241,481, finding widths 3.3045673,3.4660149,3.5541772 tending toward 3.64808465. Finite computations support, not establish, the asymptotic proof.

## originality

PASS

The source obtains high-energy widths at fixed nonzero interpolation t and analyzes t=0 separately; neither gives a uniform theorem in the joint t_m≈m^-1/2 and k≈mπ/l1 limit. The new finite nonzero translated-energy band profile is a distinct singular boundary-layer limit, not a trivial substitution into a fixed-parameter O-term. A 2018 paper concerns a different square-lattice graph.

## value

PASS

An explicit nonzero finite-width crossover regime of the genuine periodic chain-graph Bloch spectrum is a natural spectral boundary-layer question: it connects shrinking fixed-t bands to the Kirchhoff endpoint through a critical m^-1/2 interpolation and yields the full phase-dependent limiting energy band, not just a numerical width. The result isolates the nonresonance boundary and provides an analytically usable band profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
