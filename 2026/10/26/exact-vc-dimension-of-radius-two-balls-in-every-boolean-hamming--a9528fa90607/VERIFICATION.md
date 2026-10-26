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
# Reproducible verification

Run `python3 verify.py` under Python 3.10 or later. No packages, network access, or external files are required.

The checker encodes all \(3\cdot2^{10}=3072\) balls of the enlarged ten-cube family with radii \(0,1,2\) as bit positions. It computes exact membership masks for all \(56\) weight-at-most-two points, enumerates every shattered sorted sample subset using the hereditary shattering condition, and obtains the exact counts \(1540,27720,49830,0\) at sizes two through five. The last zero is the bounded exhaustive certificate used in the proof. The mathematical reduction from arbitrary dimension to ten support coordinates is stated in `RESULT.md`; the code does not replace that lemma.

The checker also tests actual fixed-radius-two balls in dimensions one through eight, using bit-translation symmetry to anchor a sample point in the larger cases, and independently checks all membership patterns on the two explicit lower-bound witnesses. A normal completion ends in `VERIFY_OK`.

**Proof limits.** Exhaustion of individual cubes through dimension eight would not prove the infinite-dimensional theorem. The infinite assertion uses the exact reduction lemma plus the exhaustive ten-coordinate enlarged-family certificate. The code has been executed in the supplied package; no independent reviewer, theorem prover, or external attestation has checked it.
