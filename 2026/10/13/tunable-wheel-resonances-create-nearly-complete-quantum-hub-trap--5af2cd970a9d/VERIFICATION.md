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

The analytical argument is complete for all integers \(n\ge3\) and all real \(g>0\), with no finite cutoff. Its necessary spectral ingredients are: the ring Fourier eigenvalues, the two hybrid roots of the hub/uniform block, the unique negative-root collision criterion, and the two-coordinate spectral projection for the hub initial state. These ingredients are derived explicitly in `RESULT.md`.

`verify.py` independently builds each adjacency matrix and computes spectral evaluation ranks with NumPy diagonalization and singular-value decomposition. It checks 84 generic single-rim cases, 119 resonant single-rim cases, 203 two-sink cases, and 119 hub-started resonance probabilities for \(3\le n\le30\). The executed output was:

```
VERIFY_OK generic=84 resonances=119 two_sinks=203 hub_resonances=119
```

Replay with `python -m pip install -r requirements.txt` followed by `python verify.py` in a folder containing these files. Numerical eigenspace grouping uses a tolerance of `2e-8` and does not certify exact multiplicity or an unbounded theorem; the paper's spectral proof supplies those claims. At fixed finite time no discontinuity in the hopping parameter is asserted.
