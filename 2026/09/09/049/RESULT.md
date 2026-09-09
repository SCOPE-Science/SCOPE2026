# Explicit conditional syndetic two-leg corner recurrence with control lemma and ergodic-uniform obstruction

## Context

Qualitative Furstenberg–Katznelson theory gives corner recurrence and
syndeticity with no explicit window. Recent sparse-corner convergence theory
(Frantzikinakis–Kuca), structural multi-correlation decompositions (Leng),
and finitary popular-difference theorems (Berger/Chu/Mandache) give no
explicit dense ergodic syndetic window for two-leg corner returns at the
popular constant. The admitted target of a uniform window over all
weak-mixing commuting systems with no rate is not achieved here and is
conjectured to fail; what is achieved is an exact conditional form plus an
unconditional obstruction.

## Definitions

Let $(X,\mu,S,T)$ be commuting measure-preserving transformations,
$f=1_A$, $\delta=\mu(A)>0$, and

$$c(m,n)=\int_X f\cdot S^m f\cdot T^n f\,d\mu
=\mu(A\cap S^{-m}A\cap T^{-n}A),$$
$$E_\tau=\{(m,n)\in\mathbb{Z}^2:c(m,n)\ge\tau\}.$$

For $N\ge 1$ and shifts $M,L\in\mathbb{Z}$ let

$$u_{N,M}=N^{-1}\sum_{m=M+1}^{M+N}S^m f,\quad
v_{N,L}=N^{-1}\sum_{n=L+1}^{L+N}T^n f,$$
$$A_{N;M,L}=N^{-2}\sum_{m=M+1}^{M+N}\sum_{n=L+1}^{L+N}c(m,n),$$
$$\alpha_{N,M}=\lVert u_{N,M}-\delta\rVert_2,\quad
\beta_{N,L}=\lVert v_{N,L}-\delta\rVert_2.$$

## Result

**T1 (shift-uniform control lemma).** For every $N\ge 1$ and all $M,L$,

$$|A_{N;M,L}-\delta^3|
\le \delta^{3/2}(\alpha_{N,M}+\beta_{N,L})
+\alpha_{N,M}\beta_{N,L}.$$

Shifted-block errors equal anchored ones:
$\alpha_{N,M}=\alpha_{N,0}$, $\beta_{N,L}=\beta_{N,0}$.

**T2 (mean limit, density, conditional window).**
Assume $S,T$ individually ergodic. Then:

- (i) $A_{N;M,L}\to\delta^3$ as $N\to\infty$, uniformly in $(M,L)$.
- (ii) For $\tau=\delta^3/2$ and $E=E_\tau$, every sufficiently large
  $N\times N$ block $B$ satisfies
  $|E\cap B|/|B|\ge \delta^2/(4-2\delta^2)\ge\delta^2/4$;
  hence $E$ meets every large block.
- (iii) If $\alpha_{N,0},\beta_{N,0}\le CN^{-\gamma}$ for some
  $C,\gamma>0$ and all $N$, then (ii) holds for every block of side
  $N\ge K(\delta):=(16C/\delta^{3/2})^{1/\gamma}$, so every
  $K(\delta)\times K(\delta)$ block of $\mathbb{Z}^2$ meets $E$.
  For $\gamma=1/2$, $K(\delta)\le 256C^2/\delta^3$.
  In particular, $L^2_0$ spectral gap (e.g. exponentially mixing) gives a
  polynomial window $K(\delta)=O_C(\delta^{-3})$.

**T3 (periodic obstruction).** Let $X_P=\mathbb{Z}/P\mathbb{Z}$ with
$P=2q$, $S=T=$ cyclic shift, $A=\{0,\dots,q-1\}$ so $\delta=1/2$ and
$\tau=\delta^3/2=1/16$. Then $E_\tau$ misses a square of side
$q-\lfloor 7q/8\rfloor\ge q/8-1=P/16-1\to\infty$ with $P$.
Hence no finite $K(1/2)$ works uniformly over all ergodic commuting pairs;
a mixing/rate hypothesis is necessary. The witnesses are rotations, hence
not weak-mixing, so the weak-mixing-uniform question is not decided.

## Proof / evidence

T1: $A_{N;M,L}=\int f\,u_{N,M}\,v_{N,L}$ exactly by measure preservation.
Write $f=\delta+g$, $u=\delta+a$, $v=\delta+b$; the three linear terms in
$\int(\delta+g)(\delta+a)(\delta+b)$ vanish, leaving
$A-\delta^3=\delta\int ga+\delta\int gb+\int fab$.
Since $\lVert g\rVert_2^2=\delta(1-\delta)\le\delta$,
Cauchy–Schwarz gives the first two bounds; $0\le f\le 1$ gives
$|\int fab|\le\lVert a\rVert_2\lVert b\rVert_2$.
Unitarity of $S^M,T^L$ fixing constants gives shift-uniformity.
T2: (i) follows from T1 and the von Neumann mean ergodic theorem.
(ii) uses $c(m,n)\le\delta$ so for block mean $\bar A$ and density $d$,
$\bar A\le d\delta+(1-d)\tau$, i.e. $d\ge(\bar A-\tau)/(\delta-\tau)$;
with $\bar A\ge 3\delta^3/4$ this yields the stated density.
(iii) inserts the rate into T1; $N^\gamma\ge 16C/\delta^{3/2}$ forces both
error terms $\le\delta^3/8$, hence $\bar A\ge 3\delta^3/4$ on every such
block. T3: for $0\le m\le q$, $|A\cap(A-m)|=q-m$ so
$c(m,n)\le(q-m)/P$; $m>7q/8$ gives $c<1/16$.

Computation is illustrative only: `artifacts/verify_corner.py` (stdlib)
checks (V1) inequality on anchored and shifted blocks including negative
shifts, (V2) the empty square for $q\in\{8,16,40,80,400\}$ (sides
1,2,5,10,50), (V3) density conversion; status `VERIFY_OK`.

## Limitations

- No uniform $K(\delta)$ over all weak-mixing systems with no rate is
  proved or disproved; no weak-mixing counterexample is constructed.
  Arbitrarily slow weak-mixing mean-ergodic rates are expected to break
  uniformity, but this remains a conjecture.
- $K(\delta)$ is conditional on an explicit $L^2$ rate $(C,\gamma)$;
  without a rate (e.g. spectral gap) it is not numeric.
- Qualitative syndeticity itself is classical Furstenberg–Katznelson;
  the contribution is the exact conditional quantitative form plus the
  obstruction witness. Host–Kra/Gowers machinery is not needed for the
  two-leg pattern (it would enter for 3-/4-point corners).

## Reproducibility

Run with stdlib Python only:

```
python3 artifacts/verify_corner.py
```

Expected output `VERIFY_OK` and `artifacts/verify_log.json` with V1/V2/V3
tables. All theorems replay from definitions above without external data.

## References

- Furstenberg–Katznelson multidimensional Szemerédi / corners recurrence
  (qualitative; no explicit window).
- N. Frantzikinakis, B. Kuca, Ergodic averages for sparse corners,
  arXiv:2510.27627.
- J. Leng, Structured extensions and multi-correlation sequences,
  arXiv:2504.07038.
- A. Berger, Popular Differences for Corners in Abelian Groups,
  arXiv:1909.12350.
