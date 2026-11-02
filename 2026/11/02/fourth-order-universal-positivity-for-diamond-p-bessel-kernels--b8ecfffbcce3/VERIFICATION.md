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

The proof uses the defining convergent series and the published positive order-raising integral for the diamond case. Its critical exact identity is the order-four divided difference of \(H_r(x)=(1-\sin(rx)/(rx))/x^2\). The strict sign is justified for all positive radii by the inequality \(t(2+\cos t)>3\sin t\) for \(t>0\), proved by derivatives on \((0,\pi]\) and a direct bound afterward. Four explicit trigonometric substitutions give the negative smaller-order witnesses.

Run `python3 CHECK.py` to replay 184 supplementary rational and numerical assertions. These tests are not substitutes for the proof's quantified infinite steps. The exact range of nonintegral orders below four is unproved. Independent audit has not been performed.
