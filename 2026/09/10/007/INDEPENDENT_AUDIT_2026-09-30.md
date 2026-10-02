---
audit_date: 2026-09-30
status: passed
---

# Independent mathematical audit

## Final claim

For the nine-vertex Limonchenko-Panov reference complex K0 over Q, H^3 of the moment-angle complex vanishes, every nonzero Hochster support has at least three vertices, the lowest positive cohomology degree is 5 and the top degree is 14; hence no nonzero positive-degree four-fold Massey product can exist, while the published nontrivial triple product occurs at the sharp order-3 boundary.

## Correctness — PASS

Using the exact 15 minimal non-faces printed in Limonchenko-Panov Theorem 2, a fresh rational simplicial-homology sweep over all 512 induced subcomplexes reproduced the cohomology profile H^0=1, H^5=4, H^7=3, H^8=10, H^9=3, H^10=4, H^11=13, H^12=21, H^13=21, H^14=8, with no H^3 and minimum nonempty support size 3. Thus four disjoint nonzero supports would require at least 12 vertices, and independently the Massey degree bound gives at least 4*5-2=18>14. The inspected second homology engine agrees on the full complex and sampled induced subcomplexes.

## Originality — PASS

Limonchenko-Panov Theorem 2 supplies this exact K0 and proves a nontrivial triple Massey product, but does not state the global no-four-fold consequence, the Hochster support census, or the 5-to-14 cohomological degree gap used here. Grbic-Linton construct higher Massey products in other moment-angle complexes; that broader construction does not imply a four-fold product at K0. A published-corpus search returned the present sharp-boundary result as the direct match for this K0.

### Equivalent formulations

The object is exactly the same reference complex; the new statement asks whether its hierarchy continues to order four.

### Broader coverage

Existence in other complexes does not force existence in K0, whose cohomology range supplies a specific obstruction.

### Exact database or table comparison

No prior K0-specific no-four-fold table was located.

### Claim versus prior implication

The triple theorem alone does not imply the sharp no-four-fold boundary without the additional cohomology calculation.

## Value — PASS

Determining the exact next-order boundary at a published reference example with a known nontrivial triple product is a motivated structural question in the Massey hierarchy. The conclusion is a sharp obstruction at that specific complex, not a generic restatement that some high-degree cohomology vanishes.

## Sources inspected

- Git tree/blobs: RESULT.md, target verifier, independent homology engine and status files. Reconstructed the minimal-nonface model and independently swept all induced subcomplexes.
- Limonchenko-Panov, arXiv:2201.12779: full PDF Theorem 2 and proof page. Confirms the exact 15 minimal non-faces and published nontrivial triple product; no four-fold boundary is stated.
- Grbic-Linton, arXiv:1911.07083: abstract and scope. Provides broad higher-Massey constructions, not this K0 boundary.

## Residual risks

- The audit is over rational coefficients only. The primary PDF contains a dimension sentence inconsistent with the printed minimal-nonface list; the audited claim follows the explicit list and does not use that sentence.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
