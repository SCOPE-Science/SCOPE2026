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

The mathematical proof is in \(`RESULT.md`\). Run \(`python3 verify.py`\) with Python 3 and no external packages. For exact finite ranges and recorded output see \(`verification_output.txt`\).

The script directly assembles the binary adjacency map and computes binary ranks, independently implements Laurent-polynomial gcds corresponding to the stated Smith factors, and enumerates complete state orbits through nine cycle positions. It checks 2,346 exact rank instances, 46 exact order instances, 3,040 symbolic-gcd dimension comparisons, and 349,504 labelled states across \(3\le n\le9\) (29 period-class checks). For every odd \(n\) in the exhaustive range, every labelled state is also checked against the proposed parity/affine period-doubling rule. It additionally tests the explicit \(n\)-step transvection identity at sampled states.

These tests are not external certification or a proof for unbounded \(n\), and the report does not assert such a proof from finite sampling. General correctness rests on the Laurent-polynomial Smith factor calculation and the exact invariant used to establish the affine involution. The historical novelty assessment remains qualified by inaccessible potentially broader literature.
