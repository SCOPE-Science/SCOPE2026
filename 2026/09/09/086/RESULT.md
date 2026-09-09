# Complete exact census of C5^3-free 3-graphs on 6 vertices

## Context

The 3-uniform tight 5-cycle $C_5^3$ is the recognized open case in the
single-tight-cycle Turan program: Bodnar-Leon-Liu-Pikhurko (2025) settle the
pair $\{C_4^3,C_5^3\}$ and single $C_\ell^3$ for $\ell \ge 7$ not divisible
by 3 at density $2\sqrt{3}-3$ with stability, explicitly excluding single
$C_5^3$; Kamcev-Letzter-Pokrovskiy leave single $C_5^3$ open
(Mubayi-Rodl lower bound $2\sqrt{3}-3 \approx 0.46410$ conjectured tight vs
Razborov $0.468$ upper). Order $n=6 = |V(C_5^3)|+1$ is the minimal host order
at which $C_5^3$-containment is nontrivial, i.e. the canonical induction
base case.

## Definitions

- Vertex set $\{0,\dots,5\}$; $3$-graphs are subsets of the $\binom{6}{3}=20$
  triples in lex order.
- $C_5^3$: vertices $v_0,\dots,v_4$ cyclic with edges
  $v_i v_{i+1} v_{i+2} \pmod 5$ (5 edges).
- A labeled copy in $H$ is an injective map $\mathbb{Z}_5 \to \{0,\dots,5\}$
  (720 injections) whose 5 consecutive-triple images all lie in $E(H)$.
- Canonical code of $H$: minimum over all $720$ vertex permutations of the
  20-bit edge mask. Isomorphism types = distinct min-codes.

## Result

On $\{0,\dots,5\}$ there are exactly **371229** labeled $C_5^3$-free
3-graphs out of $2^{20}=1048576$ (35.4%), in exactly **835** isomorphism
types. The maximum edge count is **$E_6 = 13$**, attained by a **unique**
isomorphism type (orbit size 60). No $C_5^3$-free 3-graph on 6 vertices has
14+ edges.

Labeled edge-count distribution ($m$ : count; all other $m$ are 0):

0:1, 1:20, 2:190, 3:1140, 4:4845, 5:15432, 6:37680, 7:70140, 8:95820,
9:88220, 10:46336, 11:10280, 12:1065, 13:60.

Type counts per edge number:
0:1, 1:1, 2:3, 3:7, 4:21, 5:42, 6:91, 7:146, 8:195, 9:176, 10:111,
11:33, 12:7, 13:1 (sum 835).

Unique extremal type (orbit 60), edges:

023, 024, 025, 034, 035, 045, 123, 124, 125, 134, 135, 145, 234,

with degrees $(6,6,7,7,7,6)$.
Links: $L(0)=L(1)=K_4$ on $\{2,3,4,5\}$;
$L(2)=\{03,04,05,13,14,15,34\}$; $L(3),L(4)$ analogous;
$L(5)=K_{2,3}$ on $\{0,1\}\times\{2,3,4\}$.
The 7 near-extremal 12-edge types have orbit sizes
90, 45, 15, 180, 360, 360, 15 (sum 1065).
The full 835-representative list is in `artifacts/census_types.json`.

## Proof / evidence

Exhaustive computational proof over all $2^{20}$ masks:

- Generation: numpy enumeration with 720-injection $C_5$ test
  (371229 free; $E_6=13$); min-code canonical labeling over 720 perms
  (835 types; orbit sums match).
- Independent stdlib verifier `artifacts/verify_census.py` (re-executed by
  auditor, `VERIFY_OK`):
  - V1: every representative $C_5^3$-free under independently re-coded
    definitions; edge counts match.
  - V2: every stored canon equals the recomputed min over 720 perms.
  - V3: all 720-image code sets pairwise disjoint (371229 distinct labeled
    graphs; reps pairwise non-isomorphic) plus $|orbit|\cdot|stab|=720$
    spot check.
  - V4a: stabilizer orbit sizes match stored counts; sum 371229;
    per-edge distribution matches.
  - V4b: full independent re-enumeration of all $2^{20}$ masks confirms
    371229 $C_5$-free with identical distribution (coverage exact).
- Consistency: $m \le 4$ labeled counts equal $\binom{20}{m}$
  (1, 20, 190, 1140, 4845) since $C_5$ needs 5 edges.

## Limitations

- Fixed order $n=6$ only; no asymptotic $\pi(C_5^3)$ bound is claimed.
- The surrounding target transfer lemma (dense single-$C_5^3$-free to
  $\{C_4^3,C_5^3\}$-free stability) was NOT closed: clause (d) is false for
  $n \ge 345$ (certified $K_{3,3}$ inversion), naive deletion fails for
  $n \ge 246$, and $0.01n^3$ deletion is $\Theta(1)$ not $o(1)$ in density.
  Only the exact $n=6$ census headline is claimed.

## Reproducibility

- `python3 artifacts/verify_census.py` (stdlib only) replays the full
  certificate and prints `VERIFY_OK` (~1 min; re-enumeration ~13 s).
- `artifacts/census_types.json` holds `n_labeled_free`, `n_types`, `E6`,
  `edge_dist_free`, and per-type `canon`/`count`/`edges_n`/`rep`.

## References

- L. Bodnar, J. Leon, X. Liu, O. Pikhurko, The Turan density of short
  tight cycles, arXiv:2506.03223 (2025).
- N. Kamcev, S. Letzter, A. Pokrovskiy, The Turan density of tight cycles
  in three-uniform hypergraphs, arXiv:2209.08134 (2022).
