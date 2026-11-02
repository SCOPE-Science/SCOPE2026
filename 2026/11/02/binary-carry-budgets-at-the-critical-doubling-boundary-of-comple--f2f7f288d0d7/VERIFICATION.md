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

# Reproduction checks and limits

Execute `python3 verify.py` with ordinary Python 3 (standard library only). The program uses exact `Fraction` arithmetic and integer floor division. Its expected terminal line is:

`VERIFY_OK stratum_cases=110 stratum_points=11253 arbitrary_prefix_tests=94535 pure_geometric_tests=859740 exact_integer_rational=yes`

The first tests enumerate every admissible and inadmissible finite binary word at the specified resolutions in 110 finite strata. Each candidate is compared against a long finite Brown-criterion test and the proposed binary-weight formula; 94,535 additional exact rational scales on six different finite prefixes and 859,740 pure-geometric scales are tested. These are finite checks of identities and boundaries, **not** an infinite proof and not an external certification. The mathematical proof of the unrestricted classification is in `RESULT.md`, using the exact recurrence of binary digits.
