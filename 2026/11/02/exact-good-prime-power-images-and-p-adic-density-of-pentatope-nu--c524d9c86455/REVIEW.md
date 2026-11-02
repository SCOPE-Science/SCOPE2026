# Scientific review: pentatope images over good prime powers

## Correctness (PASS)

The polynomial identity \(24\binom{x}{4}+1=((x-3/2)^2-5/4)^2\) was expanded directly and checked against the definitions. Finite-field collision classes of the reflection \(t\mapsto5/2-t\) are counted using the standard quadratic-character sum, giving \(T_p\). The only singular values are \(3/128\) and \(-1/24\); their distinction and precisely stated quadratic-character tests hold for every prime \(p\ge7\). On all other attained residue classes, an invertible derivative gives complete Hensel lifting. On each singular class, the displayed exact factorization and unit-derivative coordinate change yield a scaled square set. The number of square residues modulo every prime power and the Haar measure are then computed exactly. A separate implementation checks all 34 complete prime-power value sets (337286 inputs). The computations corroborate but are not used to infer the infinite theorem.

## Originality (PASS, historically qualified)

The prime-field cardinality is a known Dickson-polynomial specialization, and is not claimed as new. The closest work is Chou–Gomez-Calderon–Mullen (1988), exact finite-field Dickson value-set cardinality, and Bremser–Gomez-Calderon (1991), Galois-ring Dickson value-set estimates and certain preimage counts. The current mathematical content is the explicit all-good-prime, all-exponent residue set stratification, exact prime-power sizes, and Haar formula. The 2012 Mullen–Wan–Wang paper gives general finite-field bounds rather than this local refinement. Searches using the algebraically equivalent degree-four Dickson form and double-square form did not identify an explicit prior formula for this full statement. The 1991 full text could not be accessed, so this is a genuine and material priority risk; the review does not claim a uniqueness proof.

## Mathematical value (PASS)

The sequence \(\binom{n}{4}\) is the classical pentatope/4-simplex figurate sequence, and its exact attainable residue set is a natural invariant, not an arbitrary parameter slice. The set-level formula separates ordinary free-lifting residues from two distinct singular quadratic branches and gives every finite depth together with a limiting density, rather than an isolated table or a generic algorithm. The exclusion of primes \(2,3,5\) is geometrically forced by denominators and coalescing critical values. Even if the finite-field count is known, the explicit all-depth stratification is a separately motivated target. Its value is confined to good primes, and no claim is made about bad-prime completion or broader polynomial families.

## Closest literature and limitations

Relevant primary sources: Chou–Gomez-Calderon–Mullen, *Journal of Number Theory* 30 (1988), 334–344; Bremser–Gomez-Calderon, *Journal of Number Theory* 38 (1991), 240–250; Mullen–Wan–Wang, arXiv:1210.8119v1 (2012). The 1991 source was accessible only at the abstract level and remains a priority limitation. The formulas do not treat the bad primes or grant independent validation.

Self-review: passed. Independent audit: not yet performed.
