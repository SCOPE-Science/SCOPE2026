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

# Verification and limits

Run `python3 verify.py` with Python 3, NumPy and SymPy. The program forms full Hamming adjacency matrices from the one-coordinate adjacency rule, obtains numerical adjacency eigenspace projectors, and independently projects onto each pair of sink columns. It also forms exact rational projectors using a SymPy spectral interpolation polynomial for all 81 ternary 3-dimensional sites across the three sink separations. Checks compare the exact Krawtchouk expression, spectral rank, projector idempotence, trace, and the unit-capture criterion.

Recorded results in `verification_output.txt`: 13 graph-and-separation cases and 972 site comparisons; 81 exact SymPy rational site comparisons; largest numerical absolute discrepancy \(4.44\times10^{-16}\). Every check finished successfully. These tests verify finite instances only. The arbitrary-integer theorem uses the analytic Fourier and Gram-matrix proof in RESULT.md. Finite checks cannot establish independent validation or resolve historical originality.
