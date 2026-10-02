# Independent mathematical audit — SCOPE-20260917-bd810ca7b75f

Final disposition: **passed**.

## Correctness
**PASS.** The load-bearing fibre calculation was independently reconstructed from the stated quotient ring rather than accepted from the stored success log. For f=-2-t+2t^3 and g=2+t^2 in Q[t]/(t^8-1), the four vectors g^2, t g^2, t^2 g^2, t^3 g^2 have rank four. Annihilating h^2 f modulo that subspace yields four quadrics. In the b0=1 chart their Groebner basis is b1, b2-1/2, b3; each chart on b0=0 has Groebner basis containing 1. The Jacobian at [2:0:1:0] has projective rank three, so the fibre is a single reduced point. The standard finite-morphism/Nakayama argument then forces generic tangent degree one. For a (2,2,2,2) threefold, c(TX)=1+4H^2-8H^3 and H^3=16, so the Chern tangent identity gives degree 64 when the tangent degree is one.

## Originality
**PASS.** Kanazawa’s 2026 paper states the stable-range tangent-degree-one conjecture and verifies it for a general intersection of four quadrics. A theorem for a general member does not mechanically imply the property for this highly symmetric Fourier-diagonal special member. Targeted searches found no prior source identifying this exact member or an equivalent reduced singleton tangent-incidence fibre certificate.

## Value
**PASS.** Special highly symmetric complete intersections can lie outside generic open loci, so an exact certificate for a named Fourier-diagonal member is a meaningful boundary test of the new tangent-birationality conjecture. The fibre computation is compact and reusable, and the resulting tangent-variety degree is exact.

## Source inspections
- **Atsushi Kanazawa, Chern bounds and tangent geometry of polarized Calabi-Yau threefolds, arXiv:2609.17513** — Primary abstract and detailed source summary inspected. The paper conjectures tangent degree one for complete embeddings in the stable range and verifies it for general intersections of four quadrics; direct PDF retrieval was unavailable in this run. Consequence: General-member coverage does not imply the audited explicit special member.
- **Repository artifact artifacts/verify_fiber.py and its exact mathematical construction** — Source code read as evidence only. Its quotient-ring construction was independently reimplemented symbolically: rank four for g^2 K, singleton Groebner fibre, no points at infinity, and Jacobian rank three were reproduced. Consequence: Critical finite certificate independently verified from definitions rather than trusting the stored log.

## Originality comparison
- **Equivalent formulations.** Searches: Fourier diagonal four quadrics tangent degree; special (2,2,2,2) tangent incidence birational. Evidence: No equivalent named special member or reduced-fibre calculation was located. Reasoning: Searches used both tangent-degree and tangent-incidence/birational terminology.
- **Broader coverage.** Searches: general intersection four quadrics tangent degree one Kanazawa; Calabi-Yau tangent normalization m=1. Evidence: Kanazawa covers a general member and proves normalization for higher multiples. Reasoning: Generic coverage is broader in moduli dimension but does not contain every special member; the exact special-fibre certificate is therefore not mechanically implied.
- **Exact database or table.** Searches: exact Fourier coefficient pattern zeta diagonal quadrics tangent; Resultary search Fourier diagonal tangent birationality. Evidence: Only the audited record matched the explicit construction. Reasoning: The novelty conclusion uses the logical gap between a generic theorem and a named special point, not unsuccessful search alone.
- **Claim versus prior implication.** Searches: Kanazawa general four quadrics theorem; tangent-incidence degree formula complete intersection. Evidence: The primary abstract says “general intersections of four quadrics”. Reasoning: A Zariski-open general result cannot by itself certify a particular symmetric member; the independent fibre computation supplies the missing implication.

## Residual risks
- The motivating preprint is extremely recent, and a later revision could add special members.
- Full primary PDF retrieval for Kanazawa was unavailable during this run; the primary abstract and detailed theorem summary were read, and this access limitation does not override the independent exact certificate.

## Limitations
The theorem treats one explicit smooth intersection of four quadrics in projective seven-space. It does not prove tangent birationality for every smooth four-quadric complete intersection or settle the full stable-range conjecture. The motivating tangent-geometry preprint is very recent.
