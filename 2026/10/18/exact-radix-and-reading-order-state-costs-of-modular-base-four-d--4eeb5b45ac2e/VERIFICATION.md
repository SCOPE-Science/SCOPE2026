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

The base-four counter increments exactly on 3; copies of 3 reach all residues and translate any chosen one to the unique accepting residue. In binary MSD, the state retains right-aligned and opposite-parity pair counts and the final bit. Appending z changes these to (v+ez,u,z); padding the empty prefix with 0 fixes the start state. From third coordinate 0, 1100 and 0110 shift the two coordinates independently, and then a final 1 gives all third-coordinate-1 states. A 00 reset followed by shifts and an optional swap separates any differing residues; an initial 1 exposes a difference of last bit. In binary LSD, a pending low bit pairs with the next digit, and padding with a high zero preserves the count. All three residue-state types are reachable. For pending versus nonpending states, the suffixes (11)^t and 1(11)^t give incompatible conditions x=y+b−1 and x=y+b modulo r if their outputs agree for all t; the same-type distinctions follow by shifting one residue to zero. The argument uses only r≥2 and covers the empty word and binary indicator, not just full residue output. A separately constructed finite check at r=3 confirmed binary minimal sizes 18 and 9 and direct labels for 0≤n<64 with 0–4 redundant zeros. The frozen checker and its recorded r=2,…,9 log were inspected, not executed; finite checks do not replace the argument for all r.

## originality

PASS

The distinct finding is the exact binary reading-order separation 2r² versus 3r uniformly in r for the padded indicator. Neither automaticity, the Abelian-complexity theorem, the easy radix-four counter nor classical DFA minimization is claimed as new. Earlier comparisons did not resolve the binary state costs; the stronger later record for translated digit-residue sequences is an overlap for the radix-four component only.

## value

PASS

This natural family includes a previously studied automatic sequence. Its quadratic versus linear binary memory costs in the two reading orders are exact for every modulus, showing the cost of unknown pair alignment in a concrete family. The radix-four comparison supplies a simple baseline rather than the motivation for accepting the result on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
