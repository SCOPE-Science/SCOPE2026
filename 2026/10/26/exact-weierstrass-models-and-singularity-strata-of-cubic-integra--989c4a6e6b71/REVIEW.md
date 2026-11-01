# Independent mathematical audit

## correctness

PASS

Gamma ratios for monomial fractional integrals yield the cubic order polynomial after removing x^alpha and rescaling. In homogeneous [T:X:W], the inverse change W=(V+a1 U+3a0 Z)/(4a0) is defined for all projective points because a0!=0, and exact symbolic substitution gives 8a0 F=V²Z-f_homog(U,Z). With a3!=0 the only point at Z=0 is [0:1:0] and is smooth, with its tangent of multiplicity three. In affine chart singularity requires v=0=f(u)=f'(u); a degree-three f has at most one distinct multiple root, yielding node at double root and cusp at triple root; odd degree ensures irreducibility. Symbolic discriminant/E=cubic-subdiscriminant give cusp iff a2=-a1²/(48a0), a1³=162a0²a3; monic Weierstrass c4 and discriminant yield exact j. Independently checked the projective, discriminant and cusp identities in SymPy and all 3 example types. Standard genus theory gives genus one versus rational normalization.

## originality

PASS

Lawless arxiv:2610.12498 supplies the root-family polynomial, irreducibility and generic genus bounds but reports exact cubic genus/elliptic identification as an open problem. The audited coefficient-specific global linear Weierstrass transformation, singularity discriminant and j invariant add this missing identification. Classical cubic classification is standard. Galligo 2013 related fractional derivative order curves might be equivalent after parameter change; full text inaccessible; best-of-knowledge O PASS remains qualified.

## value

PASS

The original integration-root problem leaves the first elliptic cubic parameter case without an exact geometric identification; this explicit projective Weierstrass model resolves its smooth, nodal and cuspidal strata and moduli invariant for every admissible coefficient, a natural classification rather than a generic routine example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
