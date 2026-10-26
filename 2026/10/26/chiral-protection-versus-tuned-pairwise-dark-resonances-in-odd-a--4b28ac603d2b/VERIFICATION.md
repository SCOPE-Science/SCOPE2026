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

# Reproducibility

Install the packages listed in `requirements.txt` and run `python verify_odd_ssh.py`. The actual run completed with `PASS: 111 checks of spectral dark ranks, overlap probabilities, off-resonance absence, and exact Chebyshev identities`.

The test independently diagonalizes odd real symmetric Jacobi matrices for multiple lengths, all predicted third-site tunings, nearby detunings, and several independent coupling choices for the first two sink positions. It also verifies the third-site elimination polynomial with exact symbolic arithmetic. The exact all-length theorem is the separately written Jacobi/Chebyshev argument, not an inference from these finite tests. None of these checks constitutes independent scientific auditing.
