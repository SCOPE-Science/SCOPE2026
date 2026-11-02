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

The exact binary structure matrix is used to evaluate the original algebra idempotent equation over genuine extension fields. `check.py` is standalone Python 3 standard-library code. Run `python3 check.py` and compare its stdout with `check_output.txt`; its final line must be `IDEMPOTENT_EXTENSION_CENSUS_OK 2208_EXHAUSTIVE_FIELD_MATRIX_CASES`.

The checker traverses all \(2^{n^2}\) binary structure matrices in dimension \(n=1,2,3\) and fields \(\mathbb F_{2^s}\) with \(s=1,\ldots,5\) for \(n=1\) and \(s=1,\ldots,4\) for \(n=2,3\). For each it enumerates every field vector and checks \(x^2=x\) in the original algebra directly, independently computing the predicted \(\mathbb F_2\)-kernel rank. It also exhausts the explicit primitive cubic over \(\mathbb F_{2^s}\) for \(s=1,\ldots,7\), a mixed nonsemisimple dimension-four example, and 75 seeded dimension-four/five samples. There are 2,208 field/matrix configurations in total, all passing. Arithmetic uses explicit irreducible field polynomials, not integer modular arithmetic on nonprime fields.

The infinite theorem relies on the algebraic proof in RESULT.md (Fitting reduction, normal-basis construction, squarefree leading monomials/Jacobian, eigenvalue-order cutoff). The computation is a finite check and does not establish an infinite proof or any historical originality. No independent audit has been performed.
