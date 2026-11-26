---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The N=2^k cyclic k-windows are distinct, so each must be hit. A mark hits exactly k of these windows. With N/k marks each window must be hit exactly once, forcing successive cyclic gaps at least k and hence all exactly k. Thus equality is equivalent to a successful residue modulo k. I reconstructed each stated cycle independently by partitioning the k-bit words into rotation orbits, taking the primitive root of each orbit's least element, and concatenating the sorted roots. The length-k window test verified the de Bruijn property of every reconstructed cycle. Direct cyclic substring slicing and incidence checks for every factor length through k give successful residues [0], [0,1], [0,1,2,3], and [4] at k=1,2,4,8. A longer window contains a length-k window, whose occurrence is already hit. At k=16 the independent scan of all starts gives exactly the eight recorded starts for each of the six factors. The missing residue sets are {9,10,11}, {10,11,12}, {13,14,15}, {3,4,5}, {0,1,2}, {6,7,8}, whose union is all residues. Hence every equality candidate fails and the minimum is at least 4097, not necessarily equal to 4097.

## originality

PASS

The density/spacing observation and some small-order attainments have predecessors or are elementary. The supported distinct content is the exact canonical order-eight equality residue and the obstruction to full circular lower-bound attainment at canonical order sixteen, which together identify the first failure along the specified dyadic sequence. The inspected prime-order result, earlier linear order-four census, and nearby order-five circular computations do not cover those conclusions.

## value

PASS

This is a motivated exact obstruction, not an arbitrary cutoff: dyadic orders have an integral density lower bound, and the canonical Lyndon construction is a natural test case after the known prime-order result. The four preceding attainment cases and the six-factor obstruction at sixteen locate the boundary within this family, and sharply separate guaranteed sharp covering from full covering. The obstruction is small enough to be reused or compared in studying other constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
