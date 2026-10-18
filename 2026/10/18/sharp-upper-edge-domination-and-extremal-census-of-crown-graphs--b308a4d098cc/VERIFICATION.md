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
# Reproducible verification

Run `python verify.py` from this directory, using Python 3 and no third-party modules. The independent enumerator checks each subset of the \(n(n-1)\) crown graph edges at orders \(3,4,5\), constructs its dominated-edge mask from direct endpoint incidence, and tests deletion-minimality. It examines \(64+4096+1048576=1052736\) subsets. At \(n=5\) it verifies that **exactly 45** minimal-size configurations of size 4 are the predicted deranged matchings and **exactly 20** maximal-size configurations of size 6 are the predicted two-star forests. It checks the minimum derangement family already at \(n=3,4\), without claiming the upper census for those smaller orders. It also verifies all explicit two-star constructions for orders \(5\) through \(25\). The captured standard output is `verify_output.txt`.

The exhaustive finite tests do not prove the unrestricted statement. The infinite minimum and maximum theorems are justified separately by the self-contained support-pattern and star-forest proof. Bibliographic priority is not externally certified, and no independent audit is asserted.
