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

# Reproduction and scope

Run `python3 VERIFY.py` with Python 3 (standard library only). It prints `VERIFY_OK assertions=5913` on a normal supported Python runtime. The checker directly constructs wrapped-kernel recruitment matrices, tests finite matrix similarities and power traces, compares the two-reserve Perron-root formula with direct matrix eigenvalues, and checks finite rate-mixture monotonicity and the displayed numerical threshold crossing. It uses a fixed pseudorandom seed for deterministic test inputs.

This is a finite consistency check, **not** an exhaustive or formal proof of the infinite statements. The decisive argument is the exact double-integration identity followed by strict Hölder log-convexity, which covers all Borel probability mixing laws on positive rates without moment assumptions. Boundary configurations and strictly positive source and settlement multipliers are explicitly addressed in RESULT.md.

The available external scientific source material comprises a mixture of inspected complete articles, relevant inspected excerpts, and limited abstracts; the inaccessible complete Blowes–Connolly (2012) article is a remaining originality risk. Independent scientific audit has not been performed.
