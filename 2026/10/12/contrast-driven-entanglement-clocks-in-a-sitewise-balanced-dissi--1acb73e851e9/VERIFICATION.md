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
# Reproduction and verification

The exact theorem and its analytic proof appear in `RESULT.md`. In a Python environment with the versions specified by `requirements.txt`, run:

```
python verify_symbolic.py
python verify.py
```

The symbolic check is formulated entirely in exact SymPy algebra. It constructs the two fermionic jump operators with the Jordan–Wigner parity string, computes the Lindblad adjoint on the five-observable invariant sector for symbolic \(J\), \(\gamma_1\), and \(\gamma_2\), checks the Majorana definition of fermionic partial time reversal and its characteristic polynomial, and confirms preservation of the quadratic \(r=z_1z_2+w_1w_2\) relation. The actual execution returned:

```
VERIFY_SYMBOLIC_OK exact adjoint closure, twist spectrum, Wick invariance
```

The matrix check constructs the full \(16\times16\) Liouvillian and exponentiates it on each of the four occupation-projector initial conditions. It separately evaluates the closed state formula, performs fermionic partial time reversal from the complete ordered Majorana basis, compares all four twisted eigenvalues to the analytic spectrum, tests predicted leading-singular-value inequalities, checks the exact finite crossing times, and directly verifies degeneracy at the first clock. Actual execution returned:

```
VERIFY_OK 1521 direct matrix/Lindblad/singular-spectrum checks
```

Test instances include zero rates, a common positive balanced rate, opposite signs of site-rate contrast, both regimes separated by \(|\gamma_2-\gamma_1|=4J\), exact critical contrast, and two different positive coherent couplings. There are no external data dependencies.

The scripts are finite and symbolic corroborations. The proof of infinitely many oscillatory roots, the exclusion of finite lower-rate roots above threshold, the spectral-gap equivalence, and strict clock monotonicity comes from the all-parameter equations in `RESULT.md`, not from extrapolating sampled cases. No independent external audit or certification has been performed.
