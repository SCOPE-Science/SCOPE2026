# First-order rigid-unfolding parity criterion and uniform forcing number 5 for the equiangular degree-8 vertex (A8)

## Context

The target asked for the finite continuous rigid forcing minimum of the regular equiangular degree-8 single-vertex crease pattern. En route, exhaustive Maekawa enumeration and exact symbolic linearization of the rigid closure at the flat state were completed first. This record reports that emergent, self-contained triple as an EMERGENT_FINDING, sharply separated from the unfinished finite-motion target.

## Definitions

Let A8 be the single-vertex pattern with 8 sectors each alpha=pi/4, creases 0..7 cyclically. Encode mountain-valley assignments as s in {+1,-1}^8. The Maekawa necessary condition is sum s_i = +-2 (5-3 or 3-5 splits). Define P = {s : sum = +-2} (Maekawa family); F = {s in P : s takes both signs on evens {0,2,4,6} and both signs on odds {1,3,5,7}} (parity-mixed subfamily); G = P \ F. The forcing number of mu over family H is the least k such that some k-subset S has nu|_S = mu|_S implying nu = mu for all nu in H.

## Result

(a) |P| = 112, in exactly 10 dihedral orbits with size multiset [8,8,8,8,8,8,16,16,16,16]. (b) Exact first-order rigid-unfolding criterion from the flat state: with fold angles rho_k = s_k*pi and unfolding speeds v_k > 0, the linearized closure J D_s v = 0 admits a strictly positive solution v iff s is mixed on evens and mixed on odds. Hence 96 patterns are first-order admittable (|F|=96) and 16 are obstructed (|G|=16). (c) The forcing number is uniformly 5 over P (all 112) and uniformly 5 over F (all 96). Example: mu0 = (-1,-1,-1,+1,+1,+1,+1,+1) is forced by S = {3,4,5,6,7} and by no 4-subset.

## Proof / evidence

(a) {+1,-1}^8 vectors with sum +2 have exactly three -1 entries: C(8,3)=56; sum -2 another 56; total 112. Dihedral canonical form (minimum over 8 rotations and 8 reflected rotations) gives 10 orbits with the asserted sizes; script asserts cardinality, distinctness, orbit count and size multiset. Counting mixed patterns gives |F|=96, |G|=16, asserted in-script.

(b) Closure C(rho) = prod_{k=0..7} Rz(alpha) Rx(rho_k), alpha=pi/4. At flat rho_k = s_k*pi, Rx = diag(1,-1,-1) =: D for both signs. Put Fmat = Rz(alpha) D; exactly Fmat^2 = I, hence Fmat^8 = I (sympy, no numerics). Tangent column j is ax((Fmat^j) Rz E (Fmat^{7-j})), E = dRx(+-pi)/drho. Exact evaluation gives even columns (t,t,0), t=sqrt(2)/2, and odd columns (1,0,0). With u = D_s v, J u = 0 reads sum_{evens} s_i v_i = 0 and sum_{odds} s_i v_i = 0 (y-row gives the even sum; x-row gives even plus odd sums). For a fixed 4-set, positive weights with zero signed sum exist iff both signs occur (weights 1/a on plus entries, 1/b on minus entries). Applying independently to evens and odds yields the mixed-parity criterion.

(c) Brute-force check of every mu and every k-subset in increasing k (C(8,k) subsets, early break at 2 matches) gives distributions {5:112} over P and {5:96} over F. Minimality is certified by exhaustive 4-subset distinguishers: for each of the C(8,4)=70 subsets S there is nu != mu agreeing on S.

## Limitations

First-order versus finite: (b) is a tangent-space result at flat; a positive first-order mode is necessary for a finite rigid branch with those signs but sufficiency and explicit finite branches are not proved. Flat-foldability: (a)-(c) use the Maekawa necessary condition (Kawasaki automatic for equiangular A8); global layer-ordering certificates are not exhibited, so P is an upper-bound family. Hence uniform 5 applies to P and F, not yet to the finite rigid-motion set.

## Reproducibility

python3 output/artifacts/enumerate_forcing.py — exact integer pass, prints |P|, orbits, |F|/|G|, forcing distributions, witness and distinguishers, ALL EXACT CHECKS PASSED. python3 output/artifacts/jacobian_parity.py — exact sympy pass, prints Fmat, Fmat^2-I, Fmat^8-I, Jacobian columns, parity system. Both exit 0.

## References

Abel et al., Rigid origami vertices: conditions and forcing sets, arXiv:1507.01644 (J. Comput. Geom. 2016) — finite bird's-foot condition and forcing bounds n-3..n; Ouchi-Uehara, Efficient enumeration of flat-foldable single vertex crease patterns, IEICE 2019, DOI 10.1587/transinf.2018fcp0004; Ouchi-Uehara, Minimum forcing sets for single-vertex crease pattern, 2020.
