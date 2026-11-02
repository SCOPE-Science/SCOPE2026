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

# Verification and reproducibility

The proof treats the full infinite family; finite tests are consistency checks and cannot certify a limiting distribution.

## Direct finite predicate check

Run `python3 verify.py` with Python 3 and only its standard library. The `original_rule` function checks every open neighborhood by iterating over actually selected cells. The separate `row_column_rule` function verifies the formula \(d_i+e_j-2A_{ij}\ge k\). For boards of orders \(2\) and \(3\), it compares both predicates for every vertex subset and all requirements \(1\le k<2N\), totaling 2,608 direct agreements.

## Finite simulations

The same program performs reproducibly seeded Bernoulli trials at board orders \(80\) and \(180\), with fixed \(r=1\) and \(2\) and \(c=0\). For every sample it evaluates both original row/column neighbor conditions, counts low-degree rows/columns, and prints observed frequencies, proposed limits, and finite-size disagreements of the asymptotic surrogate events. The reported disagreements are expected at finite size. The complete probability limits follow from the independent-Poisson factorial moments, occupied-cell error bound, and high-probability equivalences in the proof—not from simulation.

## Independent status

The mathematical derivation and reproducibility checks have received self-review only. No independent audit or external certification has been performed. A future replication can re-run `verify.py` and independently examine the mixed-factorial-moment step and the \(O_r((\log N)^3/N)\) critical-cell bound.
