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

The coefficient encoding, finite total search domain, orbit group and derivation of the Frobenius closed-point counts are specified in `RESULT.md`. The executable programs and actual stdout records in this package are:

- `verify_groebner.py` and `verification/verify_groebner.stdout.txt`: all four product charts, exact unit-ideal smoothness over the algebraic closure, complete 804-pencil census and 13 orbit classes, transversality of every base scheme, and full Frobenius partitions through field degrees one to eight. Requires Python 3 and SymPy.
- `verify_f16.py` and `verification/verify_f16.stdout.txt`: independently implemented field arithmetic in \(\mathbf F_{16}\), a second 144-form smoothness classifier, 804 pencils, absence of all-smooth nets, and 13 orbits via row/column/permutation actions on the nine rational grid points. Requires Python 3 only.

The independent finite-extension test is exhaustive, not merely suggestive: on each chart a bidegree-\((2,2)\) equation has \(f_x\in\mathbf F_2[y]\) and \(f_y\in\mathbf F_2[x]\), both of degree at most two. If both are nonzero, any common root has coordinates in \(\mathbf F_4\). If one vanishes identically, solving the equation in the other coordinate yields a quadratic over \(\mathbf F_4\), whose roots lie in \(\mathbf F_{16}\). If both derivatives vanish identically, the equation is a square of a bilinear section, which has a zero already over \(\mathbf F_2\). Thus any geometric singularity is visible over \(\mathbf F_{16}\).

The Frobenius-cycle recovery does not assume that sampling a finite extension is sufficient to prove geometric reducedness. That point is established separately by four-chart Gröbner unit-ideal checks of \((f,g,f_xg_y+f_yg_x)\) and the intersection product \((2,2)\cdot(2,2)=8\). The field-extension samples then exhaust all possible closed-point degrees because the resulting scheme is reduced and has length eight.

Both verification programs were executed from their actual packaged paths and their stdout was preserved. No external specialist validation, independent audit or formal proof assistant certificate is claimed. Limited bibliographic coverage and exact small-field scope are specified in `RESULT.md`.
