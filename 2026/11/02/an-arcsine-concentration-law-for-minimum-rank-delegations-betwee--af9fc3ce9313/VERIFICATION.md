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

# Verification procedures

Run `python3 verify_branching.py`. No non-standard packages, input files, or network access are required.

The program enumerates all \(65{,}534\) ranked-preference sequences for \(1\le n\le15\). For each sequence it determines the costs of all feasible cut choices directly and independently finds the earliest partial-sum minimum. It aggregates exact integer frequencies and rational means to check the closed combinatorial distribution, minimum Borda excess, and BFD expectation including the middle-agent distance tie. For \(1\le n\le8\), it additionally enumerates all directed edge-choice vectors, follows edges to detect cycles without assuming the cut theorem, and checks the minimum cost over all valid branchings, making \(4{,}096\) independent feasible-branching/profile comparisons.

The program returned three `PASS` lines with the expected counts. The all-size proof uses a cut characterization and the reflection principle. The universal tie-break limiting law uses the standard Donsker invariance principle and Brownian uniqueness/arcsine theorems; finite checking does not establish them, so the proof explicitly invokes those classical results. The phrase *first public date* refers to the archived 2021-12-14 release of the initiating paper and not its 2022 proceedings date. No external or independent audit has been performed.
