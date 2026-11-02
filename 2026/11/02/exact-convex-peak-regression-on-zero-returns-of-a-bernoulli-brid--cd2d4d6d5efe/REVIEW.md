# Review of the peak–return regression

## Correctness — PASS

The argument is exact for every integer \(n\ge2\): exchangeability gives internal expected peaks in each uniform bridge; independence under prescribed return pins gives a \(1/4\) contribution per boundary; a subset expansion gives the generating-function derivative; first-return excursions give the Catalan coefficient formula; algebra yields the conditional regression. Its derivative on the full conditioning interval proves monotonicity and strict convexity, and the central-binomial convolution proves covariance and asymptotics. The packaged checker, run from its actual file, passed 3,707 exact assertions across 66,196 enumerated bridges and the larger algebraic test range. Finite checks do not establish the unbounded theorem; the written derivation does.

## Originality — PASS, subject to priority uncertainty

The directly inspected primary sources establish separate marginal peak statistics (Labarbe–Marckert 2006), return-count and excursion-renewal statistics (Godrèche 2016), and Dyck/bilateral peak bijections (Mortimer–Prellberg 2012). Their displayed statements do not imply the location-independent all-subset pinning identity for *signed* bridges or the exact convex regression conditioned on the *total interior zero-return count* without an additional joint-parameter argument. Specific published-finding corpus statement searches found no direct match; absence of matches is not a uniqueness proof. The 1986 Kreweras multi-parameter bridges chapter was identifiable but its full text was inaccessible; because its bridge terminology refers to nonnegative paths and available descriptions emphasize other joint parameters, it is not treated as proven coverage, but it remains an explicit priority risk.

## Mathematical value — PASS

The zero-return count records local time at a distinguished state; peaks record short-scale path oscillation. They are natural coupled observables of a tied-down walk. The result yields a full, all-size conditional-mean classification, unexpected strict convexity, and a time-location-independent simultaneous-pinning identity. It also quantifies a positive \(\sqrt n\)-order covariance arising despite an \(O(1)\) shift of the typical conditional peak expectation. This is structural dependence information not supplied by either separate marginal enumeration. No claim of a new central limit theorem or full joint-distribution classification is made.

## Scope and literature risks

No strong prior implication was found among the inspected statements. Historical priority requires further specialist review, especially Kreweras (1986), Csáki (1994), and older joint lattice-path enumerations. The nonnegative-Dyck contact refinements in Mortimer–Prellberg are related but do not directly include the signed-return pinning theorem. The current argument neither proves stochastic dominance of conditional peak counts nor treats biased bridges.

Self-review: passed. Independent audit: not yet performed.
