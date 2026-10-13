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

The accompanying `verify.py` enumerates all linear subspaces of the four-dimensional exterior algebra over the prime fields \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), tests closure by explicit multiplication, enumerates every ordered complementary subalgebra pair, reconstructs the corresponding idempotent projections, and verifies all 16 basis-pair instances of the weight-minus-one Rota–Baxter law. It also exhaustively evaluates the automorphism family \(\operatorname{GL}_2(\mathbb F_q)\ltimes\mathbb F_q^2\) on the incidence pairs.

The rank multiplicities were \((1,13,24,13,1)\), \((1,37,72,37,1)\), and \((1,151,300,151,1)\) for \(q=2,3,5\), respectively, and the computed incidence-orbit sizes were \(12,36,150\). All checks passed. These are genuine exhaustive finite-field enumerations for those prime fields; the arbitrary-field assertions follow from the written structural proof and are not independently certified by enumeration.

Run `python verify.py` using Python 3.8 or newer. The script uses only the standard library.
