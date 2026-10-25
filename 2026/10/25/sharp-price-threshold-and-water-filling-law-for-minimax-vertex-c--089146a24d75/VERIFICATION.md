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

# Verification and reproducibility

Run `python verify.py` in a Python 3 environment with NumPy, SciPy, and SymPy installed. The included `verification_output.txt` is the captured result from executing the included source code.

A separate symbolic test assembles the exact five-vertex star Laplacian for the conductances \((1,1,4,2)\), computes \((L+\mathbf1\mathbf1^\mathsf T/5)^{-1}-\mathbf1\mathbf1^\mathsf T/5\) over rational arithmetic, and checks all leaf/hub diagonals and the exact maximum \(71/100\). The same data are separately checked by the closed-form threshold formula with prices \((240,32,1,4)\) and budget \(284\), whose active set contains two edges.

Numerical checks cover 96 seeded positive-price cases of orders 3 through 10 vertices: budget equality, dual-simplex normalization, primal--dual equality, full matrix-pseudoinverse diagonals, separately optimized feasible allocations when the convex solver returns success, 2,880 random feasible nonuniform candidates, active-set boundaries, and the sharp equal-allocation comparison. Assertions implement tolerances explicitly. The executable does not prove completeness outside tested cases; the mathematical proof in `RESULT.md` establishes the arbitrary-price, arbitrary-order statement.

An independent audit has not been performed. The statement is not externally certified or mechanically formally verified.
