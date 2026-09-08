# Certified Kronecker atlas to n=10 with Murnaghan-ray values and S10 maximal witness

## Context

Kronecker coefficients $g(\\lambda,\\mu,\\nu)$ govern tensor products of irreducible
complex characters of $S_n$. They are central to Murnaghan/Stembridge stability
theory, the Saxl staircase-positivity conjecture, Geometric Complexity Theory
positivity benchmarks, and symmetric-function positivity test data. General
stability theorems (Briand–Orellana–Rosas; Sam–Snowden) and Saxl tensor-square
results (Pak–Panova–Vallejo; Vallejo) prove structural facts but publish no
complete certified small-$n$ atlas with an explicit ray threshold and maximal
witness. The closest computational prior (Sun–Zhang–Zhu) works out full
Kronecker data only for $S_6$.

## Definitions

- Partition $\\lambda \\vdash n$ indexes irreducible character $\\chi^\\lambda$ of $S_n$.
- $g(\\lambda,\\mu,\\nu) = \\frac{1}{n!}\\sum_{w \\in S_n}
  \\chi^\\lambda(w)\\chi^\\mu(w)\\chi^\\nu(w)
  = \\frac{1}{n!}\\sum_C |C|\\,\\chi^\\lambda(C)\\chi^\\mu(C)\\chi^\\nu(C)$,
  summed over conjugacy classes $C$ of cycle type $\\vdash n$,
  $|C| = n!/z_\\mu$, $z_\\mu = \\prod_d d^{m_d} m_d!$.
- Partitions are in decreasing lexicographic order (index 22 = $(4,3,2,1)$ at $n=10$).
- Ray: $\\lambda(n)=\\mu(n)=(n-3,2,1)$, $\\nu(n)=(n-2,1,1)$ for $6 \\le n \\le 12$
  (reduced core $\\alpha=\\beta=(2,1)$, $\\gamma=(1,1)$).

## Result

**(a) Complete atlas $n \\le 10$.** For every ordered triple
$(\\lambda,\\mu,\\nu) \\vdash n$, the exact $g(\\lambda,\\mu,\\nu)$ is tabulated
(nonzero entries listed; unlisted triples are exactly $0$):

| $n$ | $p(n)$ | ordered triples | nonzero | zero | max $M(n)$ |
|-----|--------|-----------------|---------|------|-----------|
| 1 | 1 | 1 | 1 | 0 | 1 |
| 2 | 2 | 8 | 4 | 4 | 1 |
| 3 | 3 | 27 | 11 | 16 | 1 |
| 4 | 5 | 125 | 43 | 82 | 1 |
| 5 | 7 | 343 | 143 | 200 | 2 |
| 6 | 11 | 1331 | 511 | 820 | 5 |
| 7 | 15 | 3375 | 1599 | 1776 | 9 |
| 8 | 22 | 10648 | 5048 | 5600 | 17 |
| 9 | 30 | 27000 | 14294 | 12706 | 28 |
| 10 | 42 | 74088 | 40860 | 33228 | 117 |

Argmax (ordered): $n=6$: unique $((3,2,1)^3)$, $g=5$; $n=7$: 4 ordered
(diagonal $((4,2,1)^3)$ + 3 permutations of $((4,2,1),(3,2,1,1),(3,2,1,1))$),
$g=9$; $n=8$: unique $((4,2,1,1)^3)$, $g=17$; $n=9$: 4 ordered
(diagonal $((4,2,2,1)^3)$ + 3 permutations of
$((4,3,1,1),(4,3,1,1),(4,2,2,1)))$, $g=28$;
$n=10$: **unique** $((4,3,2,1)^3)$, $g=117$.

**(b) Murnaghan-ray values.** On the ray above,
$g_6 = g_7 = \\cdots = g_{12} = 4$.
The sequence is already stable at the first computed point: in-window index
$n_0 = 6$ (true onset $\\le 6$) with stable value $g^* = 4$.

**(c) Maximal witness at $n=10$.** The largest $S_{10}$ Kronecker coefficient is
$M(10)=117$ at $\\lambda=\\mu=\\nu=(4,3,2,1)$, with
$\\sum_C |C|\\chi(C)^3 = 117 \\cdot 10! = 424569600$ verified term-by-term
over the 42 classes.

## Proof / Evidence

Two independent from-partitions routes give byte-identical $S_n$ character
tables for $1 \\le n \\le 12$: (A) Murnaghan–Nakayama rim-hook recursion;
(B) Young-subgroup permutation characters + SSYT Kostka numbers with
unitriangular dominance-order solve (no rim hooks). Every Kronecker coefficient
is evaluated by the class-sum inner product from each table separately with
exact divisibility asserted and full A-vs-B equality over all ~117k triples
($n \\le 10$); ray points $n=11,12$ likewise from both tables. Self-checks all
pass: row and column orthogonality, identity-column hook-length dimensions,
transpose symmetry, $S_3$ permutation symmetry of Kronecker tables.
Independent audit rebuilt all tables with a third implementation and
exhaustively recomputed every inner product, confirming all counts, maxima,
argmax families, ray values, and the 42-term argmax certificate.

## Limitations

- $n_0=6$ is in-window: constant on all computed points $6 \\le n \\le 12$;
  shapes undefined for $n<6$, so onset from below is not pinned.
- Stability beyond $n=12$ follows from Murnaghan's theorem, not the computation.
- Exhaustive maximality only to $n=10$ ($n=11,12$ have certified character
  tables, not full Kronecker censuses).
- No conjecture (Saxl, GCT) is proved; this is benchmark data with certificates.

## Reproducibility

Stdlib Python 3.12, ~2 s single-threaded:

```
python3 artifacts/methodB_kostka.py   # independent Kostka-inversion tables
python3 artifacts/compute_atlas.py    # Method-A tables, cross-checks, censuses, certs
```

Verification-critical artifacts copied to `output/artifacts/`
(`summary.json`, `ray_cert.json`, `argmax_n10_cert.json`, `chartable_10.json`,
`compute_atlas.py`, `methodB_kostka.py`, `DRAFT.md`). Full nonzero tables
(`kron_nonzero_{n}.json`) and all character tables reside in the candidate
artifact store.

## References

- Briand–Orellana–Rosas, The stability of the Kronecker products of Schur
  functions, arXiv:0907.4652.
- Sam–Snowden, Proof of Stembridge's conjecture on stability of Kronecker
  coefficients, arXiv:1501.00333.
- Pak–Panova–Vallejo, Kronecker products, characters, partitions, and the
  tensor square conjectures, arXiv:1304.0738.
- Vallejo, A diagrammatic approach to Kronecker squares, arXiv:1310.8362.
- Sun–Zhang–Zhu, Kronecker coefficients and Harrison centres of the
  representation ring of the symmetric group, arXiv:2407.18152.
