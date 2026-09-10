# No diameter-pinned Grove–Shiohama transition in the join-edge family J_a = S^2 * S^1_a: constant diameter, radius kink, and collapse profile

## Context

The admitted target asked for a sharp diameter-rigidity phase transition in the
one-parameter family J_a = S^2(1) *_s S^1_a (metric spherical join), at a
parameter a_c in (0,2pi) defined implicitly by diam(J_a) = pi/2 (the sharp
Grove–Shiohama constant), with rigidity (R) for a > a_c via a regular-point
(4,delta<=0.01) strainer plus Bishop–Gromov volume forcing through the
Grove–Shiohama/Perelman-stability step, versus a uniform edge obstruction (E)
(no (4,delta<=0.05) strainer on the singular S^2 edge) for a <= a_c via a new
strainer-radius-vs-cone-angle estimate Phi(a). The preset fallback was the (E)
obstruction at J_{a_c}.

Target work on audit-plan item (2) — continuity plus strict monotonicity of
diam(J_a) — from the spherical-join cosine formula instead refuted the premise:
diam is identically pi. This audit certifies the resulting emergent finding:
the diameter-keyed transition is ill-posed, plus the exact metric profile of
J_a explaining which functional was constant vs kinked.

## Definitions

- X = S^2(1): compact Alexandrov, curv >= 1, dim 2, diam pi.
- Y_a = circle of length a, a in (0,2pi]: compact Alexandrov, curv >= 1
  (1-dimensional comparison: length <= 2pi), dim 1, diam a/2 <= pi.
  The length reading is forced: a radius reading (length 2pi*a) would violate
  curv >= 1 and diam <= pi over (1,2pi], contradicting the closed curv >= 1
  join setup.
- J_a = metric spherical join X *_s Y_a with, for p_i = (x_i,y_i,t_i),
  t_i in [0,pi/2]:
  (J) cos d(p1,p2) = cos t1 cos t2 cos d_X(x1,x2)
                     + sin t1 sin t2 cos d_Y(y1,y2).
  Standard AKP/Rong–Wang/BGP spherical-join metric. The join of curv >= 1
  factors with diam <= pi is compact Alexandrov, curv >= 1, dim 2+1+1 = 4,
  diam <= pi. For a < 2pi the t = 0 slice is a singular S^2 edge with
  Sigma_p J_a = S^1(1) * S^1_a and tangent K_p = R^2 x C(S^1_a)
  (join-direction theorem).

## Result

For J_a as above, a in (0,2pi]:

1. (Constant diameter; no a_c.) diam(J_a) = pi for every a. In particular the
   equation diam(J_a) = pi/2 has no solution in (0,2pi], f(a) := diam(J_a) is
   constant (hence continuous but nowhere strictly monotone), and no
   (R)-vs-(E) dichotomy keyed to "a > a_c vs a <= a_c" can be posed as written.
   The predefined fallback object J_{a_c} is likewise undefined.
2. (Exact eccentricity and radius.) By join symmetry eccentricity depends only
   on t. With c = cos(a/2): (i) for a <= pi, ecc(t) = pi - t; (ii) for a > pi,
   ecc(t) = acos(-sqrt(cos^2 t + c^2 sin^2 t)). Consequently diam = ecc(0) = pi
   for all a, and radius r(a) = min_t ecc(t) = ecc(pi/2) = max(pi/2, a/2),
   with the sole kink at a = pi.
3. (Volume collapse.) vol(J_a) = 4pi*a/3; ratio to vol(S^4(1)) = 8pi^2/3 is
   a/2pi; equals the round volume at a = 2pi and tends to 0 as a -> 0. Hence
   small-a members are collapsed and cannot be GH-close to S^4(1).
4. (Edge link.) At S^2-edge points Sigma_p = S^1 * S^1_a,
   vol(Sigma_p) = pi*a, volume density theta(p) = vol(Sigma_p)/vol(S^3(1))
   = a/2pi (equality to 1 iff a = 2pi, i.e. regular), diam(Sigma_p) = pi for
   all a.
5. (Topology.) Every J_a is homeomorphic to S^4 (metric join topology =
   topological join; S^2 * S^1 ~= S^4). Edge points are metrically singular
   yet topologically regular for a < 2pi. Hence the bare conclusion
   J_a ~= S^4 holds uniformly with no threshold; any valid diameter-to-sphere
   implication (diam > pi/2) applies uniformly since diam = pi always.

