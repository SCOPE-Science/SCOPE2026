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

# Reproduction

Run `python3 verify.py` in this directory. No external libraries or network access are needed. The script uses exact integer coefficient arithmetic to establish the rational-matrix polynomial identities for all five listed cyclic orders, checks the critical six-state sign polynomial and exact rational witness, and reconstructs the completed Radau update independently by exact `Fraction` matrix inversion at selected steps. The expected terminal confirmation is `VERIFY_OK 930 exact polynomial/matrix assertions; cycles n=2..6`.

The complete arbitrary-step conclusions for orders \(2\le n\le6\) follow from the verified formal polynomial identities plus the sign arguments in `RESULT.md`. Independently, the theorem's statements for **all** orders \(n\ge6\) use the algebraic stability-function series and Fourier large-step limit. Finite enumerations alone do not establish those claims. The precise intermediate positivity windows for orders \(n\ge7\) are unproved.
