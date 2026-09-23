# Independent audit — 2026-09-22 campaign

**Source path:** `2026/09/08/005`  
**Audited repository state:** `253a0fe5d0217455660a277f9adb940030e567ad`  
**RESULT.md blob:** `95e96e352725cf2606ea414c618a588334aded9e`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean verification or expert attestation is claimed.

## Claim audited

A certified two-sided radial annulus 0.30 n <= |z| <= 0.75 n for every zero of the exponential partial sum s_n, for n=10,...,14.

## Correctness — PASSED

Independent high-precision root calculations and exact re-evaluation of the inner Rouché inequalities reproduced the stated n=10,...,14 annuli. The stored outer validated-winding certificate has large stated separation margins and its arithmetic structure was independently checked. The theorem is therefore supported within the documented floating-point/disc-arithmetic assumptions.

## Originality — PASSED

The original context incorrectly said classical work supplied no explicit finite-n enclosure. Peter Walker's 2003 note *The Zeros of the Partial Sums of the Exponential Series* (Amer. Math. Monthly 110, 337-339, DOI 10.1080/00029890.2003.11919971) gives explicit finite-degree zero information/regions, so that blanket statement is false. The audit did not locate the specific simultaneous radial certificate 0.30n <= |z| <= 0.75n for all zeros at n=10,...,14, nor its exact Rouché plus validated-winding certificate. With the context repaired to acknowledge prior finite-n results, this narrower certificate remains original relative to checked sources.

## Scientific value — PASSED

The repaired result gives explicit finite-degree two-sided radial bounds with deterministic certificates and margins, useful as regression data for validated polynomial-root computations and finite-n stability questions. Its value lies in that concrete certified annulus, not in claiming the first finite-n zero enclosure.

## Search and independent checks

Independent checks:

- independent high-precision root check for n=10,...,14
- exact recomputation of inner Rouché inequalities
- review of the outer winding certificate margins and arithmetic assumptions
- literature comparison with Walker 2003 and asymptotic zero-location work

Literature/search queries:
- `partial sums exponential zeros finite n enclosure Walker 2003`
- `zeros partial sums exponential series finite degree region`
- `0.75 n zeros exponential partial sum`

Sources:
- https://doi.org/10.1080/00029890.2003.11919971

## Repair / salvage attempt

RESULT.md context was corrected to acknowledge prior explicit finite-n zero results and to limit novelty to the specific two-sided radial annulus and its certificates.

## Final disposition

**REPAIRED.** The record remains accepted after the bounded wording/context repair above.
