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

The accompanying `checker.py` uses standard Python only. Execute `python3 checker.py`. It generates every reduced-row-echelon subspace of the ambient vector space and separately tests closure under the multiplication \((v,t)\circ(w,s)=(0,v\otimes w)\), then ideal closure on both sides against the generators. The program also evaluates the symbolic Gaussian counting formulas independently.

The exhaustive cases are \((n,q)=(1,2),(1,3),(2,2),(2,3)\). Their complete ambient Grassmannians contain \(5,6,2825,56632\) subspaces, respectively. Expected and observed subalgebra counts are \(3,3,221,949\), and expected and observed ideal counts are \(3,3,77,229\). In each case equality is checked **for every joint** \((r,z)\), not only the totals. The program prints `VERIFY_OK` if every comparison succeeds.

The implementation uses prime-field modular arithmetic in its finite exhaustive cases. It does not enumerate extension fields or arbitrarily large dimensions. The formulas in the theorem apply to all prime powers because the proof is linear-algebraic. No finite search is used as an infinite proof. A mathematical independent audit remains unperformed.
