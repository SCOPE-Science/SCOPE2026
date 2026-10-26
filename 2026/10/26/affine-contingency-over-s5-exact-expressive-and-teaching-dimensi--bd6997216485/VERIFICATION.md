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

# Verification of the finite algebra computations

Run `python3 checker.py` from the directory containing this report and the checker. It uses the Python 3 standard library only. It enumerates all nonempty subsets of the Boolean valuation cube for \(k=1,2,3,4\), and each possible distinguished vector, up to the stated cardinality cutoff. It forms the Boolean evaluation matrix of the \(k+2^k\) normal-form generators and computes its rank by exact bitwise Gaussian elimination.

Observed ranks, with the maximum number of worlds restricted first to \(k\) and then to \(k+1\), are respectively \((2,3)\), \((5,6)\), \((10,11)\), and \((19,20)\). The program checks that the explicit fixed teaching family has full rank in each case. Direct evaluations of randomly generated nested contingency terms are compared to their inductively computed normal forms for \(k=1,2,3\), using 1,200 deterministic random terms at each size. The run finishes with `ALL CHECKS PASSED`.

These bounded experiments are cross-checks only. The all-\(k\) dimension statement, sharp world cutoff, and optimal teaching lower bound follow from the structural induction, hyperplane/full-span evaluation, and linear algebra in `RESULT.md`; no exhaustive high-dimensional computation or independent scientific audit has been performed.
