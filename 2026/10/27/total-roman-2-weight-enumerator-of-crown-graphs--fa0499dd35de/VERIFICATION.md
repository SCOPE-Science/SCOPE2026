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

# Reproducible checks

The complete enumerator is proved for all integers \(n\ge3\) in `RESULT.md`. The script `verify.py` independently reconstructs \(\operatorname{Cr}_n\) from its missing matching, tests each ternary labeling from the original definition, and compares full weight distributions for \(n=3,4,5,6\).

From a directory containing `verify.py`, execute:

```sh
python3 verify.py
```

The program uses only the Python standard library. The expected exact output is stored in `verify_output.txt`. It inspects \(729+6561+59049+531441=597780\) ternary assignments, not a sample. For the four graph sizes, the counts of admissible assignments are respectively \(328\), \(4422\), \(48974\), \(488266\), and the numbers of minimum-weight labelings are \(3,6,10,15\). It additionally checks nonnegative full polynomial coefficients, the two low-degree coefficients, the total-count formula, and the top coefficient through \(n=60\).

The combinatorial classification, counting argument and arbitrary-\(n\) proof are given in `RESULT.md`. No finite computation proves the infinite statement. The software checks do not constitute independent mathematical certification.
