# A replay-certified Kronecker atlas to n = 10 with Murnaghan threshold on a 12-ray and a maximal witness

## 1. Objects and notation

A partition $\lambda \vdash n$ indexes an irreducible complex character
$\chi^\lambda$ of the symmetric group $S_n$. The **Kronecker coefficient**
$g(\lambda,\mu,\nu)$ is the multiplicity of $\chi^\nu$ in
$\chi^\lambda \otimes \chi^\mu$:

$$g(\lambda,\mu,\nu) = \frac{1}{n!}\sum_{w \in S_n}
  \chi^\lambda(w)\chi^\mu(w)\chi^\nu(w)
  = \frac{1}{n!}\sum_{C}\lvert C\rvert\,
  \chi^\lambda(C)\chi^\mu(C)\chi^\nu(C),$$

the sum over conjugacy classes $C$ (indexed by cycle-type partitions of $n$),
with $\lvert C\rvert = n!/z_\mu$, $z_\mu = \prod_d d^{m_d(\mu)} m_d(\mu)!$.

Fix once and for all the partition order used in every table: partitions
generated in decreasing lexicographic order (so e.g. for $n=10$ index 22 is
$(4,3,2,1)$). All artifact files record this order explicitly.

## 2. Theorem (dual-certified atlas, ray threshold, maximal witness)

The following were computed **twice, by two independent from-partitions routes**,
with byte-identical agreement on every entry, plus row/column orthogonality,
hook-length dimension, transpose-symmetry, and $S_3$-symmetry checks.

**(a) Complete atlas $n \le 10$.** For every ordered triple
$(\lambda,\mu,\nu) \vdash n$, $1 \le n \le 10$, the exact value
$g(\lambda,\mu,\nu)$ is listed in `artifacts/kron_nonzero_{n}.json`
(nonzero entries; every unlisted ordered triple is exactly $0$):

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

Argmax triples (ordered): $n=6$: unique $((3,2,1)^3)$, $g=5$;
$n=7$: 4 ordered (diagonal $((4,2,1)^3)$ plus 3 permutations of
$((4,2,1),(3,2,1,1),(3,2,1,1))$), $g=9$;
$n=8$: unique $((4,2,1,1)^3)$, $g=17$;
$n=9$: 4 ordered (diagonal $((4,2,2,1)^3)$ plus 3 permutations of
$((4,3,1,1),(4,3,1,1),(4,2,2,1))$), $g=28$;
$n=10$: **unique** ordered triple $((4,3,2,1)^3)$, $g=117$.

**(b) Murnaghan-ray threshold.** On the ray
$\lambda(n) = \mu(n) = (n-3,2,1)$, $\nu(n) = (n-2,1,1)$, $6 \le n \le 12$
(reduced core $\alpha=\beta=(2,1)$, $\gamma=(1,1)$, padded with a long first
row — the canonical Murnaghan stable form):

$$g_6 = g_7 = \cdots = g_{12} = 4.$$

Hence the sequence is already stable at the first computed point:
stabilization index $n_0 = 6$ (in-window; the true onset is $\le 6$) with
stable value $g^* = 4$ (`artifacts/ray_cert.json`).

**(c) Maximal witness at $n=10$.** The largest Kronecker coefficient of $S_{10}$
is $M(10) = 117$, attained uniquely (as an ordered triple) at
$\lambda=\mu=\nu=(4,3,2,1)$. The 42-term exact class-sum certificate in
`artifacts/argmax_n10_cert.json` satisfies
$\sum_C \lvert C\rvert\,\chi(C)^3 = 117 \cdot 10! = 424\,569\,600$, verified
term-by-term.

## 3. Method (two independent routes, stdlib only)

**Method A — Murnaghan–Nakayama (rim-hook recursion).**
Character tables built from partitions alone via the abacus rim-hook rule
$\chi^\lambda_\mu = \sum_{\text{rim hooks }H, |H|=\mu_1}
(-1)^{\mathrm{ht}(H)}\chi^{\lambda\setminus H}_{\mu\setminus\mu_1}$.

