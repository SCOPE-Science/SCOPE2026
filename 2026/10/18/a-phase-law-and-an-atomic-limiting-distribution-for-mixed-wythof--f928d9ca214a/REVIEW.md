# Review: mixed Wythoff phase law and limiting distribution

## Correctness — PASS

The representation count is exactly a convolution of the complementary Beatty indicator words. For each fixed integer, the indicator product is the interval indicator of a single explicitly identified phase-dependent arc; the three lengths yield the claimed function. Fibonacci-denominator rational approximations establish a uniformly bounded interval-count error on each convergent-denominator block, and Zeckendorf decomposition uses only logarithmically many blocks. This proves the claimed uniform error for every integer, independent of the varying interval. Irrational rotation equidistribution then establishes weak convergence and its atom and mean. The proof also handles endpoint conventions and the positive-index domain. The `verify.py` artifact independently enumerates literal representation pairs and exact integer-indicator convolutions over finite ranges.

## Originality — PASS, with stated uncertainty

Ashburn's 2026-10-04 full manuscript (arXiv:2610.04842v1, Theorem 1) treats exactly the same count but characterizes only multiplicities zero, one and two; it does not determine the normalized limiting law. Shallit's 2020 full manuscript (arXiv:2006.04177, Section 11.2) already gives an exact rank-19 automata/linear-representation method for **all** multiplicities. That is important coverage of pointwise computability, not an explicit logarithmic-error rotation phase formula or an identified atom in an empirical measure. OEIS A259598 records the generating-function convolution but not the asserted limiting law. The accessible abstracts of related 2021 and 2022 sumset papers emphasize support and additive-basis questions. Searches for Wythoff representation-count distributions and general Beatty convolution asymptotics, together with mathematical-result similarity searches, found no covering distribution theorem. The 2021 article and the 2022 Phunphayap–Pongsriiam–Shallit article were not read in full, so an implicit precursor cannot be excluded. Exact source-inspection coverage and scientific comparisons are in `AUDIT.json`.

## Mathematical value — PASS

The problem arises from a natural named representation function whose low multiplicities were resolved in recent research. Rather than recomputing known sequence values, the theorem supplies the full macroscopic behavior for every input up to a provable uniform error, and a nondegenerate limiting distribution with a **positive atomic component** at the maximal normalized multiplicity. The theorem both explains the coexistence of sparse exceptional small counts and typical linear-sized counts and determines a natural limiting arithmetic invariant; the explicit law is not supplied by the known exact enumeration algorithm without additional analysis.

## Boundaries and risks

No optimality assertion is made for the logarithmic discrepancy. Finite verification cannot certify the infinite limiting law, which instead has a complete analytic proof. The historical pointwise exact algorithm is credited rather than relabeled as new. Accessible summaries of some older primary papers do not establish their complete contents, and hidden equivalent formulations remain possible. No independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
