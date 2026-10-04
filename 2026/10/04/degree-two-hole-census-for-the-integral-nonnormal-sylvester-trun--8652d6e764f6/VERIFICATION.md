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

The verification is exhaustive for the finite claim.

First, the order-16 Sylvester character matrix is reconstructed from \(v_r(j)=(-1)^{r\cdot j}\) for row labels \(r\in\mathbb F_2^4\) and nonzero coordinate labels \(j\in\mathbb F_2^4\).  Every source-lattice point in \(P_{5,1}\) is a sign vector, so `verify.py` tests all \(2^{15}\) possibilities and finds exactly \(9552\) feasible summands.

Second, every degree-two target is uniquely \(2q\) with \(q\in\{-1,0,1\}^{15}\).  The script tests all \(3^{15}\) such vectors against all sixteen inequalities and finds \(6350363\) feasible targets.  A carry-free base-three code marks every sum of two feasible source points; exactly \(6215123\) feasible ternary targets are decomposable.  The difference is \(135240\).

Third, the script applies generators consisting of three adjacent basis swaps, one elementary transvection, and four basis translations.  These generate \(\operatorname{AGL}(4,2)\).  Breadth-first traversal partitions the complete hole set into orbit sizes \(840,13440,26880,40320,53760\), whose sum is \(135240\).  The source paper's displayed hole is additionally checked to lie in the orbit of size \(26880\).

Run `python verify.py`.  A successful replay ends with `VERIFY_OK`.  The script requires Python 3 and NumPy.  Its computation proves only the finite degree-two census stated here; it does not test or certify higher degrees.
