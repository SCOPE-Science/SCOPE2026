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

# Exact reproducibility

Use Python 3 and SymPy; run `python3 code/verify.py`. The program prints `VERIFY_OK` after constructing all 80 planar labelled binary words and all 160 degree-four relations from the original two defining cubic identities. Its checks include: (i) 79 independent generic relations via a symbolic 79-square determinant \(-2^{41}\delta^9(\delta+1)^3\) and one explicit polynomial nullvector; (ii) 76 independent exceptional relations via a \(-2^{38}\) determinant and four independent integral nullvectors; (iii) rank-two multigrading dimensions \((0,0,1,0,0)\) at \(\delta=2\) and \((0,1,2,1,0)\) at \(\delta=-1\). Nonzero minors plus nullvectors prove the rank identities over all characteristic-zero fields in the specified parameter range, not merely the two sample values. The matrices use a fully specified basis and no external data files.

Independent audit was not performed. This calculation does not establish any fifth or higher-degree dimension, nor any assertion in positive characteristic.
