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

# Reproducibility and limits

The standalone standard-library program `verify_dr.py` checks the mathematical criterion for JR by two different implementations: enumeration of **every** potentially cohesive voter subset and direct counting of unrepresented supporters for each candidate. It exhausts \(2^{nm}\) binary approval matrices with \((n,m,k)=(3,3,2),(4,3,2),(5,3,2)\), respectively \(512\), \(4096\), and \(32768\) matrices, and all \(\binom m k\) committees within each. In these cases the numbers of profiles with at least \(k\) quota-exact candidates and the numbers admitting DR are respectively \((162,162)\), \((1296,1242)\), and \((7600,7600)\). The \(54\) finite exceptions in the middle case show that enough exact-support candidates need not imply DR at a fixed finite sample size.

The program further checks the local Gaussian coefficient for \(k=3\), two moving-approval parameters and three values of \(n\), and compares \(2400\) reproducible random approval matrices at \((n,m,k,p)=(200,50,2,1/2)\) against the **exact** quota-candidate binomial probability. Those numerical checks are diagnostics, not an infinite proof or an exhaustive enumeration of larger cases. The independent-column law, conditional Hoeffding bound, union bound, binomial local limit, and off-critical entropy estimate provide the mathematical proof. Execute `python3 verify_dr.py` with an ordinary Python 3 interpreter; no extra packages or external datasets are required.

The assumptions exclude growing committee size, correlated approval events, exponential candidate supply, and general heterogeneous approval probabilities. Literature-priority checks cannot ensure that inaccessible or unindexed mathematical work has not proved equivalent statements.