**Method B — Kostka inversion (no rim hooks).**
Permutation characters $\xi^\lambda(\mu)$ = number of ways to pack the cycles
of type $\mu$ into rows of shape $\lambda$ (exact DP over cycle assignment),
Kostka numbers $K(\tau,\lambda)$ = #SSYT via horizontal-strip recursion, then
exact unitriangular solve of $\xi^\lambda = \sum_\tau K(\tau,\lambda)\chi^\tau$
in dominance order (diagonal $K(\tau,\tau)=1$ asserted at every solve step;
triangular-support $K\ne 0 \Rightarrow$ shape dominates weight verified).

Both routes produce full $S_n$ tables for $1 \le n \le 12$; agreement is
byte-identical at every $n$. Every Kronecker coefficient is then evaluated by
the class-sum inner product from **each** table separately, with exact
divisibility asserted and full A-vs-B equality asserted over all $\sim 117$k
triples ($n\le 10$); the ray points $n=11,12$ are likewise recomputed from
both tables.

Self-checks (all pass, logged): row orthogonality
$\sum_C\lvert C\rvert\chi^2 = n!$ per row; full column orthogonality matrix;
identity-column values equal hook-length dimensions; transpose symmetry
$\chi^{\lambda^t}(C) = \mathrm{sgn}(C)\chi^\lambda(C)$; $S_3$ permutation
symmetry of every Kronecker table; per-table SHA-256 hashes in
`artifacts/summary.json`.

## 4. Reproduction

```
python3 artifacts/methodB_kostka.py   # writes chartable_B_<n>.json (indep. tables)
python3 artifacts/compute_atlas.py    # rebuilds Method-A tables, cross-checks,
                                      # writes chartables, kron tables, certs
```

Runtime $\approx 2$ s total (stdlib Python 3.12, 32 cores available, single
thread used). Artifacts ($1.3$ MB, dominated by the $n=9,10$ nonzero lists)
contain the complete machine-checkable evidence.

## 5. Originality and prior art

General Murnaghan/Stembridge stability theorems (Briand–Orellana–Rosas;
Sam–Snowden), Saxl tensor-square theory (Pak–Panova–Vallejo; Vallejo), and the
$S_6$-only computational study (Sun–Zhang–Zhu) contain none of: the complete
$n \le 10$ nonzero/zero census with per-$n$ maxima above, the $n=10$ value
$117$ at $((4,3,2,1)^3)$, or the $6\ldots12$ ray certificate $g \equiv 4$.
The $n=6,7,8$ zero/nonzero counts ($511/1331$, $1599/3375$, $5048/10648$) and
maxima ($5$, $9$, $17$) agree with the prior failed-attempt fragment recorded
in the lane brief — expected, since these are mathematical facts — but that
attempt was never validated, stopped at $n=8$, used a single method, and
contains no $n=9,10$ atlas, no $11,12$ ray points, and no dual-method replay;
everything claimed here is recomputed from scratch with dual certification.

## 6. Limitations and uncertainty

- Stabilization index $n_0 = 6$ is **in-window**: the ray is constant on all
  computed points $6 \le n \le 12$, so the true onset is $\le 6$ but the
  computation does not pin it from below (that would require $n < 6$, where
  the padded shape $(n-3,2,1)$ is not even defined for $n<6$).
- Stability beyond $n=12$ is a mathematical consequence of Murnaghan's theorem
  for this padded form, not something the finite computation proves; the
  certified content is the exact values $g_n = 4$ at $6 \le n \le 12$.
- Maximality at $n=10$ is exhaustive over all $74\,088$ ordered triples —
  no sampling is involved — but maximality claims stop at $n=10$ (tables at
  $n=11,12$ are character tables only, not full Kronecker censuses).
- No conjecture (Saxl, GCT) is proved; this is benchmark data with certificates.
