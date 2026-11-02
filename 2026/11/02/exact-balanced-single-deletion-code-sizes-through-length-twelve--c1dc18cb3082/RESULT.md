# Exact balanced single-deletion code sizes through length twelve and the first fractional-packing gap

## Finding

Let \(H_m=\{x\in\{0,1\}^{2m}:\operatorname{wt}(x)=m\}\). For \(x\in H_m\), let \(D(x)\) be the **set of distinct** binary length-\(2m-1\) strings obtained by deleting one coordinate from \(x\). A single-deletion-correcting code is a subset \(C\subseteq H_m\) for which \(D(x)\cap D(x')=\varnothing\) whenever \(x\ne x'\). Define \(A_m=\max|C|\), with the maximum taken over all such codes.

**Theorem (exact initial balanced profile).** For every \(1\le m\le6\),

\[
A_m=\operatorname{Cat}_m=\frac{1}{m+1}\binom{2m}{m}.
\]

| \(m\) | Word length \(2m\) | Balanced words \(|H_m|\) | Exact \(A_m\) | Exact certified dual total |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 1 | \(1000001/10^6\) |
| 2 | 4 | 6 | 2 | \(2000002/10^6\) |
| 3 | 6 | 20 | 5 | \(5000005/10^6\) |
| 4 | 8 | 70 | 14 | \(14195149/10^6\) |
| 5 | 10 | 252 | 42 | \(42317279/10^6\) |
| 6 | 12 | 924 | 132 | \(132512205/10^6\) |

Let \(F_m\) denote the optimum of the ordinary *fractional* deletion-shadow packing LP on the same balanced universe. The relaxation is integral for \(m\in\{1,2,3\}\), whereas at \(m=4\) a rational feasible packing has objective \(1419498/100000=14.19498\), hence \(F_4>A_4\). This is the first fractional–integral separation within the balanced even-length layers.

## Assumptions and scope

The alphabet is binary, words have *exactly* length \(2m\) and weight \(m\), positions are indexed, the adversary deletes exactly one symbol at an unknown position, and duplicate deletion outputs from a single word are counted once. The optimum is over arbitrary, possibly nonlinear, subsets of \(H_m\). The fractional relaxation has variables \(z_x\ge0\), constraints \(\sum_{x:y\in D(x)}z_x\le1\) for every length-\(2m-1\) word \(y\) with weight \(m-1\) or \(m\), and maximizes \(\sum_{x\in H_m}z_x\).

## Proof

**Constructive lower bound.** Color \(H_m\) by the modified Varshamov–Tenengolts checksum

\[
s(x)=\sum_{i=1}^{2m} i x_i\pmod{m+1}.
\]

Each color class corrects one deletion: if two distinct balanced words have a common deletion output, they differ by moving a deleted bit across a contiguous block. The checksum difference, up to sign, is the number of opposite bits crossed, which lies in \(\{1,\ldots,m\}\). It is therefore nonzero modulo \(m+1\). The \(\binom{2m}{m}\) words occupy \(m+1\) colors, so some deletion-correcting class contains at least \(\lceil\binom{2m}{m}/(m+1)\rceil=\operatorname{Cat}_m\) words. This argument works for all positive \(m\), though matching upper bounds are claimed here only through six.

**Exact rational upper certificates.** The attached `dual_certificates.json` contains for each \(1\le m\le6\) a finite table of nonnegative integers \(c_m(y)\), with missing keys understood to have weight zero and denominator \(q=10^6\). Both packaged, independently implemented verifiers reconstruct all balanced input words and check the two integer inequalities

\[
\min_{x\in H_m}\sum_{y\in D(x)}c_m(y)\ge q,
\qquad
\sum_y c_m(y)<q(\operatorname{Cat}_m+1).
\]

Since deletion shadows from distinct codewords are disjoint, summing the first inequality over any deletion-correcting \(C\) and applying the second gives \(q|C|\le\sum_y c_m(y)<q(\operatorname{Cat}_m+1)\). The integrality of \(|C|\) forces \(|C|\le\operatorname{Cat}_m\). The table gives the actual rational objective totals, all strictly below the next integer. The lower and upper bounds coincide, proving all six exact values. These are finite integer certificates, rather than a reliance on solver optimality statements or floating-point tolerance.

**First fractional packing gap.** For \(m=4\), `primal_gap_m4.json` provides nonnegative integer numerators \(p(x)\) for a feasible fractional packing \(z_x=p(x)/100000\), with omitted inputs having zero weight. Every one of the binary length-seven output constraints is checked exactly and the objective is \(\sum_xp(x)/100000=1419498/100000>14\). For \(m=1,2,3\), a second, unit-weight dual supported on, respectively, \(1,2,5\) deletion outputs is independently checked to cover every source word, proving \(F_m\le\operatorname{Cat}_m\). Combined with the integral construction, \(F_m=\operatorname{Cat}_m\) for these three cases. Hence the displayed gap first occurs at \(m=4\).

## Verification

Run `python3 verify.py` and `python3 verify_independent.py` in the directory containing the two JSON certificate files. Both programs use only the Python standard library. The first reconstructs binary strings as textual words; the other uses integer bit masks and deletion by bit operations. They check every deletion adjacency for the six layers, every dual coverage inequality, all dual objective totals, and the primal feasibility and strict objective gap at \(m=4\). Their observed terminal markers were `VERIFY_OK` and `INDEPENDENT_VERIFY_OK`. This finite exhaustive check is the certified mathematical upper-bound step for the *six specific finite parameter values*, not evidence of an asserted all-length theorem.

## Relationship to prior work

Cullina–Kulkarni–Kiyavash (2012) gave modified-VT optimal **colorings** of constant-weight deletion graphs, hence a Catalan-size lower bound here. The chromatic-number result does *not* imply that the maximum independent set equals a color-class size; the paper explicitly distinguishes those questions. Kulkarni–Kiyavash (2012) developed hypergraph-matching LP upper bounds for deletion channels including constrained sources, providing the standard bounding framework but not the finite exact central-weight values or the fractional–integral gap certified here. The new mathematical content is the matching exact upper certificate through balanced length twelve, plus the first fractional relaxation failure at balanced length eight. Related finite coding results from indexed records concern other alphabets, constraints, or word lengths, and do not imply these exact central-weight independence numbers. The absence of an indexed match does not independently prove historical novelty.

## Limitations

The exact profile stops at \(m=6\) (length twelve). Neither the Catalan formula for \(m\ge7\) nor an exact value of \(F_4\) is claimed. The objective \(14.19498\) is a certified fractional *lower bound*, not a claim of LP optimality. The finite certificate does not enumerate all optimal codebooks. An older unindexed constant-weight code table might contain some exact values; independent historical-priority review has not occurred.

## References

1. D. Cullina, A. A. Kulkarni, N. Kiyavash, *A Coloring Approach to Constructing Deletion Correcting Codes from Constant Weight Subgraphs*, IEEE ISIT (2012), DOI: 10.1109/ISIT.2012.6284242, https://doi.org/10.1109/ISIT.2012.6284242.
2. D. Cullina, A. A. Kulkarni, N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056 (first posted 2012-11-16), https://arxiv.org/abs/1211.4056.
3. A. A. Kulkarni, N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128 (first posted 2012-11-13), https://arxiv.org/abs/1211.3128.
