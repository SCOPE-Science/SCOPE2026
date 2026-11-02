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

# Reproduction

The self-contained `zinbiel_joint_census_check.py` program requires Python 3 and only the standard library. Execute:

```sh
python zinbiel_joint_census_check.py
```

It constructs binomial structure constants, uses actual finite-field additions and multiplications (not integer residue arithmetic for extension fields), builds both multiplication matrices directly, and computes ranks of all powers by elimination. It checks every tested Zinbiel identity coefficient without taking characteristic-dependent inverses of integers. The expected Jordan power-rank sequences and joint rank multiplicities are compared to the independent matrix computations.

Eleven configurations are exhaustive: \((p,q,n)=(2,2,2),(2,2,3),(2,4,2),(2,4,3),(2,8,3),(3,3,3),(3,3,4),(3,9,3),(3,9,4),(5,5,5),(5,5,6)\). Three additional configurations are sampled with a deterministic seed: \((7,7,7),(7,7,8),(11,11,12)\), with 2500 vectors each. For \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_9\) the program uses degree-2 or degree-3 polynomial quotients and validates multiplicative inverses; no prime-field shortcut is used.

The recorded final marker is `ZINBIEL_FIRST_MODULAR_JOINT_JORDAN_OK 14`. The exact captured output is embedded as a separate text artifact. Finite verification is not a proof of the infinite-family claim. The mathematical proof in `RESULT.md` supplies the all-characteristic argument, including both exceptional boundary cases and the possible extra right-multiplication top-degree entry.
