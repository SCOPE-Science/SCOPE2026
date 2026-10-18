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

# Reproducibility and limits

Run `python3 verify.py` with Python 3.9+ and its standard library. The complete 4-mode proof is in `RESULT.md` and does not depend on enumerating finitely many supports.

The standalone code groups the exact momentum-energy of all size-three multisets for every four-element subset of the bands \(\{0,\ldots,N\}\) at every \(4\le N\le26\); it checks the exact ordered energy \(256\) or \(274\), the uniqueness of the exceptional collision, and the formula for the number of exceptional supports. It also checks the nonresonant sharp deficit on three grids of rational coefficient energies and checks the critical point and radical sixth-moment value by exact arithmetic in the quadratic number field \(\mathbb Q(\sqrt{97})\).

On the packaged script the observed output was:

```
VERIFY_OK 98279 quadratic 3-fold support energies; 686 resonant supports across bands; 441 rational stability checks; exact radical optimum
```

The computational checks are **not** an exhaustive test over all integer supports, all complex coefficient vectors or all real energy parameters; those claims are deduced in the analytic proof. No independent audit or formal external certification was performed.
