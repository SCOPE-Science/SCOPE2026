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

The verifier generates all \(3834\) permitted nonerasing morphisms with \(|h(A)|=1\) and \(|h(B)|+|h(C)|\le5\). Since both formula fragments have length \(2+|h(B)|+|h(C)|\), every restricted fragment image has length from \(4\) through \(7\).

Engine 1 incrementally extends valid prefixes. A new square or formula fragment created by an appended letter must be a suffix, so only suffixes need be checked. Engine 2 independently tests every whole candidate for every square factor and every permitted morphism. The two complete level sets must agree through length \(46\).

The verified level counts end with \(36,30,24,18,0\) at lengths \(42,43,44,45,46\). All \(18\) length-\(45\) words are then rescanned directly, and their orbits under letter permutations and reversal are recomputed as sizes \(6\) and \(12\).

The verification concerns only the restricted square-free certificate language. Independent audit has not been performed.
