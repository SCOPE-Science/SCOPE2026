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

# Reproducibility of the finite-alphabet two-deletion law

Run `python3 verify.py` using Python 3.9 or later; only the standard library is required. The program computes **sets of distinct deletion outputs** directly, rather than counting deletion-position pairs; independently evaluates the number of constant runs, long runs and equal-neighbor singleton patterns; compares complete distributions from edge-pattern and transfer-state enumeration; and checks both moments with exact rational arithmetic.

The direct enumerations cover every input word at alphabet sizes \(q=2,3,4,5,7\) and all lengths respectively \(2\)–\(12\), \(2\)–\(8\), \(2\)–\(7\), \(2\)–\(6\), and \(2\)–\(5\). Additional independent coefficient calculations and mean/variance checks cover alphabets \(q=2,3,4,5,8\) and lengths \(2\)–\(13\). All assertions must succeed.

The exact distribution at \(q=3\), \(n=5\) is verified as pairs of (ball size, number of source words): (1,3), (2,12), (3,24), (4,30), (5,42), (6,48), (7,42), (8,18), (9,18), (10,6). These sum to \(3^5=243\). The code does not numerically certify the all-length identity or asymptotic theorem; these are established in the separate mathematical proof.
