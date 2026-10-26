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

# Mathematical verification and reproducibility

The analytical proof solves the incidence-graph Laplacian in a mean-zero point gauge and uses exact sign decisions for all edge currents. The identity \(AA^\top=(r-\lambda)I+\lambda J\) follows from two-design balance; third-order balance supplies \(\lambda-\tau\) occurrences of each ordered point pair in blocks excluding a distinguished point. The resulting column sums are exact for every permissible simple three-design, not just those realized in examples.

Run `python3 verification_checker.py` from this package. The checker depends only on the Python 3 standard library. It constructs three complete block designs and two binary affine Steiner quadruple systems, enumerates triple-incidence counts, and checks every current column's point/block divergences and exact \(\ell_1\) norms. In the complete \((6,4)\) and affine \(3\)-\((8,4,1)\) examples, an independent exact grounded-Laplacian inverse reconstructs all incidence columns.

Verified examples: complete \((6,4)\): \(\|Q\|=31/12\), \(\|P\|=35/12\) (60 columns); complete \((7,4)\): \(14/5\), \(45/14\) (140); complete \((8,4)\): \(59/20\), \(17/5\) (280); affine \(3\)-\((8,4,1)\): \(11/4\), \(3\) (56); affine \(3\)-\((16,4,1)\): \(191/56\), \(27/7\) (560). Total: 1,096 exact columns and 116 independent grounded-system columns.

Successful checker terminator: `DESIGN_HODGE_CERTIFICATE_OK columns=1096 grounded_columns=116`.

Checks do not exhaust all designs, all dimensions, or arbitrary real edge weights; infinite quantifiers and the absence of symmetry assumptions rely on the written proof. Independent mathematical audit has not been performed.
