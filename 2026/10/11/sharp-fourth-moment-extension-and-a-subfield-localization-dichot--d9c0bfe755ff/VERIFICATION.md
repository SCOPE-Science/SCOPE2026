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

# Verification record

The general proof uses the explicit inverse-map pair-fiber classification and the stated \(\ell^2\)-normalized fourth-moment convolution expansion. For odd extension degree, check the equality cases in \(\lvert\sum f(x)^2\rvert\le\sum\lvert f(x)\rvert^2\) and \(\sum\lvert f(x)\rvert^4\ge q^{-1}(\sum\lvert f(x)\rvert^2)^2\). For even degree, check the three exceptional unordered-pair collisions per \(\mathbb F_4^\times\)-orbit, the coefficient \(8\) in the cross terms, the bound in the proof, the optimizer of the resulting concave quadratic, and the final factored deficit.

Run `python3 artifacts/verify.py` with Python 3 standard library. This performs 54 exact weighted random tests, exact fiber checks for fields of orders \(2,4,8,16,32,64\), explicit sharp packets, and negative phase witnesses. Expected output:

`VERIFY_OK fields=F2,F4,F8,F16,F32,F64 exact_weighted_fibers=54 normalized_sharp_packets=PASS equality_phase_boundary=PASS`

No finite test proves an assertion over every extension degree. The direct algebraic proof is indispensable. No independent audit has been performed.
