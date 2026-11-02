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

# Reproducibility

Run `python verify_ghm.py` using Python 3 standard library. The program directly constructs the list of neighbors of each vertex of the complete graph with the labelled perfect matching deleted and evaluates the synchronous rule on **all** ternary states. It enumerates the directed cycles of the resulting full functional graph; it does not assume any cycle-period upper bound. It also checks the independently derived color-class criterion by direct threefold iteration on every configuration at each tested order of at least six vertices.

The observed output is preserved in `verification_output.txt`. The orders tested are \(n=2,4,6,8,10,12\), covering \(9+81+729+6{,}561+59{,}049+531{,}441=597{,}870\) distinct labelled configurations. The observed orbit counts are: for \(n=4\), exactly two period-four orbits; for \(n=6,8,10,12\), respectively \(90,1428,16110,160776\) period-three orbits. Each order has exactly one fixed configuration. There were no other periodic cycles in the exhaustive cases.

# Scope of verification

The finite enumeration is exhaustive for the finite tested orders, not for the infinite family. The all-size theorem rests instead on the explicit four-case defect argument and the combinatorial inclusion–exclusion count in `RESULT.md`. The implementation is a reproducibility check, not an independent scientific audit or a proof of historical priority. No external software package, account, network resource, or hidden supporting file is required.
