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

The proof is analytic in all odd field orders. It requires no external certificates. Run `python3 verify.py` for exact checks on prime fields of orders \(5,7,11,13,17,19\). The checker directly reconstructs each convolution Gram entry using modular inversion, verifies diagonal/total integer counts and nonconstant row sums, and tests the discrete variance inequality. It does not claim to exhaust general prime-power fields or determine the exact operator norm.

The equality \(\mathbf1^*A\mathbf1=2(q-1)^2\) follows by counting diagonal pairs and a unique off-diagonal solution per ordered \((u,v)\) with \(u\ne v\). The strict gap follows from \(2(q-1)^2\equiv2\pmod q\) and positive semidefiniteness.
