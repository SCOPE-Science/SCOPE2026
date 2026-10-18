---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Count lower-symbol multiplicity j in a four-term window. For u>0, j=0,1,4 contradict largest=sum of two smallest; j=2,3 work iff v=2u. For u=0, only 4 zeros or one zero can appear; sliding cannot transition between these counts without forbidden intermediate 2 or 3 zeros, hence only zero constant or one zero in every window, giving e_(i+4)=e_i and exactly four phases. Build 8-state suffix transfer matrix for binary 4-blocks with 2 or 3 ones. Independent exact symbolic inversion of I-zM gives GF (1+z+2z²+3z³−z⁴−2z⁶−2z⁷+z⁹)/(1−z−z³−z⁴+z⁶); characteristic x(x+1)(x^6−x^5−x^3−x²+1). Essential 7-state graph strongly connected and primitive by 3- and 4-cycles; Perron spectral radius >1 yields entropy and uncountably many aperiodic paths. Independent exact counts n=0..13 agree [1,2,4,8,10,16,25,39,61,95,149,233,364,569].

## originality

PASS

Nacin 2023 defines Van der Laan property and develops increasing/Padovan-related sequences, with one known periodic (1,1,1,2) example. Full two-symbol alphabets, zero/positive rigidity dichotomy, entire finite-word generating function, and entropy are not contained in the inspected sections. Positive topological entropy follows from standard finite-type-shift methods, not a novel theorem of symbolic dynamics.

## value

PASS

Identifies exactly what happens on the smallest nontrivial alphabet for a recently introduced integer recurrence: a rigid zero branch versus a positive-entropy family. Complete local-language count and entropy quantify complexity far beyond the known isolated period-four example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
