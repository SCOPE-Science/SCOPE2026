# Independent mathematical audit

## correctness

PASS

For C_m=union of q_j=y²+xz+jx², m>=2, each q_j is irreducible smooth and distinct. A projective stabilizer must permute components, hence preserve the conic pencil <q_0,x²>. The rank-one member x² is its unique singular pencil element, forcing x_prime=a*x. Write y_prime=b*x+c*y,z_prime=e*x+f*y+g*z; requiring q_0 pullback in pencil gives c²=ag and af+2bc=0, so the induced parameter map on j is affine. Any affine permutation of {1,...,m} has slope ±1 by preserving nonzero centered second moment, hence identity or reflection. Normalizing a=1 and solving c²=±1 yields exactly U_t R_m^k, k=0..3. Independent SymPy substitution verified q_j(U_t)=q_j, q_j(R_m)=-q_(m+1-j), R^4=1, R U_t R^-1=U_(it), and the infinitesimal syzygy x∂_yQ-2y∂_zQ=0. All m>=2 follows symbolically rather than finite experiments.

## originality

PASS

Pokora 2024 Example 4.2 already uses exactly Q_m and states its freeness and mdr(Q_m)=1; those facts do not give the full projective stabilizer, the nonreductive one-parameter subgroup, component reflection and lifted order-four extension. Cheltsov treats even Płoski curves in GIT/stability context without the submitted group description on inspected material. Related published projective-stabilizer results concern other arrangements. Best-of-knowledge PASS with terminology and special-curve isotropy risks.

## value

PASS

The full projective stabilizer is a natural structural invariant of a named family of free plane curves. Proving Ga⋊μ4 distinguishes continuous shear symmetries from a finite reflection lift, and exhibits a geometric explanation for a known Jacobian syzygy. This is a complete all-m classification of actual projective symmetries, not just a negative computer test or routine reassignment of a numerical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
