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
Run the embedded `verify.py` using Python 3.10+ without third-party dependencies. The program independently generates all rank-two flats for \(N=4,5,6,7\), forms the exact pairwise-intersection graph and enumerates all inclusion-maximal cliques via bitset Bron--Kerbosch search. It verifies the predicted histogram in each case and the two-edge flat-closure axiom. Expected terminal line: `VERIFY_OK`.

# Logical scope
The finite verifier does not certify the arbitrary-size conclusion. The general result depends on the exhaustive four-case proof on the three pairwise intersection edges of a nonstar triple. The closest 2026 preprint was available as an abstract but not as fully inspected primary text; historical priority remains uncertain.
