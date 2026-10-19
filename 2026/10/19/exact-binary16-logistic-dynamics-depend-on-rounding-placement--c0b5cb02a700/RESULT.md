# Exact binary16 logistic dynamics depend on rounding placement

## Finding

Let \(R\) denote IEEE 754 binary16 round-to-nearest, ties-to-even, with subnormal numbers retained. The two maps
\[
 F(x)=R\bigl(4x(1-x)\bigr),\qquad
 G(x)=R\bigl(4R(xR(1-x))\bigr)
\]
act on the same set \(\mathcal H\) of all nonnegative binary16 numbers in \([0,1]\), with one arithmetic result rounded in \(F\) and separate rounded subtraction and multiplication in \(G\). Despite representing the same real polynomial before rounding, their *entire finite-state dynamics* differ sharply.

There are \(15{,}361\) states. Their exact periodic orbit and basin census is:

| Map | Primitive cycle period | Basin states | Uniform-real-start weight, units of \(2^{-25}\) | Largest entry time |
| --- | ---: | ---: | ---: | ---: |
| \(F\) | 1 (zero) | 15,236 | 33,285,590 | 109 |
| \(F\) | 1 (three quarters) | 8 | 25,258 | 7 |
| \(F\) | 5 | 117 | 243,584 | 14 |
| \(G\) | 1 (zero) | 5,092 | 11,340,767 | 55 |
| \(G\) | 1 (three quarters) | 2 | 22,528 | 1 |
| \(G\) | 40 | 10,267 | 22,191,137 | 83 |

The maps disagree on precisely \(2{,}774\) of their single-step state transitions. Moreover, precisely \(10{,}194\) starting *states* differ in whether their eventual cycle is zero. If \(U\) is uniform on the real interval \([0,1]\), its initial value is rounded once using \(R\), and the resulting orbit is iterated deterministically, then the expected infinite-time Cesàro means exist and are exactly
\[
 \mathbb E\left[\lim_{n\to\infty}\frac1n\sum_{j=0}^{n-1}F^j(R(U))\right]
 =\frac{19241579}{4294967296}=0.00448002922348678\ldots,
\]
\[
 \mathbb E\left[\lim_{n\to\infty}\frac1n\sum_{j=0}^{n-1}G^j(R(U))\right]
 =\frac{11845614952233}{35184372088832}=0.336672626196815\ldots.
\]
The difference is exactly \(11687987937065/35184372088832\), or approximately \(0.332193\).

## Assumptions and scope

For each index \(b\) from \(0\) through hexadecimal `0x3c00`, interpret \(b\) as the *nonnegative* IEEE binary16 bit pattern. Signed negative zero is excluded, as are negative numbers, numbers above one, infinities, and NaNs. This set has exactly \(\mathrm{0x3c01}=15{,}361\) members. The real polynomial is evaluated exactly before its *single* final rounding in \(F\); it is **not** claimed that a particular instruction compiler performs this fusion. In \(G\), the subtraction \(1-x\) rounds first, the product rounds second, and the final factor of four rounds last. The input is exact binary16 at each step; all output values remain in \([0,1]\). Every tie chooses the even final significand. The stated ensemble statistics assume **uniform real initial sampling followed by one binary16 rounding**, not uniform sampling from the discrete representable states and not the real logistic invariant measure.

## Proof

Define \(Q=2^{24}\). The exact value \(h_b\) of the binary16 state indexed by \(b\) can be written \(h_b=q_b/Q\) with an integer \(q_b\). If \(e\) and \(f\) are the exponent and fraction fields, then
\[
 q_b=\begin{cases}f,&e=0,\\(1024+f)2^{e-1},&1\le e\le15.\end{cases}
\]
These \(15{,}361\) integers are strictly increasing from \(q_0=0\) to \(q_{15360}=Q\). To round any nonnegative rational \(p/d\) in units of \(Q^{-1}\), use exact integer comparisons against its two nearest consecutive \(q_b\) values and break midpoint ties by bit-pattern parity. This implements the stipulated IEEE rounding exactly, including across exponent boundaries and subnormal/normal boundaries.

Consequently the index maps are computed with *integers only* by
\[
 \begin{split}
  f(b)&=\mathcal R\bigl(4q_b(Q-q_b)/Q\bigr),\\
  s(b)&=\mathcal R(Q-q_b),\\
  p(b)&=\mathcal R(q_bq_{s(b)}/Q),\\
  g(b)&=\mathcal R(4q_{p(b)}),
 \end{split}
\]
where \(\mathcal R(z)\) returns the bit index of the binary16 number nearest to \(z/Q\), ties-to-even. The supplied `verify.py` constructs *every* directed edge from these formulas with exact integer arithmetic. Its two packed little-endian 16-bit edge-list SHA-256 digests are

