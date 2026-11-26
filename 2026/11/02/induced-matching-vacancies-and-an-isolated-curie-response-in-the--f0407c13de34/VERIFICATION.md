---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An independent exact enumeration built the regular icosahedron from cyclic shifts of (0,±1,±φ) with squared edge length 4, using arithmetic in Z[φ]. Recursing over all 531441 spin assignments and adding only bonds to previously assigned sites reproduced all thirteen minima and their multiplicities. It also checked both inclusions of the vacancy geometry by comparing exact vacancy keys with all four-sets whose induced degrees are (1,1,1,1); there were 75 keys with two signings each. At occupancy 10 the 30 vacancy keys are precisely edges, with eight signings each. At r=1/2 the equality states all have M=0 and counts 72, 240, 150 at occupancies 12, 10, 8. At r=1 the equality table is (m,M;count)=(0,0;1),(6,0;80),(7,−1;60),(7,1;60),(8,0;150). The sharp bounds 2b+m≥−8 and b+m≥0 give the piecewise lower envelope by interpolation between the boundaries; m≤12 and m≥0 give the two outer rays, and the asserted states attain each bound. Spin reversal equates the two signs for each two-signing vacancy set and forces zero thermal mean. Differentiating at zero field first gives χ/β=E[M²]; the finite uniform ground-state limit is 120/351=40/117 only at D=J. This is total magnetization susceptibility, with no per-site scaling. Replay: python3 /workspace/branches/independent_finite_checks.py 2.

## originality

PASS

Verified prior coverage includes the fully occupied 72-state Ising limit. A later indexed full-field study supplies the matching zero-field phases and degeneracies and implies the Curie fraction from its magnetization-resolved table, but is not earlier evidence and does not supply the exact induced-2K2 vacancy rule. The complete geometry is a distinct supported claim on the bounded comparison.

## value

PASS

For a natural frustrated finite cluster, the result does more than recompute its Ising ground energy or report the number of ternary states. It exactly identifies the vacancy supports that open the intermediate phase and determines how the two coexistence degeneracies differ in their zero-field response. The induced-matching support criterion is usable without repeating a spin enumeration, and remains a distinctive contribution even in light of the later aggregate table. No bulk phase transition or quantum interpretation is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
