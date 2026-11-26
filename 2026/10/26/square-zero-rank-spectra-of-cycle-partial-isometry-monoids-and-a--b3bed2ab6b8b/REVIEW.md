# Independent mathematical audit

## correctness

PASS

The frozen formula is mathematically correct, although not original. In particular, for any partial isometry f:A→B the composition has empty domain iff A∩B is empty; on extending f to a dihedral permutation the admissible domains select independent vertices along each orbit. Checking the multiplicities gives the empty correction 2n−1, rank-one correction n(n−1), and even antipodal rank-two correction 2(n/2)(n/2−1). For the repaired statement the dominant polynomial M is the sum over reflections and the even half-turn, with t=n/2 giving (t+1)(1+2z)^t+t(1+2z)^(t−1) in even size and n(1+2z)^((n−1)/2) in odd size. Normalizing these polynomials gives precisely the stated binomial laws and weights. The two-state trace shows that the independent-set count of a d-cycle is λ^d+(−1/λ)^d; odd d are bounded by λ^d, and even d≥4 have d-th root at most 7^(1/4). Summing over at most n rotations and adding O(n²) extra representations bounds the coefficient ℓ¹ discrepancy E. Since |s_n−M(1)|≤E, renormalization has coefficient ℓ¹ discrepancy at most 2E/M(1); polynomial correction terms are exponentially smaller than the stated errors. This proves the quantitative total-variation claim. Evaluating M at one and dividing by the cited monoid size gives both rarity constants, and the means and variances of all the binomials agree with n/3 and n/9 up to O(1), proving the CLT and LLN. The n=3 boundary has the empty map and six rank-one maps; the extensions and the proof still apply.

## originality

PASS

Original finding: FAIL for originality of its advertised exact rank polynomial. The earlier bounded-nilpotency enumerator states a stronger theorem; setting h=2 produces the exact same polynomial for every n≥4, including all correction terms. The trivial n=3 addition does not rescue that assertion. Repaired finding: PASS for the asymptotic rarity and conditional rank law, quantified by an exponentially accurate global approximation with an explicit even-cycle mixture. The repair expressly credits the exact polynomial instead of claiming it. Neither the earlier indexed enumeration nor the inspected foundational monoid theorems states or directly specializes to the quantitative dominance estimate. This narrower result uses uniform spectral bounds on longer rotation orbits and control of duplicate representations; a Gaussian theorem alone would not give the repaired total-variation result.

## value

PASS

The repaired conditional law resolves more than a routine finite specialization or a limit for one moment. It explains the parity effects in the rare-event probability and gives an explicit approximation valid uniformly over rank events with exponential error. Counting the half-turn in the even reference law retains a class of extension pairs of only algebraically smaller relative mass than the reflections, rather than dropping it for a weak Gaussian limit. The useful result is this quantitative conditional law and its interpretation for sampling distinct partial maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
