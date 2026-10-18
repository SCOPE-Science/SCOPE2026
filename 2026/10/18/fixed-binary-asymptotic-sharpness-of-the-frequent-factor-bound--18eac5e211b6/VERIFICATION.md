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

The proof constructs a binary de Bruijn cycle of order \(d\) using an Eulerian circuit, verifies that every cyclic phase has a distinct factor of every length at least \(d\), and bounds its occurrences in the length-\(n\) prefix by the minimum residue-class count. An integer cutoff ensures strict frequency greater than factor length. Elementary inequalities with \(d=\lfloor\tfrac12\log_2(n/\log_2 n)\rfloor\) complete the estimate for every integer \(n\ge64\).

`verify.py` is a standalone Python 3 checker using a separately coded cyclic construction and naive factor enumeration. Running it produced `output.txt`. It checked fifteen constructed words: twelve automatically selected orders at lengths 64, 65, 79, 101, 127, 128, 191, 255, 256, 257, 333, 511 and three fixed-order checks (200, 3), (350, 4), (1000, 5), the binary cycle property for all orders 1 through 8, and 20,919 additional integer-cutoff instances up to length 999,054. The checker is supportive finite evidence, not proof of the asymptotic statement. No external or independent scientific validation is asserted.
