---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and its limits

The exact proof in `RESULT.md` handles every integer lattice frequency. It reduces three-adically, bounds every mask by an explicit trigonometric inequality, identifies the first nonextremal digit, gives a rigorous rational separation bound, and reduces every cyclotomic mask numerator modulo three to prove nonvanishing. These proof arguments, rather than a finite search, support infinite quantifiers.

The standalone standard-library checker `artifacts/verify.py` can be run using `python3 artifacts/verify.py`. Its successful output includes `CARPET_FOURIER_CERTIFICATE_OK 12306 mask_and_frequency_checks`, and displays two nontrivial Fourier values with 16 decimal places. It checks mask identity on a rational grid, nine-adic separation for all reduced residue pairs, coefficient ordering on the \(85\times85\) frequency box (excluding the origin), digit-ring residue calculation and a rigorous rational lower bound of \(515/7776>1/16\).

The finite checks provide independent numerical and algebraic consistency evidence, not an exhaustive computational proof or external mathematical certification. The literature-access and historical-novelty qualifications are described in `REVIEW.md`.
