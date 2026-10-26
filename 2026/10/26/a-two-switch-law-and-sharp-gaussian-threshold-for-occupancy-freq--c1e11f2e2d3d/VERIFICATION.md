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

# Reproduction and verification

From the containing directory, execute `python3 check.py`. The program uses Python's standard library only and prints a count of successful tests. It exhaustively enumerates sample allocations for three, four, and five boxes at small sample sizes, compares every distinct frequency-pair covariance with independent multinomial calculations using exact rational arithmetic, checks the exact adjacent-ratio law in 20,520 aggregate tests, and independently checks the sign-reversal witness and large-sample approximation.

To reconstruct the general proof without computation: expand \(M_r M_s\) over ordered box pairs and use the two-cell multinomial distribution; cancel adjacent factorials to obtain \(Q_{r,s+1}/Q_{r,s}\); identify the unique ratio crossover; expand the exact three-cell multinomial probability using Stirling in a central \(\sqrt n\) window and evaluate the maximum at the ratio crossover. Critical-boundary equality and exhaustive literature priority are not decided by the checker. The printed finite count is not an infinite proof.
