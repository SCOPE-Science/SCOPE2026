# Scientific review: sharp dyadic transition in fifth-column Stirling differences

## Correctness — PASS
The exact inclusion-exclusion identity for \(5!S(m,5)\) leads to four integer summands with valuations \(n+q+2\), \(n+q+3\), \(2^n+1\), and \(2^{n+1}\). The unique-minimum rule gives both off-boundary cases. At the sole tie, a normalized congruence modulo four proves that exactly one additional power of two divides the sum. Dividing by \(5!=120\), whose dyadic valuation is three, gives all three cases. The proof quantifies all \(n\ge3\) and \(q\ge0\), including arbitrarily large shifts, without induction from numerical data. The bundled verifier independently checks 119 modular cases and six direct Stirling-recurrence cases.

## Originality — PASS, with residual risk
Theorem 1.3 of Zhao–Hong–Zhao (arXiv:1209.6284; published 2014, DOI 10.1016/j.jnt.2014.01.005) prints the uniform expression \(n+\nu_2(a-b)-\lceil\log_2k\rceil+s_2(k)+\delta(k)\). For \(k=5\), \(a=1+2^q\), \(b=1\), it predicts \(n+q-1\); the exact theorem verifies this only in a bounded range of \(q\), and gives explicit contrary values beyond the range. Their later arXiv:1407.8443 presents different statements, including asymptotic settings; it does not by itself imply the complete three-case uniform transition described here. Searches of published research-index summaries and accessible own-archive claims found no equivalent \(k=5\) formula. A related prior archival finding concerned \(k=15\), not this column. The literature comparison is not an exhaustive proof of priority, and unlocated corrections, errata or equivalent formulas remain risks. The result makes no claim against fixed-parameter eventual formulas.

## Mathematical value — PASS
The natural question is exactly how the fifth-column Stirling-difference valuation depends jointly on the dyadic base and dyadic shift. A single phase transition, a one-unit resonance spike, and a high-shift plateau supply a complete uniform answer rather than a numerical exception. The qualitative transition explains a real obstruction to extending a published formula uniformly in all parameters and identifies the precise sharp boundary. The argument is brief but a meaningful resolution of a quantifier-sensitive valuation problem.

## Closest sources and limitations
The closest primary source is Zhao–Hong–Zhao, arXiv:1209.6284, Theorem 1.3; the closest follow-up is arXiv:1407.8443. Classical Stirling inclusion-exclusion, elementary lifting-the-exponent, and work of Lengyel motivate the question. The present proof does not address general \(k\), and the literature risks above remain. The displayed computations corroborate rather than certify the infinite theorem.

Self-review: passed. Independent audit: not yet performed.
