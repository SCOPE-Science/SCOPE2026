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

# Mathematical verification

The proof establishes an exact weighted-monomial singular system: \(T_\rho\) maps each normalized input monomial to a scalar multiple of a different normalized target monomial. This supplies the nonzero singular values with exact multiplicities. Gamma-ratio asymptotics and an explicit summable bound justify exchanging the transverse-degree sum with the counting-function limit. The coefficient's Abelian asymptotic follows from \(A_b^{p_*}\sim m^{-(n-1)}b^{n-1}\).

The included `check_spectral.py` performs numerical diagnostics of the gamma expression, a closed type-four coefficient, and truncated counting functions. Use `python check_spectral.py` after installing the two packages in `requirements.txt`. These checks require no external data or third-party paper content. Numerical agreement at finitely many cutoffs is evidence about implementation, not a proof of the infinite Weyl law. The analytic argument in RESULT.md is the proof.

The assertion concerns fixed contraction \(\rho<1\) before the spectral threshold tends to zero; the divergence as \(\rho\uparrow1\) is taken afterward. Simultaneous scaling is unproved. No independent mathematical audit has been performed.
