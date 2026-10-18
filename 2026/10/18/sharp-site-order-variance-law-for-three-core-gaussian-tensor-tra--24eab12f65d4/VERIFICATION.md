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

The proof is algebraic. To reproduce finite checks with Python 3 and NumPy, run `python verify_order.py` in the same directory.

The script checks 30,000 exact rational inequalities/identities for random positive purity triples at \(1\le\chi\le15\). It also generates 140,000 independent three-site Gaussian samples for each of three distinct physical-mode orderings, compares sample variance to the exact formula within an announced 8% tolerance, and prints amplification ratios tending to \(\chi\) as the local dimension increases. The script was run against its actual embedded contents and all assertions passed.

The infinite all-purity and all-bond-dimension results follow from the conditional Gaussian moment identities, exchange identity and positive factorization in `RESULT.md`, not from the finite checks. No independent external audit has been performed.
