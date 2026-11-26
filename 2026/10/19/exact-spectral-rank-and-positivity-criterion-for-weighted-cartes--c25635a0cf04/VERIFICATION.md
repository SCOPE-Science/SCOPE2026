---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Replayed via the star's adjacency spectral projectors E_0,E_+,E_- at 0,+nu,-nu. E_0 is the leaf-contrast projector. E_± have hub-hub entry 1/2, hub-leaf entry ±1/(2 sqrt(r)), and leaf-leaf entry 1/(2r). In the instantaneous mixing matrix the per-sign Fourier coefficients F_{±1}=E_0∘(E_++E_-) equal Q_L/r. F_{±2}=E_+∘E_- is (r+1)Q_R/(4r) by its radial row and zero row sums. The zero mode follows from M(0)=I: eigenvalues 1,(r-2)/r,(r-1)/(2r). Thus the stated polynomials and orthogonal sectors apply at every t. The commuting Cartesian summands give a tensor product before Cesàro averaging, and each finite Fourier term survives exactly when its weighted frequency is zero. All surviving weights in each sector are nonnegative; the resulting dimensions and kernel description follow without cancellations. All local constants are positive for r>=3, while an isolated contrast in any r=2 factor stays null at all weights. Off the bounded relation hyperplanes only zero modes survive, yielding the generic rank. Equal-frequency P3 powers allow exactly an even number of contrast factors, giving (3^d+1)/2; in P3 times K_{1,3}, the two distinct positive-frequency ratios restore dimensions two and one respectively, giving ranks 10 and 9 over the baseline 8.

## originality

PASS

Pass applies to the explicit three-sector weighted star-product spectrum and resonance rank/kernel classification. The general projector formula, synchronous tensorization and signed-frequency technique are established. Prior one-star work and the general projector identity already provide a short route to the robust positivity criterion alone; it is a consequence here, not the distinguishing advance. The extra radial sector and ±2 effective-frequency modes create rank jumps not covered by the inspected precedents.

## value

PASS

Stars are a natural class containing a singular one-factor average (P3) and positive ones. For coupled clock frequencies the exact kernel can shrink without disappearing, and different commensurabilities restore different dimensions, even in the smallest hybrid. The sector calculation separates that phenomenon from known factor positivity and supplies a reusable exact rank and nullspace test instead of re-diagonalizing each product Hamiltonian.

The dated certificate retains the supplied scientific assessment, sources and limitations.
