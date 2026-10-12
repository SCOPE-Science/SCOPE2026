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

# Exact replay

Both complete verification programs use only the Python standard library. From a directory containing the packaged `verify_exact.py` and `verify_independent.py`, run `python3 verify_exact.py` and `python3 verify_independent.py`.

The exact certificate loops over all \(24\) strict priority permutations and every binary context of length \(w+2\), for \(2\le w\le9\). For each order it computes the number of contexts of each Hamming weight whose leftmost minimizer changes between adjacent windows. It then verifies the transformed polynomial coefficient signs, exactly identifies zero polynomials, checks the excluded comparison, and verifies the factorization of the two competitive density polynomials. The proof that the crossing polynomial has exactly two simple roots uses Descartes' rule of signs and checked exact rational sign brackets; decimal approximations are not used for certification.

A second implementation evaluates changed selections through boundary departure or strict improvement by the newly arriving two-mer, rather than computing both argmins. It independently recomputes event vectors and globally compares all rankings at five rational biases per width. Both scripts completed successfully. The mathematical verification is valid for all real bias values in the stated domain because its certified polynomial signs and Descartes calculation apply throughout; the five tested fractions are secondary checks, not the proof of interval-wide optimality.

No numerical linear/integer solver, trusted external table, or external independent audit was used. The historical literature comparison and possible prior unindexed computation remain bibliographic limitations.
