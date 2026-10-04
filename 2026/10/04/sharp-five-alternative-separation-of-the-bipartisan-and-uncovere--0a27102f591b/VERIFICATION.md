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
The embedded `verify_bipartisan_uncovered_first_layer.py` performs an exact finite replay using only the Python standard library.

For every tournament of orders \(1\) through \(5\), the maximal lottery is computed independently by rational Gaussian elimination and by Pfaffian null-vector formulas on candidate supports. Both implementations verify positivity, normalization, zero payoff on the support, and nonnegative payoff against every pure alternative.

The uncovered set is independently computed from the covering relation and from the equivalent two-step-king characterization.

The verifier confirms:
- equality \(BP(T)=UC(T)\) for every tournament through order \(4\);
- exactly \(120\) strict cases among the \(1024\) order-five tournaments;
- exact incidence \(15/128\);
- order-five joint-size counts \((1,1):320\), \((3,3):520\), \((3,4):120\), \((5,5):64\);
- one strict isomorphism class of full orbit size \(120\);
- canonical maximal lottery \((1/3,0,0,1/3,1/3)\);
- canonical sets \(BP=\{A,D,E\}\) and \(UC=\{A,C,D,E\}\).

Run:

`python3 verify_bipartisan_uncovered_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite first separation.
