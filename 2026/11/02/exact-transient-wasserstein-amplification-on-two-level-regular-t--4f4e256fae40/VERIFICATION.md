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
# Verification and limits

`CHECKER.py` is an executable standalone supplementary checker requiring Python 3, NumPy, and SciPy. Run `python CHECKER.py` from a directory containing that file. A completed replay produced:

```
PASS: matrix/flow comparisons = 783; transport LPs = 5; large-branching tests = 8
```

The checker constructs the incidence matrix from the actual tree edges, exponentiates the complete edge Laplacian independently, and compares all inner- and outer-orbit row norms against the two-block formula. For selected cases it reconstructs the vertex heat transition matrix and computes \(W_1\) by accumulating masses on unique descendant subtrees. It additionally solves independent finite primal optimal-transport linear programs for five edge pairs and tests the large-branching trend at prescribed times. Full-spectrum finite computations, floating-point comparisons, and linear programs are not infinite proofs. The analytic identity and asymptotic are derived directly in `RESULT.md`; the untested infinite parameter range is covered only by that argument.

The formula presumes integer branching \(b,k\ge2\), the graph path metric with unit edges, symmetric unit edge jump rates, and the unnormalized Laplacian. Replacing the generator by the degree-normalized walk changes the result. A historical priority assessment remains qualified; no independently performed scientific audit is represented.
