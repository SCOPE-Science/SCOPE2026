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

Run `python3 verify.py` in this folder. The verifier implements the adjacency-edge definition independently of the Walsh-space argument. It constructs binary cubes by bit operations and tests that each edge sees exactly \(d-1\) red edges among its \(2(d-1)\) adjacent edges. It enumerates every red/blue edge assignment of \(Q_2\) and \(Q_3\) and verifies that the respective complete sets of valid assignments coincide exactly with the stated sign-vector construction. It then constructs all predicted assignments for \(Q_4\), \(Q_5\), \(Q_6\) and \(Q_7\), checks uniqueness and their validity edge-by-edge. The exact observed console line is stored in `verify_output.txt`.

These finite computations do **not** exhaust all possible edge assignments for \(d\ge4\). Exhaustiveness there is a consequence of the analytical eigenfunction argument in `RESULT.md`, which diagonalizes the finite-dimensional hypercube adjacency operator for every dimension and checks necessity and sufficiency. No external checker or independent mathematical audit has been performed.
