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

# Reproducible checks
Run `python3 verify.py` with Python 3 and no external dependencies. The code independently enumerates faces via induced degrees and forbidden 3-path triples, checks all 2,046 faces and 149 facets, constructs all 1,021 matching pairs, checks all 8,946 Hasse covering incidences for acyclicity by complete topological sorting, and computes the exact signed integral Morse attaching column \((-1,-1)\). Separate direct mod-two boundary rank calculations corroborate the resulting homology.

`verification_output.txt` records the actual run and must finish with `ALL_CHECKS_PASS`. The decisive homotopy step is the standard theorem that an acyclic discrete-Morse matching yields a CW complex whose signed integer differential is computed by the displayed algebraic cancellations; for a CW complex with two four-cells and one five-cell the primitive attaching degree cancels one four-cell because \(\pi_4(S^4\vee S^4)\cong\mathbb Z^2\).

The nonpure shellability conclusion follows from the verified facet dimensions and Björner–Wachs Theorem 4.1. No formal proof assistant, independent human audit, or claim of a general Möbius-ladder classification is supplied.
