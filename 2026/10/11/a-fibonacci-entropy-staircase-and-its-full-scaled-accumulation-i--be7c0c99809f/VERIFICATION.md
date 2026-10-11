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

# Reproduction and limits

Run `python3 verify_fibonacci_cover.py` with Python 3 standard library. The checker constructs the Fibonacci fixed-point word by its substitution recurrence; for every integer \(n\) from \(1\) through \(200\), it verifies that observed factor sets have the complete Sturmian counts \(n+1\) and \(n+2\), that one left- and one right-special factor exist, and that the two exact directed first-return lengths to the unique branching vertex agree with the predicted adjacent Fibonacci integers. It also brackets the universal constant by numerical bisection. The observed language saturation uses the known Sturmian factor-complexity theorem; numerical bisection is not a proof of transcendental equalities.

The infinite step depends on the published Fibonacci bispecial-length and directed-loop results (Bruin–Leplaideur, arXiv:1309.7934v1) and on a separately written line-graph and Perron proof. A finite prefix cannot establish facts about every \(n\). The entropy is natural-logarithmic; the finite-memory cutoff is the permitted word length \(n+1\), not \(n\). No independent audit or independent validation has been performed.
