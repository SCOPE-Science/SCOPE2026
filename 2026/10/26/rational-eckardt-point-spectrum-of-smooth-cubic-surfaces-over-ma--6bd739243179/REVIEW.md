# Independent mathematical audit

## correctness

PASS

Geometric smoothness for F homogeneous cubic in four variables over F_2 is equivalent to the gradient quadrics having no common projective zero. Since four quadrics in four variables with empty projective zero locus form a homogeneous regular sequence, the quotient Hilbert series is (1+t)^4; degree 5 is zero. Conversely, if degree-5 gradient ideal is entire 56-dimensional space, no projective common zero can exist. At each smooth rational point P, restricting F to tangent plane with basis (P,A,B) gives t Q(u,v)+B_3(u,v). Three distinct geometric lines through P occur exactly when Q=0 and binary cubic B_3 is squarefree, in characteristic two equivalent to ad+bc=1 for cubic coefficients (a,b,c,d). The rational roots of B_3 count 0,1,3 and give the Frobenius-splitting classes E_0,E_1,E_3. The supplied package includes orbit and direct full 2^20 coefficient enumerators. Crucially, an entirely NEW independently written C++17 program enumerated all 1,048,575 nonzero binary cubic vectors, built its own monomial/gradient-degree5 rank test, 35-line restrictions, tangent-plane ternary restrictions and root counts, and reproduced 384,840 rationally nonsingular equations, exactly 322,560 geometrically smooth equations, the 24 joint (N,L,E0,E1,E3) rows and marginal 0:189952,1:115920,2:10080,3:2800,4:3360,7:420,15:28, with zero failed squarefreeness tests. This independently verifies the whole finite domain, not a sample. The original orbit program also identifies 36 PGL4(F2) smooth classes; this count is prior literature. Both the direct exhaustive domain and algebraic classification criteria have been checked; independent code and output remain privately preserved.

## originality

PASS

PASS, but NARROW and strongly qualified: the full 36 smooth PGL4(F2) orbit classification, their rational point/line counts, and their Eckardt counts from triples of RATIONAL lines are conclusively prior in Dickson/Karaoğlu (2021), Table 1 and Theorem 3.1. The surviving original claim is the refined incidence distribution of F2-RATIONAL Eckardt points with 0,1,3 Frobenius-fixed geometric lines, including Eckardt points with NO rational line; the prior table is not the requested total geometric incidence census. The 2022 Betten–Karaoğlu full text could not be read, leaving a material exact-priority risk. No old orbit/E3 discovery is claimed.

## value

PASS

The finite-field arithmetic distinction between a rational Eckardt point and three rational lines through that point is mathematically substantive: 0 rational branches (a Frobenius 3-cycle), one rational branch (a conjugate pair), and three rational branches are different descent types. Their exact joint distribution over all geometrically smooth F2 cubic equations and the consequence that even N<=3 rational-point surfaces have a rational GEOMETRIC Eckardt point despite no rational lines is a natural complete classification; the 24-profile table is not recoverable from the prior line-count columns. This is a motivated finite arithmetic-geometric invariant, not merely a known orbit-count table or a proof of general finite-field behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
