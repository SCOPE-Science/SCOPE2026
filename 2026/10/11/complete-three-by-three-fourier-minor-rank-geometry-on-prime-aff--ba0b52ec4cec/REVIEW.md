# Independent mathematical audit

## correctness

PASS

For arbitrary complex 3×3 matrices with unimodular entries, diagonal phase normalization gives the determinant condition (u−1)(t−1)=(v−1)(w−1). If nonzero, conjugation gives ut=vw and then u+t=v+w, forcing equal normalized rows or columns; the zero-factor case also gives such equality. In F_p^2 the proportionality equations say that every difference in the opposite index triple lies in the kernel of one nonzero functional. A noncollinear triple has 3 distinct edge directions, and each orthogonal direction admits exactly K=p*binom(p,3) collinear partner triples, all rank 2. A linear triple is controlled by the projection of the opposing 3 points to a p-element quotient: respectively 1/2/3 distinct values give rank 1/2/3; rank-3 partners p^3*binom(p,3), rank-1 partners K. Counting L=p(p+1)*binom(p,3), U=binom(p^2,3)−L yields R1=L*K, R2=3U*K+L*(T−p^3*C−K), R3=U*(T−3K)+L*p^3*C. Sympy independently factors these to (p+1)p^4(p−1)^2(p−2)^2/36 and (p+1)p^5(p−1)^3(p−2)/6 for R1,R2 and proves total T^2. Independently authored Python and separately written C++ exact primitive-root cyclotomic coefficient enumerators checked all 7056 pairs for p=3 and all 5,290,000 pairs for p=5, with rank totals (36,1296,5724) and (15000,600000,4675000), and zero incidence mismatches. These finite checks corroborate, not establish, the all-prime theorem.

## originality

PASS

Best of knowledge: the complete all-prime F_p^2 3x3 rank-incidence classification is not present in the accessible full primary texts and exact Resultary comparisons. Closest cyclic prime-square all-minors result addresses a different group and produces different counts. Known rank-deficient block tilings/uncertainty and principal-minor theorems do not by themselves establish the fixed-support rank strata and closed multiplicities. The unit-modulus determinant lemma is elementary prior background, not a novelty component. The full Delvaux–Van Barel 2007 same-object Kronecker source could not be accessed and is recorded as a substantial risk, not deemed NOT_COVERING from its abstract. Failed searches are not a novelty proof.

## value

PASS

Exact 3×3 minors are the first nontrivial planar Fourier-interpolation rank condition. Their complete geometric classification and separate rank-one/rank-two/rank-three counts for all primes are a natural exact invariant of the character table of F_p^2. The rowwise refinement distinguishes line and triangle supports, gives every rank rather than merely support-size inequalities, and can be directly used to identify interpolation obstructions and design small harmonic subframes. The object and invariant are mathematically motivated, and this all-prime positional incidence is not just an arbitrary finite slice or recomputation of a cited rank table; a downstream theorem is not required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
