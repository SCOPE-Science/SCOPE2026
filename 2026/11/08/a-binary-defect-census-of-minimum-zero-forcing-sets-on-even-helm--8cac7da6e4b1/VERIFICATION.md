---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Forcing chains partition the 2k pendant vertices into chains having at most two pendants each, so any k-vertex minimum start is leaf-only. A forced hub first requires a 111 triple; chain endpoints imply exactly one such hub force. After hub coloration, zero-index rim vertices can only be seeded by neighboring 11 selected rims and propagated across isolated selected rims; all but one zero component must be seeded, and the final unseeded singleton is the physical 000. This is equivalent to one adjacent equal-type pair of each defect kind with all other defects alternating. Marking the unique 11 pair and distributing odd alternating gaps gives N_k=2k sum_{r>=2}(r-1) binom(k-2,2r-3) and hence 6 (k=3) or k^2 2^(k-4) (k>=4). Independent zero-forcing closure enumerated all leaf-balanced subsets for n=6,8,10,12,14 giving 6,16,50,144,392, confirming boundaries; full proof addresses unbounded k. The slide graph is edgeless because a leaf slide necessarily gives an internal selected vertex.

## originality

PASS

Best-of-knowledge: the earlier helm treatment determines zero-forcing numbers and propagation times but not the all-minimum-set defect classification, exact number, or slide-reconfiguration order. Neighboring published zero-forcing censuses concern different graphs (subdivided helms, cycle powers, circular ladders).

## value

PASS

The even helms are a natural infinite graph family already studied for zero forcing; exact enumeration and an if-and-only-if local defect description of every minimum configuration are significant structural invariants. They enable reconfiguration and sampling analyses and are not obtained from the known zero forcing number. The slide-isolation is a transparent but legitimate corollary, not the sole value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
