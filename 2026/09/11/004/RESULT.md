# Exact L1-distortion census for six small cubic-symmetric graphs

## Context

The least-distortion problem asks for the optimal constant for embedding a
finite metric space into $L_1$. For graph shortest-path metrics this is
governed by cut-cone linear-programming duality (Linial–London–Rabinovich).
A recognized program seeks exact least-distortion constants for named
highly-symmetric graphs: Vallentin (JCTB 2008) for Euclidean embeddings of
distance-regular graphs via SDP, extended in the Euclidean setting by
Cioaba–Gupta–Ihringer–Kurihara (2023). The present result extends the exact
program to the $L_1$ cut-cone setting for the standard small
cubic-symmetric benchmarks fixed by the Foster / Conder census.

## Definitions

Let $G=(V,E)$, $n=|V|$, $m=|E|$, and $d$ the shortest-path metric.
For $S \subseteq V$ let $\delta_S(u,v)=1$ if $S$ separates $u,v$ and $0$
otherwise (cut metric). A nonnegative combination $z=\sum_S w_S\,\delta_S$
($w_S\ge 0$) is an $L_1$ metric. The least $L_1$-distortion is the least
$C\ge 1$ for which cut weights exist with

$$d \le z \le C\cdot d \quad \text{pointwise on pairs},$$

equivalently the optimum of the primal LP (P): $\min C$ s.t.
$z=\sum_S w_S\delta_S \ge d$ on all pairs, $z \le C$ on $E$
($C$-Lipschitz on edges implies $C$-Lipschitz everywhere by path routing),
$w_S\ge 0$. Its dual (D) with demands $f_{uv}\ge 0$ and edge budgets
$g_e\ge 0$ is $\max\sum d(u,v)f_{uv}$ s.t. $\sum_e g_e=1$ and
$\sum_{\mathrm{pairs}(S)}f\le\sum_{\mathrm{edges}(S)}g$ for every cut $S$.

Graphs: Petersen F10A/C10.1 ($n=10$), Heawood F14A/C14.1 ($n=14$),
Möbius–Kantor F16A/C16.1 = GP(8,3) ($n=16$), Pappus F18A/C18.1 = Levi graph
of the Pappus $(9_3)$ configuration ($n=18$), Desargues F20B/C20.2 =
GP(10,3) ($n=20$), Dodecahedron F20A/C20.1 ($n=20$).

## Result

| Graph (Foster) | $n$ | $\|\mathrm{Aut}\|$ | #pair-orbits | $c_1(G)$ |
|---|---|---|---|---|
| Petersen (F10A) | 10 | 120 | 2 | 1 |
| Heawood (F14A) | 14 | 336 | 3 | 4/3 |
| Möbius–Kantor (F16A) | 16 | 96 | 5 | 4/3 |
| Pappus (F18A) | 18 | 216 | 4 | 4/3 |
| Desargues (F20B) | 20 | 240 | 5 | 1 |
| Dodecahedron (F20A) | 20 | 120 | 5 | 1 |

Each value is certified twice in exact rational arithmetic: an explicit
Aut-orbit cut family attaining it as an upper bound, and an
Aut-symmetrized cut-cone dual feasible point attaining the same value as a
lower bound (weak-duality match). The largest distortion in this range is
4/3, attained jointly by Heawood, Möbius–Kantor, and Pappus.

Symmetry-reduction theorem: if $G$ is arc-transitive, (P) attains its
optimum at an $\mathrm{Aut}(G)$-invariant weight vector and (D) at an
$\mathrm{Aut}(G)$-invariant demand with constant $g_e\equiv 1/m$; hence
$c_1(G)$ equals the quotient LP with one variable per pair-orbit (2–5
variables here). Proof by group averaging: the cut cone, constraint family,
and objective are $G$-invariant, and edge-transitivity forces uniform
$\bar g$.

Certificates (pair-orbits pure-distance; $m=15,21,24,27,30,30$):

- Petersen: orbits $\{d{=}1{:}15\},\{d{=}2{:}30\}$; $p=(1/15,0)$, LB $=1$.
  Primal: one cut-orbit, $|O|=12$, rep $\{2,3,4,7,9\}$, $\lambda=3$; $z=d$.
- Heawood: orbits $\{d{=}2{:}42\},\{d{=}1{:}21\},\{d{=}3{:}28\}$;
  $p=(0,0,1/63)$, LB $=84/63=4/3$. Primal: one 28-cut orbit, $\lambda=14/3$.
- Möbius–Kantor: orbits $d{=}1{:}24$, $d{=}2{:}48$, $d{=}3{:}24$,
  $d{=}4{:}8$, $d{=}3'{:}16$; $p=(0,0,0,1/96,1/48)$,
  LB $=32/96+48/48=4/3$. Primal: two orbits ($|O|=16,\lambda=4$;
  $|O|=6,\lambda=1$).
- Pappus: orbits $d{=}2{:}54$, $d{=}4{:}18$, $d{=}1{:}27$, $d{=}3{:}54$;
  $p=(0,1/54,0,0)$, LB $=72/54=4/3$. Primal: one 18-cut orbit, $\lambda=6$.
- Desargues: orbits $d{=}1{:}30$, $d{=}2{:}60$, $d{=}3{:}60$, $d{=}4{:}30$,
  $d{=}5{:}10$; $p=(1/30,0,0,0,0)$, LB $=1$. Primal: one 10-cut orbit,
  $\lambda=5$; $z=d$.
- Dodecahedron: same orbit profile; $p=(1/30,0,0,0,0)$, LB $=1$. Primal:
  one 20-cut orbit, $\lambda=5$; $z=d$.

## Proof / evidence

Independent stdlib-only verifier `output/artifacts/verify.py` recomputes
from `output/artifacts/certs.json`: checks each stored generator is an
automorphism, closes the group (orders 120/336/96/216/240/120), recomputes
APSP and pair-orbits from generators (2/3/5/4/5/5), checks the dual
objective equals claimed $c_1$ as `Fraction`, checks every dual inequality
over all $2^{n-1}-1$ cuts per graph (511 to 524287; ~1.2M total) in exact
arithmetic, and checks primal domination plus Lipschitz bounds on all
pairs via full Aut-orbit expansion. Result: `ALL VERIFY_OK`.
Graph identities independently match the Conder 2048-list
(girths 5/6/6/6/6/5; diameters 2/3/4/4/5/5; bipartiteness F/T/T/T/T/F).

## Limitations

Scope is the six stated graphs; larger Foster orders not computed.
Discovery used an in-house tableau simplex (float + `Fraction`); optimality
rests on the independent exhaustive exact verifier, not on trusting the
solver. Pappus identity is pinned by the full invariant match
(cubic/bipartite/girth-6/diameter-4/$|\mathrm{Aut}|=216) via its Levi
construction.

## Reproducibility

```
python3 output/artifacts/verify.py   # replays all certificates from certs.json
```

## References

- F. Vallentin, Optimal embeddings of distance regular graphs into
  Euclidean spaces, JCTB 98 (2008). https://arxiv.org/abs/math/0509716
- Foster Census of Cubic Symmetric Graphs (Conder/Potočnik).
  https://fostercensus.graphsym.net/
- M. Conder, Trivalent (cubic) symmetric graphs on up to 2048 vertices
  (list). https://www.math.auckland.ac.nz/~conder/symmcubic2048list.txt
