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

Separations of one or two along the cyclic list of selected vertices are isolated, since two consecutive such separations create induced degree two. They are exactly the pairs; cuts at separations at least three yield the unique singleton/short-pair/long-pair blocks. Thus m=2|D|+s+l+e, with s of parity |D|, giving the optimum and exactly the listed defect types, each realizable from m=7 onward in its residue. Marked-component counting weights each ordered block list by m divided by its component count, including periodic words. To verify the nontrivial exchange table, fix the empty insertion site. It has at least one selected neighbor by maximality. With one, that neighbor must be paired, and removing it or its mate gives two moves. With two, remove one and require that the survivor be unpaired after removal; with three or more there is no move. The middle of a long pair contributes two. Between paired components, a gap of 3 between selected endpoints gives zero; a gap of 4 gives two moves at each end and none in the middle; a gap of 5 gives two at each of its four sites. When singletons occur, all gaps between components are of length 3 and all pairs are short: an S–P gap contributes one, an S–S gap four, a P–P gap zero. These rules give degrees 8,6,4 for paired configurations with zero, one, two long pairs at residue two, and degree 6 or 4 for consecutive or nonconsecutive singletons. At residue one, the E roots move by 4 and an L rooted at x attaches to E roots x and x−4; the computed degrees exhaust all neighbors. At residue three, the S root moves by ±4, exhausting its two neighbors. In residue two the frozen legal moves reduce to short-pair configurations; surplus transfers connect all surplus vectors with one pair anchored and carrying one surplus around all the gaps moves each pair one step, so all labeled phases connect. Combining the counts with handshaking gives every listed edge total. Independent direct subset and one-token enumeration for 7<=m<=14 agreed, e.g. m=10 gives 50 vertices, 160 edges, degrees {4:5,6:30,8:15}; m=14 gives 105, 322, {4:21,6:56,8:28}. The frozen script was inspected, not executed: it exhausts subsets through 16 and checks generated words through 32; longer tests stated in the notes are separate from that script's default loop. The local gap proof, not finite enumeration, validates the infinite theorem.

## originality

PASS

The labeled maximum-dissociation exchange invariant, especially the full degree census and edge counts, is distinct within the inspected sources. Several close prior classification frameworks concern independent sets, a nonsquare graph or a different selected-set condition; a later induced-matching record gives a significant structural overlap on a proper subproblem, not earlier full coverage.

## value

PASS

The square cycle is a natural first nontrivial power for induced-degree-one selection. Maximum size alone misses a sharp periodic mobility transition and the exchange-degree heterogeneity at residue two; these exact invariants describe how the whole labeled optimum state space can be traversed without relaxing optimality. The local defect argument is reusable beyond individual finite checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
