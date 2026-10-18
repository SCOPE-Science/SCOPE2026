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

# Verification record

The finite-volume likelihood identity was derived from the exact Curie–Weiss partition sum by conditioning on the observed block. The separate Hubbard–Stratonovich representation gives the asymptotic mixture in the proof. The numerical program `verify.py` compares a direct enumeration of all spin configurations with the binomial formula for the same marginal; the brute force check is exhaustive only at the explicitly tested small system sizes.

The program was executed with Python, NumPy and SciPy. It completed 87 assertions. Checks included all listed small pairs \((N,k)\) for \(2\leq N\leq10\), limiting normal-mixture mass and second-moment normalization for \(\alpha\in\{1/8,1/2,1,2,4,8\}\), strict monotonicity on that grid, and finite-volume comparisons at \(N\in\{256,1024,4096\}\). Approximate output includes \(d(1)=0.1993891554\) and \(d(2)=0.5726993115\). The checks neither prove convergence nor establish non-overlap with every possible earlier theorem.

The proof uses the exact spin-mixture identity, a global positive quartic/quadratic lower bound on the free-energy potential, uniform exponential moments of the latent field, an \(L^2\) likelihood-ratio bound, a central limit theorem under the reference product measure, and the established Gaussian information–MMSE identity. The infinite-volume convergence and endpoint expansions follow analytically from those steps. The limits are restricted to fixed positive \(\alpha\); uniformity across shrinking or growing \(\alpha\) is not claimed. Independent audit has not been performed.

To reproduce the finite checks, install the dependencies in `requirements.txt` and run `python verify.py`.
