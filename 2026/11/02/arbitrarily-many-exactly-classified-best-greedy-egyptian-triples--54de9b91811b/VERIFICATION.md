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
# Reproducibility and scope

Run `python3 verify.py` in a standard Python 3 environment. It uses only the standard library, exact `Fraction` arithmetic and integer divisor enumeration, and prints the tested parameter values and checks. Ten odd parameter values (3, 5, 7, 9, 11, 15, 21, 35, 105, 1155) are checked for greedy denominators, the entire prescribed divisor-parameterized family and its cardinality, the distinction between weak and strict denominator conventions, and all construction bounds. For the first eight values it checks every bounded pair of first two denominators and confirms that (a) all exact three-unit representations of the constructed rational value are precisely those prescribed, and (b) none can yield a better strict underapproximation below the constructed target. Across those eight cases, 58,020 bounded first-two-denominator pairs enter the candidate screen.

The universal theorem has a symbolic proof in RESULT.md. Enumeration at finitely many q is not a certificate for all odd q, and these checks do not establish priority over the entire literature. Independent audit has not been performed.
