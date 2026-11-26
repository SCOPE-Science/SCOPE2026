# Independent mathematical audit

## correctness

PASS

Every factor of Q_T is prime to a, and the chosen b_T is also prime to a. In Q_T=ax+b_T y the congruence forces y≡−1 mod a and the size constraint gives 2≤y≤T. For composite y use its least prime divisor at most √T; for prime y use the −1 residue-class factor. In either case p divides Q_T and y but not a, so divides x, including when x=0. Consequently Q_T is not primitively representable. The fixed-modulus prime number theorem gives log Q_T=T/φ(a)+o(T); the additional small-prime weight is O(√T log T). The offset of b_T from Q_T/T is less than a, yielding b_T→∞ and Q_T/(b_T log b_T)→φ(a). Every cover must include every prime in the forced class because that prime itself is an eligible y. The matching log-weight upper bound from Q_T gives asymptotic optimality only in the stated cover class. An independent exact check gives Q_20=1870, b_20=95 and y=2,5,8,11,14,17 with respective gcds 2,5,2,11,2,17 for a=3; it does not compute the exact Frobenius number or reproduce all 615 cases. The supplied script was inspected, not executed.

## originality

PASS

The obstruction architecture and the fixed-a logarithmic lower-growth order are already in Ding–Wang–Zhang. The explicit φ(a) bound is an optimization of their actual CRT proof, not a new mechanism or a consequence of the printed coefficient. The supported distinction is the residue-class sieve that accomplishes this optimization, and the matching asymptotic minimum over all divisor covers of that class. The inspected same-day indexed theorem has a different growth regime; the later fixed-a indexed theorem uses a related mechanism with coefficient 1.

## value

PASS

The fixed-generator logarithmic growth was known but its lower coefficient was not quantified by the closest prior statement. The coefficient here explains the leverage of the progression's prime density and the sharp cover-weight comparison proves that this economy is not arbitrary prime selection. This value does not depend on claiming a new obstruction architecture or an unrestricted optimal coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
