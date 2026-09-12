# Rank-two Schottky group over Q3 with generators in four distinct residue classes

## Context

Let $K=\mathbf Q_3$ with maximal ideal $3\mathbf Z_3$ and residue field
$\mathbf F_3$, so $\mathbf P^1(\mathbf F_3)=\{0,1,2,\infty\}$ has four points.
A rank-two $p$-adic Schottky group is a free discrete purely loxodromic
subgroup of $\mathrm{PGL}_2(K)$ on two generators, certified by the
non-archimedean ping-pong criterion: four pairwise-disjoint closed discs
$D_1^+,D_1^-,D_2^+,D_2^-$ with strict inclusions
$\gamma_i(\mathbf P^1\setminus D_i^-)\Subset D_i^+$ and
$\gamma_i^{-1}(\mathbf P^1\setminus D_i^+)\Subset D_i^-$ imply freeness,
discreteness, and a good fundamental domain
$\mathcal F=\mathbf P^1\setminus\bigcup$ (open discs).
The admitted target asks whether such a group exists over $\mathbf Q_3$
whose four attracting/repelling fixed points occupy four distinct residue
classes mod 3 (an integral-disc domain), in contrast to the published
Morrison–Ren pair whose discs $B(4,1/9),B(1,1/9),B(5,1/9),B(2,1/9)$ confine
every fixed point to the two classes $\{1,2\}$.

## Definitions

- $D_0=\{|z|_3\le 1/3\}$, $D_1=\{|z-1|_3\le 1/3\}$,
  $D_2=\{|z-2|_3\le 1/3\}$, $D_\infty=\{|z|_3\ge 3\}\cup\{\infty\}$:
  the four maximal residue discs, reducing to $0,1,2,\infty$ in
  $\mathbf P^1(\mathbf F_3)$.
- Multiplier: for $\gamma(z)=(az+b)/(cz+d)$ at a finite fixed point $z$,
  $m=\det\gamma/(cz+d)^2$; at $\infty$, $m=\det\gamma/a^2$ in the $w=1/z$
  chart. Attracting means $|m|_3<1$ ($v_3(m)>0$); repelling $|m|_3>1$.
- Pairing: $D_1^+=D_0$, $D_1^-=D_\infty$, $D_2^+=D_1$, $D_2^-=D_2$.

## Result

Let
$$\gamma_1=\begin{pmatrix}27&0\\0&1\end{pmatrix},\quad
  \varphi=\begin{pmatrix}2&1\\1&1\end{pmatrix},\quad
  \gamma_2=\varphi\gamma_1\varphi^{-1}
  =\begin{pmatrix}53&-52\\26&-25\end{pmatrix}\in\mathrm{GL}_2(\mathbf Q_3).$$
Then $\Gamma=\langle\gamma_1,\gamma_2\rangle$ is a rank-two Schottky group
over $\mathbf Q_3$, free on $\{\gamma_1,\gamma_2\}$, with good fundamental
domain on the four discs above. The fixed points are $0,\infty$ for
$\gamma_1$ and $1,2$ for $\gamma_2$, reducing to the four distinct classes
$0,\infty,1,2$ in $\mathbf P^1(\mathbf F_3)$. Multipliers are $27$ at $0$
and $1$ (attracting) and $1/27$ at $\infty$ and $2$ (repelling). This
answers the target affirmatively and attains maximal residue spread.

## Proof / evidence

Fixed points: $\gamma_1(z)=27z$ fixes $0,\infty$; direct evaluation gives
$\gamma_2(1)=(53-52)/(26-25)=1$ and $\gamma_2(2)=(106-52)/(52-25)=2$, and
conjugacy to $\gamma_1$ (trace 28, determinant 27) forces no others.
Disjointness: distinct finite centres differ by a $3$-adic unit
($|a-b|_3=1>1/3$), and $D_\infty$ lies outside the unit disc.
Ping-pong for $\gamma_1$: $\mathbf P^1\setminus D_1^-=\{|z|\le 1\}$ maps to
$\{|w|\le 1/27\}\Subset D_1^+$; $\mathbf P^1\setminus D_1^+=\{|z|\ge 1\}$
has preimage $\{|z|\ge 27\}\Subset D_1^-$.
Transfer: $\varphi(z)-1=z/(z+1)$ and $\varphi(z)-2=-1/(z+1)$ exactly, so for
$|z|_3\le 1/3$ ($|z+1|_3=1$) one gets $\varphi(D_1^+)=D_2^+$ onto, and for
$|z|_3\ge 3$ ($|z+1|_3=|z|_3$) one gets $\varphi(D_1^-)=D_2^-$ onto (both
directions via $\varphi(0)=1$, $\varphi(\infty)=2$ and $\det\varphi=1$).
Since $\gamma_2=\varphi\gamma_1\varphi^{-1}$ and $D_2^\pm=\varphi(D_1^\pm)$,
the strict inclusions transfer to $\gamma_2$. The complement
$\mathcal F$ is nonempty ($z=3$ has $|3|_3=1/3$, $|3-1|_3=|3-2|_3=1$),
so the standard criterion yields freeness of rank exactly two,
discreteness, and purely loxodromic action.
Machine certificate `output/artifacts/verify_schottky.py` (exact rational
arithmetic) re-checks conjugation, determinants/traces, fixed points,
multipliers and valuations, residue distinctness, disjointness, transfer
identities, and the witness, printing ALL CHECKS PASSED.

## Limitations

Existence only: no classification of such pairs, no minimality or
Hausdorff-dimension claims. The script samples representative rational
points for the transfer maps; full disc inclusions rest on the displayed
ultrametric valuation proof.

## Reproducibility

Run `python3 output/artifacts/verify_schottky.py` (no dependencies); all
identities are exact over $\mathbf Q$. The proof uses only ultrametric
valuation identities reproducible by hand.

## References

- L. Gerritzen, M. van der Put, Schottky Groups and Mumford Curves,
  Springer LNM 817 (1980) — non-archimedean Schottky criterion.
- R. Morrison, Q. Ren, Algorithms for Mumford curves, J. Symb. Comput. 68
  (2015) — good-generators algorithm; two-residue-class motivating pair.
- J. Poineau, D. Turchetti, Schottky spaces and universal Mumford curves
  (2022); R. Hidalgo, noded Schottky groups (2020) — related moduli theory.
