# Certified interior-vs-contracted-boundary spectral gap for the cube Q3

## Context

For a fixed discrete graph topology $G$, Band–Levy (*Quantum graphs which
optimize the spectral gap*, Ann. Henri Poincaré 2017, arXiv:1608.00520)
pose the per-topology maximizer/supremizer program: optimize the spectral
gap $k_1$ over the length space $L(G)$ at fixed total length and decide
whether optimizers lie in the interior (maximizers) or on the
contracted-boundary strata (where edges shrink to length zero).
Maximization is solved only for stars/flowers/stowers/mandarins; the cube
$Q_3$ is left open. The generic $L,E$-only bound (Kennedy et al.)
$k_1 \le \pi E/L$ cannot separate per-topology points. This record decides
one interior-vs-boundary stratum for $Q_3$: the equilateral interior point
versus the center of the canonical single-edge-contraction boundary
stratum, as reusable stratum-elimination lemma.

## Definitions

- $\Gamma_{\mathrm{eq}}$: equilateral metric cube $Q_3$ at total length
  $L=1$ (12 edges of length $\ell_{\mathrm{eq}}=1/12$) with Kirchhoff
  (Neumann) vertex conditions.
- $\Gamma_{\mathrm{con}}$: single-edge-contracted cube at $L=1$: contract
  one edge of $Q_3$ (all edges equivalent under $\mathrm{Aut}(Q_3)$);
  remaining 11 edges equilateral at $\ell_{\mathrm{con}}=1/11$, Kirchhoff
  conditions. Committed edge list (merged vertex $0$ of degree 4):
  $01,02,03,04,12,25,16,34,45,56,63$; degree sequence $[3^6,4]$.
- $k_1$: square root of the first nonzero Kirchhoff eigenvalue
  ($\lambda_1 = k_1^2$).
- $P = D^{-1}A$: random-walk transition matrix of the discrete graph.
- $\theta = \arccos(1/3) \in (L,U)$ with
  $L = 123095938/10^8 = 1.23095938$,
  $U = 123095946/10^8 = 1.23095946$.

## Result

$$k_1(\Gamma_{\mathrm{eq}}) \in [a,b], \qquad
  k_1(\Gamma_{\mathrm{con}}) \in [c,d]$$

with exact rational endpoints

$$[a,b]=\left[\frac{184643907}{12500000},\frac{184643919}{12500000}\right]
  \approx [14.77151256,\,14.77151352],$$
$$[c,d]=\left[\frac{677027659}{50000000},\frac{677027703}{50000000}\right]
  \approx [13.54055318,\,13.54055406],$$

widths $b-a = 9.6\times 10^{-7} \le 10^{-6}$,
$d-c = 8.8\times 10^{-7} \le 10^{-6}$, each interval containing exactly
the $k_1$ root of its secular equation and no smaller positive root, and
disjointness $a - d = 2461917/2000000 \approx 1.23096 > 0$. In particular
$k_1(\Gamma_{\mathrm{eq}}) > k_1(\Gamma_{\mathrm{con}})$ with certified
margin $> 1.23$.

In closed form: $k_1(\Gamma_{\mathrm{eq}})=12\theta$ and
$k_1(\Gamma_{\mathrm{con}})=11\theta$, with $[a,b]=12[L,U]$,
$[c,d]=11[L,U]$.

## Proof / evidence

1. **Equilateral reduction (von Below, self-contained).** For an
   equilateral graph with edge length $\ell$ and $k>0$,
   $\sin(k\ell)\ne 0$: $k^2$ is a Kirchhoff eigenvalue iff
   $\mu=\cos(k\ell) \in \mathrm{spec}(P)$; otherwise $k = n\pi/\ell$
   (vertex-vanishing branch).
