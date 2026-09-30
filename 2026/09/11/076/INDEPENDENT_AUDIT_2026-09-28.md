# Independent Audit — 2026/09/11/076

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `49d739a69ebf38438fd87f2b5ec6938d758923a0`  
**Audited current source tree:** `49d739a69ebf38438fd87f2b5ec6938d758923a0`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** repaired

The current `main` record tree matches the assignment tree SHA.

## Correctness

PASS FOR THE REPAIRED CENSUS. I independently reconstructed the 20-orbit model. Exactly 29,420 first-row-group states survive; completion histogram 45:1125, 55:2750, 65:7500, 70:7000, 75:6500, 90:4500, 225:45 has weighted sum 2,082,000. Centralizer transitivity gives 20,820,000 unnormalized. The earlier 65-specimen mate claim is removed because its artifacts are absent.

## Originality

SUPPORTED, NARROW. Targeted searches did not locate the exact 2,082,000 count. Egan–Wanless stops at order 9 and Gill–Wanless studies a different relation-defined subset. This supports the exact C5-equivariant census as a distinct finite datum without treating search failure as proof of priority.

## Scientific value

MEANINGFUL EXACT CENSUS. The fixed-point-free diagonal C5 action is a natural symmetry stratum for order-10 Latin-square/MOLS searches; the exact denominator is reusable for future mate and triple searches.

## Independent checks

- 20-orbit parametrization independently reconstructed
- exact 2,082,000 normalized census independently recomputed
- completion histogram cross-check
- record tree unchanged; cited sample artifacts absent

## Limitations

- The exact census was independently verified; the prior 65-specimen mate claim was not.
- The specimen/search artifacts cited by the prior package are absent.
- No isotopy-class census or C5-equivariant triple decision is claimed.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/11/076
- https://arxiv.org/abs/1406.3681
- https://arxiv.org/abs/2204.10996

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
