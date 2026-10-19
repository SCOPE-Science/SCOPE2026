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
# Reproducible calculations and proof boundary

`verify.py` requires Python 3 and NumPy and runs without external data:

```bash
python verify.py
```

It checks each actual one-pivot matrix residual against the analytic trace gain; the expected spectral mean; five convex test-function bounds; and equality in the eigenbasis and in a numerically constructed orthogonal basis with zero diagonal for \(A^2-qA\). A fixed pseudorandom seed generates tests in every dimension from two through eight, including repeated and zero eigenvalues. The executable performs 1,680 grouped configurations/checks plus two numerically tested planar endpoints. Its expected output is embedded in `verification_output.txt`.

The exact planar example has eigenvalues 1 and 4. In an eigenbasis the trace gains are 1 and 4 with probabilities \(1/5\) and \(4/5\); with a 45-degree orthogonal rotation they are identically \(17/5\), and both bases yield expected residual trace \(8/5\). The upper variance is exactly \(36/25\), the lower exactly zero.

The universal convex-order assertions and attainability in arbitrary dimension follow from the mathematical proof in `RESULT.md`, not from the finite numerical checks. These tests do not establish novelty, infinite-dimensional results, multi-pivot concentration, numerical stability, or independent validation.
