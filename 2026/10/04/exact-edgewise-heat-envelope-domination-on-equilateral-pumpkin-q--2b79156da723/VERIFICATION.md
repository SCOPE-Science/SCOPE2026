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
# Verification

The analytic proof establishes the infinite statement. The computational replay is deliberately finite and is used only to check algebraic components and representative evaluations.

`verify.py` performs three groups of checks. First, for \(2\le N\le12\) it constructs the exact rational orthogonal projector \(I-N^{-1}\mathbf1\mathbf1^T\), verifies idempotence and diagonal entries \(1-1/N\), and confirms that the symmetric-cosine plus antisymmetric-sine edge weight equals exactly \(2/\ell\) for several rational edge lengths. Second, it evaluates truncated heat series for several \(N\), \(\ell\), \(t\), and cutoffs, checking that direct level summation equals the closed formula and that the difference from the decoupled Neumann-edge series is \((N-1)/(N\ell)\) to floating-point tolerance. Third, it checks the associated finite-energy step count at exact eigenvalue thresholds and immediately below them.

Running the supplied file with a standard Python 3 interpreter prints `VERIFY_OK`.

The script does not prove completeness of the spectrum, convergence of the infinite heat series, or the all-parameter theorem. Those points are proved in `RESULT.md` from the differential equation, the two vertex conditions, and the eigenspace projector trace.
