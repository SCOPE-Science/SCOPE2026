# Exact binary16 logistic dynamics depend on rounding placement

## Finding: a coupled real-start comparison

Let \(R\) be IEEE 754 binary16 nearest-even rounding with subnormals retained. Compare the maps
\[
F(x)=R(4x(1-x)),\qquad G(x)=R(4R(xR(1-x)))
\]
on the 15,361 nonnegative binary16 encodings from `0x0000` to `0x3c00`. Use **one** uniform real sample \(U\) on \([0,1]\), round it once, and start *both* deterministic orbits at \(R(U)\). The following table gives the complete joint law of their eventual cycles; entries are in units of \(2^{-25}\).

| Eventual cycle under \(F\) | \(G\): zero | \(G\): \(3/4\) | \(G\): period 40 |
| :--- | ---: | ---: | ---: |
| Zero | 11,335,435 | 0 | 21,950,155 |
| \(3/4\) | 2,730 | 22,528 | 0 |
| Period 5 | 2,602 | 0 | 240,982 |

Thus switching from \(F\) to \(G\) sends exactly \(21{,}950{,}155/2^{25}\) of real starts (about 65.4%) from eventual zero to a nonzero cycle. The reverse change, from a nonzero \(F\) cycle to zero under \(G\), occurs on only \(5{,}332/2^{25}\) of starts (about 0.0159%). Neither a comparison of cycle periods nor the two marginal basin probabilities identifies these directional events under a common start.

The infinite-time Cesàro means of the two orbits exist for every rounded start. Their expectations for the stated real ensemble are
\[
\mathbb E[C_F]=\frac{19241579}{4294967296},\qquad
\mathbb E[C_G]=\frac{11845614952233}{35184372088832}.
\]
The increase is \(11687987937065/35184372088832\), about 0.332193. This is not the mean under uniformly chosen bit encodings.

## Model and exact finite proof

Exclude negative zero, negative values and values above one, infinities and NaNs. Every input and stored result is a nonnegative binary16 encoding. In \(F\) the polynomial is evaluated exactly up to its final rounding. In \(G\) subtraction, product and multiplication by four round at exactly the locations displayed. No compiler or instruction semantics are inferred.

Put \(Q=2^{24}\). The value at encoding \(j\) is \(q_j/Q\); for exponent field \(e\) and fraction field \(f\), \(q_j=f\) if \(e=0\) and \(q_j=(1024+f)2^{e-1}\) otherwise. The \(q_j\) increase from 0 to \(Q\). To round a value \(p/(dQ)\), find consecutive encodings bracketing \(p/d\) and compare the exact integer distances from \(p\) to their \(d q_j\). On a tie choose even encoding parity, which is even low significand bit, including at format boundaries. With \(\mathcal R(p,d)\) denoting the resulting index, the two successors are
\[
f(j)=\mathcal R(4q_j(Q-q_j),Q),\qquad
g(j)=\mathcal R(4q_{\mathcal R(q_j q_{\mathcal R(Q-q_j,1)},Q)},1).
\]
The certificate checks that the arguments to this interval rounder are in range for every call. Starting at each unlabelled code, follow successors until reaching a labelled code or encountering an earlier code of the current path. In the second case the repeated suffix is a new primitive cycle. Give every code on the path the resulting cycle label. This algorithm processes all encodings, including fixed points and their basin states. Each map has a zero fixed point, a \(3/4\) fixed point and exactly one nonfixed cycle, whose period is 5 or 40, respectively.

The initial rounding cell of code \(j\) has length \(w_j/(2Q)\), where \(w_j=q_{j+1}-q_{j-1}\) in the interior; clamp a missing neighbor to the endpoint code. These lengths are consecutive midpoint intervals truncated at 0 and 1. The tie convention changes only endpoints of measure zero. The integer weights sum to \(2Q\). To compute the displayed table, add \(w_j\) to the entry indexed by the pair of labels of code \(j\), not by labels from two independent starts. This is an exhaustive sum over both graphs on the common grid. The row sums are \((33285590,25258,243584)\), and column sums are \((11340767,22528,22191137)\). Periodic tails give each code the arithmetic mean of its labelled cycle. In the table's row order the cycle means under \(F\) are \((0,3/4,8837/16384)\); in column order those under \(G\) are \((0,3/4,533001/1048576)\). Dotting each set of cycle means with the respective marginal, normalized by \(2Q\), gives the two fractions above.

## Comparisons and limitations

[*Exact complete expanded-evaluation binary16 logistic cycle census*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-three-incompatible-complete-cycle-spectra-for-half-precision-log--46d23de07c7c), in “Prior coverage and value,” credits the same once-rounded and staged-factored cycle periods, encoding basin counts and edge digests to [*Rounding placement changes the complete binary16 logistic attractor census*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-rounding-placement-changes-the-complete-binary16-logistic-attrac--ec3a649c6929). We use those finite graphs as comparison baselines, not as claims of a new cycle census. The referenced record itself was not available for a direct comparison of initial ensembles. The independently stated comparison numbers are for the counting law on encodings. They do not determine the midpoint-weighted joint law of the two basins: the pair of labels for each shared initial code is required. [*Two exact binary16 logistic cycle spectra under algebraically equivalent evaluation*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-two-exact-binary16-logistic-cycle-spectra-under-algebraically-eq--35a3ca4a276d) shares the once-rounded baseline but compares it to an eight-cycle completed-square map, not \(G\). Klöwer et al. ([DOI 10.1038/s41598-023-37004-4](https://doi.org/10.1038/s41598-023-37004-4), logistic section and Methods) study low-precision periodic orbits, including binary16, but the inspected passages do not give the two-map coupling or real-start means stated here.

This is an exact comparison of two finite maps and one initialization law. It is not a claim about compiler optimizations, stochastic rounding, other evaluation trees, or the real logistic invariant measure. The comparisons do not exclude an unindexed calculation or the possibility that an unavailable graph reference also reports a real-start quantity.

The bfloat16 comparison [*Exact bfloat16 logistic basin inversion under a single intermediate rounding*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-bfloat16-logistic-basin-inversion-under-a-single-intermedi--305f9651a5de) likewise cross-classifies basins on a common grid, under uniform counting of bfloat16 encodings. It uses a different floating-point format and rounds the complement but not the inner product of its staged map. Its dominant migration goes toward zero, not away from it. It is a counterpart, not a calculation of the real-start binary16 weights above.

## Replay

`python3 verify_ensemble.py` reconstructs the joint table and asserts the cycle means and marginal-derived expectations. Binary16 rounding comparisons, weight additions and cycle sums use exact integers, and the expectations use exact fractions from the Python standard library. The companion `verify.py` addresses the baseline graph census and the marginal ensemble means, not the new joint table.
