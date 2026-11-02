---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS. The binary addition recurrence t(2n+j+b)=t(n+floor((j+b)/2)) XOR((j+b)mod2) gives residual transition (j,s)→(floor((j+b)/2),s XOR((j+b)mod2)), starting (c,0), output t(j) XOR s. Distinct j,s residuals are output-distinguishable because a period or anti-period for Thue–Morse would contradict alternating parity at numbers 2^h−p as h changes, including eventual periods. After e input bits u, reachable state is (floor((c+u)/2^e), t((c+u)mod2^e)); residue intervals yield v_e(c) and two exceptional coordinate-two corrections, while lower coordinates eventually contribute exactly four states. Disjoint upper-level first coordinates give the exact arbitrary-c sum; m≥2 sharp bounds follow from each v_e in [2,4] and explicit endpoint shifts. Independent BFS computed exact reachable pairs and matched the formula for every c=0..2047; finite checks support the symbolic all-c proof.

## originality

PASS

PASS, best of knowledge with clearly bounded literature/access risks. The cited general upper bounds/MSD estimates give neither exact LSD state counts nor parity/residue corrections and do not dominate the theorem. The result supplies genuinely different orientation-specific state complexity.

## value

PASS

PASS. Orientation-sensitive minimum automaton complexity for a canonical automatic sequence is a natural exact invariant; generic finite kernel bounds or MSD-first state counts do not determine per-shift minimal LSD state counts. The explicit binary-digit formula and sharp dyadic extremal range provide a structural classification of an infinite family, not a tautological restatement of a standard DFAO construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
