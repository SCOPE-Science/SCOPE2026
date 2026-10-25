# Self-review

**Correctness — PASS.** For a fixed idempotent first factor, the off-diagonal block equations follow from direct multiplication. The canonical splitting by the idempotent \(D^2\) is unique and reversible; this yields a zero-product matrix-pair enumeration for which the Gaussian coefficient formula is derived. The image of the second factor is explicitly determined, proving its rank. Both boundary cases and the commuting specialization follow from the same construction. A standalone exhaustive verifier has replayed the full enumeration for finite fields of orders \(2,3,4,5\), including degree four over the binary field. Finite tests are corroboration, not the general proof.

**Originality — PASS, best knowledge with documented risk.** Erdős (1967) and Alahmadi–Jain–Leroy–Sathaye (2015) discuss existence of idempotent factorizations; the inspected results do not imply the three-rank finite-field count. The closest published database hits count idempotent–nilpotent or other distinct factorization types. The earlier set-transformation enumeration is not a vector-space count. The full text of Laffey (1983) was inaccessible, so its potential implicit coverage remains a historical-priority risk; a failed search is not a proof of novelty.

**Value — PASS.** The simultaneous factor and product ranks are intrinsic structural parameters of a natural idempotent-product locus in a classical finite linear monoid. A complete closed formula for every field and dimension gives an exact noncommuting-versus-commuting ratio and handles genuinely noncommuting strata rather than a routine marginal single-idempotent count.

**Limits and sources.** See RESULT.md and AUDIT.json for full comparison. Only labeled pairs with idempotent product are classified; no orbit classification, longer products, or independent mathematical validation is claimed. Relevant primary references are Erdős (1967), Laffey (1983; abstract only), and Alahmadi et al. (2015).

Self-review: passed. Independent audit: not yet performed.
