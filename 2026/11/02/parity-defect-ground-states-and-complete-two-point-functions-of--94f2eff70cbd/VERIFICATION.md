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

# Verification of the finite antiprism Ising theorem

Run `python3 verify.py` in this directory with Python 3 and its standard library. Observed replay: `VERIFY_OK brute_n=7 transfer_n=32 constructive_n=49`.

The checker (1) exhaustively enumerates every labelled Ising spin configuration for each \(3\le n\le9\), (2) independently minimizes the periodic four-local-state transfer recursion and counts magnetization sectors for \(3\le n\le34\), and (3) explicitly constructs every stated ground state and performs exact rational two-point averages for \(3\le n\le51\). These computations check values and normalizations against separate closed formulas. They do not prove any untested larger size; the all-size result uses the frustration-incidence inequality and equality-case classification in RESULT.md.

The ground-state measure fixes \(n\) and the zero external field before taking \(T\downarrow0\). No finite-temperature closed form or independent validation is claimed.
