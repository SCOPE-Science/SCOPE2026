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

## Reproduction
Run the two programs from the same directory:

```
python verify_cubic_intersections.py
python verify_independent_count.py
```

The first program requires Python 3 only; the second requires SymPy. Compare output to `primary_output.txt` and `independent_output.txt`. No data downloads or other package files are required. The coefficient monomial order is explicitly defined in both scripts. All evaluation is in characteristic two.

**Checked facts:** exact \(1023\)-form search, \(522753\) unordered distinct pairs, \(13965\) excluded unordered pairs, \(508788\) admissible unordered pairs, seven-bin frequency distribution, \(210\) extremal unordered pairs, five complete projective orbits of orders \(84,28,28,28,42\). Restriction-pattern counting and exact gcd spot checks are an independent implementation cross-check, not an external scientific audit.

**Limits:** The theorem is finite and restricted to the binary field. The gcd spot-check is not substituted for the complete algebraic degree argument. No claim of publication priority, external review, or infinite-field extension is made.
