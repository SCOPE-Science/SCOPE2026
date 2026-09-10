# Certified pruning of the least eliminated 2-cover twist of the Balakrishnan–Dogra rank-excess benchmark curve

## Context

Classical Chabauty–Coleman fails once Jacobian rank reaches genus. Quadratic
Chabauty restores finiteness with heavy $p$-adic-height machinery. The
independent classical alternative is covering collections: an unramified
$2$-descent splits a rank-excess genus-2 problem into finitely many twist
problems, each pruned twist being a certified descent step (Flynn–Wetherell,
Bruin–Stoll). The object here is the first published rank-exceeds-genus
benchmark curve of Balakrishnan–Dogra, *Quadratic Chabauty and rational
points II* (arXiv:1705.00401), attacked by this independent descent route.
Only the preset single-twist fallback is claimed; no full $X(\mathbf{Q})$
census is asserted.

## Definitions

Let
$$X = X_{31}:\quad y^2 = f(x) := x^6+31x^4+31x^2+1.$$
Put $g_1(x)=x^2+1$, $g_2(x)=x^4+30x^2+1$, so $f=g_1g_2$.
Let $E_{31}:\ y^2=x^3+31x^2+31x+1=(x+1)(x^2+30x+1)$,
with $2$-torsion point $(-1,0)$ and $\mathrm{disc}(E_{31})=2^{11}\cdot 7^3$.
$\mathrm{Jac}(X)$ is isogenous over $\mathbf{Q}$ to $E_{31}\times E_{31}$
via $(x,y)\mapsto(x^2,y)$ and $(x,y)\mapsto(x^{-2},yx^{-3})$; with $E_{31}$
of rank $2$, $\mathrm{Jac}(X)$ has rank $4>2=g$.
Let $\mathrm{Res}(g_1,g_2)=28^2=784$ (since
$g_2-(x^2+29)g_1=-28$).
For squarefree $d\mid 28$, $d>0$, define the $2$-cover twist
$$D_d:\quad d\,u^2=g_1(x),\qquad d\,v^2=g_2(x),\qquad y=\pm d\,u\,v.$$
Since $g_1>0$ on $\mathbf{Q}$, every $(x,y)\in X(\mathbf{Q})$ lifts to
exactly one $D_d(\mathbf{Q})$ with $d\in\{1,2,7,14\}$.

## Result (headline claim)

For $X_{31}$ as above, let $D^\*=D_7$ be the least-twisting-parameter
unresolved twist. Then $D_7$ has no $\mathbf{Q}$-rational point:
$$D_7:\ 7u^2=x^2+1,\quad 7v^2=x^4+30x^2+1$$
satisfies $D_7(\mathbf{Q})=\varnothing$, certified by an explicit local
obstruction at the least non-soluble place $v^\*=2$.

## Proof / evidence

(i) **Least eliminated twist.** The $14$ known affine rational points of $X$
are on $X$ (exact check). Their twist assignment is $d=1$ ($2$ points,
$x=0$) and $d=2$ ($12$ points). Explicitly
$D_1(\mathbf{Q})\ni(0,1,1)$ since $g_1(0)=g_2(0)=1$, and
$D_2(\mathbf{Q})\ni(1,1,4)$ since $g_1(1)=2$, $g_2(1)=32=2\cdot 4^2$.
Hence $d=1,2$ are not eliminated and the least candidate is $D_7$.

(ii) **Local obstruction at $2$.** $D_7(\mathbf{R})\ne\varnothing$
($x=0$, $u=1/\sqrt7$), so $v^\*$ is finite.
Lemma (mod-$8$ wall, exhaustive over $8^3=512$ triples): every solution of
$X^2+Z^2=7U^2$ in $(\mathbf{Z}/8)^3$ has $X,Z,U$ all even; there are $32$
solutions and $0$ with an odd coordinate.
A $\mathbf{Q}_2$-point of $7u^2=x^2+1$ clears denominators to
$X^2+Z^2=7U^2$ over $\mathbf{Z}_2$ with $(X,Z,U)$ primitive (not all in
$2\mathbf{Z}_2$); reduction mod $8$ contradicts the Lemma. Infinite
$2$-descent leaves only $(0,0,0)$. Hence $D_7(\mathbf{Q}_2)=\varnothing$.
The Hilbert log $(7,-1)_2=-1$ records the same obstruction invariantly.
Cross-check: $D_7(\mathbf{Q}_7)=\varnothing$ as well
($X^2+Z^2\equiv 0\bmod 7\Rightarrow 7\mid X,Z$, by $\mathbf{F}_7^2$
exhaustion, plus descent). The named least place is $v^\*=2$ since
$\mathbf{R}$ is soluble and $2$ fails.

(iii) **Implication.** $D_7(\mathbf{Q}_2)=\varnothing\Rightarrow
D_7(\mathbf{Q})=\varnothing$: exactly one Selmer twist pruned.

Replay (stdlib only):
`python3 output/artifacts/verify_fallback.py` → `VERIFY_OK`,
plus `verify_target.py` (twist table, mod-$7$ descent) and
`verify_E31.py` (model data).

## Limitations

Full target **not** claimed: $D_1$ and $D_2$ both contain rational points
and their complete resolution needs elliptic-curve Chabauty over quadratic
fields on positive-rank quotients, not completed here. No exact $X(\mathbf{Q})$
census asserted; $D_{14}$ emptiness is logged as corroboration only. An early
incorrect rank-$0$ guess for a descent quotient was caught by point search
and withdrawn; no rank claim is made.

## Reproducibility

All claims replay from stored integer logs with stdlib-only checks in
`output/artifacts/`. Factor identity, $14$ affine point checks, twist
assignment, mod-$8$ exhaustion ($32$ all-even solutions), Hilbert parity,
and mod-$7$ exhaustion are exact.

## References

- J. S. Balakrishnan, N. Dogra, *Quadratic Chabauty and rational points II:
  Generalised height functions on Selmer varieties*, arXiv:1705.00401.
- F. Bianchi, O. Padurariu, *Rational points on rank 2 genus 2 bielliptic
  curves in the LMFDB*, arXiv:2212.11635.
- E. V. Flynn, J. L. Wetherell, *Covering collections and a challenge
  problem of Serre*, Acta Arith. 98 (2001); *Finding rational points on
  bielliptic genus 2 curves*, manuscripta math. 100 (1999).
