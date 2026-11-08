---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For each r and cyclic shift d the inverse DFT of intensities equals C_r(d)=Σ_n x_n conjugate(x_{n−d}) ω^{r(n²−(n−d)²)} with normalization 1/p. For d≠0, directed Sidon means precisely one nonzero ordered product P_ab at a−b=d; no cancellation, so D is common and |D|=s(s−1). Ratio C_{r1}(d)/C_{r0}(d)=ω^{(r1−r0)d(a+b)} determines a+b (p odd and distinct masks), hence both ordered endpoints and all P_ab. With s≥3, P_ji P_ik/P_jk=|x_i|² reconstructs the rank-one Hermitian Gram matrix up to global phase; with s=2, energy E and pair product P give the two roots for squared moduli, and swapping moduli gives two classes unless equal; with s=1 all p positions identical. For any phase-only masks, the s=1 site and s=2 magnitude-swap obstructions persist. With one mask, masked-signal translation preserves intensities, translates nonempty proper Sidon support S; p prime makes S+t≠S for nonzero t, so one mask cannot be injective when s≥3 exists (p≥7). Independently checked p=7 {0,1,3} ordered pair decoding and phase-only swap invariance using exact residues. The proof handles all p, not just finite experiments.

## originality

PASS

The relevant aliases are chirp-coded phase retrieval, Sidon-label tomography, quadratic Fourier masks and coded autocorrelation; overlapping unmasked Fourier ambiguity and Gabor tomography are not identical measurement models. None of the more general sounding phase-retrieval theorems implies the exact deterministic minimal two-chirp measurement design; measurement sets and quantifiers differ. The new reconstruction and obstruction claims are strictly more specific than, and do not follow logically from, the checked general phase retrieval results. Best-of-knowledge priority assessment with listed risks, not certification.

## value

PASS

An exact uniform deterministic coded-diffraction fiber theorem on natural Sidon/Golomb-ruler sparse supports, including absolute support recovery, arbitrary complex amplitudes, and sharp information-theoretic one/two-support obstructions. This materially separates all-support phase retrieval from generic recovery and establishes two-mask minimality in the nonvacuous regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
