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
The proof is analytic. Parseval fixes the nonprincipal squared Fourier mass, expansion around its equal-radius value gives the exact norm-deficit identity, Fourier inversion of the autocorrelation gives the difference-set equality criterion, and a second Parseval identity yields the two-sided stability estimates.

`verify.py` provides corroborative finite checks only. It exhaustively checks every half-set of \(\mathbb Z_7\) and \(\mathbb Z_{11}\), checks random cyclic half-sets for the exact deficit identity and both variance inequalities, and verifies the quadratic-residue Fourier magnitude and difference multiplicities for every prime \(p\equiv3\pmod4\) below \(300\).

Finite tests cannot prove the universal statements. No unproved classification of difference sets is used: equality is characterized intrinsically by the difference-set condition, and the Paley construction is used only to show attainment for prime \(p\equiv3\pmod4\).
