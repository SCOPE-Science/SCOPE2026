---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed the four-qubit Pauli inversion identity P12+P13+P14=1+(A1+tau)/2>=1 with tau the nonnegative squared spin-flip overlap. The 4x4 Gram formula 256 P=64+2 sum_{r<s}|sum_{c=0}^3 i^(f_rc-f_sc)|² and equal parity of each integer real/imag part imply purities in multiples 1/64; at least one is >=ceil(64/3)/64=11/32. The displayed 16-digit phase witness has three exact numerator-88 purities and vanishing four one-qubit coherences. A unique subtraction of the five coefficients of affine phase gauge fixes f at 0,1,2,4,8, leaving exactly 4^11=4,194,304 classes. Independently compiled and executed a separately coded full C++ enumeration over all 4^11 canonical classes using exact integer Gram overlaps (not the stored checker); it found minimum 88/256, exactly 96 minimizers all with (88,88,88), and among all 2048 real-sign classes minimum 96/256 with 272 minimizers. Separately generated the complete transformed canonical orbit of an optimizer (24 permutations ×16 bit flips ×2 conjugations), yielding exactly 96 distinct classes. The 16 local-Z labels form an orthonormal Walsh basis for any flat vector. This is truly exhaustive for a finite search space, not extrapolation.

## originality

PASS

Best-of-knowledge PASS. Pauwels–Gühne arXiv:2608.21185 fully accessible as mathematical HTML despite its unavailable PDF; Sections I–V and appendices address local encodings and globally entangled four-qubit measurements but not optimizing reduced purity over the discrete Z4 flat-phase alphabet nor enumerating all 96 gauge classes. Gour–Wallach supply the general four-qubit purity/linear-entanglement benchmark; Chen–Wang treat ±1 hypergraph-state families. Resultary search hits concern Fourier fourth-moment problems on cubes, not the three quantum reduced-purity Gram matrices. No inspected prior statement implies the constrained frontier and orbit count. Priority under an unindexed discrete-state classification remains a risk.

## value

PASS

PASS: Equal-magnitude four-qubit fiducials with quarter-root diagonal phases form a natural finite preparation alphabet. The exact worst balanced-cut purity optimum quantifies the gap to unrestricted entanglement, and the complete optimizer census plus single orbit provides a usable classification for choosing entangled measurement fiducials. Real-only phase control strictly worsens the optimum. The orthonormal Z-basis consequence is known and is not the asserted new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
