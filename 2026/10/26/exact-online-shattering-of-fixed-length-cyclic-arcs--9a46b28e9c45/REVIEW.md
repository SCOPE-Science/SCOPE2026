# Scientific review: exact online shattering of fixed-length cyclic arcs

## Correctness
PASS. The complement reduction fixes \(s=\min(k,n-k)\); every query has exactly \(s\) positive hypotheses, giving the sharp upper bound on a full binary mistake tree. Two disjoint center blocks of size \(2^{\lfloor\log_2s\rfloor}\) exist on either side of the first query, and subsequent cyclic queries realize all prefix cuts on each block. This supplies every branch of the required tree without probabilistic or computational inference. The VC bound uses the impossibility of including the two outside members of a triple without the middle member in arcs of size at most a half-cycle. Independent brute-force implementations of the finite recurrence, direct VC traces, and explicit leaf checking passed; their finite scope is stated.

## Originality
PASS under best-knowledge priority assessment, with residual risk. Published treatments of the Littlestone/stability interface (Malliaris–Moran 2021 and 2022) do not provide this exact parameter formula. Chase–Freitag–Reyzin 2023 study general query learning and use disjoint intervals in one example; that one-dimensional result does not imply the logarithmic cyclic-window calculation. Exact record-overlap checks identify a previous classification restricted to four-point translates (which covers the \(s=4\) special case only), and a recurrence for *all* intervals on a finite chain (a different hypothesis class). Neither gives the displayed all-length formula or its VC/Littlestone comparison. Direct searches for the same formula under cyclic-arc, sliding-window, circular-threshold, and stable-rank terminology did not establish stronger prior coverage. Index and priority incompleteness remains possible.

## Mathematical value
PASS. The exact classification covers every \(n,k\), including small and complementary cases, and determines the optimal deterministic realizable mistake bound for a canonical family of translated geometric ranges. Its sharpness proof is constructive and identifies when the class attains the information-theoretic maximum \(\lfloor\log_2n\rfloor\). At the same time, VC dimension never exceeds two. Thus a geometrically elementary family exhibits an unbounded quantitative gap between static and adaptive shattering, with the arc's shorter length—not the number of hypotheses alone—setting the exact adaptive complexity. No broader paper-sized consequence is claimed.

## Sources and remaining limits
See the source-to-claim comparisons, source material inspected and residual literature risks in `AUDIT.json`. Proof checks cover all integer parameters; finite scripts provide additional consistency evidence, not independent verification of infinite claims. The result does not treat randomized regret or general circular ranges.

Self-review: passed. Independent audit: not yet performed.
