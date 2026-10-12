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
The self-contained `verify.py` requires Python 3.10+ and SymPy 1.12+. Execute `python3 verify.py` in a directory containing the script. It checks the full quartic-square coefficient identities, the \(\gamma\)-identity, the resultant product decomposition, irreducibility of the degree-eight and degree-sixteen polynomials, and independently enumerates restricted quartic square conditions over each prime \(5\le p<200\) (forty-four primes). The observed output is `VERIFY_OK`.

The finite-field enumeration does not certify untested primes or natural densities. Those follow from the symbolic argument in `RESULT.md`, the normality and degree of the common Galois field, and Chebotarev's theorem. The assertion is about bitangent lines; characteristics two and three and tangency point fields are outside scope. An independent audit has not been performed.