2. **Cube spectrum.** $Z_2^3$ characters
   $\chi_a(x)=(-1)^{a\cdot x}$ give
   $\mathrm{spec}(A)=\{3,1^3,(-1)^3,-3\}$, so $\mathrm{spec}(P)$ has
   Perron value $1$ (simple) and second value $1/3$ (multiplicity 3).
   All identities are exact integer checks.
3. **Contracted spectrum.** For $B = 12P_{\mathrm{con}}$ (integer
   $7\times 7$ matrix),
   $$\det(yI-B)=(y-12)(y-4)(y+4)(y^2+4y-16)(y^2+8y-16),$$
   proved by exact integer Bareiss elimination: both sides monic of
   degree 7 agreeing at 8 distinct integers $y=-3,\dots,4$. Exact root
   ordering gives largest eigenvalue $12$ (simple), second $4$ (simple),
   i.e. $\mathrm{spec}(P_{\mathrm{con}})$ has second value $4/12=1/3$.
   The committed 11-edge list is isomorphic to an actual one-edge
   contraction of $Q_3$ (verified by explicit permutation).
4. **Theta enclosure.** Taylor order $N=10$ about $0$ in exact
   `Fraction` arithmetic; since $U^2<6$ the cosine series terms decrease
   for $n\ge 1$, so the Leibniz bound $|{\cos x - S_{10}(x)}|\le
   x^{22}/22!$ applies. This yields $\cos L > 1/3 > \cos U$ plus
   $\cos U > 1/4$ and $U < 3.14 < \pi$; cosine decreasing on
   $(0,\pi)$ gives unique $\theta=\arccos(1/3)\in(L,U)$ of width
   $8\times 10^{-8}$.
5. **Exclusion and uniqueness.** No eigenvalue below $a$ (resp. $c$):
   cos-branch impossible since $k\ell \le L < \pi$ forces
   $\cos(k\ell) \ge \cos L > 1/3$; vertex branch starts at
   $\pi/\ell = 12\pi$ (resp. $11\pi$) far above. Next-branch exclusion:
   cube next value $\mu=-1/3$ lifts above $b$ since
   $\pi - U > U$; contracted next values $\le 1/4 < \cos U$ (via
   $20<25$, $32<49$) lift above $d$. Hence $12\theta$ (resp.
   $11\theta$) is the least positive eigenvalue, unique in its
   interval.
6. **Assembly.** $[a,b]=12[L,U]$, $[c,d]=11[L,U]$; widths and exact
   rational disjointness $a>d$ as above.
7. **Replay.** `python3 output/artifacts/verify_fallback.py` prints
   `VERIFY_OK` using only the standard library (`fractions`, `math`).

## Limitations

- Only the two equilateral points and their comparison are certified.
- The full D4 rung-vs-ring section unique-maximizer target ($t^*=1/3$
  over $t\in(0,1)$ via Hadamard energies) is NOT proved here; the
  six-sector secular analysis remains a conjecture outline.
- No other boundary strata and no non-equilateral section points are
  decided.
- $k_1 = \sqrt{\lambda_1}$ with Kirchhoff conditions at $L=1$; other
  normalizations must rescale.

## Reproducibility

Run `python3 output/artifacts/verify_fallback.py` (stdlib only) and
expect `VERIFY_OK`. Independent cross-checks: sympy confirms the
contracted charpoly factorization; float check
$\arccos(1/3)=1.2309594173\ldots \in (L,U)$.

## References

- R. Band, G. Lévy, Quantum graphs which optimize the spectral gap,
  Ann. Henri Poincaré 2017. https://arxiv.org/abs/1608.00520
- J. B. Kennedy, P. Kurasov, G. Malenová, D. Mugnolo, On the spectral
  gap of a quantum graph. https://doi.org/10.1007/s00023-016-0460-2
- J. von Below, Sturm–Liouville eigenvalue problems on networks (1988).
  https://doi.org/10.1002/mma.1670100404
- J. Harrison, T. Weyand, Spectral determinants of almost equilateral
  quantum graphs (2025). https://doi.org/10.1007/s13324-025-01070-w
