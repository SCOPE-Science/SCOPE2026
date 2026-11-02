# Scientific review: two-scale corner-collision distance tails

## Correctness — PASS

The result is restricted to independent uniform-area points in the explicitly normalized convex body \(K_r=[-1,1]^2\cap \overline B(0,r)\), with \(1\le r\le\sqrt2\). The diameter and area formulas follow from elementary antipodal geometry and the four disjoint cut-off circular caps. All near-maximal pairs localize to antipodal circle points for fixed \(r<\sqrt2\), and to four ordered opposite-corner pairs when \(r\to\sqrt2\). Explicit local Jacobians yield the \(5/2\) and \(4\) powers. Both joint limits include their own rescalings and are proved by dominated convergence on bounded domains. The limiting double integral for the curvature-scale law is evaluated exactly in two branches; the corner-scale limit is an elementary four-dimensional simplex integral. The included `CHECK.py` independently evaluates the near-diameter inequality by numerical quadrature and checks the symbolic formulas (25 assertions passed). None of the finite computations is used as an infinite proof.

**Limits:** No error bound uniform in unbounded scaling parameters is proved. Independence of a future external audit is not asserted.

## Originality — PASS with residual historical uncertainty

Searches of published mathematical records and the available earlier findings considered Euclidean two-point distance tails, disk-square intersections, clipped squares, random diameter crossovers, and equivalent covariogram formulations. The closest directly related published comparison treats the maximum distance in a growing sample from an intersecting **two-disk lens**, rather than the distance between just two uniform points in a disk-clipped square. Koshizuka (1978, Section 2; open full text inspected) compares the separate disk and square distributions, and Kumar et al. (2014, Appendix C; indexed public text) tabulates the square distance law. Alagar (1976) treats balls and adjacent squares; Ehlers and Enns (1981) describe covariogram-based random secant laws. Sheng (1985) gives general distance-integral representations for many planar regions. Those general integrals do not furnish the explicit two distinct joint parameter limits without a separate singular asymptotic calculation. No inspected source states the two displayed crossover laws for this family.

**Closest-source limitation:** The complete text of Sheng (1985) was unavailable after open-access/preprint searches and an authorized institutional attempt; only the publisher abstract and bibliographic data were inspected. This leaves a genuine priority risk, but no decisive statement-equivalent or stronger crossover result was found. The conventional disk and square endpoint laws are acknowledged as earlier knowledge.

## Mathematical value — PASS

The collision of a positive-measure family of antipodal circular maximizers with a finite set of square-corner maximizers makes two different local scales mathematically necessary. The exact curvature-scale function has a nontrivial breakpoint, while a second corner-scale limit is a different quadratic polynomial. These facts give a complete local double-scaling picture for a natural one-parameter interpolation between two classical geometric-probability models; neither endpoint distance law determines either crossover. This information is relevant to rare long-distance events and, through standard pair-counting constructions, prospective extreme-distance analysis for samples from degenerating bodies. Such applications are motivation, not established consequences here.

**Scope:** This is a self-contained result for concentric square-disk intersections; general polygonal roundings and sample extreme-value limits remain unproved.

Self-review: passed. Independent audit: not yet performed.
