---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For all real k>1 with s=sin^2(k), reproduce the original source Eq. (9), whose denominator (k^2-1)^2*s is positive away from n*pi. Independent SymPy polynomial reduction with x=k^2 yields (F+2)D=-8(1-(x+1)s)(x-(x+1)s) and (F-2)D=-4(2s-1)((x+1)^2*s-2x), both identities exactly zero residual; a=1/(x+1)<c=2x/(x+1)^2<1/2<b=x/(x+1). Hence the two exact intervals are [a,c] and [1/2,b]. Original secular equation excludes k=n*pi; k=1 is outside claimed exact domain. For large n, implicit-root/Taylor expansion near n*pi gives summed narrow-band measure 2(sqrt2-1)/(n*pi)+O(n^-2); expansion near (n+1/2)pi gives central removed-gap measure 2/((n+1/2)pi)+O(n^-2). A full phase cell contributes pi/2 + [2(sqrt2-1)-2]/(n*pi)+O(n^-2). Absolute summability of remainders and harmonic summation prove K/2-2(2-sqrt2)/pi*log K+O(1), including bounded partial cells. The exact 2100-byte verify.py file was independently reconstructed to its Git blob SHA and replayed, reporting VERIFY_OK, with finite-cutoff slope -0.3729231537 vs exact -0.3729232286. Direct independent brentq boundary checks at n=50,200,1000,4000 agree. These finite checks are corroborative, not infinite proofs.

## originality

PASS

Best-of-knowledge PASS for the exact two-branch half-flux momentum criterion and the nonzero second-order logarithmic deficit in this precise model. The 2023 model paper supplies the original half-flux Floquet inequality (Eq. 9), its narrow-band first-order width and the leading momentum density 1/2, but not the finite-cutoff central gaps or their competing harmonic contribution. The 2013 momentum-density paper concerns the leading limiting measure for periodic graphs; it does not determine this model-specific correction. A separately published triangular preferred-orientation graph has an analogous logarithmic correction but a distinct coupling/geometry and no implication for the magnetic square lattice. Actual Resultary and literature searches disclosed no covering exact formula; this is not proof of historical priority.

## value

PASS

The same magnetic square quantum graph has a naturally defined high-energy momentum-band density 1/2 in the 2023 primary literature. The precise finite-K deviation is a motivated open quantitative spectral question: the previously discussed narrow integer-centered bands increase the measure at harmonic order, while previously unquantified half-integer-centered wide-band holes decrease it at a larger harmonic rate. The exact two-branch interval condition resolves the geometry of both sets, and the coefficient -2(2-sqrt2)/pi gives a nontrivial universal second-order rate for the fixed half-flux/length normalization. This is a mathematically meaningful structural and asymptotic refinement, not just a renaming of the leading limit or an arbitrary finite cutoff. The result is specific to half flux and does not purport to solve arbitrary rational/irrational flux spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
