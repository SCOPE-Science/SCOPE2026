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

# Reproduction and verification

The complete proof and exact parameter range are in `RESULT.md`. The claim is an exact analytic theorem; numerical or finite-grid tests are not used to infer the continuum phase maximization.

Run `python3 verify.py` using a standard Python 3 installation, with no third-party dependencies. The program checks \(K^2=3I_4\) and Hermiticity entry by entry, the four exact phase saturators and sixteen boundary correlation entries, the complete-basis dephasing Fourier twirl, and all fourth-root-of-unity phase triples. Its expected success line is:

`VERIFY_OK conference_identity=16 boundary_gram=16 finite_phase_grid=64 four_extremizers=4 dephasing_twirl=16`

**What remains mathematical rather than computational:** The inequality for arbitrary continuous phases is the displayed sum-of-squares identity in the proof. Exactly four projective equality points follow from its equality cases and phase alignment. The witness lower bound applies to all random-unitary decompositions because fixing every basis projector forces each unitary summand to be diagonal. The boundary ensemble and its unique weights are exact algebraic identities. Finite tests cannot establish the global priority of this result; independent scientific audit and broader priority verification have not been performed.
