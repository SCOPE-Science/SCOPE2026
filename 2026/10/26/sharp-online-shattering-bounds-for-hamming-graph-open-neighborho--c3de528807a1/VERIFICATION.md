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

# Verification of finite certificates

Run `python3 VERIFY.py WITNESSES.json` with Python 3 from the extracted file directory. This uses only the standard library and is self-contained. It tests all labels on all root-to-leaf paths of the two depth-three and one depth-two query trees against the actual open-neighborhood functions of their specified centers, not against an externally asserted answer table. The result is 8 paths at \(H(2,3)\), 8 at \(H(4,2)\), and 4 at \(H(3,2)\).

The separate exact Littlestone recurrence in the verifier computes the full version-space game on all graph instances with \(d=1\), \(2\le q\le6\); \(d=2\), \(2\le q\le5\); \((d,q)=(3,2),(3,3),(4,2)\). Every returned dimension agrees with the theorem. Additional finite stress tests directly inspect Hamming-neighborhood intersections and restricted coordinate-line traces for \(1\le d\le4\), \(2\le q\le5\), and \(q^d\le256\). The attached `VERIFIER_OUTPUT.txt` contains the actual recorded results ending in `ALL_CHECKS_OK`.

No code enumeration is claimed to certify every finite parameter. The all-dimensional and all-alphabet theorem relies on the structural proof in `RESULT.md`. In particular, the key fact that every second positive branch either lies on a coordinate line or has at most two centers is proved independently of the test range. Historical novelty is a scientific literature judgment with residual risks, not a result of executing this verifier. Independent audit status remains not performed.
