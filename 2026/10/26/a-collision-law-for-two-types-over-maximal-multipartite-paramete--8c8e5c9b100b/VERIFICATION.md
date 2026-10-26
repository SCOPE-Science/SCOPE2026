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

# Reproduction

With Python 3 from the package root, run `python3 verification/check_counts.py`. No dependencies beyond the standard library are needed. The checker generates the finite named multipartite graph, adds two new vertices with all possible neighborhoods and both choices for their mutual adjacency, and directly checks for \(K_{r+1}\)-cliques by enumerating vertex combinations. It checks 41 input size vectors with total parameter size at most six, independently of the product-counting reasoning, and prints `ALL_TESTS_PASS` on agreement.

The checker also prints exact balanced cases. These are finite confirmations only: the proof's counting bijection and asymptotic error estimate are general arguments in RESULT.md. The uniform asymptotic estimate uses fixed \(r\) and minimum part size tending to infinity. No randomized tests, external proof assistant, or independent scientific audit were used.
