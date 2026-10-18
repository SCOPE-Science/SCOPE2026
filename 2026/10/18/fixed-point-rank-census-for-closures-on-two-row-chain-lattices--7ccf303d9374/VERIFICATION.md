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

# Reproducibility and verification

Run `python3 verify.py` with Python 3 standard library. The program explicitly generates the product order on \(C_2\times C_n\), enumerates every subset containing the greatest element, tests pairwise meets, and compares the histogram of the number of fixed elements with the coefficient array of \((1+t+t^2)^n-(1+t)^{n-1}\) for each \(1\le n\le8\). It independently enumerates *all* extensive endofunctions from their available image sets and tests the original monotonicity and idempotence axioms through \(n=5\), matching the subset results without presupposing the closure-system representation. For each meet-closed set through \(n=4\), it reconstructs the operator from intersections of upper fixed points and rechecks each axiom.

The run yields total counts \(2,7,23,73,227,697,2123,6433\) for \(n=1\) through \(n=8\), and prints `VERIFY_OK`. All arithmetic is exact integer arithmetic. The code does not verify the literature claims, the general infinite-family proof, the asymptotic central limit theorem, or the published characteristic-map correspondence; those are respectively supported by the written mathematics and identified primary sources. No timeout or partial enumeration is treated as a mathematical obstruction. Independent audit has not been performed.
