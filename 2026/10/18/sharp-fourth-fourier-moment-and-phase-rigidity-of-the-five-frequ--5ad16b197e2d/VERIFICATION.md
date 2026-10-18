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

# Verification of five-frequency cross fourth-moment theorem

The program `artifacts/verify.py` is standalone Python 3 and uses `cmath`, `itertools`, `random`, `fractions`, and `collections`; optional SymPy checks the rational square completion. Invoke `python artifacts/verify.py` from the document directory. The actual output from the current files is `artifacts/verification_output.txt`.

The test recomputes the fourth moment in two independent ways for \(240\) random complex vectors: by direct grid evaluation and by the difference autocorrelation identity. The test checks the claimed bound on each sample and all \(72\) prescribed extremizers. It also enumerates all \(3^5-1\) nonzero integer sign/zero coefficient patterns on each of three finite grids, checks the exact target mass distribution with rational arithmetic, and uses symbolic arithmetic for the displayed square completion.

The proof is elementary and uniform in the grid order: orthogonality isolates exactly the integer differences, positivity of the pair-product coefficients allows amplitude equalization, and one-variable square completion gives the sharp constant. Choosing nonnegative equal-amplitude antipodal pairs saturates the mass-deficit envelope for every prescribed mass triple. No finite computation is substituted for the universal proof. These computations do not establish novelty, and they do not independently audit the paper.
