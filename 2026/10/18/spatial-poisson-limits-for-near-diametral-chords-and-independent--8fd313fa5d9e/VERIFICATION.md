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

# Verification instructions and limits

Run `python3 verify.py` using Python 3 standard library. Expected final output:

`VERIFY_OK perfect_matchings 146598 assertions 75`

Checks are exact rational and exhaustive for every uniformly matched chord diagram of sizes \(n=2,3,4,5,6,7\). The script checks potential-edge class counts, exact crossing means and variances, exact deficiency-class/crossing covariances for the first three classes (where feasible), and a mixed third-order factorial-moment identity. It does not by itself prove weak convergence or historical originality. The independent Poisson process limit is proved through joint factorial moments and bounded candidate-edge conflicts; the independence from crossings follows from uniform finite-edge conditioning and the established marginal crossing central limit theorem of Flajolet and Noy. Limitations: fixed \(J\), no quantitative asymptotic rate; independent audit not performed.
