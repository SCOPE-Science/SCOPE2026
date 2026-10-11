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

The included `scripts/verify.py` is standalone Python 3 using only the standard library and exact `fractions.Fraction` arithmetic for graph-cut squared distances. Execute `python3 scripts/verify.py` from the extracted artifact directory. It enumerates all nonempty proper vertex subsets for graph dimensions \(d=1,2,3,4\), comparing each normalized squared cut distance against the proved value and checking exactly the contact subsets described in the theorem.

The script additionally checks the full Walsh character orthogonality tables and low-dimensional tangency annihilation, and samples deterministically generated cuts in \(d=5,6\). Expected terminal line:

`VERIFY_OK graphical-hypercube-inball d1-4_exhaustive=yes d5-6_sampled=yes universal_analytic_proof=required`

The analytic proof includes the uniform edge-isoperimetric bound, its equality rigidity at powers of two, the strict endpoint minimum, a cut-decomposition criterion for all possible ball centers, and the Walsh contact-normal rank. The exhaustive finite checks are not an infinite certificate; the sampled higher-dimensional checks are explicitly nonexhaustive. All statements use the standard intrinsic Euclidean metric, not an arbitrary embedding or a weighted edge metric.
