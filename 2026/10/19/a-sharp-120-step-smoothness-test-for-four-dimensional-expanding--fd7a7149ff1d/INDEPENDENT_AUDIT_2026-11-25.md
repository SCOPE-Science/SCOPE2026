# Independent mathematical audit

## correctness

PASS

For a nonzero algebraic integer, two integral powers make the gcd power rational by Bézout, hence integral. Exponents are therefore the multiples of the least one and matrix exponents are lcms over the irreducible factors. All conjugates of a root with an integer power have common modulus r. In degree two the ratio of the two conjugates is a root of unity in the quadratic field, and the power is rational exactly when this ratio raised to that power is 1. Thus degrees of cyclotomic fields give exactly the allowed orders 2, 3, 4, 6. An irreducible cubic has exactly one real root ±r, with norm ±r³, hence least exponent 3. For a quartic, complex conjugation takes α to q/α with q=r². If there are real roots, either all four of the same modulus would be impossible or the real pair is ±r, which forces an even minimal polynomial. In the nonreal case reciprocity pairs the cubic and linear coefficients and the constant is q². When the polynomial is even, β=α² has degree two and rational powers of α must be even by conjugacy with −α, giving {4,6,8,12}. Otherwise the nonzero cubic coefficient gives rational q via the linear coefficient c=qa, hence integer q since q² is integral. Now α=√q ζ_m, and in Q(√q,ζ_m) its stabilizer has size at most two because ζ_m can go only to ±ζ_m. Degree four gives φ(m)=2,4,8. The φ=2,4 lists only give exponents from {2,3,4,5,6,10}, according as m/gcd(m,2) is taken alone or with the required factor 2 for nonsquare q. For φ=8 the only orders allowing the necessary automorphism ζ↦−ζ are 16,20,24 (φ(m)=8 implies m uses only the primes 2,3,5). In the 16 and 20 cases the maps ζ↦ζ⁹ or ζ↦ζ¹¹ fix the unique real quadratic subfields Q(√2) and Q(√5), respectively, so cannot also flip √q. Order 24 gives only index 12. Combining linears, cubics and two quadratics gives no additional indices. Witnesses for 2,3,4,6 have roots ±√2 or the conjugate pairs 2e^{±iπ/3}, √2e^{±iπ/4}, √3e^{±iπ/6}; indices 5 and 10 follow from 2ζ₅ and √5ζ₅ (the latter has degree four by its trivial stabilizer and the displayed polynomial by its four signed cyclotomic conjugates). For the even quartics of indices 8 and 12, squaring the root gives −1±i and (3±i√3)/2 respectively, with quadratic exponents 4 and 6; Eisenstein proves the quartic degree. All witnesses are expanding and semisimple. Their lcm is 120 and divisibility is necessary for any candidate universal exponent. Nonzero Jordan blocks retain their defect under powers because the first superdiagonal scales by jλ^{j−1}≠0. Over Q, a rational semisimple matrix with integral eigenvalues has a rational eigenbasis, so the cited smooth-Markov theorem gives precisely the claimed test. The frozen exact diagnostic script was inspected, not executed; the finite totient range in that script is not used as the upper bound proof.

## originality

PASS

The Markov criterion, finiteness of the possible indices in each dimension, the factor-lcm reduction, and the full quadratic spectrum are prior. The checked distinct addition is the dimension-four exact index set with attained witnesses and the optimal single exponent; this requires the quartic exclusions, not just selecting 120 from a finite bound. The exact power criterion follows from the arithmetic result and the existing dynamical theorem, rather than constituting a new Markov existence theorem on its own.

## value

PASS

An explicit optimal single-power test replaces an open-ended search over powers for a motivated geometric existence criterion. The complete dimension-four arithmetic list, including its less predictable indices 8 and 10 and counterexamples to every smaller universal exponent even in semisimple cases, is a useful finite classification, not merely a loose complexity bound or a recomputed dimension-two table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
