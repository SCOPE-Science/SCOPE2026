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

# Direct checks

`python3 check_rc4.py` compares the predicted counts with direct generation of both channel outputs on every word of length \(d+4\), for binary displacements \(1\le d\le10\) and quaternary displacements \(1\le d\le5\). A separate exhaustive binary-word calculation verifies the expected number of pair collisions at each \(4\le n\le12\), with exact fractions. The checker asserts all equalities and prints `PAIR_SPECTRUM_RC4_PASS` on success.

The proof does not rely on extrapolation from the finite checks. It covers every even \(q\ge2\), all \(n\ge4\), and all eligible site separations. It excludes nonuniform inputs, complements with fixed points and multiple-step errors. Independent audit evidence is absent.
