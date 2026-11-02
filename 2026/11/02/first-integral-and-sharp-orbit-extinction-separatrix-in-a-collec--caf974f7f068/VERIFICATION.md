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

The analytical calculation of the conserved function \(H\), endpoint asymptotics and level-set classification is in `RESULT.md` and applies for every integer \(N\ge3\), \(2\le M<N\), with \(0<c<h(p)\), \(b,\varepsilon>0\), and the critical linear-feedback parameter.

Run `python check_critical_collective_risk.py` after installing the listed SymPy, NumPy and SciPy dependencies. On the completed package, the program reports 36 exact symbolic cancellations for \(N=3,\ldots,10\) and a 200-unit ordinary numerical test with energy drift below \(6\times10^{-9}\). No finite test establishes the infinite-parameter result or bibliographic novelty. No independent validation or audit has been performed.
