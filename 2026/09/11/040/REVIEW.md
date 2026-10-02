# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. A fresh symbolic check confirmed the factorization f=(x-1)g, the coprimality identity, all three square-sandwich identities, and discriminant 1957=19*103. The sign argument for x at most -3 and the strict consecutive-square inequalities for x at least 3 close every integer x other than 1 and 2; direct evaluation gives exactly (1,0) and (2,plus-or-minus 3). An independent exhaustive sanity scan over -10000 through 10000 found no additional integral x. The finite-field point counts are not needed for correctness.

Originality: PASS. Exact web searches for the quintic equation and for the discriminant together with genus-two integral-point terms did not locate a prior exact census. The LMFDB-facing search did not return this curve as an exact hit, and the published-record semantic search returned this record plus different genus-two curves. General Mordell-Weil sieve and Chabauty literature covers methods for rational points but does not imply this elementary integral census.

Scientific value: PASS. The integral locus is a natural, exact subproblem of a motivated genus-two rational-point target. It supplies a complete self-contained boundary result while honestly leaving non-integral rational points open. The proof is short but curve-specific and potentially useful in any later rational closure or denominator analysis.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
