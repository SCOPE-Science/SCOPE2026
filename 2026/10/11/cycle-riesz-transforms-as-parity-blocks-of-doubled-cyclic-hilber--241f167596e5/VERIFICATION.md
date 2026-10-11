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

The analytic proof uses exact Fourier identities. The accompanying `verifier.py` performs independent numerical regression checks of the following finite statements over many sizes:

- the multiplier \(i e^{\pi i k/N}\) Fourier-inverts to \(-\cot(\pi(r+1/2)/N)\);
- the multiplier square equals the multiplier of \(-T(I-P_0)\);
- the cyclic Hilbert kernel on \(C_{2N}\) vanishes on even offsets and produces both stated parity blocks on odd offsets;
- the kernel absolute-sum, half-grid cotangent sum, and doubled-Hilbert endpoint sum coincide;
- the scaled remainder approaches \(\pi/18\) for even \(N\) and \(-7\pi/36\) for odd \(N\).

Run `python3 verifier.py`. Finite floating-point checks do not certify the universal theorem or the asymptotic remainder order; those are established by the exact Fourier and Euler--Maclaurin arguments in `RESULT.md`.
