# Exact first-base spectrum for propagating digit-square cycles through length twenty

## Finding

For an integer base \(b\ge2\), write a positive integer as \(n=qb+r\) with \(0\le r<b\). Define \(S_b(n)=q^2+r^2\) whenever \(n<b^2\); this is the ordinary sum of squared base-\(b\) digits for those integers. A primitive period-\(\ell\) cycle is **propagating** if every state \(n\) satisfies \(1\le n<b^2\) and \(b\nmid n\).

Let \(\beta(\ell)\) be the smallest base admitting such a cycle of length \(\ell\). For **every** integer \(2\le\ell\le20\), the exact values are:

| Cycle length | Least base \(\beta(\ell)\) |
| ---: | ---: |
| \( 2 \) | \( 3 \) |
| \( 3 \) | \( 8 \) |
| \( 4 \) | \( 7 \) |
| \( 5 \) | \( 27 \) |
| \( 6 \) | \( 16 \) |
| \( 7 \) | \( 15 \) |
| \( 8 \) | \( 58 \) |
| \( 9 \) | \( 144 \) |
| \( 10 \) | \( 63 \) |
| \( 11 \) | \( 122 \) |
| \( 12 \) | \( 127 \) |
| \( 13 \) | \( 163 \) |
| \( 14 \) | \( 393 \) |
| \( 15 \) | \( 287 \) |
| \( 16 \) | \( 311 \) |
| \( 17 \) | \( 1120 \) |
| \( 18 \) | \( 96 \) |
| \( 19 \) | \( 269 \) |
| \( 20 \) | \( 1230 \) |

In particular, the least **uniform** upper bound on \(\beta(\ell)\) for \(2\le\ell\le20\) is exactly \(1230\), attained at length \(20\). This strengthens the existence bound in Remark 2.13 of the cited paper to an exact, sharp classification. The spectrum is nonmonotone: for example, the first length-\(17\) cycle needs base \(1120\), but length \(18\) first occurs already in base \(96\).

## Assumptions and scope

Only classical square-digit dynamics are considered. The term propagating has the precise two-digit and nonzero-units-digit meaning above. The range \(2\le\ell\le20\) and all integer bases \(b\ge2\) are included. No assertion is made about the least bases for other lengths or about nonpropagating cycles.

## Proof

For fixed \(b\), define a directed graph \(G_b\) with vertex set
\[V_b=\{n\in\mathbb{Z}:1\le n<b^2,\;b\nmid n\}.\]
For \(n=qb+r\in V_b\), place a directed edge from \(n\) to \(r^2+q^2\) **exactly when** the latter integer is also in \(V_b\). Every vertex has out-degree at most one. By the definition of \(S_b\), the directed cycles of \(G_b\) are exactly the propagating cycles, with identical primitive lengths. No possible propagating cycle can use a state outside \(V_b\), so this equivalence is exhaustive.

An exact finite enumeration of every \(G_b\), for \(2\le b\le1230\), is supplied by `propagating_cycle_spectrum_verifier.cpp`. Two independently programmed procedures agree on the values in the displayed table. Method A walks each unvisited eligible vertex, using a three-color functional-graph traversal; the first repetition in the current walk identifies one cycle and its length, and all traversed vertices become permanently classified. Method B constructs the successor graph independently, repeatedly removes all vertices of in-degree zero and then traverses each remaining cycle. For a finite directed graph with out-degree at most one, vertices surviving iterative zero-in-degree deletion are **precisely** the directed cycles: a noncycle component ends at a missing edge or feeds into a cycle, and its acyclic predecessors all peel away. Both procedures therefore visit all possible cycles of every enumerated base, rather than testing selected seeds.

The program exhausts bases \(2\le b\le1230\), and for each base covers **every** one of the at most \(b^2-1\) positive integers with up to two digits. The total of all squared base bounds is \(621045654\), and all arithmetic is exact signed integer arithmetic with values well below \(2^{31}\). The two procedures return the same first-occurrence table; the code asserts each entry against the stated values. File `propagating_cycle_witnesses.tsv` lists one actual period-\(\ell\) cycle in base \(\beta(\ell)\) for every \(2\le\ell\le20\), and each entry has been checked directly against the digit-square formula.

For each length in this range, the witness provides \(\beta(\ell)\le b_\ell\), and the exhaustive examination of all earlier bases supplies \(\beta(\ell)\ge b_\ell\). These inequalities give the claimed equalities. The maximum of the nineteen exact values is \(1230\), proving the final sharp uniform cutoff.

## Verification

Compile and run the enclosed standard C++17 source:

```sh
c++ -O3 -std=c++17 propagating_cycle_spectrum_verifier.cpp -o verify
./verify
```

It prints all nineteen first-base pairs followed by `VERIFIED`. The independent graph algorithms are both implemented within that source; both were executed and their results matched. The witness table provides further directly testable positive certificates. The complete enumeration is finite; it does not infer infinitary behavior from tested data.

## Relationship to prior work

Lorenzini, Melistas, Suresh, Suwama, and Wang introduced propagating cycles in their work *Integer Dynamics*, and their Remark 2.13 observes that each length through \(20\) occurs by base \(1230\), while raising the question of how first bases grow with length. Their text does not supply the exact nineteen-term first-base spectrum or prove that \(1230\) is minimal as a uniform cutoff. Their later example explicitly identifies base \(15\) as the first base for length \(7\), which is one entry of the present classification. Their propagation theorem gives arithmetic progressions of bases *after* a seed cycle, not a least-base certificate. The present statement is a finite first-occurrence classification, not a replacement for the published existence, propagation or density results.

## Limitations

This classification is limited to cycle lengths at most twenty and to propagating, two-digit cycles. Some larger-base cycles can have more than two digits or a zero units digit, and they lie outside the claim. The exact table gives no polynomial bound in the variable cycle length for arbitrary lengths. It is reproducible as a program-verified finite mathematical assertion; independent external validation has not been performed. A prior unindexed census cannot be excluded solely from the literature and search checks performed.

## References

D. Lorenzini, M. Melistas, A. Suresh, M. Suwama, and H. Wang, *Integer Dynamics*, arXiv:2105.14361v1 (first publicly available 2021-05-29), especially §2, Theorem 2.4, Corollary 2.8, Proposition 2.12, and Remark 2.13. https://arxiv.org/abs/2105.14361
