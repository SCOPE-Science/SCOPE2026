# Independent mathematical audit

## correctness

PASS

With the cyclic shift unitary, (D²)*D²=(D*D)², and constants are its entire kernel. I independently checked the quartic Green kernel by symbolic finite differences (using reflection at the cyclic wrap-around), checked its zero sum, and summed the quadratic form of a consecutive block at arbitrary cardinality. Hilbert duality gives the real squared constant as max σᵀGσ over signs, or 4 times the maximum indicator energy. The kernel strictly decreases on 0,…,floor(N/2). Its positive layer decomposition uses cycle powers with radii less than floor(N/2); at fixed cardinality Vasilev's Theorem 1 supplies a single consecutive set that maximizes each layer, with the radius-zero count and constant term fixed. The block polynomial is strictly increasing in m(N−m), hence a balanced block attains it, and Gσ attains the primal inequality by its saturated dual pairing. The complex spectral-gap estimate is sharp by constant-modulus first characters. A real equality vector must have constant nonzero modulus, so odd N is impossible; for even N the first-mode eigenvector equation for its signs forces cos(2π/N)∈{−1,0,1}, which leaves only N=4, attained by (1,1,−1,−1). The squared leading terms N⁵/1920 and N⁵/(16π⁴) give the stated ratio. Replay symbolic identities with python /workspace/branches/math_checks.py 4. The frozen verification/check_cycles.py was inspected, not run; its bounded sign enumeration is not the all-N proof. The result uses counting measure and does not classify every real equality vector.

## originality

PASS

The distinct contribution supported here is the exact real cyclic second-difference constant and balanced-block optimizer, with the resulting real–complex comparison. The complex constant alone is an immediate sharp spectral-gap consequence; the cycle-power rearrangement is Vasilev's existing theorem and is not credited as new. No inspected exact statement or dominating theorem supplies the real second-order constant as a stated or routine special case.

## value

PASS

The real sharp constant is a natural second-order periodic Sobolev endpoint rather than an isolated size calculation. The exact all-size norm, attaining real family and finite-size scalar-field separation capture behavior that a Poincaré estimate alone cannot give. In particular the real optimization remains meaningful after crediting the already implied complex formula and the existing combinatorial theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
