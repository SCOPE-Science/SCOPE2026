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

# Computational verification

Execute `python3 verify.py` with Python 3.8 or newer. No third-party dependencies are needed.

The executable checks the exact Laurent-symbol factorization and calculates binary adjacency ranks by Gaussian elimination for each of the \(529\) pairs with \(3\leq m,n\leq25\). It also checks the independent diagonal-orbit parity calculation for every pair and verifies that six explicitly oriented instances satisfy \(A+A^{\mathsf T}=Q\) and the rank formula.

The output from the included checker is:

```text
VERIFY_OK symbolic_factorization=1 all_parity_rank_tests=529 diagonal_orbit_parity_tests=529 orientation_tests=6 m_n_each_3_to_25=true
```

Each finite equality uses exact binary integer bit operations, not floating-point tolerances. Enumeration does not establish an unbounded theorem; the proof in `RESULT.md` proves the statement for every integer pair in scope. The half-rank-to-ancilla step is the mathematical theorem cited from DOI 10.3934/amc.2021015. Independent audit has not been performed.
