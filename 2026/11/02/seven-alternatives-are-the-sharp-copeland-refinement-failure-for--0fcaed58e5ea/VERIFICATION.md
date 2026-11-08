---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The stated 2024 DSR home-plus-away score is specialized explicitly to strict tournaments, with both active partition conditions and the empty-successor case. We independently wrote a C implementation of the score separate from the source dsr_verify.c, compiled it and enumerated without pruning every integer bit encoding of each labeled tournament n=2,...,7. Failure counts were exactly 0,0,0,0,0,5040 out of 2,8,64,1024,32768,2097152; first failure is bit mask 1324. The witness scores were independently recovered as DSR (6,3,2,4,5,14,14) and Copeland (3,3,2,2,2,5,4). A separate independent 7! permutation-orbit enumeration found 5040 distinct relabelings of witness 1324, hence trivial automorphism group; original package code checks all 5040 failures lie in that orbit. These exact finite exhaustive checks establish the bound n<=7, not arbitrary larger tournaments. Primary 2024 source Proposition 7 and scoring equations were inspected.

## originality

PASS

Hou 2024 Sections 4 and 6.3 established up-to-four containment, reported five-case verification and posed a general Copeland refinement conjecture. The new bit-coded exhaustive first failure at seven and unique asymmetric isomorphism class refutes that exact 2024 rule. The 2025 journal abstract repeats the smaller guarantee; a 2026 DSR tournament solution uses a different scoring version, and its full text could not be accessed due to VPN disconnection. Resultary seven-alternative Banks/uncovered census concerns different tournament correspondences and does not cover this DSR/Copeland condition. Qualified PASS, with a precise risk of an already-known counterexample in 2025/2026 follow-ups.

## value

PASS

This resolves an explicit universal refinement conjecture for a named voting rule, determines its sharp first counterexample size, and classifies/counts every first-layer failure. The finite census is natural and complete over the alleged minimal order, not an arbitrary search for small exceptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
