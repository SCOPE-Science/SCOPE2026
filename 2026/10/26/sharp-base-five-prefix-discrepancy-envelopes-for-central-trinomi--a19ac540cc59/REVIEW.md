# Assessment of sharp trinomial residue discrepancy envelopes

**Correctness — PASS.** The exact digit congruence is cited to Deutsch–Sagan, Theorem 4.7. The fresh part is derived from the five-block counting identity and the four-state Bellman recurrence. Tables of all necessary minimum and maximum vectors plus the three transfer identities for each residue are reproducibly checked with exact integer arithmetic in `verify.py`. Translation equivariance proves the claimed two-step minimum orbit and one-step maximum orbit for every length. Finite scans are corroboration, not infinite proofs. All prefix boundaries and the \(L\ge2\) condition are explicit.

**Originality — PASS, with residual risk.** Deutsch–Sagan supply the digit-Lucas lemma, not an attainable residue-by-residue four-class sharp excursion formula. Rampersad–Shallit's central-trinomial theorem handles nonvanishing and uniform recurrence, which do not numerically imply these exact upper/lower envelope coefficients. OEIS A002426 gives values, not the claimed invariant. Searches for exact residue prefix extrema and digital discrepancies did not identify a dominating statement. The common automatic-sequence framework may contain an implicit corollary or an unlocated paper may state the same result; this is a nonzero risk and is not treated as a proof of uniqueness.

**Mathematical value — PASS.** Earlier work makes the central-trinomial mod-five sequence a concrete test case for finite-state number theory but leaves the maximal unbalanced-prefix behavior undetermined. Here a natural four-residue counting invariant is determined for every power-of-five range, including attainability, an explicit pair of asymmetric optimal slopes and a sharp quantitative strengthening of limiting equidistribution. It is a complete extremal classification rather than a low-depth table or an arbitrary coefficient normalization.

**Scope:** The result is specific to central trinomials modulo five; general moduli and arbitrary shifts remain open. Literature priority and mathematical correctness have not been independently assessed.

Self-review: passed. Independent audit: not yet performed.
