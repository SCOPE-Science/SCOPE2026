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

# Reproduction and limits

Run `python3 verify_c60.py` with Python 3 (standard library only). The supplied `verification_output.txt` records the output of an actual run. The program creates the icosahedron and its 60-site truncation from a finite reproducible edge prescription, enumerates all 125 icosahedral perfect matchings with 64 choices each, and reconstructs the 8,000 distinct frustration patterns as spin configurations modulo inversion.

Critical independent checks include all 8,000 energy values, state-by-state total spin zero, unique frustration patterns, 30 cross-pentagon correlations of \(-1\), 60 pentagonal correlations of \(-3/5\), a 30-by-30 exact integer matrix identity, five exact integer row-reduction rank calculations, and the full graph-distance census of 1,770 unordered site pairs. The eigenvalue factors are derived from the integer identity and kernel dimensions, not numerical spectral fitting.

**Logical boundary:** The exhaustiveness of the state enumeration relies on the facial-parity/matching bijection proven in `RESULT.md`; no computational test alone establishes it. The external historical novelty assessment is incomplete where the full texts of earlier Ising papers were inaccessible. Independent scientific audit has not been performed.
