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

Run `python3 CHECK.py` with a standard Python 3 interpreter. No third-party dependency is required. The checker builds every value of \(J_n(j/50)\), for integer \(1\le n\le11\) and \(0\le j\le2000\), as an exact integer-arithmetic enclosure of its alternating power series. It takes 150 terms, tracks outward integer rounding at scale \(10^{90}\), and encloses the next alternating-series term. The checker then evaluates the entire composite Simpson sum as an integer interval and proves \(S_1>51/500\) and \(S_n<7/100\) for \(2\le n\le11\).

The analytical Simpson error follows from \(|J_n^{(a)}|\le1\) at every integer derivative order, which yields \(|(rJ_n^6)^{(4)}|\le52704\) on \([0,40]\); the error is less than \(1/500\). The exact radial tail is bounded by \(1/100\) through the published Bessel amplitude inequality, using only \(\pi>3\) and integer square comparisons. For all \(n\ge12\), published fifth-power and uniform Landau bounds imply \(I_n(6)<91/(400n^{1/3})<1/10\). The latter is checked as an exact integer cubic inequality, not by enumerating modes. Expect the output `CHECK_OK 15` after the eleven order-specific interval assertions and three analytical-threshold assertions.

The transfer from moment ordering to the optimal mixed-norm stability coefficient and equality cases follows from the explicitly cited theorem of Xu (arXiv:2610.19648v1). The checker does not independently verify Xu's theorem or claim a complete classification for other exponents. No independent mathematical audit has been performed.
