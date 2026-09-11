# 96-packet bush-plus-planks sharpness obstruction on a fixed C2-perturbed cone at R0 = 4096

## Context

Sharp l2-decoupling for the 3D light cone (Bourgain–Demeter) and its stability
under curvature perturbation feed Strichartz estimates on manifolds, cone
local smoothing, eigenfunction bounds, and Kakeya-compression models. The
subcritical window p = 4 is where cone degeneracy and Kakeya bunching compete.
The admitted program asked for a one-cell decision at a fixed perturbed profile:
either a quantified epsilon-gain over the round-cone bound via a degree ≤ 4
polynomial-partition transverse count, or an explicit wave-packet family
attaining the old exponent and blocking improvement. Target work showed the
gain route is structurally blocked (fully concurrent wall-capturable bush core
coexists with a clean transverse shell), and delivered the exact preset
fallback: an explicit 96-packet obstruction certificate.

## Definitions

- Perturbed cone (chi = 1 on [3/4, 5/4]):
  Gamma_* = {(r cos theta, r sin theta, r + eps0 r chi(r) cos 3theta)} ,
  r in [1/2, 2], eps0 = 0.01.
- Scale R0 = 4096, tube radius r = R0^{1/2} = 64, ball B_{R0} in R^3,
  N = 64 canonical plates of angular width R0^{-1/2} = 1/64 at
  theta_j = 2pi j/64.
- Perturbed ruling normal at plate j (verified dr x dtheta direction):
  n_j propto (-cos theta_j - eps0(cos theta_j cos 3theta_j
    + 3 sin theta_j sin 3theta_j),
    -sin theta_j + eps0(-sin theta_j cos 3theta_j
    + 3 cos theta_j sin 3theta_j), 1), normalized to unit length.
- Weight w(x) = (1 + |x|/R0)^{-100}: w <= 1 everywhere, w ~= 1 on B_{R0}.
- Tube envelope for axis {o + t n}:
  W_T(x) = exp(-d(x,axis_T)^2/(2r^2)) exp(-s(x)^2/(2R0^2)),
  d = transverse distance, s = longitudinal coordinate
  (Schwartz envelope adapted to R0 x r x r tube).
- Family F_*: 32 bush tubes (even plates j = 0,2,...,62, axis through origin
  along n_j) + 64 planks (every plate j, axis {o_j + t n_j} with
  o_j = 512 u_j, u_j perp n_j unit, |o_j| = 512); all amplitudes +1.
  Same-plate bush/plank axes are parallel, 512 apart.
- W_* = sum_{T in F_*} W_T; W_{*,theta} = per-plate sub-sum.
- Ratio R_* = ||W_*||_{L^4(B_{R0})}^4 / sum_theta ||W_{*,theta}||_{L^4(w)}^4.
- Reference K0 = 16 (conservative; identical eps-independent ledger at eps = 0
  attains >= 17.2, in fact >= 138).

## Result

The explicit 96-packet family F_* above satisfies

  R_* >= 138.4 >= 8 = K0/2,

a binary PASS of the admitted exact success criterion. Hence the old
round-cone exponent level is attained on the perturbed cone at this cell: no
epsilon-improvement of the l2-decoupling constant at p = 4 on this cell is
possible against this packet class (sharpness obstruction, not an upper bound).

## Proof / evidence (auditable ledger + replay)

Numerator (core ball B(0,32)): each bush tube gives
W_T >= exp(-32^2/(2·64^2))·exp(-(32/4096)^2/2) =: c0 ≈ 0.88247;
planks >= 0. So W_* >= 32·c0 ≈ 28.239 on B(0,32). With
wmin_core = (1+32/4096)^{-100} ≈ 0.459225 (conservative factor),
NUM_LB = (4/3)pi(32)^3 · 0.459225 · (32·c0)^4 ≈ 4.008e10.

