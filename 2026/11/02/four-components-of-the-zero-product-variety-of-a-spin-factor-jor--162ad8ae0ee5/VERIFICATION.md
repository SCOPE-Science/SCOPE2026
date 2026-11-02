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

The proof reconstructs zero Jordan products directly from \(ab+B(u,v)=0\) and \(av+bu=0\). The component assertion is for the reduced geometric zero fiber. The essential nonstandard geometric step identifies the rank-one isotropic component as the affine cone over the Segre image of a smooth projective quadric times a projective line. The finite-field formula follows by exact annihilator-size stratification and the classical quadratic Gauss-sum evaluation.

Run the included `check.py` with standard Python 3. It uses independent finite-field multiplication, including \(\mathbb F_9=\mathbb F_3[z]/(z^2+1)\), and tests all ordered pairs for twelve configurations. Expected terminal marker: `SPIN_FACTOR_ZERO_PRODUCT_OK 12`. The supplied `check_output.txt` is the recorded output. It is a finite cross-check rather than a proof for every form, dimension, or field. The original quadratic ideal is not claimed to be reduced, and no independent audit has been performed.
