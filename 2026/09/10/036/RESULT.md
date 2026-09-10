# Explicit nodal genus-10 limit rank-2 bundle of multidegree (6,6) with six sections

## Context

Mercat's rank-2 conjecture predicts $\mathrm{Cliff}_2(C)=\mathrm{Cliff}_1(C)$.
Generic truth is known (Bakker–Farkas), while special counterexamples are
known only for $g>10$ (Farkas–Ortega via Koszul divisors), leaving genus 10
at maximal Clifford index $4$ as the first undecided threshold. The minimal
symmetric violating numerics are rank 2, degree 12, $h^0\ge 6$
($\mathrm{Cliff}_2\le 2<4$). This record banks the special-fiber half of that
attack as an exact, checkable degeneration input. It does not claim smoothing
to a smooth curve.

## Definitions

- $X_0=C_1\cup C_2$: two smooth trigonal genus-$4$ curves meeting
  transversely in $3$ nodes. Dual graph: two vertices of weight $4$ joined by
  $3$ edges. Arithmetic genus $p_a=4+4+3-1=10$.
- $L_i$ a $g^1_3$ on $C_i$ ($\deg 3$, $h^0=2$); $E_i=L_i\oplus L_i$
  (rank 2, degree $6$, $h^0=4$).
- Nodes are full fibers of the pencils: $p_1+p_2+p_3\in|L_1|$,
  $q_1+q_2+q_3\in|L_2|$; node $j$ identifies $p_j\sim q_j$.
- Gluing $\varphi_j=I_2$ (scalar $2\times 2$ identity) at each node.
  Total degree $6+6=12$, multidegree $(6,6)$.
- Normalization sequence:
  $0\to H^0(X_0,E_0)\to H^0(C_1,E_1)\oplus H^0(C_2,E_2)
  \xrightarrow{\Phi}\bigoplus_{j=1}^3 M_j$, $M_j\simeq\mathbf{C}^2$.
  Domain dimension $8$, codomain dimension $6$.

## Result

There exists an explicit nodal curve $X_0/\mathbf{C}$ of arithmetic genus 10
as above carrying a limit semistable (strictly, polystable; split) rank-2
bundle $E_0$ of total degree $12$ and multidegree $(6,6)$ with

$$h^0(X_0,E_0)=6\ge 6,$$

verified by the normalization exact sequence and per-component slope
inequalities. $E_0$ is strictly semistable ($F_0\oplus F_0$ with $F_0$ the
limit line bundle of bidegree $(3,3)$); no stability beyond semistable is
claimed.

## Proof / Evidence

Fiber model: $L_i=f_i^*\mathcal{O}(1)$ for trigonal $f_i:C_i\to\mathbf{P}^1$,
so $H^0(C_i,L_i)=f_i^*H^0(\mathcal{O}(1))$. On an unramified fiber
$\{3\text{ distinct points}\}$, sections evaluate as $s(p_j)=s'(t)\cdot c_j$;
the $3\times 2$ evaluation matrix has proportional rows (rank 1). Frame
rescaling makes rows identical, e.g. $\mathrm{ev}=[[1,2],[1,2],[1,2]]$;
gluings $I_2$ are stated in these normalized frames.

Hence with $A=B=\mathrm{diag}(\mathrm{ev},\mathrm{ev})$ ($6\times 4$),

$$\Phi=\begin{pmatrix}A & -B\end{pmatrix}\quad (6\times 8\text{ integer matrix}).$$

Exact fraction arithmetic gives $\mathrm{rank}(\Phi)=2$, so
$h^0(X_0,E_0)=8-2=6$. Generic evaluation points give rank $6$, $h^0=2$,
confirming fiber alignment as the extremal mechanism.

Slope semistability: $\mu(E_1)=\mu(E_2)=6/2=3$ (balanced). Any line
subbundle $M\hookrightarrow E_i=L_i\oplus L_i$ projects non-trivially to some
summand, so a nonzero $M\to L_i$ gives $\deg M\le 3$, $\mu(M)\le 3=\mu(E_i)$.
Summands attain equality: each $E_i$ is strictly (poly)stable-semistable;
$E_0$ is limit (weights $1/2,1/2$) semistable.

Machine checks: `output/artifacts/verify_fallback.py` (exact fractions:
rank 2, $h^0=6$; generic control rank 6/$h^0$ 2; slope and $p_a$ checks)
prints `VERIFY_OK`; `output/artifacts/verify_nodal.py` (numeric:
symmetric 6, generic 2, stable-direction perturbation rank $2\to 3$,
$h^0$ $6\to 5$) prints `VERIFY_OK`.

## Limitations

- $E_0$ is strictly semistable/split, not stable.
- No smoothing to a smooth Clifford-index-$4$ $(C,E)$ is claimed:
  upper semicontinuity goes the wrong way; breaking scalar gluing drops
  $h^0$ ($6\to 5$ computed); generic $(6,6)$ gives $h^0=2$.
- The integer matrix is attained in normalized frames via the
  pullback-proportionality argument; no fixed projective equations for
  $C_i$ are logged (existence uses general genus-4 trigonal curves).
- Filed as a searchable degeneration input for the remaining
  one-inequality smoothing step or adjacent $(d,h)$ cells.

## Reproducibility

- `python3 output/artifacts/verify_fallback.py` → `VERIFY_OK`.
- `python3 output/artifacts/verify_nodal.py` → `VERIFY_OK`.
- Stdlib only (fractions) for the exact check; numpy for the numeric
  cross-check. Dual graph, genera, multidegree, gluings, matrix, and slope
  inequalities are all logged above.

## References

- V. Mercat, Clifford's theorem and higher rank vector bundles.
- G. Farkas, A. Ortega, The maximal rank conjecture and rank two
  Brill–Noether theory (arXiv:1010.4060): $g>10$ abstract existence,
  general bounded-genus truth; $g=10$ left undecided.
- B. Bakker, G. Farkas, Mercat conjecture for rank 2 on generic curves:
  generic truth every genus.
- H. Lange, P. E. Newstead, Vector bundles of rank 2 computing Clifford
  indices (arXiv:1012.0469): $g\ge 11$ known violations; genus-10
  degree-12 $h^0\ge 6$ cell not decided.
- P. Grzegorczyk, V. Mercat, P. E. Newstead, Stable bundles of rank 2
  with four sections: genus-10 $h^0=4$ cell, different numerics.
- F. Fu, B. Osserman et al.: smoothings on elliptic chains genus 22–23,
  different fiber.
