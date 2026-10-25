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

# Reproducible checks and proof boundary

Run `python verify.py` using Python 3. The command prints the output embedded as `verification_output.txt`. It enumerates all four-coordinate nonnegative integer compositions of lengths \(5\) through \(9\), tests all admissible pairs of light compositions, and checks no admissible light triple at length five. It also independently verifies the explicit construction's three-symbol deletion shadows at every length \(5\) through \(20\).

At lengths \(5,6,7,8,9\), light-composition counts are \(16,10,4,1,0\), and compatible-light-pair counts are \(12,0,0,0,0\). At length five, the only light partners of \((0,1,2,2)\) are \((2,2,0,1)\) and \((2,2,1,0)\), which are incompatible with one another.

The unbounded proof is mathematical: heavy-coordinate disjointness, maximum light mass eight, the light-pair inequality, and the complete length-five type analysis. These code checks are finite corroboration, not an assertion of exhaustive validation at unbounded length. Independent scientific validation has not been performed.