Denominator (integrated against w over all R^3, hence valid over B_{R0}):
transverse ∫W_T^4 = pi r^2/2 exact Gaussian; longitudinal w-integral along ANY
line ≤ ∫_R (1+|t|/R0)^{-100} dt = 2R0/99 ≈ 82.7475, since for x = o + s·n + y
with o,y perp n, |x|^2 = s^2 + |o+y|^2 >= s^2 (covers both o = 0 bushes and
|o| = 512 planks). One tube ≤ (pi r^2/2)(2R0/99) ≈ 5.324e5 =: T_{w,ub},
dominated by stated loose pi·R0·r^2 ≈ 5.27e7. Two-tube (even) plates use
(a+b)^4 ≤ 8(a^4+b^4); same-plate cross terms additionally carry exp(-24)
suppression (min of 3da^2+db^2 = 196608 at da=128,db=384 over 2r^2 = 8192,
given parallel axes 512 apart; recorded second ledger ~152 over |B_{R0}|).
Hence sum ≤ 32·16·T_{w,ub} + 32·T_{w,ub} =: DEN_UB ≈ 2.896e8.

Ratio: R_* >= NUM_LB / DEN_UB ≈ 138.40 >= 8 = K0/2. PASS with factor ~17.

Replay: `python3 output/artifacts/certify_fallback.py` → VERIFY_OK
(packets 96 = 32 bush + 64 planks; core-cube overlap 32 bush + 0 planks;
R_LB = 138.3983). Packet geometry independently re-derived (dr x dtheta =
draft normal formula to 1e-15; all plank offsets verified perpendicular,
|o| = 512). Supporting counts: x-axis 64-cube incidence log (core 32+0,
max total 64) and full-ball 64-grid histogram (1,099,136 voxels in B_{R0};
max bush 32, max total 64); `verify_overlaps.py` → VERIFY_OK
(S1 = 331.410681, nearest-neighbour angle 0.063563 rad, shell proxy
7.87 → 0.49, Mmax = 64).

## Limitations

Single-scale certificate at R0 = 4096 with Schwartz tube-envelope packet
model; proves sharpness obstruction (blocks epsilon-gain against this packet
class), not a decoupling upper bound and not a transfer to true Helmholtz
extension extremals. K0 = 16 is a recorded conservative reference certified by
the identical eps-independent ledger at eps = 0, stated explicitly rather than
imported. Full-ball histogram is corroborating (no committed generator);
the ratio PASS depends only on the proved ledger plus replayed packet table
and x-axis incidence log.

## Reproducibility

- `output/artifacts/certify_fallback.py` (stdlib only): builds normals,
  offsets, packet_table.csv, incidence_log.csv; asserts 96 rows, perpendicular
  512 offsets, core 32+0; prints full ledger; ends VERIFY_OK.
- `output/artifacts/verify_overlaps.py` (stdlib + numpy): perturbed normals,
  S1, nearest-neighbour angle, transverse-shell profile, Mmax; ends VERIFY_OK.
- Data: `output/artifacts/fallback_packets/packet_table.csv` (96 rows:
  id,kind,plate,nx,ny,nz,ox,oy,oz,amp),
  `incidence_log.csv` (127 x-axis 64-cubes),
  `overlap_histogram.csv` (full-ball 64-grid histogram).

## References

- J. Bourgain, C. Demeter, The proof of the l2 Decoupling Conjecture,
  Ann. of Math. 182 (2015).
  https://annals.math.princeton.edu/wp-content/uploads/annals-v182-n1-p09-p.pdf
- J. Bourgain, C. Demeter, D. Kemp, Decouplings for Real Analytic Surfaces of
  Revolution, arXiv:1908.07053 (upper-bound direction; perturbed cone as
  example class; no packet table or ratio log).
- C. Demeter, Decouplings and applications (ICM survey).
  https://www.math.uni-bonn.de/ag/ana/WiSe1819/geo-harmonic/ICM-Demeter.pdf
- Target-exit transverse-vs-wall separation lemma: S1 = 331.410681,
  shell proxy 7.87 (rho=256) → 0.49 (rho=4096), Mmax = 64 bush concurrency
  (replayed by verify_overlaps.py).
