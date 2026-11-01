# Independent mathematical audit

## correctness

PASS

Re-derived one-step M(s) directly from source Eq. (26) in scaled momentum-position coordinates; verified det M=1 by exact identity A²+BC=4D², and independently factored tr(M(t)M(s))±2 with multivariate exact polynomial arithmetic. In the open square (0,sqrt(8))², Q=s²t²−8(s+t)²+192>0 by negative partial derivatives and zero corner limit, so trace<2. The sign of Δ=F(s,t)F(t,s) is therefore equivalent to strict elliptic/hyperbolic 2x2 symplectic classification. Boundary trace −2 has Jordan growth except P=−I; monotonic positive off-diagonal magnitude ratio enforces s=t=s0. Substituting st=4 makes both F factors negative. Antisymmetric expansion near s0 gives tr P=−2−gamma²δ²+O(δ^4) and log spectral radius=gamma|δ|+O(|δ|³). Checked rational stable/unstable witnesses and exact identities; proof handles all continuous parameters.

## originality

PASS

Dubois and Rojas-Quintero provide precisely the one-step Simpson map, symplecticity and step-dependent conserved energy, but their inspected source does not analyze composing distinct steps. Skeel documents variable-step instability for another method (Verlet), which establishes the phenomenon generally without this Simpson-specific exact two-period polynomial diagram and resonance coefficient. Closest 2024 quadratic-Lagrangian followup describes implicit integration, not the same explicit canonical two-step product. Qualified originality; possible specialized older Floquet calculation.

## value

PASS

Alternating individually stable symplectic time steps can become hyperbolically unstable. The exact phase region, neutral Jordan versus semisimple boundaries, protected reciprocal-step curve and sharp first-order resonance law provide a nontrivial parameter-selection/stability result for a named integrator beyond conventional fixed-step analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
