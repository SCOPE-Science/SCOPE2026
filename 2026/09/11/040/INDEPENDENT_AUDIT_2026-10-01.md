# Independent audit — 2026-10-01

**Record:** `SCOPE-20260911-040`

## Correctness — PASS

A fresh symbolic check confirmed the factorization f=(x-1)g, the coprimality identity, all three square-sandwich identities, and discriminant 1957=19*103. The sign argument for x at most -3 and the strict consecutive-square inequalities for x at least 3 close every integer x other than 1 and 2; direct evaluation gives exactly (1,0) and (2,plus-or-minus 3). An independent exhaustive sanity scan over -10000 through 10000 found no additional integral x. The finite-field point counts are not needed for correctness.

## Originality — PASS

Exact web searches for the quintic equation and for the discriminant together with genus-two integral-point terms did not locate a prior exact census. The LMFDB-facing search did not return this curve as an exact hit, and the published-record semantic search returned this record plus different genus-two curves. General Mordell-Weil sieve and Chabauty literature covers methods for rational points but does not imply this elementary integral census.

### Structured originality checks

- **equivalent_formulations:** Searches: exact quintic equation integral points; factorization (x-1)(x^4+x^3-4x^2+1) integral points. Evidence: No distinct exact equation match with a complete integral-point census was found. Reasoning: The claim is unchanged under the factorized formulation; neither search produced prior coverage.
- **broader_coverage:** Searches: genus 2 integral points hyperelliptic algorithms; Mordell-Weil sieve genus 2. Evidence: General methods exist for integral/rational point determination. Reasoning: Those methods do not mechanically return this exact census without curve-specific computation or a database row.
- **exact_database_or_table:** Searches: LMFDB genus 2 exact polynomial/discriminant 1957; published-result semantic search exact equation. Evidence: The web-facing LMFDB search returned unrelated objects with discriminant/conductor 1957 rather than this curve; the semantic index returned the audited record as the exact match. Reasoning: No exact database/table coverage was identified.
- **claim_vs_prior_implication:** Searches: Stoll Mordell-Weil sieve; genus 2 Chabauty and sieve references. Evidence: Prior literature provides general techniques but not the curve-specific consecutive-square identities. Reasoning: The final integral-point census follows from special polynomial identities discovered for this curve, not from a quoted general result with substituted parameters.

## Scientific value — PASS

The integral locus is a natural, exact subproblem of a motivated genus-two rational-point target. It supplies a complete self-contained boundary result while honestly leaving non-integral rational points open. The proof is short but curve-specific and potentially useful in any later rational closure or denominator analysis.

## Source inspections

- **Stoll, The Mordell-Weil Sieve** (method reference). Bibliographic/method-level reference; no exact curve row was found in exact-equation searches. Assessment: BROADER_NOT_COVERING_EXACT_CLAIM. Provides a general method rather than this elementary integral-point census.
- **LMFDB genus 2 curves over Q** (LMFDB database). Web-facing searches using the exact polynomial and discriminant 1957. Assessment: NO_EXACT_MATCH_FOUND. Search results surfaced unrelated objects with 1957, not an exact curve record or integral-point table for the audited equation.

## Residual risks

- No exhaustive historical search of every genus-two integral-point table is possible; novelty is best-knowledge based.
- The full rational-point set remains open in this record and is not inferred from the integral proof.

## Disposition

**PASSED**. The final claim passes correctness, originality, and scientific value.
