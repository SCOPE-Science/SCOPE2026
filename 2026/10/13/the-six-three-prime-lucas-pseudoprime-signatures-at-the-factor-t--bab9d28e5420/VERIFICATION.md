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

Run `python3 VERIFIER.py` with the Python 3 standard library. The program recomputes all \(160\) bounded sign/quotient configurations derived from the symbolic proof and independently enumerates primes \(5\le q\le21\), \(q<r\le65\), and all eight sign triples. Both outputs are compared exactly. It verifies all three Korselt divisibility conditions for the six surviving rows and finds one prime discriminant witness for each using Euler's criterion. The exact output of a successful run is embedded in `VERIFIER_OUTPUT.txt`.

The finite loops are logically exhaustive because the proof establishes \(k\in\{1,2\}\), the corresponding bounds on \(j\), and \(q\le21, r\le65\). They do not prove Dirichlet's theorem or equidistribution of primes in progressions, which are invoked as established mathematical results. The work does not classify nonprime discriminants or other prime-factor shapes.
