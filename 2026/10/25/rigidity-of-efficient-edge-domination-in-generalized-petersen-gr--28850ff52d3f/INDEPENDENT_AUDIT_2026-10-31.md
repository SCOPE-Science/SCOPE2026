# Independent mathematical audit

## correctness

PASS

The black/white characterization of an induced dominating matching requires every covered vertex to have exactly one covered neighbor, and every uncovered vertex to have no uncovered neighbor. Outer white gaps must be 2 or 3 because adjacent whites and three consecutive blacks are forbidden. At each outer white u_i, the black inner spoke endpoint v_i has exactly one of v_{i-2},v_{i+2} black; the neighboring outer-gap lengths force those two states to correspond to gap length 2. Thus successive 2/3 gaps alternate, giving n divisible by 5. The outer black/white pattern fixes all inner states; all five shifts of the explicit period-five pattern satisfy the complete vertex constraints. The five shift matchings partition all 3n edges. For a cubic graph an edge dominates itself and four incident edges, hence a maximal matching needs >=|E|/5=3n/5 edges. Equality makes these closed edge neighborhoods disjoint and yields a DIM; similarly five strong colors force each color class to be a DIM. Independent exact-cover reconstruction for every n=5..15 found five solutions exactly at multiples of five, including edge partition. Finite checks corroborate but do not prove all n.

## originality

PASS

The periodic construction and its size were previously known (2024 Observation 7); reported strong chromatic index values for GP(n,k), k=1..3, were also known from Yang--Wu 2018. Neither the accessible inspected prior statements nor other close published indexed records established that these are the only five DIMs, all minimum maximal matchings, and the unique strong five-edge-coloring. Best-of-knowledge PASS concerns those complete equality classifications, not existence/index numbers. The 2018 full article was not obtained, and its possible uniqueness statement is a substantive residual priority risk.

## value

PASS

A complete characterization of efficient edge domination in the natural generalized Petersen family, plus a classification of all saturation minimizers and strong-coloring rigidity, is an independent graph-structural result. It determines the equality structures, rather than merely rechecking known numerical parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
