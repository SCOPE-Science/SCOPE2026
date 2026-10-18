# Joint cyclic discrepancy and linear-complexity spectrum of binary order-five de Bruijn cycles

## Finding

Consider binary cyclic de Bruijn sequences of order five, counted modulo cyclic rotation only (not modulo complement or reversal). For a cycle \(w=(w_0,\ldots,w_{31})\), define its cyclic discrepancy by
\[
D(w)=\max_{0\le i<32,\ 1\le h\le32}\left|\sum_{j=0}^{h-1}(2w_{(i+j)\bmod32}-1)\right|,
\]
and its binary linear complexity \(L(w)\) as the least length of a linear feedback recurrence over \(\mathbb F_2\) generating the infinite periodic sequence \(w^\omega\). The exact joint spectrum \(N_{\ell,d}=\#\{w:L(w)=\ell,\ D(w)=d\}\) is:

| Linear complexity | Discrepancy 5 | Discrepancy 6 | Discrepancy 7 | Discrepancy 8 | Total |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 21 | 0 | 0 | 8 | 0 | 8 |
| 22 | 0 | 0 | 0 | 0 | 0 |
| 23 | 4 | 4 | 4 | 0 | 12 |
| 24 | 0 | 12 | 4 | 4 | 20 |
| 25 | 10 | 10 | 12 | 0 | 32 |
| 26 | 4 | 8 | 16 | 8 | 36 |
| 27 | 10 | 22 | 28 | 4 | 64 |
| 28 | 28 | 56 | 88 | 8 | 180 |
| 29 | 24 | 96 | 72 | 32 | 224 |
| 30 | 52 | 156 | 184 | 56 | 448 |
| 31 | 92 | 324 | 496 | 112 | 1024 |
| **Total** | **224** | **688** | **912** | **224** | **2048** |

All omitted pairs have multiplicity zero; in particular linear complexity 22 does not occur. Exactly **92** cycles simultaneously have maximum linear complexity \(31\) and minimum discrepancy \(5\). Thus among the 224 minimally discrepant cycles, exactly \(92/224=23/56\) have maximal linear complexity; the corresponding unconditional frequency is \(1024/2048=1/2\). These two quality criteria are not independent in this finite ensemble.

## Assumptions and scope

The alphabet is \(\mathbb F_2\), the order is exactly five and the period is 32. Each cyclic word is counted once, anchored at the unique occurrence of the length-five all-zero factor. Every contiguous factor in the discrepancy definition may cross the cyclic boundary; the empty factor has discrepancy zero and is immaterial. Complementation and reversal are **not** quotient operations. Binary linear complexity refers to recurrences over \(\mathbb F_2\), not algebraic degree of a nonlinear generating rule.

## Proof

**1. Exhaustive feedback parameterization.** Write a length-five state as bits \(x_0x_1x_2x_3x_4\). Any de Bruijn cycle induces a state permutation whose successor shifts left and appends one bit. The two states with common four-bit suffix \(v=x_1x_2x_3x_4\) must have opposite appended bits: otherwise their successors would coincide, contradicting that the 32 states constitute one cycle. Hence the feedback necessarily has the unique nonsingular form
\[
(x_0,v)\longmapsto (v,x_0\oplus f(v)),\qquad f:\mathbb F_2^4\to\mathbb F_2.
\]
There are exactly \(2^{16}\) candidate functions. Conversely, whenever the induced state permutation is one 32-cycle, its 32 output bits form a de Bruijn cycle. A de Bruijn cycle has a unique all-zero five-bit state and so is counted once by the orbit test rooted there. The `verify_fsr.py` program visits every candidate function and checks the orbit by exact integer masks. Precisely 2048 candidates pass.

**2. Exact discrepancy computation.** Every order-five de Bruijn cycle has 16 zeros and 16 ones, because each bit occurs equally often as the first bit of a length-five factor. Define prefix balances \(p_0=0\) and \(p_{i+1}=p_i+2w_i-1\) for \(0\le i<32\). Since \(p_{32}=p_0\), the maximum absolute sum of any cyclic interval is \(\max_i p_i-\min_i p_i\). This follows because each interval has a difference of two prefix balances, and any pair of positions is connected by a directed cyclic interval. The first checker uses this range formula; the second checks all starting positions and all lengths directly.

**3. Exact linear-complexity computation.** Let \(P_w(X)=\sum_{i=0}^{31}w_iX^i\) over \(\mathbb F_2\). For the periodic generating series, \(\sum_{i\ge0} w_iX^i=P_w(X)/(1-X^{32})\). The minimal recurrence length equals the degree of the reduced denominator. Since \(1-X^{32}=(1+X)^{32}\) in characteristic two, it follows that
\[
L(w)=32-\nu_{1+X}(P_w),
\]
where \(\nu_{1+X}\) is the multiplicity of the factor \(1+X\), with the all-zero sequence excluded by the de Bruijn condition. The first checker divides the integer bit-mask polynomial exactly by \(1+X\) until the remainder is nonzero.

**4. Independent full enumeration.** The binary de Bruijn graph on four-bit vertices has 32 labeled edges \(x_0x_1x_2x_3x_4\), from prefix \(x_0x_1x_2x_3\) to suffix \(x_1x_2x_3x_4\). Euler tours traverse every edge once and are equivalent to order-five de Bruijn cycles. Fixing the unique all-zero edge as the first edge removes precisely cyclic rotation. The `verify_euler.py` program enumerates all such rooted Euler tours, obtains exactly 2048 tours, and independently evaluates linear complexity using Berlekamp–Massey on 64 terms of the repeated period. It independently computes the cyclic discrepancy by testing all 32 start positions and every positive length up to 32. The two algorithms return the same 44-entry table including all zero cells shown above. Therefore the displayed joint multiplicities are exact.

## Verification

The files `verify_fsr.py`, `verify_euler.py`, and `verify_joint.py` are complete, standalone Python 3 source with no nonstandard dependencies. Execute `python3 verify_joint.py` from their common directory. The driver recomputes both full enumerations and compares both dictionaries to the displayed reference matrix, including zero cells, total 2048 and the simultaneous optimum 92. The two full enumerators employ different combinatorial objects and different linear-complexity and discrepancy algorithms.

## Relationship to prior work

Gabrić and Sawada, *Investigating the discrepancy property of de Bruijn sequences* (arXiv:2005.01638, May 4, 2020), analyze cyclic imbalance and explicit constructions but do not supply the joint order-five linear-complexity table. Álvarez, Becher, Mereb, Pajor and Soto, *De Bruijn Sequences with Minimum Discrepancy* (arXiv:2407.17367, July 24, 2024), prove existence of minimum-discrepancy sequences of every binary order, without joint complexity counts. Chang and Wang, *Efficient generation of odd order de Bruijn sequence with the same complement and reverse sequences* (arXiv:2408.01794, August 3, 2024), study CR symmetry and divisibility of the number of maximum-linear-complexity sequences; their Theorem 3.11 does not provide the above joint distribution. The separate order-five discrepancy marginal \((224,688,912,224)\) is previously established and not claimed as new here. Neither that marginal nor a separate linear-complexity marginal implies the intersection count 92 or the 11-by-4 joint table.

## Limitations

The classification is finite and restricted to binary order-five de Bruijn cycles. No analogous claim is made for order six or larger. The joint optimal fraction need not persist asymptotically. The calculations provide exhaustive finite proofs given the demonstrated encodings, not independent external certification. Possible unindexed previous tabulation of the precise joint invariant is a residual originality risk.

## References

1. Daniel Gabrić and Joe Sawada, *Investigating the discrepancy property of de Bruijn sequences*, arXiv:2005.01638 (first posted 2020-05-04), https://arxiv.org/abs/2005.01638.
2. Nicolás Álvarez, Verónica Becher, Martín Mereb, Ivo Pajor and Carlos Miguel Soto, *De Bruijn Sequences with Minimum Discrepancy*, arXiv:2407.17367 (first posted 2024-07-24), https://arxiv.org/abs/2407.17367.
3. Zuling Chang and Qiang Wang, *Efficient generation of odd order de Bruijn sequence with the same complement and reverse sequences*, arXiv:2408.01794 (first posted 2024-08-03), https://arxiv.org/abs/2408.01794.
