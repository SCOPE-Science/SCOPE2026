# Review: characteristic-two elementary symmetric cubic

## Correctness

PASS. The geometric point classification follows from an exact common quadratic for coordinate values and a two-block parity analysis. Local scheme equations, not point enumeration alone, show that each point has local algebra \(k\) for odd \(n\) and \(k[\epsilon]/(\epsilon^2)\) for \(4\mid n\). The polar Hessian and nonvanishing of its radical quadratic value establish smooth projective quadratic tangent cones in the latter case. The roots-of-unity filter and independent finite checks agree. See RESULT.md and verify.py.

## Originality

PASS, with stated literature risk. Xie, arXiv:2610.00259v1, determines dimension and extremal components and generic multiplicity at coordinate components, but says smaller-dimensional components are not classified. Orzel, arXiv:2509.05009v3, supplies dimension bounds. Cafure–Matera–Privitelli, arXiv:1109.2265v1, provide partition-space bounds. The present all-dimensional node set and doubled Jacobian local structure for the smaller-dimensional cubic case are neither those statements nor formal consequences of their dimension bounds. An unindexed equivalent classification remains a residual risk.

## Mathematical value

PASS. The complete small-degree classification is motivated by a specific gap in the positive-characteristic derivative-locus literature. It yields an exponential exact node count and distinguishes geometric ordinary quadratic double points from nonreduced Jacobian schemes in characteristic two; this is a structural and enumerative invariant, not a one-off table entry.

## Limitations

Algebraically closed characteristic-two base; elementary symmetric cubic; \(n\ge3\) and \(n\not\equiv2\pmod4\). No claim of independent verification or global literature exhaustiveness. Finite checks are supplementary.

Self-review: passed. Independent audit: not yet performed.
