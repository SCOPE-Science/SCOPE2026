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

The mathematical claim follows from the four proof steps in `RESULT.md`. Finite test cases are independent checks, not exhaustive proof for all primes.

Run `python3 checks/verify_conic.py` with Python 3 (standard library). It enumerates every shift and every frequency of \(\mathbb F_p^2\) for each of the two quadratic-form types at primes \(5,7,11,13,17\). It reconstructs the conic, all translated intersections, and integer vectors of phase-residue counts. Equality of all \(p\) residue counts is the exact algebraic criterion for a vanishing sum of \(p\)-th roots of unity; no floating-point threshold is used to establish zero/nonzero. The script additionally tests intersection populations, ranks, and numerical Kloosterman and cosine magnitudes. Compare the script output to `checks/check_output.txt`.

Run `python3 checks/dense_svd.py` with NumPy for a separate direct matrix check of the operator normalization and singular-value multiplicities. It constructs all 625 measurement rows at \(p=5\), \(d=1\), and compares the full dense numerical SVD with all separately computed ambiguity moduli. The reproduced output in `checks/dense_svd_output.txt` gives complex rank 225, largest singular value 4, smallest nonzero approximately 0.381966011250, and maximum array discrepancy about \(7.6\cdot10^{-15}\). Floating-point agreement does not certify an infinite family.

Not checked: all larger primes by enumeration; prime-power extension fields, composite moduli, and weighted windows (outside the claim). Neither numerical testing nor self-review constitutes independent auditing.