- `262e0316d1e5e82c3b1c694ecde3dde9b8c6a8a24956d407f6b6b008c2d116af` for \(F\);
- `300ed95c25d2fe4a9b836b60802d0c6b8af3c9c1c01e0654f895781ea889027c` for \(G\).

A directed graph with one outgoing edge at each vertex decomposes uniquely into disjoint directed cycles with rooted in-trees. The script traces each unprocessed vertex until it enters a known component or revisits a vertex; in the latter case it records the newly closed cycle, then labels every vertex on the prefix path in reverse order. An independent edge-by-edge check verifies equal basin IDs across edges and exactly decreasing entry time off cycles, followed by a full check that each state's advertised number of iterations actually reaches its recorded cycle. Thus no unexamined state, cycle, or branch can remain. These finite exhaustive calculations yield the table, both maximum entry times, and the \(2{,}774\) and \(10{,}194\) comparison counts.

For a Lebesgue-uniform real initial point, initial rounding to state \(b\) selects the interval between adjacent rounding midpoints. Its length is \(w_b/(2Q)\), with
\[
 w_0=q_1-q_0,\quad w_b=q_{b+1}-q_{b-1}\ (0<b<15360),\quad
 w_{15360}=q_{15360}-q_{15359}.
\]
The integer weights sum to \(2Q=2^{25}\). Because every state eventually cycles, its Cesàro mean is the ordinary arithmetic mean of its primitive cycle. Summing the rational cycle means against the **exact** basin weight totals in the table produces both displayed rational ensemble means. Exchanging expectation and the limit is also valid by bounded convergence, since all iterates stay in \([0,1]\). No numerical asymptotic extrapolation is involved.

## Verification

Run `python3 verify.py`. It requires only Python's standard library, computes every transition from integers, proves by exhaustive finite-state logic that every state enters its assigned cycle, and asserts all tabulated counts and rational means. Optionally run `python3 verify.py --native` with NumPy installed: this independently evaluates all \(30{,}722\) individual transitions through native `float16` arithmetic and compares the resulting bit patterns with the exact integer implementation. Both commands were executed successfully; all \(30{,}722\) native comparisons agreed.

## Relationship to prior work

Klöwer, Coveney, Paxton and Palmer's public preprint (2022) studies finite-precision chaotic dynamics, initially emphasizing the generalized Bernoulli map; the expanded 2023 version also studies the logistic map in binary16 and documents spuriously attracting fixed points and short cycles. It motivates finite-precision orbit analysis, but the inspected relevant logistic-map sections do not report the two precisely defined evaluation orders, their **exhaustive** orbit/basin tables, or their exact uniform-real-start means. Galias (2021) systematically classifies logistic-map cycles at **single and double** precision, not these binary16 operations. Persohn and Povinelli (2012) investigate finite-bit logistic pseudorandom number generators; their published abstract does not establish this binary16 expression-order comparison. These sources establish methodology and known qualitative phenomena rather than the exact present comparison.

## Limitations

This is a theorem about the two precisely specified **finite binary16 state maps** and the stated initial ensemble. It does not say which expression a compiler chooses, or make claims for stochastic rounding, fused instruction semantics, other evaluation orders, other precisions, or the true real-valued logistic invariant distribution. Completeness is finite and follows from checking every one of the \(15{,}361\) possible states, not from evidence about real-valued infinitely many trajectories. Bibliographic searches and accessible source inspections do not rule out an uncatalogued implementation-specific census or table; an independent literature and mathematical audit remains outstanding.

## References

1. M. Klöwer, P. V. Coveney, E. A. Paxton, T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, Research Square preprint first posted **8 November 2022**, DOI: `10.21203/rs.3.rs-2223046/v1`; expanded *Scientific Reports* **13**, 11410 (2023), DOI: `10.1038/s41598-023-37004-4`.
2. Z. Galias, *Periodic orbits of the logistic map in single and double precision implementations*, *IEEE Transactions on Circuits and Systems II* **68**, 3471–3475 (2021), DOI: `10.1109/TCSII.2021.3081604`.
3. K. Persohn, R. J. Povinelli, *Analyzing Logistic Map Pseudorandom Number Generators for Periodicity Induced by Finite Precision Floating-Point Representation*, *Chaos, Solitons & Fractals* **45**, 238–245 (2012), DOI: `10.1016/j.chaos.2011.12.006`.
