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

Read entire RESULT.md at frozen blob 7b607ba36acbcb6bd34ca311f4efa52b3270ba29. Required weight-two de Bruijn edges form disjoint directed rotation necklace circuits, each with one incoming and outgoing required edge at every incident (k-1)-word. Adding the cycle induced by 10^(k-2) has length k-1 and passes through all single-marker (k-1)-words; each required necklace touches one, hence the union is balanced and connected and Eulerian. For the lower bound, subtract one copy of each mandatory edge. Any fewer than k-1 additional edges decompose into short periodic circuits. A short circuit meeting the adjacent-pair necklace cannot meet another weight-two necklace; Fine–Wilf forces any two meeting short circuits to have identical primitive vertex support. Thus short extras cannot connect the required distinct necklaces. Fresh independent Euler constructions checked literal windows for k=4..17; exhaustive shorter cyclic binary words were checked at k=4,5. These are finite corroborations of the all-k Fine–Wilf proof.

## originality

PASS

Ruskey–Sawada–Williams (2012) explicitly use a shorthand fixed-weight universal cycle, a cyclic encoding through (k-1)-windows, not a literal covering of all k-length weight-two windows. Consequently their binom(k,2) length does not settle the additional connector cost k-1. Published universal-cycle and bounded-weight de Bruijn constructions were compared but no direct sharp literal-cover implication identified.

## value

PASS

The exact optimal circular host length for all binary weight-two k-mers is a natural string assembly and covering invariant. It quantifies unavoidable necklace-connector overhead and supplies a constructive optimum for every k, not a single arbitrary computational instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
