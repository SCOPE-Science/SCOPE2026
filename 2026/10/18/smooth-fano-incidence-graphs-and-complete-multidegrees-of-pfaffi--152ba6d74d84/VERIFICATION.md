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
# Verification of the Pfaffian graph computation

The full mathematical proof is in `RESULT.md`. The executable `verification/check_multidegrees.py` is standard-library-only and contains two independently implemented exact formulas: recurrence \(a_j=\binom{n+1}{j}-2a_{j-1}\) and a full finite binomial sum from the twisted Euler sequence. Both compute the graph multidegrees. The script checks the first four reference sequences, \(a_0=1\), \(a_1=n-1\), \(a_2=(n-1)^2-(\binom n2-1)\) and \(a_{n-1}=(n+1)/2\) for each odd \(5\le n\le101\), inclusive. `verification/check_output.txt` is the actual stdout obtained by running the embedded script. In the first case the sequence is \((1,4,7,6,3)\) and the anticanonical top intersection is \(86\).

This program is an arithmetic checker, not a computational proof of the general graph identification, Bertini smoothness/irreducibility, adjunction or ampleness. Those facts are established by the symbolic geometric argument in the result. The originating source gives the birational parametrization, the degree of the base locus, and the degrees of the map and Pfaffian target; the general full graph class and Fano identification are assessed separately in `REVIEW.md` and `AUDIT.json`. No independent audit is claimed.
