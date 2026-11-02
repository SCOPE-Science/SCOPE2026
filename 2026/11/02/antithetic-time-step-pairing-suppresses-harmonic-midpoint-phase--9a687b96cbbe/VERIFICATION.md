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

# Verification and limits

The analytical proof derives the exact midpoint matrix, real phase sums, characteristic-function representation of endpoint ensemble variance, and the unique countermonotone block optimum. It uses exact uniform moments \(\mathbb EU^2=1/3\), \(\mathbb EU^4=1/5\), and \(\operatorname{Var}(U^2)=4/45\), with a uniform fourth-derivative bound for the arctangent angle. Both positive leading constants are obtained by taking \(m\to\infty\) at fixed \(T,\kappa,\alpha>1\). A finite grid alone does not justify the limit, and no automated checker supplies a universal or independent proof.

`VERIFY.py` is a standalone rerun script requiring Python 3, SymPy and mpmath (versions in `requirements.txt`). Run `python VERIFY.py` in the same directory. It symbolically checks the arctangent derivative identities, evaluates uniform moments, computes one-dimensional quadrature for exact finite-block phase and endpoint dispersions, and checks scaled limiting constants for six grid sizes. It prints `VERIFY_OK` only if all assertions pass. The reproducibility check returned `VERIFY_OK 77 symbolic, exact uniform-moment, high-precision finite-grid checks`.

The code does not test all admissible \(T,\kappa,\alpha\), every finite step size, or all possible couplings. Those quantified assertions require the proof. No independently performed audit or publication certification is asserted.
