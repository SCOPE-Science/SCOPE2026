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

The proof is analytic. The included `verify.py` checks only the elementary algebra in the final nonvanishing optimization and a uniform geometric-series bound for fixed Euler factors.

It verifies, for four values of \(\sigma<1\), that the symplectic density for
\[
\phi_\sigma(x)=\left(\frac{\sin(\pi\sigma x)}{\pi x}\right)^2
\]
gives the average-multiplicity bound \(1/\sigma-1/2\) and hence the nonvanishing lower bound \(5/4-1/(2\sigma)\), tending to \(3/4\) as \(\sigma\to1^-\). It also checks the closed geometric bound \(\sum_{e\ge1}p^{-e/2}=1/(\sqrt p-1)\), which makes every fixed prescribed prime contribute \(O(1/\log X)\) to the explicit formula.

Replay command: `python verify.py`

Expected output:
`VERIFY_OK sigma_cases=4 limit_nonvanishing=0.750000 fixed_prime_geometric_bound=1`

The executable check does not certify the Shintani-zeta functional equation, local Fourier transforms, or field-counting estimates. Those analytic inputs are the cited primary results; their stability under fixed local factors is proved in `RESULT.md`.
