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
# Reproducibility and verification

Run `python3 verify.py` beside `census.json` using Python 3 and its standard library. Expected output:

`TRIBONACCI_PSEUDOPERIOD_CENSUS_PASS factors= 91 triples= 13244 valid= 55`

The code regenerates the sixth-iterate-scale word from the morphism, enumerates the 91 length-45 factors of the ninth iterate, checks closure under substitution, enumerates every one of 13,244 triples with maximum shift 44, and checks their exact classification against `census.json`. An independently generated longer iterate is then scanned directly at 500 positions and yields the identical accepted-triple set. All rejected triples have a concrete length-45 violating factor in the certified complete factor set.

The proof of substitution closure is essential for the infinite-position assertion; direct prefix scanning alone is not an infinite proof. No statement about shift maxima greater than 44 is checked or asserted. Independent mathematical audit has not been performed.
