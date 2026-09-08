# Row/column/symbol-Hamiltonicity census over McKay order-7 representatives with an explicit atomic witness and a bounded order-8 fragment

## Context

A Latin square of order $n$ is row-Hamiltonian when the permutation induced by
every pair of distinct rows is a single $n$-cycle. Row-Hamiltonian squares are
equivalent to perfect 1-factorisations of the complete bipartite graph
$K_{n,n}$. Column-Hamiltonian and symbol-Hamiltonian are defined analogously; a
square with all three properties is called atomic. Up to conjugacy there are
six conjugates, and the number $\nu(L)$ of row-Hamiltonian conjugates lies in
$\{0,2,4,6\}$, with $\nu(L)=6$ exactly for atomic squares (Allsop-Wanless).
McKay's database records bare squares and counts (147 main-class and 564
isotopy-class representatives at order 7; 283657 main-class at order 8) with no
per-square Hamiltonian spectra.

## Definitions

Work with symbols $S=\{0,\dots,n-1\}$. For rows $a\ne b$, the row permutation
(in symbol domain) is $r_{a,b}(s)=L[b][\mathrm{pos}_a(s)]$ where
$\mathrm{pos}_a(s)$ is the column of $s$ in row $a$. For columns $a\ne b$,
$c_{a,b}(s)=L[\mathrm{pos}^c_a(s)][b]$ where $\mathrm{pos}^c_a(s)$ is the row of
$s$ in column $a$. For symbols $a\ne b$ (rows domain),
$s_{a,b}(r)=\mathrm{row}_b(\mathrm{col}_a(r))$ where $\mathrm{col}_a(r)$ is the
column of $a$ in row $r$ and $\mathrm{row}_b(c)$ is the row of $b$ in column
$c$. $L$ is row/column/symbol-Hamiltonian when all $\binom{n}{2}$ respective
permutations are single $n$-cycles; atomic means all three hold. Then
$\nu(L)=2\times(\text{number of Hamiltonian aspects among row/column/symbol})$.

## Result

For the 147 McKay main-class representatives of order 7: exactly 1 is
row-Hamiltonian (index 37), exactly 2 are column-Hamiltonian (indices 37, 39),
exactly 1 is symbol-Hamiltonian (index 37), hence exactly 1 is atomic (index
37). The $\nu$-distribution is $\{\nu=0:145,\ \nu=2:1\ (\text{idx }39),\
\nu=6:1\ (\text{idx }37)\}$; no representative has $\nu=4$. The column-only
representative (index 39) has $(r_h,c_h,s_h)=(15,21,15)$.

For the 564 McKay isotopy representatives of order 7: row-Hamiltonian 2
(indices 67, 300), column-Hamiltonian 2 (indices 67, 294), symbol-Hamiltonian 2
(indices 67, 365), atomic 1 (index 67); $\nu$-distribution
$\{0:560,\ 2:3,\ 6:1\}$; no $\nu=4$.

Atomic witness (main-class index 37), compact row-major string
`0123456130456220613453415620453620156420136250134`, i.e.

```
0 1 2 3 4 5 6
1 3 0 4 5 6 2
2 0 6 1 3 4 5
3 4 1 5 6 2 0
4 5 3 6 2 0 1
5 6 4 2 0 1 3
6 2 5 0 1 3 4
```

is atomic: all 21 row-pair, 21 column-pair, and 21 symbol-pair permutations are
7-cycles (63/63). All 63 permutations are listed in
`artifacts/atomic_cycles.json`.

Bounded order-8 fragment: the cyclic table $\mathbb{Z}_8$ has
$(r_h,c_h,s_h)=(16,16,16)$ of $\binom{8}{2}=28$ (not row-Hamiltonian). Among
the first 300 McKay main-class representatives of order 8: 0 row-Hamiltonian,
0 column-Hamiltonian, 0 symbol-Hamiltonian, 0 atomic; per-aspect maxima are
16/16/16. No claim is made about the remaining 283357 classes.

## Proof / evidence

Direct computation with independent replay. Each stored string was checked to
be a Latin square. For each of the $\binom{7}{2}=21$ row, column, and symbol
pairs the induced permutation was formed via row/column inverse-position
tables and tested for single-$n$-cycle status by orbit walk (63 permutation
checks per square; $147\times 63+564\times 63$ total plus $300\times 84$ at
order 8). Per-representative counts are in `artifacts/mc7_census.csv`,
`artifacts/is7_census.csv`, `artifacts/mc8_head300_census.csv`. The replay
script `artifacts/verify.py` re-derives every CSV entry from the committed
tables, recomputes each of the 63 atomic-witness permutations from the witness
grid and checks the 7-cycle property, and confirms the headline counts. The
auditor additionally recomputed all verdicts with independently written code in
a second formulation and via the full 6-conjugate $\nu$ test; agreement was
complete (147/147, 564/564, 300/300; 63/63 cycle certificates).

## Limitations

Counts are relative to McKay's fixed representative lists (indices above are
0-based line numbers in the committed files). The cyclic group table
$\mathbb{Z}_7$ is atomic with $(21,21,21)$ but does not occur verbatim among
either McKay reduced list, so "exactly one atomic representative" is a
statement about the lists, not a claim that only one atomic square of order 7
exists. Order 8 covers only the first 300 main-class representatives. No
transversal or orthogonal-mate claims are made. The absence of $\nu=4$ at
order 7 is consistent with, but does not reprove, the Allsop-Wanless theorem
that $\nu=4$ forces odd order $\ge 11$.

## Reproducibility

Run `python3 artifacts/verify.py` from the record root (the directory containing
`RESULT.md`; stdlib only; seconds for order 7, about a minute including the
order-8 head sample). Expected terminal output ends with `VERIFY_OK` and the headline counts above.

## References

- McKay combinatorial data: Latin squares (147 main-class / 564 isotopy-class
  representatives at order 7; bare squares only).
  https://users.cecs.anu.edu.au/~bdm/data/latin.html
- Allsop, Wanless, Row-Hamiltonian Latin squares and Falconer varieties,
  arXiv:2211.13826 (Proc. London Math. Soc. 2024): row-Hamiltonian =
  P1F of $K_{n,n}$, $\nu\in\{0,2,4,6\}$, infinite $\nu=4$ family solving
  Falconer 1970. https://arxiv.org/abs/2211.13826
- Allsop, Wanless, Perfect 1-factorisations of $K_{11,11}$,
  arXiv:2506.02455: order-11 enumeration (different order).
  https://arxiv.org/abs/2506.02455
- Allsop, Cycles of quadratic Latin squares and anti-perfect
  1-factorisations, arXiv:2302.12942: quadratic/anti-perfect constructions.
  https://arxiv.org/abs/2302.12942
- Gill, Wanless, Perfect 1-factorisations of $K_{16}$, arXiv:1905.07535:
  3155 P1Fs of $K_{16}$; no atomic order-15 from the new P1Fs.
  https://arxiv.org/abs/1905.07535
