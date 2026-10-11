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

The theorem is analytic. Reproduce the checks by running `python3 verify.py` in the same directory as this document. The program uses only Python's standard library and prints `NOWHERE_POSITIVE_SEMIGROUP_RATIONAL_BOUNDS_AND_CUTOFF_OK` if all assertions pass.

The rational computation certifies \(\sum_{n\geq1}n^2(1/20)^n=420/6859\) and \(1+840/6859<2\), while the Taylor lower bound certifies \(e^3>20\). It also checks the polynomial Taylor inequality needed for \(e^n>4n\) on \(n\geq3\), including its positive derivative at the boundary, and exercises several rational-time cutoff instances.

For any \(t>0\) and integer \(n\geq\lceil t+3\rceil\), the all-real-time comparison uses \(e^{2t}-1<2te^{2t}\), \(e^{n^2-nt}\geq e^{3n}>4ne^{2n}>4ne^{2t}\). These are complete analytic inequalities and are not deduced from finite samples. The Dyson–Phillips series bound for the off-diagonal reference entry and the reducing-subspace formula for the antisymmetric perturbation are spelled out in RESULT.md; they are the nontrivial infinite-dimensional steps. The individual-orbit bound uses the spectral gap, Duhamel's formula, and the explicit uniform-in-time estimate on the antisymmetric correction. No finite experiment or code execution is treated as an infinite-dimensional proof.

The only external source needed to identify the underlying operator and compare previously stated conclusions is the lawful public first version of Alexander Dobrick, arXiv:2609.00425v1. The proof and numerical checks do not require unpublished data or nonstandard software. The independent audit status remains unperformed.
