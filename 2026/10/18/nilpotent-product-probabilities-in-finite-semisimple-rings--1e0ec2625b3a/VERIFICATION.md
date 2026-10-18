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

# Verification evidence and scope

**Universal proof checks.** Reconstruct the Fitting decomposition into invariant nilpotent and invertible subspaces; check that the number of ordered dimension-\(j\) direct-sum splittings is \(G_r/(G_jG_{r-j})\). This gives the nilpotent census \(q^{r^2-r}\). Check the fixed-rank factor normal form and nilpotency of the upper block matrix, then identify the probability \(q^{-\operatorname{rank} C}\) with kernel containment of an independent uniform vector. Starting from the rightmost factor, every fresh uniform matrix acts uniformly on a nonzero vector; zero is absorbing. The resulting \(m\)-fold survival probability is \((1-q^{-n})^m\). The direct-product proof uses the independence of block coordinates and the componentwise nilpotence criterion.

**Exact reproducibility.** Run `python verification/verify_nilpotent_products.py` with standard Python 3 (no extra packages). The checker enumerates all matrices in the tested prime-field rings, repeatedly convolves weighted product counts, determines nilpotency from the \(n\)-th matrix power, and compares exact integer numerators and denominators with the claimed formula. A captured successful run appears in `verification/exhaustive_counts.txt`. Its complete cases are \((n,q,m)=(1,2,1..4),(2,2,1..4),(2,3,1..3),(3,2,1..3)\).

**Limitations.** This computation alone cannot verify an unbounded integer range, a nonprime finite-field order, or the semisimple direct-product construction. Those are addressed by the proof, not by extrapolation. No independent third-party audit is claimed.
