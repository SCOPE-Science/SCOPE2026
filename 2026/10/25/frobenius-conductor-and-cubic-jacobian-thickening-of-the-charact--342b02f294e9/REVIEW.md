# Independent mathematical audit

## correctness

PASS

In k[a,b,c] characteristic 3 the standard cubic discriminant reduces to Δ=a²b²−b³−a³c, irreducible by primitiveness and linearity in c with relatively prime coefficients; substituting b=−aλ, c=λ³+aλ² gives zero, and a≠0 recovers λ=−b/a. λ satisfies monic λ³+aλ²−c=0, so B=k[a,λ] is finite birational and normal, hence normalization. With R=k[a,c], B is free basis 1,λ,λ², and A=R⊕aRλ⊕a²Rλ²: b=−aλ and b²=a²λ², while reduction λ³=c−aλ² makes multiplication by b stable. Thus B/A≅R/(a)⊕R/(a²). The conditions hλ,hλ²∈A for h=h0+ah1λ+a²h2λ² give a²|h0 and a|h1, so conductor=a²B=(a²,ab,b²)A=(a,b)². Partial derivatives are Δ_a=−ab², Δ_b=−a²b, Δ_c=−a³; using Δ=0 also b³ is in the Jacobian ideal, so exactly J=(a,b)³, with radical (a,b). On reduced singular/conductor line a=b=0 the normalized map c=λ³ is purely inseparable degree3. Independent SymPy computations mod3 checked substitution, derivatives, cubic relation/module multiplication; the universal conductor result follows from the displayed free-module reasoning.

## originality

PASS

PASS best-of-knowledge for the simultaneous explicit affine monic cubic conductor square, Jacobian cubic thickening and normalization module in characteristic three. The parametrization of the cubic discriminant and its repeated-root locus are classical; Fehér–Némethi–Rimányi treat coincident-root equivariant classes over C rather than these char3 local ideals. Shimada proves a general inseparable degree-three phenomenon in characteristic three for dual-variety singularities, so degree-three Frobenius itself is prior background, not claimed novel. The new assessed content is the precise ring/module ideal and conductor comparison for this canonical universal cubic. An earlier modular discriminant/conductor formula could imply it; this remains a genuine residual priority risk.

## value

PASS

The universal cubic discriminant in characteristic three is a natural test case where inseparable geometry makes intrinsic singular-scheme thickness differ from the normalization conductor. Giving exact ideals (a,b)^3 vs (a,b)^2 and B/A torsion exponents supplies a concrete structural invariant measuring that difference. This is meaningful modular algebraic geometry even without a projective compactification or general theorem for all discriminants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
