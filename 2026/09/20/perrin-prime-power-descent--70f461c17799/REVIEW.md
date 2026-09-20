# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The core congruence is the classical matrix Gauss congruence

`tr(A^(p^k)) = tr(A^(p^(k-1))) (mod p^k)`.

For the Perrin companion matrix `M`, `P_n=tr(M^n)`; because `det(M)=1`, `M^{-1}` is integral and the same theorem applies to negative indices. This proves the two displayed Perrin congruences. The descent implications are immediate and were checked for modulus strength: from `p^k|P_{p^k}` one obtains the stronger statement `p^k|P_{p^(k-1)}`, hence the required lower-power condition. The same argument works for `P_{-n}+1`.

The finite `10^20` classification has three ingredients: any prime-power pseudoprime below the bound has base prime below `10^10`; descent forces its square to pass; and OEIS A173656 explicitly states that below `10^10` only `521` and `190699` have the needed square lift. Exact arithmetic then shows both cubes fail and both squares fail the negative congruence, excluding every higher power by descent.

The modular residues were recomputed using two distinct exact representations: matrix exponentiation and polynomial arithmetic modulo `x^3-x-1`. Agreement was exact. The same check was also applied to the newly listed third A173656 prime `36944128783`.

## Originality

PASS, to the best of our knowledge, with a material residual risk.

The matrix Gauss congruence itself is established prior mathematics and is explicitly excluded from the originality claim. OEIS A173656 also already records the square-lift condition `p^2|P_p`, so that condition alone is not new.

The checked current Perrin sources define the unrestricted and restricted tests, list known square examples, and provide computational tables. Searches for Perrin prime powers, cubes, lifting/descent, Gauss congruences applied to Perrin pseudoprimes, and equivalent matrix-trace formulations did not locate the exponent-descent statement, the minimal-restricted square criterion as a two-sided lift, or the resulting prime-power classification below `10^20`. The current SCOPE archive was searched under Perrin, pseudoprime, matrix-trace, and Gauss-congruence terminology with no overlapping result found.

The principal uncertainty is older specialized literature. Adams--Shanks (1982), DOI `10.1090/S0025-5718-1982-0658231-9`, is the foundational Perrin paper and contains substantial arithmetic analysis. Adams (1987), DOI `10.1090/S0025-5718-1987-0866094-6`, gives a broad characterization of third-order recurrence pseudoprimes in terms of periods. Their bibliographic records, abstracts/snippets, citations, and secondary descriptions were inspected, but complete full text was not available for direct theorem-by-theorem checking. Either paper could imply the present prime-power descent under another formulation. This is residual possible coverage, not evidence that coverage exists.

## Value

PASS.

The result turns the isolated square-lift data in A173656 into a structural statement: admissible prime-power exponents form an initial segment for both unrestricted and minimal restricted Perrin tests. This reduces every prime-power search to a square filter followed by successive local lift checks. Coupled with the current `p<10^10` completeness statement, it gives a clean exact frontier at `n<10^20` and rules out prime powers in all stronger Perrin tests in that range. The verification also determines that every prime currently listed in A173656 has unrestricted height exactly two and restricted height one.

## Limitations

The large enumeration behind the A173656 completeness statement was not independently repeated. The result does not classify non-prime-power pseudoprimes or determine whether further Perrin square-lift primes exist. Older full texts most likely to contain equivalent recurrence-theoretic consequences were not directly inspected, so the originality assessment remains qualified.
