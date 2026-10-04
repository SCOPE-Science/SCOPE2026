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

The source LFS rate was independently reconstructed from
\[
q=e^{-\gamma u},
\qquad
r=\sqrt{\cos^2u+z^2\sin^2u},
\]
and the four system-ancilla eigenvalues
\[
\frac{1-q}{4},\quad
\frac{1-q}{4},\quad
\frac{1+q+2qr}{4},\quad
\frac{1+q-2qr}{4}.
\]
The proof reduces the all-time monotonicity question to a sharp information-theoretic derivative ratio and then to a one-variable geometric maximization.

`verify_lfs_threshold.py` uses only the Python standard library. It checks the derivative-ratio bound on a deterministic grid, verifies the analytic maximizer of the geometric factor, evaluates the exact source benchmark \(z=0\), checks the LFS-versus-LPP hierarchy, and performs supplementary time-domain sign tests above and below the boundary. It prints `VERIFY_OK`.

The finite replay is supplementary. The exact threshold for every \(z\in[0,1]\) and every \(\gamma\ge0\) is supplied by the analytic proof in `RESULT.md`.

No independent audit has been performed.
