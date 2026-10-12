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
# Verification

Run `python3 verify.py` beside `certificate.json`.

The verifier enumerates every binary palindrome through length \(23\), tests prefix normality directly against all same-length factors, and checks the known count sequence. For every \(1\le m\le11\), it maps each even prefix-normal palindrome \(xx^R\) to \(x0x^R\), verifies the image is prefix normal, checks injectivity, and confirms that the all-one odd palindrome lies outside the image.

A second pointwise check replays the two factor reductions in the proof for every tested image: short center-crossing factors become extendable factors after deleting the inserted zero, while all long factors cross the center and reduce to factors one symbol shorter. The finite replay is a consistency check only; the infinite theorem rests on the symbolic factor argument in `RESULT.md`.

Independent audit has not been performed.
