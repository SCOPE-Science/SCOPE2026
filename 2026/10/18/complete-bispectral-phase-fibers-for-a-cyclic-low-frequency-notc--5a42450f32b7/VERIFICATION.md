---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For arbitrary nonzero complex Fourier coefficients on S={-r..-2,2..r} modulo N, r>=3,N>2r, equality of power spectra leaves unit phase ratios; every nonzero full-bispectrum triple imposes exactly e_a+e_b=e_c in an integer quotient lattice. The Pontryagin characters of this lattice give the entire free phase fiber, no unstated genericity. For r>=6, elementary unwrapped triples force e_k=k t and a wrapped positive triple exists exactly if N<=3r, imposing Nt=0; absent wrap yields free Z and T. For r=3,4,5, the explicitly specified integer relation matrices have Smith forms yielding the stated T^d x finite torsion table. Independently rebuilt full relations and Smith forms for all 57 (r,N) cases with r=3..8 and 2r<N<=3r+4, matching all cases including r=4,N=10 torsion N and r=5,N=14,15 torsion 2,3. Translation forms exactly mu_N because 2 and 3 are supported. The conclusion assumes both complete power and full bispectrum, not bispectrum alone, and no interior coefficient vanishes.

## originality

PASS

Kakarala's nonvanishing Fourier/group-support uniqueness hypotheses do not encompass a support missing 0 and +/-1. Pinilla--Mishra--Sadler 2021 finite-support recovery Proposition 1 uses nonzero central Fourier coefficient in its relevant construction. The closest published independent asymmetric-band theorem was read in full from its Git result: mask {-s..-1,1..r} includes first harmonics and has a single free-phase chain; the submitted mask omits both +/-1, leading instead to exceptional high-dimensional/torsion phase fibers and a distinct threshold N=3r at r>=6. Shared character-lattice idea is credited, not novelty. A broader spectral-gap phase theorem could cover it; original 1984 phase-estimation paper was not read fully.

## value

PASS

The absence of DC and first harmonics invalidates standard sequential phase recovery and yields a genuine identifiability boundary. A complete ambiguity-group classification (including mixed torus/torsion exceptions) tells exactly when all signals on a natural symmetric frequency-notch mask are translation identifiable, and when infinitely many inequivalent signals share all noiseless second and third spectral invariants. Both necessary/sufficient boundary and precise finite torsion are independently useful, not a renamed phase-translation lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
