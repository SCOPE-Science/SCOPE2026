---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The cycle selects at most one member of each of 120 nonpalindromic length-eight reversal pairs. Its balanced directed de Bruijn incidence forces selected signed ports to pair positively/negatively in each of 72 reversal orbits; matching omitted pair ports through cost-one edges yields a perfect matching on 240 ports. The independently rebuilt graph has 120 cost-one omission plus 210 cost-zero transition edges. The actual pinned DUAL.txt 240 integers sum to 28 and satisfy y_u+y_v<=cost for every one of 330 edges, proving at least 28 omitted reversal pairs and hence length<=92 without trusting solver output. The pinned WITNESS.txt has exactly 92 cyclic distinct nonpalindromic length-eight factors, no reversal collisions and fundamental period92. A separate independent script reconstructed graph, all inequalities, port-count and witness tests from source bytes. No exhaustive search or computational timeout is invoked as impossibility.

## originality

PASS

The published lower construction length 92 and previous published upper 96 are different assertions. A new exact integral matching dual certificate that proves upper 92 closes that genuine gap; no inspected primary source states the bound 92 as proved.

## value

PASS

Resolves a concrete and long-tabulated natural extremal sequence problem at the first disputed small order beyond exact cases. A compact exactly checkable matching-dual obstruction proves optimality of a previously known construction and may guide further order-specific certificates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
