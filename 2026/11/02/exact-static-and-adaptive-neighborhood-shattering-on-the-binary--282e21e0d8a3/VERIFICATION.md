---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For F_2^4, the 35 two-planes are exactly the sets of three nonzero XOR-closed vectors. Pairwise intersection gives the 35-by-35 open adjacency with strongly regular parameters (35,18,9,9). A fresh independent script enumerated all 52360 four-supports (41160 shattered) and all 324632 five-supports (none shattered); independent version-space recursion gave Littlestone dimension five. The supplied grassmann35_cert.json independently checked a 32-leaf tree and 16 fixed response witnesses; the cardinality bound 35<64 excludes depth six. Boundaries at ambient dimensions 2 and 3 are singleton / complete graph. This is an exhaustive proof for the finite stated object only.

## originality

PASS

Prior ordinary Johnson and Hamming graph VC theorems concern different graphs; newer strongly regular graph bounds have potentially relevant VC consequences but the abstract does not imply the exact 35-vertex census or adaptive dimension. Published semantic search did not surface an exact duplicate. Best-of-knowledge original with a material inaccessible-source risk.

## value

PASS

The rank-two q-Grassmann graph is a canonical finite-geometry test case. The explicit first low-rank separation between offline and online neighborhood shattering, full static census and sharp adaptive tree are motivated, nonroutine combinatorial invariants, not a random parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
