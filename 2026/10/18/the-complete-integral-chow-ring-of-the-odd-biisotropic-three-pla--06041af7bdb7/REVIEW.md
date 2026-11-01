# Independent mathematical audit

## correctness

PASS

For general two alternating forms on C^7, the smooth sixfold X in Gr(3,7) is the regular zero set of E=(Λ²U∨)⊕2. Its top Chern class is e=(x+y)^2(x+z)^2(y+z)^2=(c1 c2-c3)^2. Fonarev–Kuznetsov 2026 Theorem 1.1 and the Białynicki–Birula paving yield free integral Chow/cohomology ranks (1,1,2,2,2,1,1) in codimensions 0..6, zero odd cohomology, integral perfect pairings. Independently recomputed all 26 Schur intersection numbers via sympy Jacobi–Trudi complete symmetric functions and Grassmannian Vandermonde top coefficient, obtaining M0,6=[1,1,1,2,1], M1,5=[2,4,3,3], M2,4=[[1,5,4,3],[1,4,3,3]], M3,3=[[2,4,1],[4,8,2],[1,2,1]], and ∫_X c1^6=61. The low/high matrices have unit entries or gcd(2,3)=1, M2,4 has determinant -1 from its first two columns, and M3,3 has determinant 1 on rows/cols 1 and 3. These unimodular pairings between ambient restrictions force integral bases in each graded degree, hence surjectivity CH*(Gr)→CH*(X), including the middle. Projection formula then identifies the restriction kernel exactly with Ann(e) in the integral Grassmannian Chow ring, giving Z[c1,c2,c3]/((h5,h6,h7):e), not merely rational equality. The source verify.py was materially inspected but the independent check uses a separately written sympy implementation; finite exact certificates support specific entries while the stated all-degree conclusion uses geometric duality and algebraic argument.

## originality

PASS

Qualified best-of-knowledge originality for the full INTEGRAL multiplication ring of the smooth odd-ambient sixfold BIGr(3,7). Fonarev–Kuznetsov (2026) explicitly establish only the additive cellular ranks and in Remark 1.2 call the multiplicative ring a separate problem; the submitted additional theorem is integral Schubert restriction surjectivity plus its kernel as the annihilator of the top Chern class. Benedetti 2018 gives a ring theorem for I_2Gr(2,6) in EVEN ambient dimension and k=2, not this odd 3-plane case. Bernardara–Fatighenti–Manivel 2019 develop Hodge and derived relations of other Grassmannian sections, not these integral structure constants. Actual Resultary semantic searches returned different Grassmannian/cohomology findings, not an exact or dominating ring computation. There is a directly plausible A. Kuznetsov in-preparation same-sixfold manuscript referenced in the October 2026 source; the full manuscript was not available and historical priority is qualified, not certified.

## value

PASS

The odd sixfold is the first positive-dimensional three-plane member of the natural biisotropic family. Fonarev–Kuznetsov Remark 1.2 specifically identifies integral multiplication as an unsolved separate question from graded Betti groups; this result supplies all Chow/cup products, including integral saturation rather than rational approximations. The unimodular Schubert restrictions give a useful structural method for computing primitive generators of nonhomogeneous complete-intersection Chow rings. The full ideal-quotient presentation is a natural precise invariant and was not mechanically determined by previously known degree 61/additive ranks. The theorem is deliberately for the general (3,7) case and does not claim all ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
