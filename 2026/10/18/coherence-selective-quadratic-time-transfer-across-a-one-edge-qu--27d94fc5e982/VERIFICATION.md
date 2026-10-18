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

# Verification of the transfer statement

The exact graph Hamiltonian is reconstructed from two complete \(n\)-cliques connected by one unit-weight bridge, with degrees \(n-1\) and \(n\). The analytic proof explicitly checks the left sum-zero eigenspace, parity reduction, exact even-sector eigenvalues, odd-sector characteristic polynomial, and \(\det(I-M_-)=2/[n(n-1)]\). The critical eigenprojector-weight inequalities hold simultaneously for every integer \(n\ge3\). Their resulting envelope is uniform over **all** observation times and arbitrary left-nonbridge complex launch packets, rather than only the sampled values in the tests.

Run `python check_tunneling.py` with packages specified by `requirements.txt`. The script independently constructs the full graph matrix and the parity-reduced matrices and reports **482 passing matrix, spectral, and numerical assertions**. Tested graph sizes, times and sampled launch states are explicitly visible in the script. This finite computation does **not** exhaust all integers or all times, does not constitute an infinite certification, and cannot establish historical originality. The theorem's infinite quantifiers follow from the analytic inequalities and the continuity argument for the first fixed-threshold time.

The overall normalized adjacency is used throughout; changing the Hamiltonian normalization changes the frequency and may invalidate the bound. The packet is supported on the left nonbridge vertices. A right-clique measurement includes its right bridge vertex. The asymptotic onset statement is for \(n\to\infty\); no independent scientific audit has been performed.
