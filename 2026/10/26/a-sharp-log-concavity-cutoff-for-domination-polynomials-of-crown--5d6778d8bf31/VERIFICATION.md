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

# Reproducibility and boundaries

Run `python3 verify.py` from the package directory. It needs only the Python 3 standard library.

The program makes two independent computations of the domination enumerators: direct enumeration of every subset of the labelled crown graphs for \(2\le n\le7\), and evaluation of the derived convolution formulas. These are compared coefficient by coefficient for the ordinary and total domination polynomials. There are exactly 21,840 exhaustively enumerated labelled subsets across these orders.

The program then computes every nontrivial adjacent-coefficient minor for the complete bounded range \(2\le n\le12\). The closed-form coefficient identity in `RESULT.md` reduces this to finite exact integer arithmetic and supplies an independently inspectable certificate table. It also tests the algebraic obstruction \(d_3^2-d_2d_4=-n^2(n-1)(n^2-13n+8)/4\) for \(13\le n\le60\), and the claimed strict modes, middle coefficients and high-degree binomial tails for \(4\le n\le60\).

Expected output begins `VERIFY_OK direct_subsets=21840 brute_orders=6 finite_logconcave_orders=11 failure_orders=48 strict_modes=57` and prints boundary values for \(n=4,12,13\). The finite tests by themselves do not prove any infinite assertion: the case classification, polynomial identity, algebraic sign computation, convolution lemma and combinatorial mode proof in `RESULT.md` provide those infinite arguments.

Scientific limitations: independence of the mathematical assessment has not been established; related pre-2026 domination-root work remains a historical-priority risk. No external audit has been performed.
