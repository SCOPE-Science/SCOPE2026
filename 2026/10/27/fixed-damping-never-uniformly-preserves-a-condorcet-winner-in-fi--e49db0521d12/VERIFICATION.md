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

The standalone `verify_ballotrank.py` requires standard Python 3 only. Execute:

```sh
python verify_ballotrank.py
```

It constructs the exact complete rankings for the six-pair gadget at several positive integer multiplicities, reconstructs the majority-margin matrix, inserts BallotRank's specific normalized-win diagonal, and solves the stationary linear system over rational numbers. It checks each margin and column-sum invariant, the exact \(601\)-voter score difference at \(d=17/20\), and five further rational damping/examples. It also verifies rational identities for the limiting \(B-A\) expression.

Observed output from the packaged source:

```
PASS: 81 exact-rational majority, stationarity and limiting-formula assertions
d=17/20, k=25, voters=601: B-A=2462202045070872571152/1625203582777781791390465
d=17/20 limiting: B-A=3876/87233
```

These finite assertions do not prove the quantified claim for all real \(d\) or unbounded \(k\). The proof supplies the needed limiting column-stochastic matrix, the Neumann-series resolvent continuity argument, algebraic positive-gap identity, and the absorbing-state/Abel-limit argument. The score difference is strictly positive at \(d=17/20\), \(k=25\), and the general positive limiting gap ensures a finite witness exists for every fixed \(0<d<1\). No probabilistic simulation, infinite certificate, or external expert assessment is claimed.
