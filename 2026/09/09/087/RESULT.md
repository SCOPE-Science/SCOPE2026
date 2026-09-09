# First e-positivity certificate beyond Ellzey's directed cycle: full e-expansion of C_{8,2}

## Context

Let $X_{\vec{G}}(\mathbf{x};t)$ denote Ellzey's chromatic quasisymmetric function of a
digraph (arXiv:1709.00454, Def. 1.3). Ellzey proves an $F$-basis expansion for all
digraphs via $G$-descents (Thm. 3.1), a $p$-positivity formula in the symmetric case
(Thm. 4.1), symmetry for circular-indifference digraphs (Thm. 5.5 / Cor. 5.7), and an
$e$-formula solely for the directed cycle $k=1$ (Thm. 6.1 / Cor. 6.2), conjecturing
$e$-positivity for all circular-indifference digraphs (Conj. 1.4). No $e$-coefficient
for any $k \geq 2$ circular power was previously recorded; $F$- and $p$-expansions do
not imply $e$-signs.

## Definitions

For integers $n \geq 3$ and $1 \leq k < n/2$, let $C_{n,k}$ be the digraph on vertex set
$\mathbb{Z}_n$ with arcs $i \to j$ iff the clockwise distance from $i$ to $j$ lies in
$\{1,\dots,k\}$ (the $k$-th circular power of the directed $n$-cycle).
A proper coloring is a proper coloring of the underlying undirected graph; an ascent is
a directed edge $(u,v)$ with $\kappa(u) < \kappa(v)$; $\mathrm{asc}(\kappa)$ is its number.
$X_{\vec{G}}(\mathbf{x};t) = \sum_{\kappa} t^{\mathrm{asc}(\kappa)} \mathbf{x}_{\kappa}$.
A circular-indifference digraph is one whose arcs are exactly the pairs $[i,j]$ contained
in some member of a family of circular intervals (Ellzey Def. 5.1).

## Result

**Theorem (full $e$-vector of $C_{8,2}$).** Let $C_{8,2}$ be the digraph on
$\mathbb{Z}_8$ with arcs $i \to j$ iff the clockwise distance is $1$ or $2$
($16$ arcs). Then $X_{C_{8,2}}}(\mathbf{x};t)$ is symmetric and

$$X_{C_{8,2}}}(\mathbf{x};t)=\sum_{\lambda \vdash 8} c_{\lambda}(t)\,e_{\lambda}(\mathbf{x}),$$

with

- $c_{(8)}(t) = 8t^3+64t^4+224t^5+456t^6+616t^7+672t^8+616t^9+456t^{10}+224t^{11}+64t^{12}+8t^{13}$,
- $c_{(7,1)}(t) = 32t^5+136t^6+208t^7+208t^8+208t^9+136t^{10}+32t^{11}$,
- $c_{(6,2)}(t) = 24t^6+64t^7+64t^8+64t^9+24t^{10}$,
- $c_{(5,3)}(t) = 8t^6+48t^7+80t^8+48t^9+8t^{10}$,
- $c_{(4,4)}(t) = 4t^6+40t^7+80t^8+40t^9+4t^{10}$,

and $c_{\lambda}(t)=0$ for the other $17$ partitions of $8$.
Every $c_{\lambda}(t)$ has nonnegative integer coefficients, is palindromic with
center $|E|/2 = 8$, and is unimodal.

## Proof / evidence (replayable computation)

`python3 output/artifacts/verify.py` prints `VERIFY_OK` (reproduced by auditor):

1. **Membership.** The $8$ circular intervals $[i,i+2]$ generate exactly the $16$ arcs
   of $C_{8,2}$ (arc-set equality checked); symmetry of $X$ follows from Ellzey Cor. 5.7.
2. **$G$-descent census.** Exhaustion of $S_8$ ($40320$ permutations) with
   $(G,\sigma)$-ranks, $G$-descent sets, and $\mathrm{inv}_{\vec{G}}$ gives the
   $\delta(k,\ell)$ distribution ($33$ cells). Cor. 3.3's
   $\chi(m,t)=\sum_{k,\ell}\delta(k,\ell)\binom{m+k}{8}t^\ell$ verified against direct
   proper-coloring enumeration at $m=2$ ($0$), $m=3$ ($0$), $m=4$ ($168$ colorings).
3. **Exact $e$-solve.** $106$ unordered proper set partitions / $136488$ proper ordered
   partitions (canonical independent-block DFS times $l!$ color orders) give the
   $m$-expansion; per-monomial symmetrization divides type-$\mu$ weights by
   $\ell!/\prod_c m_c(\mu)!$ (integrality asserted entrywise). Exact conversion with the
   $22 \times 22$ $e$-to-$m$ matrix over $\mathbb{Q}$ (Fractions, $q=8$ variables) yields
   the table above.
4. **Acyclic-orientation row sums (Thm. 6.5).** Exhaustion of all $2^{16}$ orientations
   gives $4968$ acyclic ones; $\sum_{\ell(\lambda)=k}c_{\lambda}(t)$ matches the
   sink-count/asc distribution for $k=1$ ($=c_{(8)}$) and $k=2$
   ($=32t^5+172t^6+360t^7+432t^8+360t^9+172t^{10}+32t^{11}$); rows $k \geq 3$ empty on
   both sides.
5. **Sign/shape checks + byte identity.** All coefficients nonnegative integers;
   palindromicity about degree $8$ and unimodality asserted; recomputed table is
   byte-identical to committed `ctable_82.json`.
6. **Auditor triangulation.** Specializing $e_{\lambda}(1^m)=\prod_i \binom{m}{\lambda_i}$
   predicts $t$-chromatic distributions matching direct coloring enumeration at
   $m=2,3,4,5$ and $m=6$ ($64440$ colorings), independent of the $G$-descent code.

## Limitations

Claims only the $C_{8,2}$ datum, not the infinite $C_{n,k}$ family. The $e$-solve goes
through the exact $m$-expansion plus rational $e/m$ matrix (equivalent to the $p$-basis
transfer route, fully logged). Exploratory $C_{6,2}/C_{7,2}/C_{8,3}$ tables are unclaimed.

## Reproducibility

Stdlib-only Python (`verify.py`, `sym.py`, `ellzey.py`, `ecoeff.py`, `fast.py`,
committed `ctable_82.json`). S_8 enumeration ($40320$) plus $2^{16}$ orientation scan
plus $136488$-term ordered-partition scan; runs in minutes on a laptop.

## References

- B. Ellzey, A directed graph generalization of chromatic quasisymmetric functions,
  arXiv:1709.00454.
- B. Ellzey, Chromatic quasisymmetric functions of directed graphs (FPSAC),
  arXiv:1612.04786.
- P. Alexandersson, G. Panova, LLT polynomials, chromatic quasisymmetric functions and
  graphs with cycles, arXiv:1705.10353.
- J.-C. Aval, R. Melgar, Chromatic quasisymmetric functions for signed graphs,
  arXiv:2508.20200.
- J. White, The Chromatic Quasisymmetric Class Function of a Digraph,
  arXiv:2106.02665.
