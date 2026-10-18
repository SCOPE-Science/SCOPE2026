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
# Reproduction and limitations

Execute `python3 artifacts/verify.py` using a standard Python 3 interpreter. The checker uses exact rational pairs for the field \(\mathbb Q(\zeta)\) and row reduction to compute the kernel and row-span closure of Fourier evaluation submatrices.

The checker enumerates all \(\sum_{j=0}^3\binom{27}{j}=3304\) candidate generating row sets of the four-column affine-independent Fourier matrix; its exact output must give zero counts \(\{0,1,2,3,5\}\). It also verifies the planar line-plus-point zero counts \(\{0,1,2,3\}\), parallelogram zero counts \(\{0,1,2,3,5\}\), the partition of the \(126\) four-sets into \(72\) line-containing sets and \(54\) caps, and all fourteen explicit exact coefficient witnesses.

Completeness is justified by the row-rank-closure lemma in RESULT.md. The local finite calculation is exhaustive, not a finite sample used to predict a larger matrix. The higher-dimensional theorem follows algebraically from the \(3^{d-r}\)-fold frequency-coset repetition for affine-span dimension \(r\). A successful program exit does not constitute independent external audit or historical novelty certification.
