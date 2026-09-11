# Shrinking-tube non-scarring for narrow torus quasimodes

## Context

Whether high-frequency modes on the flat torus can concentrate (scar) in
shrinking neighborhoods of closed geodesics is central to scarring,
restriction theory, observability, and damped-wave decay. Prior work —
Bourgain–Rudnick nodal and restriction characterizations via lattice
counts, Canzani–Galkowski geodesic-beam toolkits on general manifolds,
and superscar constructions for perturbed point scatterers — leaves open
a uniform shrinking-tube rate for narrow quasimodes of the unperturbed
Laplacian. The admitted target asked for a 7/8 limsup bound for
o(h^2) badly approximable (exponent-2) quasimodes in the h^{1/2} tube
around the horizontal geodesic.

## Definitions

Let T^2 = R^2/Z^2 with Lebesgue measure, e_k(x) = e^{2 pi i k.x},
k in Z^2, orthonormal basis. Semiclassical parameter h -> 0+.
Horizontal primitive geodesic gamma_0 = {x_2 = 0}.
Uncertainty-scale tube T_h = {dist(x,gamma_0) < h^{1/2}}.
For h < 1/4 the x_2-slice is I_h = [0,d) union (1-d,1], d = h^{1/2},
of measure 2 h^{1/2}. Quasimodes u_h are L^2-normalized with
r_h := ||(-h^2 Delta - 1) u_h|| = o(h^2). The badly approximable
exponent-2 cone subclass is the admitted Diophantine class.

## Result (headline)

Every L^2-normalized sequence u_h on T^2 with residual o(h^2) satisfies

  int_{T_h} |u_h|^2 dx -> 0 as h -> 0.

Hence for the badly approximable exponent-2 cone subclass,
limsup_{h->0} int_{T_h} |u_h|^2 = 0 <= 7/8: no admissible Diophantine
quasimode scars more than 7/8 inside the uncertainty-scale tube.
The proved limit is stronger than the 7/8 threshold and needs no
Diophantine hypothesis; the Diophantine case follows as a corollary.
Single-shell tube bound: M(v) <= 4 h^{1/2} ||v||^2; total bound
<= 8 h^{1/2} ||v||^2 + 2 ||w||^2 -> 0.

## Proof / evidence

Write u_h = sum_k c_k e_k, m_N = sum_{|k|^2=N} |c_k|^2,
R^2 = 1/(4 pi^2 h^2). By the spectral theorem,
r_h^2 = sum_N (4 pi^2 h^2)^2 |N - R^2|^2 m_N, i.e.
sum_N |N - R^2|^2 m_N = eta_h := r_h^2/(4 pi^2 h^2)^2 -> 0
since r_h/h^2 -> 0. The o(h^2) width is sub-spacing (shell gap
4 pi^2 h^2), forcing single-shell concentration. Let N_* minimize
|N - R^2|. Every other integer has |N - R^2| >= 1/2 (tie-safe).
With v the N_*-shell projection and w = u_h - v,
||w||^2 = sum_{N != N_*} m_N <= 4 eta_h -> 0.

Write v(x) = sum_{|k|^2=N_*} a_k e_k and group by k_1:
v(x_1,x_2) = sum_{k_1} e^{2 pi i k_1 x_1} g_{k_1}(x_2),
g_{k_1}(x_2) = sum_{k_2: k_1^2+k_2^2=N_*} a_k e^{2 pi i k_2 x_2}.
For fixed k_1, k_2 = +-sqrt(N_* - k_1^2): at most J <= 2 terms
(exact lattice geometry, not a divisor estimate). By Parseval in x_1
then Cauchy-Schwarz, int_{T_h} |v|^2 = sum_{k_1} int_{I_h} |g_{k_1}|^2
<= |I_h| sum J_{k_1} (shell mass at k_1) <= (2 h^{1/2})(2) ||v||^2
= 4 h^{1/2} ||v||^2 -> 0. Finally |u_h|^2 <= 2|v|^2 + 2|w|^2 gives
int_{T_h} |u_h|^2 <= 8 h^{1/2} ||v||^2 + 2 ||w||^2 -> 0. QED.

Computational replay output/artifacts/verify_tube_bound.py (ALL CHECKS
PASS): thin-window shell uniqueness at 8 h values; fiber counts <= 2
over 232 spectral/random cases; analytic decay table; 9 random
single-shell eigenfunctions (N = 65, 325, 4225) with tube masses
0.10–0.32 consistent with <= 4 sqrt(h).

## Limitations

Specific to the flat square torus Fourier basis and the h^{1/2} tube
around a coordinate geodesic; gives no rates for wider O(h)
quasimodes (e.g. Gaussian x_2-width ~h^{1/2} beams correctly excluded
since their spread is ~h), perturbed operators, or non-flat
geometries. The badly approximable hypothesis is sufficient but not
needed for this threshold.

## Reproducibility

DRAFT.md contains the full self-contained proof. Running
python3 output/artifacts/verify_tube_bound.py with the Python
standard library reproduces all checks. No external data needed.

## References

- Bourgain–Rudnick, Restriction of toral eigenfunctions to
  hypersurfaces and nodal sets (2012), arxiv:1105.0018.
- Bourgain–Rudnick, On the nodal sets of toral eigenfunctions,
  Invent. Math. (2011).
- Canzani–Galkowski, Eigenfunction concentration via geodesic beams,
  arxiv:1903.08461v3.
- Kurlberg–Lester–Rosenzweig, Superscars for arithmetic point
  scatters II, Forum Math. Sigma 11 (2023).
- Hezari–Rivière / Bourgain–Jakobson / Sogge–Zelditch torus
  restriction and quantum-chaos surveys (background).
