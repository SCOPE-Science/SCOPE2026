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

# Reproduction

Use Python 3 (standard library only) from the directory containing the packaged files:

```bash
python verify_transfer_dynamics.py
python verify_cycle_basis.py
python verify_open.py
python verify_spectral.py
```

The first program constructs the exact three-vertical-difference transfer count with Laurent exponent bookkeeping and separately evolves all initial CCA colorings for \(n=3,4,5,6\). The second enumerates the same configurations by independently testing the top-cycle and all square-cycle winding integrals. The third checks the open-ladder count against all labelled trajectories through six rungs. The fourth tests the explicit characteristic polynomial identity at five nonzero rational Laurent specializations and checks exact integer transfer totals for longer lengths against the Laplace asymptotic. The actual outputs are in `VERIFICATION_OUTPUT.txt`.

The numerical checks do not prove the general theorem. All-size correctness comes from the graph-height bijection, column transfer and determinant identity in `RESULT.md`, combined with the published synchronization--irrotationality theorem. The Gaussian leading coefficient is derived by Fourier coefficient extraction and a unique nondegenerate spectral maximum. Only new mathematical content in this package was assessed; independent review remains unperformed.
