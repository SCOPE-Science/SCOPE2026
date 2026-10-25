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

# Reproducibility of finite checks

Run `python verify.py` using Python 3.11+ with no external dependencies. The program constructs its spectral roots independently by high-precision Decimal bisection on each interlacing interval and evaluates the positive residues from the secular equation. Across six one-to-five-atom probability laws, it checks the residue sum, spectral probability normalization, nonnegative Boolean entropy, and the approximation of the calculated second coefficient by \(n\Gamma(\mu_n\mid\mathbf b)-v\log n/2\) at five increasing sample sizes. It separately uses rational arithmetic to verify fourth-moment identities and compares a family of finite spectra with the published explicit four-point special-case formula. It finally checks the zero-eigenvalue boundary mass \(1/(n+1)\) for symmetric two-point Nevanlinna input.

Actual execution result: `PASS 116 root, residue, normalization, asymptotic, moment, published-special-case, and zero-atom assertions`.

**Limits of computation.** The finite test grid and high-precision calculations do not prove the all-atomic and all-\(n\) theorem, do not rule out unexamined numerical regimes, and do not independently validate the scientific novelty. The mathematical proof of the universal claims is supplied in `RESULT.md`; no independent audit or formal proof certification has been performed.
