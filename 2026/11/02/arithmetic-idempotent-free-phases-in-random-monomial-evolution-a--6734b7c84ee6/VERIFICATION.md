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

# Reproduction and verification

Execute `python3 verify.py` using Python 3 and its standard library; the verifier ends with `VERIFY_OK` when every assertion passes. The exact direct enumeration constructs all \(n!(q-1)^n\) labeled weighted-permutation structure matrices for each tested field and dimension, including binary extension fields of sizes \(4\) and \(8\), and checks each vector's original multiplication equation \(x^2=x\). It separately calculates the expected zero-idempotent probability and the first two moments from the cycle-index coefficient recurrence, and tests equality as exact rational numbers.

Exhaustive instances are \(q\in\{2,3,4,5,7,8\}\), \(n\in\{1,2,3\}\), together with \(q\in\{2,3,4\}\), \(n=4\). Additional exact recurrence/support comparisons extend through \(n=22\) for \(q\in\{4,7,8,11\}\). Sample checks include \(\Pr(N=0)=1/3\) at \((q,n)=(4,2)\), \(2/7\) at \((8,3)\), and \(2/9\) at \((4,4)\); the respective exact variances are \(2\), \(6\), and \(21\).

The checker uses exhaustive computation only for the listed finite cases; it does not certify all dimensions or the limiting singularity estimate. The supplied symbolic derivations provide the infinite argument. The periodic generating-function singularity argument has been independently re-expanded algebraically, but no separate external validation is claimed. The exact idempotent counts of individual permutation cycles are previously available in the literature and are not presented as newly discovered facts.
