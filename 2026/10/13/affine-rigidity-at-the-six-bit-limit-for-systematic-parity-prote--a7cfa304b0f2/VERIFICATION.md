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

Run the standalone verifier from the extracted package directory:

```sh
python3 verify.py
```

The execution checked \(30\) locally admissible edge-color patterns, \(720\) distinct six-direction assignments, all message pairs for each assignment, the constructions at message dimensions \(2\) through \(6\), and all \(16^4=65536\) possible four-check-bit maps on the two-dimensional message cube. The observed output was:

```text
VERIFY_OK: 30 square patterns; 720 distinct linear assignments; 23040 affine maps; k=2..6 valid; 65536 four-check-bit maps excluded
```

The count \(23040\) uses the separately proved uniqueness of the origin value and six labeled edge increments; the verifier does not enumerate all nonlinear maps on the six-dimensional input cube. The proof in `RESULT.md`, in particular its square-XOR color rigidity, is what excludes such maps. The finite checks do not establish unrelated distances, dimensions, or channels. No independent scientific review or independent audit is asserted.
