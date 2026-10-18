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

# Reproducibility

Run `python3 verify.py` with Python 3.9 or newer. The checker uses only the standard library and reproducibly tests:

- Every one of 65,536 spin states of the \(4\times4\) periodic plaquette Hamiltonian, compared with an independently defined six-neighbor hard-core graph.
- Exact independent-set polynomial \(1+16z+72z^2+96z^3+16z^4\), giving \(201\) one- and two-spin-stable configurations.
- All single and pairwise simultaneous physical flip energies of the one-spin minima.
- Direct triple-flip destabilization at sizes \(L=4\) and \(L=8\).
- Protected interior defect-pair geometry for \(5\times5\) blocks at sizes \(L=8,16\), and the block-count inequality.
- One hundred twenty seeded checks of \(T^L=I\) at dyadic sizes \(4,8,16\).

The correctness of the exponential probability bound comes from conditioning and elementary counting in the accompanying proof, not simulations or finite-size extrapolation. The stated constant is not asserted sharp, and no independent external audit is available.
