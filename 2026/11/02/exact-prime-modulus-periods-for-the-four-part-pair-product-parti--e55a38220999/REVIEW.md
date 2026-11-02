# Scientific review: exact prime-modulus periods of a four-part partition statistic

## Correctness — PASS

For each \(n\geq0\), the claimed statistic is the sum of \(\sum_{i<j}\lambda_i\lambda_j\) over partitions into precisely four positive parts, with repetitions allowed. The proof parametrizes each partition uniquely by four nonnegative gaps, correctly assigning size \(4+x_1+2x_2+3x_3+4x_4\). The elementary symmetric polynomial is explicitly expanded, then summed by the three standard geometric moments. Integer-polynomial multiplication establishes the exact reduced generating function \(q^4P(q)/H(q)\) with \(\deg(q^4P)=16\), \(\deg H=22\), and \(H(0)=1\).

The critical nonstandard check is the complete modular noncancellation: division of \(P\) by the four cyclotomic factors of \(H\) yields constants \(864,32,6,-12\), none divisible by a prime \(p\geq5\). Therefore even an eventual period forces \(H\mid1-q^T\). Primitive third and fourth roots force \(12\mid T\); the multiplicity-six root at one forces \(p^{\nu_p(T)}\geq6\). Conversely the appropriate \(T\) clears the reduced denominator in characteristic \(p\), with polynomial quotient degree strictly below \(T\); this proves *pure* periodicity from index zero. All quantifiers and boundary cases including \(p=5\) are accounted for.

The standalone checker was executed successfully. It independently builds the generating numerator, confirms the exact denominator factorization and cyclotomic remainders, checks 41 coefficients against direct enumeration, and checks periodic patterns for seven sample primes. These checks corroborate the integer identities; the proof does not infer an infinite conclusion from sampling.

## Originality — PASS within the inspected evidence

The originating 2024 public preprint of Ballantine–Beck–Merca (arXiv:2408.13346, later published in 2025) explicitly labels the numerical table as conjectural and proves only moduli 2, 3, and 4. The values for primes 5, 7, 11, 13, and others in that table are **not** new observations. The new claim is their proof in one structural argument plus a least-period classification for *every* prime at least five. Its stronger eventual-period statement also follows from the reduced denominator, rather than merely showing periodicity.

Nijenhuis–Wilf and Kwong provide classical cyclotomic methods for unweighted partition sequences and rational series; the method is not asserted to be original. The 2024 *Elementary symmetric partitions* and 2025 *On partitions associated with elementary symmetric polynomials* address partition-map images and injectivity, not this weighted-period determination. Searches using statistic aliases, exact periods, rational denominator, and broader-period terminology found no known implication already specializing to this all-prime result. A theorem deriving the same rational function or its complete prime-period implications under a more general statement could still exist outside the inspected material; independent bibliographic validation has not occurred.

## Mathematical value — PASS

The originating paper presents the prime periods as a numerical research gap. Determining the least period—not just some period—for every prime \(p\geq5\) supplies a natural complete classification of the first unproved prime-modulus cases, explains the exceptional prime five by pole multiplicity six, and establishes pure as well as eventual periodicity. The result answers a specific arithmetic question for a named partition statistic and contains a reusable structural numerator–denominator identity. It is more than a finite table completion or the generic observation that rational sequences are eventually periodic.

## Limits and closest sources

The exact period has not been determined here for prime powers or composite moduli, nor for moduli two and three. The 2024 preprint's conjectured table is the closest primary source; its moduli 2/3/4 results and the older unweighted partition-period theorems remain properly attributed. Literature searching is not proof of absolute priority. Unindexed or unavailable mathematical work remains a residual bibliographic risk and is not treated as inspected.

Self-review: passed. Independent audit: not yet performed.
