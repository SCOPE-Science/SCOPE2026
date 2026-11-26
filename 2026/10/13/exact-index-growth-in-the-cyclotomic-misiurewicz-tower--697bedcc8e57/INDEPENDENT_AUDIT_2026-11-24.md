# Independent mathematical audit

## correctness

PASS

The repaired finding states maximality of the polynomial root's order, not field nonmonogeneity: the latter reading of the frozen consequence is not justified. In fact at p=3,j=2,k=1 with norm 21, beta²=zeta−4 and u=zeta², eta=(beta−u)/2 satisfies eta²+u eta+1=0. Its norm polynomial X^4−X^3+3X²−X+1 has constant one, giving u=−eta−eta^(−1) in Z[eta]. Thus the relative bases (1,beta) and (1,eta) differ by an index of four over Z, exactly the computed index of the original order. The even-j level field is monogenic. For the quantitative theorem, translation by 2j gives Phi_p(Y^(2^k)+2j) and contains Z[zeta] through zeta=beta^(2^k)+2j. The norm is odd and greater than one, and squarefreeness gives valuation one at each prime of the radicand, so Eisenstein proves relative irreducibility and local maximality there (powers of a uniformizer have distinct valuations modulo the degree). Away from those primes and 2 the binomial discriminant is a unit. At each prime over 2 the base is unramified and the shifted polynomial has only one linear residual factor. With s=v2(j), its first principal face is (0,1) to (2^k,0) if s=0, (0,s+1) to (1,k) if s>k, and (0,s+1) to (2M,s−1) with M=2^(k−s) otherwise. In the third case the midpoint is the only non-endpoint coefficient on the first face, and its nonzero residual coefficient makes the residual quadratic separable; all other faces have residual degree one. Checking coefficient heights and increasing slopes gives the floor ordinates in the repair. Their sum by level counting is 2^k−2^(k−min(s,k)); summing residue degrees over 2 multiplies by p−1 for the absolute index. The 105-case frozen verify.py / verification_output.txt polygon replay was inspected, not executed; it does not compute maximal orders or independently prove Ore regularity. The revised RESULT.md and SLOGAN.txt were checked against the universal argument and the example.

## originality

PASS

The corrected surviving claim is the exact index for the specified power basis, particularly the valuations at all levels for even j. The same-family primary proposition already proves index one for odd j, and the general criterion detects nonmaximality of a polynomial order; neither provides the powers of two for even j. The exact rational pure-field discriminant calculation is a precedent for the method, not a directly applicable theorem for the radical over the cyclotomic base. Closest inspected indexed records concern different generators or different problems.

## value

PASS

An exact absolute order index is the natural quantitative invariant after the generating-polynomial monogeneity test in the same tower. Rather than just detecting a bad prime, the formula shows precisely how the dyadic defect changes with iteration depth and the valuation of j. The repaired distinction about alternative integral generators prevents a materially wrong interpretation of that defect, while leaving the substantive all-level calculation intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
