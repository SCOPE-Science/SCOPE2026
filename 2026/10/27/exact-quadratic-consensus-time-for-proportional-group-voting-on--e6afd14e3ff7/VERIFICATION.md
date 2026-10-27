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

The accompanying `verify.py` was executed from the packaged working directory with Python 3 and no third-party packages. It enumerated and independently solved 336 finite labeled absorbing-chain instances with exact rational arithmetic. The result was `PASS exact labeled CTMC: 336 hyperpath/seed instances` followed by `PASS unique active hyperedge, exact state count, fixation and hitting-time formulas`.

The proof uses an invariant finite Markov chain and checks its mean hitting-time recurrences algebraically for every admissible parameter; finite checks do not establish the infinite family on their own. Tested parameter ranges were \(2\le L\le7\), \(2\le k\le8\), \(1\le s\le\lfloor k/2\rfloor\), and \(1\le j<L\). No verification of other graph structures, rewiring, majority dynamics, empirical applicability, or publication priority is implied.
