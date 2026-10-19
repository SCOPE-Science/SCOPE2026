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

Execute `python3 verify.py` from a directory containing the attached `verify.py` file. The program needs only Python 3 and its standard-library `fractions` module. It directly constructs each transient minority-count transition matrix from the mathematical update, differentiates the matrix recursion, and checks exact rational inequalities (no floating-point comparisons).

Recorded output from execution of the attached program:

```
PASS n=3..16 mu=0,1/4,1/2,3/4,1: 5292 stochastic-order comparisons, 6615 exact derivative-sign tests, 5145 exact state comparisons.
PASS n=2 exception and n=3 geometric closed form.
```

The first statement represents checks through horizon 20. In the strict survival comparisons and derivative checks the horizon condition is evaluated as \(t\geq r\), where \(r\) is the initial minority count. The complementary \(t<r\) equalities were also checked. The program's direct exact matrix construction is a finite consistency test. The general theorem, including arbitrarily large populations and horizons and all real mutation probabilities in the stated range, requires the proof given in RESULT.md.

The mathematical evidence does not verify biological applicability beyond the stated assumptions. Independent external verification is not performed.
