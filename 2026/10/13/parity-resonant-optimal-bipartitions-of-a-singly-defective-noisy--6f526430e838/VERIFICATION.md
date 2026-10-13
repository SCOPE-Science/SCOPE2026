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

Run `python3 verify.py` with Python 3 and NumPy. The program constructs the noisy states by applying the local channel separately to the four input matrix-unit tensors and diagonalizes the partially transposed matrices directly, independently of the paper's cut-spectrum argument. It checks 20 small channel systems and 228 bipartitions, the limiting formula along 12 critical-window sequences, and four exact resonance cases with perturbations on each side.

Expected output on successful completion: `VERIFY_OK channel_states=20 partial_transposes=228 critical_parities=2 critical_sequences=12 resonance_cases=4`.

The tests do not establish all-dimensional claims. The proof of the exact formula is algebraic, the lattice-optimality proof is deterministic, the asymptotic limit uses a differentiable scalar expansion, and the full-separability characterization imports the explicitly cited Dür--Cirac theorem for a canonical GHZ-diagonal subfamily. Neither originality nor an independent audit is established by the verifier.
