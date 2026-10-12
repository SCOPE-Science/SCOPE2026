# Review: exact square-splitting Möbius residue-class distribution

## Correctness

**PASS.** The proof reconstructs the local prime-power values of the square-splitting Möbius function, proves its ordinary square-divisor convolution with the classical Möbius function, and independently reconstructs the fourth-power-free indicator by fourth-power divisor inversion. The unconditional prime number theorem in fixed arithmetic progressions supplies the only analytic input needed for \(o_q(x)\) signed cancellation in reduced classes. Every nonreduced class reduces to finitely many q-supported prime-power factors and finitely many reduced classes, so the cancellation remains valid without a coprimality assumption. Exact congruence counts establish the support formula with \(O_q(x^{1/4})\) error. All vanishing boundaries are handled, including \(q=1\) and classes divisible by \(p^4\).

The finite implementation is independent numerical corroboration, not a substitute for the infinite proof.

## Originality

**PASS.** The identical primary paper is Talukdar and Saikia, INTEGERS 26 (2026), article A56. Its Theorem 3 gives the arithmetic function, and its Theorem 11 computes only the total support density \(1/\zeta(4)\). The conclusion explicitly notes further distributional questions. General fake-Möbius studies by Martin–Yip and Saraeb were inspected: their global oscillation or smoothed-sum results do not state or directly dominate the present full three-value fixed-residue distribution. Exact-equivalence, periodic-class, fourth-power-free, and Möbius-convolution searches did not reveal an equivalent classification.

Residual risk: a general unindexed theorem might imply the explicit specialization; a failed search alone is not evidence of uniqueness.

## Value

**PASS.** The source determines where the function is nonzero in aggregate but does not say whether either sign dominates in specific arithmetic progressions. The exact three-way classification answers this naturally posed quantitative question for all fixed moduli, including noncoprime classes, and identifies the sharp structural vanishing obstruction \(p^4\mid\gcd(q,a)\). The result also provides an explicit support error without a finite cutoff or empirically chosen parameters.

## Closest literature and limitations

The prior support theorem is recovered as a special case by summing the two signs over the unit modulus. The extension relies on standard Möbius cancellation and exact congruence counting, not a claimed new general prime-number theorem. No estimate uniform in growing \(q\) or finer sign-discrepancy rate is proved.

Self-review: passed. Independent audit: not yet performed.
