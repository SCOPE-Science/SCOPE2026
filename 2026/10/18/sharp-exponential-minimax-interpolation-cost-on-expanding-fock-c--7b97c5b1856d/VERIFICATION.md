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

# Reproduction and evidence boundaries

The operator is normalized as in `RESULT.md`; in particular the data inner product uses \(1/N\). The finite circular Gram entries are \(e^{-\rho N}e^{\rho N\omega^{i-j}}\), and discrete Fourier eigenvalues of the Gram divided by \(N\) are \(p_{N,m}\). Their finite Poisson congruence sums can be checked numerically using the included `checks/fock_circle_check.py` (Python standard library only). It checks positivity, normalization of the residue probability distribution, the direct Fourier spectrum, and numerical agreement between observed rates and the stated variational expression for representative parameter choices.

The numerical checks do not certify the arbitrary-\(N\) asymptotics. The proof uses an actual Gram identity, Stirling inequalities with uniform alias bounds, strict convexity of the Poisson rate, and selection of near-maximal residues. No machine-assisted infinite verification, external certification, or independent audit was performed.
