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

# Verification of frozen Potts ladder formulas

The standalone file `verify_potts_ladder.py` uses only Python 3 standard-library modules. Run `python3 verify_potts_ladder.py` from a directory containing the script. A successful run concludes with `VERIFY_OK`.

For \(q=2,3,4\) and \(n=3,4,5\), and for \((q,n)=(3,6),(5,3),(5,4)\), it independently enumerates every one of the \(q^{2n}\) spin arrays on \(C_n\square K_2\), computing each site's proposed energy change for every alternative color from its three adjacent spins. It counts accepted frozen states by their upper-row wall numbers **and by energy obtained from the three kinds of undirected lattice edges** and compares both integer histograms to the independently generated recurrence coefficients. It also directly checks the two geometric classes for each accepted state. The sum of inspected spin arrays is exactly \(2{,}123{,}582\), and the twelve count comparisons succeeded.

Separately, the script constructs the \(q^2\)-state unweighted memory transfer and multiplies its matrices to check \(\operatorname{tr}T(1)^n\) against the independent recurrence for five values \(q=2,\ldots,6\) and eight lengths \(n=1,\ldots,8\). The formal small-length checks test the transfer, not a claim about small physical cylinder graphs.

These checks are exhaustive for their finite parameters. The classification and asymptotic normality for arbitrary \(n\) are established by the written local-stability, spectral and analytic moment-generating-function proofs, not by extrapolation from the program. The reachability distribution under stochastic dynamics is not computed.
