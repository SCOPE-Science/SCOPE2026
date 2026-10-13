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

# Reproducible checks and scope

Run `python3 ladder_degree_checker.py` from the directory containing that script. No external packages are used. Its recorded output is `ladder_degree_checker_output.txt`. For \(m=2,3,4,5,6\) the script enumerates every nonzero binary support vector whose support indicator satisfies all the quadratic equations. For each support, it computes the exact Jacobian rank over the prime field of order \(101\), forms the maximal singular supports and compares them with the coordinate-component formulas. It also counts the remaining quadratic equations on each predicted component to test the degree computation. The output concludes `FINITE_CHECK_OK`.

These are finite regression tests, not proofs of any assertion for all integers \(m\). The written proof derives the global components and degree formulas by an exhaustive symbolic Jacobian case distinction and established complete-intersection primeness. Binary-support representatives do not replace the full analysis of complex-valued points; the written argument handles them.

The transverse ordinary-node claim holds **generically** on each irreducible component. No computation or argument here determines Jacobian scheme multiplicities or independently validates every step. The self-review is documented separately.
