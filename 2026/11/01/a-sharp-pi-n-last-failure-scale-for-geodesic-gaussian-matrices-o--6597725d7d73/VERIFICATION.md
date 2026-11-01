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

# Verification scope

The analytic proof in `RESULT.md` establishes the uniform upper bound and the full-parity lower witness by exact identities, Poisson summation, and dominated convergence. The supporting script `check_cycle_gaussian.py` requires `mpmath` and may be invoked with `python check_cycle_gaussian.py` in a directory containing that script. It makes no network requests, and its output is not an external certificate.

The script ran successfully with precision set to 100 decimal digits. It checked the sign of a specific cyclic Fourier eigenvalue at \(t=(\pi\pm0.5)/n\) for twelve cycle orders spanning the four residue classes modulo four, checked the analytic positive-tail inequality at the larger parameter, and repeated finite Fourier evaluations at four small orders. Those examples are not exhaustive over all sample sizes or all parameters. The infinite theorem rests on the symbolic estimates displayed in the proof.

The proof does not determine exact transition points for finite \(n\), prove that there is only one sign crossing, or establish anything for nonequispaced samples. Independent validation remains unperformed.
