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

# Verification and limitations

The analytic classification follows from an excitation Lyapunov identity, the parity-resolved Jordan–Wigner equivalence, the exterior-power dark-subspace lemma, and Chebyshev continuant equations. These four arguments supply the infinite-dimensional-in-parameter proof for all finite ring lengths, all real detunings and all positive rates.

For finite-sector corroboration run `python verify.py` from this package with Python 3, NumPy and SymPy. The program constructs complete spin Hamiltonians and fermion exterior-power Hamiltonians, compares them in all excitation sectors on lengths 4 through 8, checks Chebyshev polynomial identities symbolically, and tests both signs of fermion boundary twist through length 16. Actual execution returned `VERIFY_OK 369`. Computations are finite and do not by themselves prove the all-size statement. No external independent audit has been performed.
