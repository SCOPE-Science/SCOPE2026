# Independent mathematical audit

## correctness

PASS

For a degree-seven cyclic cover of the projective line, Deuring–Shafarevich gives −1=−7+6r, so there is one branch point; reduced Artin–Schreier form and Riemann–Hurwitz give 16=−14+6(d+1), hence pole order d=4. Move it to infinity, translate x to kill the cubic term, scale x to normalize the quartic coefficient, and translate y to remove the constant over the algebraically closed field. The nine x^iy^j dx with 7i+4j≤16 have distinct valuations at infinity and are regular: the different exponent is 30, so div(dx)=16P. They form a basis by genus. Expanding y^j=(y^7−f)^j and retaining exponents 6 modulo 7 verifies the active block over F7[a,b]; e.g. coefficients of x^6 and x^13 in f^4 are 6a²b² and 4b, and the y and y² rows of the last column are −4(a³+3b²) and 12a. Raising the actual matrix coefficients to seventh powers preserves rank over the perfect field. For a≠0 the relevant three-column minor is 4a³ and the two first columns are collinear; for a=0≠b the relevant two-column minor is b² and only two independent columns remain; at the origin the matrix vanishes. Consequently the a-numbers are 6, 7, 9 throughout the specified family, not just at F7 points. The frozen checker was inspected, not executed; an independently implemented sparse expansion also returned BASIS_OK and MATRIX_OK.

## originality

PASS

The supported distinct result is the complete coefficient-plane stratification and exclusion of a-number eight in the characteristic-seven genus-nine zero-p-rank family. The normalized one-pole framework, the monomial value, the genus-nine example without extra automorphisms, and general a-number bounds and computations all have prior coverage.

## value

PASS

The result fills the interval left by established ramification-only bounds with exact loci for a complete natural p-rank-zero family. In particular it identifies a genuine missing a-number and shows exactly which coefficient degenerations change the rank. It is not a value claim for the already-known monomial point or a claim about coarse moduli.

The dated certificate retains the supplied scientific assessment, sources and limitations.
