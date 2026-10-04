# Same-model review

## Correctness
**PASS.** The proof reduces the random \(b\)-symbol distance to a sum of clean-window indicators. The pairwise union size is counted exactly on the cycle, including the two-overlap regime when \(2b>n\). Independence of coordinate errors then gives every covariance term. Direct exhaustive reconstruction with rational probabilities agrees with both the first and second moments for all tested small parameters, and a larger parameter grid confirms the simplified \(n\ge2b\) expression.

## Originality
**PASS, with recorded residual risk.** Searches covered stochastic \(b\)-symbol distance, random \(b\)-weight, Bernoulli cyclic-window coverage, moment/variance language, and pair-symbol aliases. The closest published-finding corpus record concerns optimal cyclic symbol-pair codes rather than stochastic moments. The open Ding--Zhang--Ge full text defines the metric but studies MDS code bounds and constructions. Vega's open full text studies \(b\)-weight distributions inside structured cyclic codes. Song--Fujiwara is the closest sphere-bound paper; its abstract and metadata were inspected, but its full text was unavailable through the lawful routes used here, leaving a specific residual risk of an unstated intermediate overlap.

## Value
**PASS.** Under independent substitutions, overlapping \(b\)-symbol reads are correlated even though coordinate errors are independent. The exact variance quantifies that dependence for every block length, read width, and substitution probability, and the stable \(n\ge2b\) formula gives the exact root-\(n\) fluctuation coefficient. This is a natural stochastic channel invariant rather than a chosen finite parameter cell.

## Closest literature and limitations
The closest inspected literature defines the same metric and studies deterministic code bounds or structured codeword weight distributions. The theorem here concerns a different probability law: arbitrary words subjected to iid substitution locations. It does not cover dependent errors or the full probability generating function. The inaccessible full text of the 2018 sphere-bound paper is retained as an originality risk rather than being declared non-covering.

Same-model review: passed. Independent audit: not yet performed.
