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

The complete symbolic proof in RESULT.md establishes exclusion for every qualifying positive integer and exactly evaluates the lower density of the explicit obstruction set. Its main steps are: forced even-length difference; transported prefix equality with the short-denominator case separated; a sharp prefix-ratio inequality; and a concavity argument for the lower density at dyadic shell boundaries.

The separate verify.py script uses exact arithmetic. It checks all excluded candidates below 5000 against antipalindromic denominators of at most 16 binary digits, checks further products for odd multipliers up to 255, enumerates every shell at indices 1 through 8, and computes a high-precision decimal approximation of the absolutely convergent series. Every finite check is auxiliary, not a proof for arbitrary lengths.

To reproduce: run `python3 verify.py` with a standard Python 3 interpreter. No external software dependencies or input files are required.

Limitations: the proof does not determine the true asymptotic density of all unrepresentable quotients, and the numerical checks do not independently certify an unbounded search. Independent audit has not been performed.
