# Self-review

## Correctness — PASS

The claim was reconstructed using nonempty approval ballots, ordinary (not excludable) strategic reporting, an unrestricted simplex allocation and all Nash maximizing tie resolutions. Exact KKT certificates establish global optimality for each of the 329 anonymous profiles with 1–4 voters and three labeled projects. An optimum-face vertex enumeration bounds every deviator's **true** utility for every optimal tie-break. The code returns 0, 0, 0, and 6 manipulable anonymous profiles, with 12 profitable report pairs and gain set \(\{5/4,(9-\sqrt{17})/4\}\). The all-electorate two-project immunity follows analytically from singleton-voter counts. The verified enumeration is not extrapolated beyond four voters.

## Originality — PASS (qualified historical priority)

Aziz–Lederer–Vollen (2026, arXiv:2605.11736) prove an unrestricted factor-two Nash incentive bound; it does not establish the exact first four-voter three-project frontier or \(5/4\) extremum. Aziz–Bogomolnaia–Moulin (2017, arXiv:1712.02542), including the appendix, construct far larger excludable-strategyproofness violations, a different notion. The related Brandl et al. (2020, arXiv:2005.07997) funding mechanism concerns contributions and participation. Actual searches for fixed numbers of projects, minimal electorate and gain ratios identified no implication-equivalent earlier claim. No independent historical-priority certification has occurred; full historical coverage is not claimed.

## Mathematical value — PASS

The result resolves a natural small-market question left open by a global asymptotic manipulability factor: *when* does strategic vulnerability first appear, *how many* small profiles exhibit it, does Nash tie-breaking matter, and what is the exact incentive? The two orbit structures, sharp 5/4 gain and universal two-project immunity are substantively informative for small approval-budget systems. They are not asserted to provide new general efficiency or fairness guarantees.

## Limitations and evidence

The proof applies only to unweighted binary approvals; the 1–4 voter finite census requires exactly three projects, and the two-project immunity holds for any voter count. All positive report gains persist across Nash-optimal ties. The checker requires Python 3.11+ and the pinned SymPy dependency. The mathematical claim is supported by the supplied exact code and analytic KKT argument, not by numerical solver logs. The background funding-project literature was only partly read and constitutes a limited historical-priority risk; no decisive stronger covering result was identified.

Self-review: passed. Independent audit: not yet performed.
