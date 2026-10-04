---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The infinite proof has four critical checks. First, the phase map on nonzero states advances by one modulo \(k\) under every nonzero transition. Second, every killed canonical phase representative must traverse the unique chain labeled by a full copy of \(u\) before entering the sink. Third, distinct killed phases force distinct occurrence-start residues modulo \(k\), and unborderedness then separates selected occurrences by at least \(k+1\). Fourth, the first displayed copy of \(u\) merges the two states in every nonzero phase, so later deterministic actions cannot recreate multiplicity within a phase.

`artifacts/verify_pribavkina_profile.py` reconstructs the automaton from the transition definition and independently computes exact subset-image distances. The recorded run checks every binary unbordered word for \(2\le k\le7\) and every ternary unbordered word for \(2\le k\le5\), including every witness \(u(au)^r\). The output reports \(84\) binary words and \(216\) ternary words and ends with `VERIFY_OK`.

These finite computations are stress tests only. They do not certify unenumerated alphabets or lengths; those are covered by the symbolic proof.
