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

Run `python3 verify.py` from the directory containing this document. The program depends on the Python standard library only. It validates finite-field multiplication, the \(25\)-vertex Paley adjacency predicate, strong-regularity parameters \((25,12,5,6)\), all clique faces and bounds, and exactly \(75\) legal high-dimensional elementary collapses. It independently evaluates the \(126\)-generator spanning-tree presentation and its legitimate Tietze eliminations, including orientation and word substitutions. It checks mod-two boundary ranks, every natural semiaffine automorphism, all signed simplex fixed-point Lefschetz traces, and the resulting character distribution.

Expected final line: `VERIFY_OK_PALEY25_FLAG_HOMOTOPY_SEMIAFFINE_CHARACTER`. The file `verification_output.txt` contains the actual successful output captured from this verifier. The verifier's assertions and exact group-presentation transformations—not the log alone—justify the finite claims. Integral homotopy follows from the elementary collapses, vanishing fundamental group, Euler characteristic, Hurewicz and Whitehead. The trace calculation uses ordinary rational homology concentrated in degree two, so it is not merely an alternating virtual character.

Limits: no independent external audit, no general-order theorem, and no inference that a database search establishes uniqueness or novelty.
