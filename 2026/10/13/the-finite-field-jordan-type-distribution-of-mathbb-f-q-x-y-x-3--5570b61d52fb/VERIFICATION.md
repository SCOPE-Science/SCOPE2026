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

# Reproducible verification

Run `python3 check_jordan.py` in the same directory as this file. The program constructs \(9\times9\) multiplication matrices over \(\mathbb F_q\), directly multiplies polynomials modulo \((x^3,y^3)\), and computes Jordan type from ranks of all powers. It checks against the structural coefficient classification and against the theoretical total counts. Observed successful output includes:

```
EXHAUSTIVE_OK 2 256
EXHAUSTIVE_OK 3 6561
SAMPLE_OK 4 2000
SAMPLE_OK 5 2000
SAMPLE_OK 7 2000
VERIFY_OK_JORDAN_CI33
```

The first two lines represent actual complete enumerations of all \(q^8\) elements for \(q=2\) and \(q=3\). The following three lines are deterministic random samples, **not** exhaustive tests. Field \(\mathbb F_4\) is represented with the irreducible relation \(t^2+t+1=0\). The proof in `RESULT.md` covers all prime powers and does not infer universal validity from finite experiments. The code uses only the Python standard library. No independent audit has been performed.
