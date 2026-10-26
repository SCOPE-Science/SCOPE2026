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

# Verification and reproducibility

Run `python verify_multiplex.py` using Python 3.9+; no third-party modules are needed. The reported execution completed with `PASS: 707 finite exact-identity, direct-spectrum, and neighboring-design checks`.

The script replays exact rational identities for the two budget thresholds on integer sizes \(3\le n\le24\), and computes full \(2n\)-vertex weighted Laplacian spectra using an independent Jacobi iteration for \(3\le n\le11\). It also tests feasible neighboring symmetric allocations in all regimes. The exact proof for all \(n\ge3\) and every real \(B>0\) is in `RESULT.md`, based on permutation averaging, invariant blocks, strict concavity, an equality test in two characteristic polynomials, and a global high-budget Rayleigh bound.

Finite tests are not exhaustive over real budgets or all graph orders. No numerical result is used to prove infinitude, global uniqueness, or novelty. Later literature [2] in `RESULT.md` could not be inspected in full. Independent mathematical auditing has not occurred.
