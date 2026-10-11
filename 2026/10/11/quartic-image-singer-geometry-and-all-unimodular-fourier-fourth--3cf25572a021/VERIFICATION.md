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

Run `python3 artifacts/verify.py` with the standard Python 3 interpreter; no nonstandard packages or files are required. The checker independently regenerates the quartic graph's unordered pair-sum fibers, confirms the fifteen displayed comparison relations and the histogram, computes the exact ordered energy \(445\), and verifies that the fourth-power image is a perfect difference set.

The checker uses fraction-free integer determinant computation to verify both specified minors (eight-by-eight determinant \(1\) and nine-by-nine determinant \(13\)), checks modular rank eight, and tests that arbitrary fourth-power-phase labels combined with additive characters satisfy every equality relation. It also checks that a single-point phase perturbation can break equality. Its expected output is

`VERIFY_OK prime=13 fibers=76 nontrivial_fibers=15 energy=445 rank_Q=9 rank_mod13=8 delta8=1 delta9=13 phase_components=13 torus_dimension=4`

The algebraic determinant and kernel argument in `RESULT.md` supplies the mathematical proof. The integer computation is exhaustive at the explicitly stated finite prime \(13\), not evidence for any claim about all prime fields. No unrestricted-operator optimality, other-field classification, or independent external validation has been established.
