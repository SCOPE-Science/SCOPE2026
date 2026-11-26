---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The theorem uses the existence of four distinct proper divisors, not minimal cardinality. For n=2pq, the deficiency Δ=pq−3p−3q−3 must be positive, excluding p=3, and Δ<pq excludes pq as a summand. The remaining six divisors give fifteen four-subsets of sum Ap+Bq+c. The factorization (p−3−B)(q−3−A)=(3+A)(3+B)+c+3 has two positive factors because q≥7, A≤3 and the right side is positive. The constants are at most 39, so q≤45. The prior independent bounded enumeration after this proved cutoff directly tested all odd prime pairs and all four-subsets of proper divisors; it returned only 238, 310 and 322, with deficiencies 44, 44 and 68 and the stated witnesses. The frozen certificate's claim field is false on its broader wording: 165=3·5·11 is odd squarefree, has σ(165)=288 and 330−288=1+3+5+33. The verifier copies the claim label, so a data replay does not validate that wording. The complete replacement repairs/1/classification_certificate.json restricts the text to the proven even support; a parsed comparison here verified that all remaining fields match the frozen certificate. RESULT.md needs no scope change. The bundled verifier was inspected, not executed; frozen VERIFICATION.md describes expected output, not a recorded transcript.

## originality

PASS

The distinct claim is the exhaustive exactly-four classification on even squarefree three-prime support, not the isolated integers, the general definition or the divisor-factorization technique. The closest checked same-support classification has exactly three summands. The broader-looking one-divisor and two-prime results do not cover the four-divisor equation on 2pq. No checked exact table or stronger result supplies the iff list.

## value

PASS

The even squarefree three-prime family is a natural low-support case of the cardinality-stratified deficient-perfect problem, already studied for exactly three summands. The result replaces an unbounded prime search by a small proved global cutoff and gives a complete iff list with witnesses. This answers a classification question not answered by a mixed-cardinality membership table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
