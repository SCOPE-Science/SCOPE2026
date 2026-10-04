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

Run `python verify.py` in the package directory. The script uses only the Python standard library.

It factors every integer through \(10^6\), restricts to square-free integers, and compares two independent tests: direct integrality of \(\sigma(n)/\tau(n)\), and the structural criterion that odd square-free integers are always arithmetic while an even square-free integer is arithmetic exactly when it has a prime factor congruent to \(3\pmod4\). Any discrepancy aborts the run.

The script also counts the square-free non-arithmetic integers at \(10^4\), \(10^5\), and \(10^6\), reports the normalized quantity \(E_{\mathrm{sf}}(x)\sqrt{\log x}/x\), and evaluates a truncated Euler product for the predicted coefficient \(2K_{\mathrm{LR}}/\pi^2\).

Expected final line:

`VERIFY_OK limit=1000000 squarefree=607926 exceptions=42186 coefficient≈0.15486409`

The finite computation corroborates the exact support reduction and the leading constant. The infinite asymptotic itself rests on the symbolic Euler-product factorization and the Landau–Selberg–Delange theorem.
