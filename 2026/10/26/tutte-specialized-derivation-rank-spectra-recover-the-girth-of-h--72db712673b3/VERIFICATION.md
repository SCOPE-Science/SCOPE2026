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
# Verification of the derivation rank law

Run `python3 verify_derivation_rank.py` with a standard Python 3 interpreter. The program constructs a multiplication table for each finite height-two poset directly from vertex idempotents and edge elements. It then sets up the matrix of linear Leibniz constraints for a completely unspecified endomorphism, row-reduces the full system, enumerates its kernel, and computes the ranks of all resulting endomorphisms. The comparison side uses the graphic rank of every subset from union-find, independent of the unknown-operator calculation. No assumption that all derivations have a specific normal form is made in the computation.

The exhaustive configurations include one edge over \(\mathbb F_3\), two disconnected edges over \(\mathbb F_3\), a star and a path each with three edges over \(\mathbb F_3\), the four-cycle over \(\mathbb F_2\) and \(\mathbb F_3\), a four-cycle with a leaf over \(\mathbb F_2\), and the six-cycle over \(\mathbb F_2\). All derivation-rank coefficients agree with formula (1), and the number of derivations in each case equals \(q^{2m}\). An additional arithmetic expansion normalizes the formula for several prime powers, including 4 and 9. These do not constitute a direct Leibniz-matrix census over proper extension fields; the proof uses general field properties and supplies the all-prime-power conclusion.

The code does not implement a comprehensive literature priority check or any external verification. The proof establishes the infinite family; finite enumerations only provide reproducibility and regression checks.
