---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For all n>=6 the occupied-column projection of a connected set cannot bypass an empty run; domination forbids >=3 empty columns. Empty-run lengths 0,1,2 give respectively two full rails, 2n(n-1) one-empty/one-double states, and 2n two-empty/two-double states, all size n. The exhaustive seven-case A/B/C one-swap table gives degree multiset (2 at degree 2n; 4n at 6; 4n at 5; 2n(n-4) at 4), 4n(n+2) edges, connectivity, and the exact rail-to-rail distance n by a constructed n-move path and disjointness lower bound. Independent full subset enumeration for n=6,7,8 yields exactly (74,192),(100,252),(130,320) configuration/edge pairs and the predicted degrees, but finite enumeration does not prove all n.

## originality

PASS

Closest literature studies prism domination parameters or connected domination reconfiguration under different move rules. Resultary top matches include complete-prism K_n square K_2 and Rips topology of circular ladders, neither the same invariant. No inspected statement implies the entire three-family minimum enumeration together with the exact unrestricted token-jumping exchange graph; this is best-of-knowledge only.

## value

PASS

Minimum connected dominating sets are canonical optimal graph backbones; their fixed-size token-jumping reconfiguration connectivity, complete degree distribution, and exact two-rail distance are independent nontrivial structural invariants, not routine restatements of domination number n. The exact all-n exchange table can be reused for reconfiguration and spanning-backbone questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
