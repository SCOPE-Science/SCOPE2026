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

# Verification and limits

Running `python verify.py` produces:

`VERIFY_OK: exact field gap histograms at 9 Fibonacci orders, 6 joint-word partitions, entropy limit -0.586755256450162`

The program uses integer-pair arithmetic for elements of \(\mathbb Q(\sqrt5)\), exact sign comparisons and sorting of fractional rotation endpoints. It directly constructs the two disjoint index windows and their cyclic gap sizes for orders \(6\le k\le14\), then checks the predicted exact multiplicities. It independently creates finite Sturmian observations at interior sample points of every refined circle arc and verifies the number of distinct ordered word pairs for orders \(6\le k\le11\). Finally it evaluates the finite entropy table and the asymptotic constant numerically.

The proof in `RESULT.md`, not the finite computations, establishes the formulas for every integer \(k\ge6\). Numerical checks of joint word labels use interior floating-point samples for these finite orders; the exact neighbor/gap comparisons do not use tolerance-based ordering or decisions. The completeness argument for symbolic cylinders is analytic. No independent scientific audit has been performed. Historical priority, especially against inaccessible earlier three-distance sources, has not been certified.
