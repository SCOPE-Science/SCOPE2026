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

The included `verify.py` uses SymPy to reconstruct the fermionic Hubbard Hamiltonian on sixteen-dimensional occupation-qubit space; the four-dimensional fixed-number sector; the commuting code-stabilizer projectors; the spectral eigenstates; and their exact logical Bloch vectors. It also checks twenty nonzero-temperature parameter choices and thirteen monotonicity samples. Execute `python verify.py` in a Python environment satisfying `requirements.txt`; success prints `VERIFY_OK`.

The finite sample checks do not certify the universal temperature classification or asymptotics; those rely on the complete analytic argument in `RESULT.md`. The stabilizer-polytope equivalence is established by Pauli postselection and conditional Clifford decoding, not by numerical linear programming. No independent validation has been performed.
