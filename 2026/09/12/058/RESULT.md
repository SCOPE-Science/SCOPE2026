# Disproof of the uniform 1/n local Gibbs rate inside the gaseous facet

## Context

Random domino tilings of the Aztec diamond with 2-periodic weights exhibit three
macroscopic phases — solid (frozen), liquid (rough/disordered), and gas
(smooth/gaseous) — separated by an arctic-type limit shape. A central question
is how fast finite-domain pattern probabilities converge to infinite-volume
ergodic Gibbs values. The admitted target asked for a proof or disproof of a
uniform O(1/n) local-limit rate inside the central gaseous facet with a
slope-only comparator: sup over faces x_n in a scaled compact sub-disc nF of
|P_n(E;x_n) − P_infty(E;s(x_n/n))| ≤ C(E,a,F)/n.

## Definitions

- A_n: order-n Aztec diamond with fixed 2-periodic weights (1,a), 0<a<1 fixed;
  representative symmetric weighting W*: horizontal edge in column x has weight
  1 (x even) or a (x odd), vertical edge in row y likewise.
- F: fixed compact sub-disc strictly inside the central smooth (gaseous) facet.
- E: fixed finite connected face-pattern event; the headline witness is a
  single-edge occupation event.
- P_n(E;x_n): probability of E at face x_n under the finite-domain Boltzmann
  dimer measure.
- P_infty(E;s): probability of E under the infinite-volume ergodic Gibbs
  measure of slope s equal to the limit-shape gradient at the scaled location.
- Kasteleyn symbol on |z|=|w|=1: K(z,w)=[[1+az, i(1+aw^{-1})],[i(1+aw),
  1+az^{-1}]], P(z,w)=det K=|1+az|^2+|1+aw|^2=2(1+a^2)+2a(cosθ+cosφ).
- Torus expectations: U=E[1/P], C=E[cosθ/P]; weight-1 horizontal edge value
  p_1=U+aC; weight-a horizontal edge value p_a=aC+a^2U.

## Result

The claimed uniform O(1/n) rate is FALSE. At a=1/2 with E a single-edge event,
the two sublattice-parity classes converge inside the central gaseous facet to
distinct smooth-phase Gibbs values p_1 and p_a with exact gap
p_1−p_a=(1−a^2)E[1/P]≥0.30, so any slope-only (parity-blind) comparator q_0
misses one parity class by at least 0.15 along central sequences in nF. Hence
sup_{x_n in nF}|P_n(E;x_n)−P_infty(E;s(x_n/n))|≥0.1 eventually, contradicting
the C/n bound and indeed contradicting convergence itself to the stated limit.
The general identity holds for all 0<a<1; a=1/2 is a representative instance.

## Proof / Evidence

1. Gas certification: for 0<a<1, P≥2(1−a)^2>0 on the unit torus (at a=1/2,
   min P=0.5, mean E[P]=2.5), so B=0 lies in a bounded amoeba complement: the
   smooth/gaseous phase. Diagonal-reflection symmetry puts B=0 at the Aztec
   centre; for a≠1 the centre lies in the gaseous facet (Chhita–Johansson).
2. Exact parity gap: Kenyon's periodic Gibbs Fourier formula gives
   p_1=U+aC, p_a=aC+a^2U, hence p_1−p_a=(1−a^2)U with U>0. Jensen gives
   U≥1/E[P]=1/[2(1+a^2)], so p_1−p_a≥(1−a^2)/[2(1+a^2)]; at a=1/2 this is 0.30
   with no numerics required.
3. Corroborating quadrature (certificate only): midpoint rule at 400^2 and
   1600^2 grids agreeing to 8 digits gives U≈0.5081, p_1≈0.4405, p_a≈0.0595,
   gap≈0.381, with sum rules E[P/P]=2(1+a^2)U+4aC=1 and 2p_1+2p_a=1 verified.
4. Facet collapse: the height function is affine on the smooth facet (Ronkin
   linear on bounded amoeba components), so the slope map is constant s≡s_0 on
   F and the comparator is a single number q_0 for all x_n in nF.
5. Two-sequence contradiction: nF contains central faces of both parities;
   finite-size local convergence in the smooth region (Chhita–Johansson,
   gas-region inverse-Kasteleyn convergence to the periodic smooth kernel)
   gives P_n(even)→p_1, P_n(odd)→p_a. For any fixed q_0,
   max(|p_1−q_0|,|p_a−q_0|)≥(p_1−p_a)/2≥0.15, so sup-error ≥0.15−o(1)≥0.1.
   A parity-aware comparator could restore convergence but is a different claim.

## Limitations

The finite-n convergence step (central faces of both parities converge to the
periodic smooth-phase Gibbs values; centre gaseous for a≠1; facet slope
constant) is imported from published theorems (Chhita–Johansson local
convergence; Kenyon–Okounkov–Sheffield amoeba/Ronkin theory) rather than
re-proved. The disproof refutes the parity-blind formulation; it does not rule
out a parity-aware O(1/n) rate, which was not posed.

## Reproducibility

Run output/artifacts/compute_gap.py (numpy) to regenerate
output/artifacts/gap_numbers.json: checks Pmin, U, C, p_1, p_a, gap identity,
Jensen lower bound 0.3, and grid independence. All analytic bounds are
hand-verifiable from the formulas above.

## References

- Kenyon–Okounkov–Sheffield, Dimers and amoebae, Ann. Math. 2006.
- Kenyon, Lectures on dimers (Fourier formula for K^{-1} edge probabilities).
- Chhita–Johansson, Domino statistics of the two-periodic Aztec diamond,
  Adv. Math. 2016.
- Cerf–Kenyon; Sheffield, Random surfaces (facets = constant slope).
