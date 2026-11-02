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

The proof is analytic. It uses exact Hilbert--Schmidt projection identities, finite transposition invariance of an exchangeable distribution, weighted-mean ordering, and absolutely convergent double sums in the infinite case. All positive denominators are almost surely nonzero under the stated \(X_j>0\) assumption.

Run `python3 verify.py` with Python 3. The checker uses exact rational enumeration for 2–6 modes, including degenerate eigenvalues, dependent exchangeable amplitudes, and the explicit three-mode instance. It reports 1,984 iid assignments and further dependent and equality checks. These computations are consistency tests only; no finite checker establishes the theorem over arbitrary distributions or infinitely many modes.

Scientific limitations are recorded in RESULT.md. No independent mathematical audit has been performed.
