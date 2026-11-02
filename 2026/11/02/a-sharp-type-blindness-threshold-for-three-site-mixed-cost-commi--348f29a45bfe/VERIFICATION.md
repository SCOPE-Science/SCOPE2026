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

# Verification and reproducibility

`verify.py` is the standalone exact-rational verification program. Run `python3 verify.py` from the folder containing that file. It uses only Python's standard library and has no external data dependencies.

The program computes all three facility-pair costs for every one of the eight maximum/average type assignments. It checks the two affine cost-difference identities in the proof, the universal-optimum criterion, homogeneous optimality of a shortest pair, and both explicit counterexamples. It passed for \(8{,}327\) integer triangle triples with \(1\le p\le r\le q\le44\), together with \(3{,}339\) additional reproducibly seeded positive rational triangle triples; these are finite checks, not an infinite certificate.

The general theorem is certified here only by its human-readable algebraic proof. The inequalities \(q\le p+r\le2r\) and the complete linear form in the three binary type variables are its critical noncomputational steps. The four-point example is checked exactly. Independent audit has not been performed.
