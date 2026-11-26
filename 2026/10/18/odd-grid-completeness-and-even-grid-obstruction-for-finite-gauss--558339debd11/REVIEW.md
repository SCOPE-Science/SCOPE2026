# Independent mathematical audit

## correctness

PASS

Complexifying the real Hermitian domain gives the entire m²-dimensional span of z^j w^k for 0≤j,k<m, where w=x−iy; the real form is exactly the Hermitian coefficient condition. For even m the pure terms z^m,w^m cancel in x^m−(−1)^(m/2)y^m, while lower total degrees automatically fit. The pure x^m term makes the proposed vanishing polynomial nonzero as a polynomial in x,y. For odd m, degree-preserving monic reduction by p_X and p_Y leaves the unique tensor-product remainder of x,y degrees <m, which vanishes identically if it vanishes on the grid. In particular the highest homogeneous form of an element of the grid ideal has no terms with both exponents <m: any offending nonreduced term loses total degree on reduction. If its degree is n+r, n=m−1, it equals (x²+y²)^r times a form of degree n−r. Extracting exactly the middle k=m−r coefficients gives the stated binomial matrix. For even r=2q each parity block is positive definite by the symbol |1+e^{it}|^{2q}. For odd r=2q+1, k is even, and the two opposite-parity blocks are transposes of one another; one has symbol (1+e^{it})|1+e^{it}|^{2q} up to reversal, with real part positive almost everywhere. Integration against the nonzero vector's trigonometric square proves strict accretivity and invertibility. This contradicts any nonzero top form. The rank-one consequence follows by Gram equality of the coefficient vectors up to scalar phase; positive Gaussian weights do not affect injectivity. Replay: RESULT.md lines 27–69. Inspected check_cartesian.py, the saved check_output.txt, and VERIFICATION.md without rerunning uploaded code. The modular full-rank observations concern selected grids; the exact general proof does not assert even nullity m/2 or rule out pure-signal uniqueness for all even m.

## originality

PASS

The strongest indexed parity analogue is the cyclic full-lift result for a specific chirp-plus-impulse window. The strongest primary finite polynomial sampling overlap is a norming result for differences of two intensities. Neither inspected statement gives arbitrary Cartesian-node unisolvence for the full Hermitian space, or its explicit even-grid annihilator.

## value

PASS

The natural m² measurements match the real dimension of the lifted space, but dimension alone cannot decide their rank. The result gives an exact parity criterion independent of spacing or symmetry for any allowed Cartesian grid, with an explicit obstruction a user can construct in the even case. It separates exact full-lift sampling from both stability and ordinary phase retrieval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
