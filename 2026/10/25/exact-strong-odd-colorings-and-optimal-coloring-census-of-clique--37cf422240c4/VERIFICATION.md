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

Run `python verify.py` with Python 3.10+ and the standard library. The exact-integer verifier evaluates the signed-binomial character sum and an independently implemented subset-XOR dynamic program, checks that no smaller palette admits a coloring for the parameter cases listed in its source, and additionally enumerates permutations of colors assigned to labeled blade vertices for selected small cases.

Expected final output is `VERIFICATION_OK`. Test points include odd and even numbers of blades and clique sizes between two and six. For \(m=2\), the outputs agree with the factorial formula; for even \(m\) and \(s=2\), they agree with the closed form. No randomization or external dependencies are used.

The finite tests do not certify the all-parameter statement. The written proof uses the Gale–Ryser binary incidence criterion and exact Fourier parity projection. The proof is not machine-checked or independently audited. The full text of arXiv:2610.01441 was not available to rule out priority overlap.
