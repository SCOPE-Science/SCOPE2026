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

Run `python verify.py` with Python 3 and SymPy available. The completed run printed `ALL CHECKS PASS`.

The program checks local flip conditions against an independently constructed physical graph for every labeled spin state of each size from four through eight columns. It compares all energy-graded weak and strict counts with a separate cyclic transfer recurrence and checks ground multiplicities. Further exact checks cover the marked 16-state characteristic factorization, positivity of the fifth power of the 14-state active component, and the 4-state nilpotent expansion used to count ground states. For lengths four through eleven it checks the total weak counts listed in the theorem.

The determinant and interval/root calculations use exact symbolic arithmetic except for final decimal display. They do not, by themselves, establish the infinite-size law; that conclusion additionally uses the analytic Perron argument given in the proof. This verification does not assess dynamical hitting probabilities, the bulk triangular-lattice limit, or global bibliographic novelty. Independent scientific validation has not been performed.