## Proof / evidence

- Factor embeddings: t1 = t2 = 0 in (J) gives cos d = cos d_X; t1 = t2 = pi/2
  gives cos d = cos d_Y; t1 = 0, t2 = pi/2 gives cos d = 0, i.e. d = pi/2.
  Slice maps are isometric embeddings at mutual distance pi/2.
- Diameter lower bound: antipodal x1,x2 in S^2 with d_X = pi at t1 = t2 = 0
  gives cos d = cos pi = -1, so d = pi; diam >= pi. The t = 0 antipodal pair
  is well defined (Y collapses at t = 0).
- Diameter upper bound: cos t_i, sin t_i >= 0 on [0,pi/2] and
  cos d_X, cos d_Y >= -1, so
  cos d(p1,p2) >= -cos t1 cos t2 - sin t1 sin t2 = -cos(t1-t2) >= -1,
  hence d <= pi; diam <= pi. Combining gives diam = pi identically.
- Eccentricity: maximize d over (t',dx,dy), i.e. minimize
  C = cos t cos t' cos dx + sin t sin t' cos dy with dx in [0,pi],
  dy in [0,a/2]. dx contributes -cos t cos t'. dy contributes
  c sin t sin t' with c = cos(a/2) = min cos dy. For a <= pi (c >= 0),
  dC/dt' = cos t sin t' + c sin t cos t' >= 0 so minimum at t' = 0,
  ecc = pi - t. For a > pi (c < 0), tan t'* = -c tan t gives
  min C = -sqrt(cos^2 t + c^2 sin^2 t); radius min over t at t = pi/2
  with value a/2. Full derivation in output/artifacts/ecc_profile.md.
- Volumes from join densities: vol(J_a) = vol(S^2)*a*int_0^{pi/2}cos^2t sin t dt
  = 4pi*a/3 (integral 1/3); vol(Sigma_p) = 2pi*a*int_0^{pi/2}cos t sin t dt
  = pi*a (integral 1/2). Round endpoints confirm normalization:
  J_{2pi} = S^4(1) volume 8pi^2/3; Sigma_{2pi} = S^3(1) volume 2pi^2.
- Cited Alexandrov stability/join/direction/topology theorems used only in
  standard qualitative form; all quantitative identities proved from (J).
- Computed consistency checks: seven stdlib-only scripts replay via
  output/artifacts/replay_all.py (exit 0, REPLAY_ALL PASS): factor isometry
  exact (err 0.0), antipodal distance pi, grid maxima <= pi, link-volume
  integral err ~1e-13, volume ratio a/2pi, radius formula to 1e-3.

## Limitations

Proved from (J) plus replay scripts: constant-diameter lemma, eccentricity/
radius profile, volume/link/topology identities, and negative corollaries
((R) route redundant for topology and insufficient for metric closeness;
(E) operative parameter is cone angle a vs 2pi, not diameter pi/2; regular vs
edge loci compatible at same a). A retracted packing-count attempt
(Bishop–Gromov sign error) is documented and not cited. NOT proved:
explicit-modulus Phi(a) bound with delta0 = 0.05 exclusion (candidate
Phi(a) >= pi - a/2 sketched only; eps-modulus missing). No numeric a_c
claimed (none exists). Originality claimed only for the assembled
no-transition verdict plus exact J_a profile, not for cited general theorems.

## Reproducibility

Run: python3 output/artifacts/replay_all.py (stdlib only; asserts all pass).
Key scripts: check_join_diameter.py (antipodal pi, grid max <= pi),
check_factor_isometry.py, check_link_volume.py, check_link_diameter.py,
check_volume_collapse.py, check_radius_and_topology.py, check_eccentricity.py.
Proof notes: constant_diameter_lemma_full.md, ecc_profile.md,
normalization_check.md.

## References (tools used, not results claimed)

Perelman/Kapovitch stability; Mitsuishi–Yamaguchi good coverings;
Hebda–Ikeda comparison/sphere criterion; Alexander–Kapovitch–Petrunin
foundations (joins, directions, cones); Rong–Wang join/quotient results;
Burago–Gromov–Perelman strainer/critical-point theory.
