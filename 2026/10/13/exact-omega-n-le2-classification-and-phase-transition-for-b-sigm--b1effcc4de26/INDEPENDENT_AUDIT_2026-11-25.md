# Independent mathematical audit

## correctness

PASS

Prime factorization gives exactly p, p² and pq with p≠q. Substituting their divisor sums gives cp=b−k, cp²−bp+k−b=0, and cpq−b(p+q)=b−k, respectively. Multiplication by c and addition of b² gives the signed product T; reconstruction by u↦(u+b)/c is injective and reversible, with order removed and equal primes excluded. At T=0, c divides ab and is coprime to both a and b, so c=1 and k=b(b+1). The prime candidate is then −b² and the square discriminant is −3b². One of the two distinct primes must equal b, so there are no solutions when b is composite or 1, and precisely bq with q prime and q≠b when b is prime. Removing q=b gives the exact counting function; the prime number theorem gives the fixed-base asymptotic. Independently enumerated 49,770 coprime triples with 2≤a≤16 and 0<|k|≤315 against 593 eligible n≤1300, using positive-divisor and prime-power sieves for the direct side. No mismatches; both signs of T, all 15 zero-T cases, and six exceptional triples were covered. The frozen verifier and its saved output were inspected, not executed; their original test domain and replay are documented in VERIFICATION.md. Neither finite test establishes the unbounded conclusion, which follows from the algebra.

## originality

PASS

Pass for the exact all-parameter classification in Ω≤2, including the finite sporadic classes, not for introducing the regular family or its prime-number-theorem asymptotic. Kwan and Miller's regular-solution formula already gives the exceptional family and its exact low-multiplicity count on restricting the regular part. The material additional assertion is exhaustion in that layer and a reversible signed-divisor classification outside it.

## value

PASS

The natural cutoff is the first layer admitting distinct-prime multiplicativity. Solving it exactly closes a gap left by asymptotic counting: it converts the finite search to factoring a specific integer and handles the degenerate boundary without mistaking the older regular-family construction for an exclusion of sporadics. The proof is elementary; the useful result is the complete classification, not the individual linear or quadratic substitutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
