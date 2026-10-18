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

The analytic reduction in `RESULT.md` uses the fact that \(J=M/a\) is a real orthogonal complex structure, so its complex eigenmodes are \(i\) and \(-i\). Each full-state mode is a repeated-root \(2\times2\) block with \(N^2=0\) and \(\|N\|_2=1\). The closed singular-value formula for an elementary Jordan shear gives the exact all-integer power norm. Its global maximum follows from explicit \(k=0,1,2,3\) values and the elementary decreasing bound \(2^{-k}(2k^2+2)\) for every \(k\ge4\). Synchronized component propagation gives a separately stated original-variable gain.

Run `python verify_dgda.py` with Python 3; no third-party modules are required. The program checks direct complex powers through \(k=40\), synchronized vectors, algebraic finite-peak comparisons, and explicit real update trajectories. It produces the embedded `verification_output.txt`, recording 209 passing deterministic checks. These computations do **not** certify infinitely many dimensions or horizons: those quantifiers rest entirely on the analytic proof.

The result does not claim the original DGDA convergence theorem is false; a weaker geometric rate remains compatible with a Jordan polynomial factor. It does not include an external audit or mathematical validation by another party.
