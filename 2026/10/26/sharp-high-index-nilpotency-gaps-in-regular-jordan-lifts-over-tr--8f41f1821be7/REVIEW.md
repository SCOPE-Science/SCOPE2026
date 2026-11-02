# Independent mathematical audit

## correctness

PASS

For arbitrary finite field F_q, e>=3,m>=2, the companion basis u,Au,...,A^{m-1}u lifts the mod-epsilon Jordan cyclic basis, so K=1+epsilon M_m(R) acts transitively on each fixed characteristic polynomial. Its centralizer reducing to identity has size q^((e-1)m), giving uniform fiber q^((e-1)(m²-m)). In S=R[T]/(T^m-sum_h epsilon^h a_h(T)), the identity T^((e-1)m+j)=epsilon^(e-1) T^j a_1(T)^(e-1) holds because all other multinomial terms contain epsilon^e. This is nonzero precisely when j+(e-1)v<m with v=ord_T(a_1), yielding the strict high-tail indices em-(e-1)v and no others; the equality boundary belongs to the low tail. Counting valuation-v polynomials a_1 gives (q-1)q^(m-v-1), then all other coefficients and uniform fibers yield (q-1)q^((e-1)m²-v-1), complementary total q^((e-1)m²-ceil(m/(e-1))), and maximum frequency 1-1/q. Independent exhaustive powers of all 256 F2[epsilon]/epsilon³ lifts of J2 gave counts index 2:16, 3:48, 4:64, 6:128 and no index 5; symbolic proof covers arbitrary e,m,q.

## originality

PASS

The cyclic companion description and local principal ideal ring similarity framework are prior work. The new claim is the precise high-index valuation threshold and multiplicities for e>=3, a regime not covered by the earlier complete e=2 distribution; a more general existing classification might still contain the resulting corollary.

## value

PASS

High-index persistence of a Jordan nilpotent block under local-ring thickening is a canonical algebraic invariant. The full arithmetic support of indices above (e-1)m, explicit forbidden gaps, and exact fiber counts for all dimensions/ring lengths are a meaningful natural classification even though lower-index multiplicities remain open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
