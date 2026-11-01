---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For U4={0,1}^4\{1111}, π0=id and parity(πv)=(-1)^|v| on 14 remaining corners, the count is 12^14. A Γ-fixed assignment is determined independently on Γ-orbit representatives by the allowed-parity elements centralizing Γv; this is a bijection, not a heuristic. An odd frame cannot commute with a 3-cycle fixing the weight-one remaining coordinate because C_S4((123))=C3 is even. A separate exact enumeration generated the 24 permutations and all 30 subgroups, computed every fixed count and exact stabilizer by downward subgroup Möbius subtraction, and verified the listed table, Burnside total 53,496,608,995,008, nontrivial 151,266,816 assignments/12,608,256 orbits. The seven file identities reconstruct the assigned Git tree SHA. No closure/enclosure claim follows.

## originality

PASS

The exact normalized S4 orbit/stabilizer census and no-three-cycle obstruction were not found in the inspected primary article, its single-subgroup program, the closest published Chair44 tiling-symmetry result, Resultary searches or exact-number web searches. The 32/768/6912 values are present in the primary paper, but the new full subgroup/stratum table is not. Best-of-knowledge only, with unindexed-source priority risk.

## value

PASS

This is a natural finite classification for the exact symmetry-reduced slice of Kamenetsky’s explicitly open 4D chair-frame search, whose raw space is 12^14 under the fixed-origin normalization. The three-cycle impossibility supplies structural pruning before expensive coarsening tests, while all stabilizer strata and orbit totals quantify all inequivalent symmetric candidates. It is motivated by the source’s stated larger-subgroup search reduction, not an arbitrary numerical slice; it does not certify any feasible monotile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
