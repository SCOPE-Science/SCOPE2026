# Emptiness of the first sub-174/55 homogeneous 10-point system L(136;43^10)

## Context

The Segre-Harbourne-Gimigliano-Hirschowitz (SHGH) / Nagata interpolation
problem for 10 general points in P^2 is open in the strip

  sqrt(10) < d/m < 174/55.

Ciliberto-Miranda (arXiv:0812.0032) prove expected dimension for
homogeneous 10-point systems only at or above d/m = 174/55.
Dumnicki (math/0606716) proves the homogeneous Harbourne-Hirschowitz
statement only for multiplicity m <= 42. Petrakiev (arXiv:1211.6380)
proves emptiness only for d/m < 2280/721 = 3.1622746, just below
sqrt(10). At the minimal new multiplicity m = 43, degree d = 136 is the
unique integer in the open strip (43*sqrt(10) = 135.978 < 136 < 136.036
= 43*174/55). Hence L(136;43^10) is the canonical first undecided
homogeneous cell below the proved slope.

## Definitions

Let X be the blowup of P^2 at 10 general points. L(d;m^10) denotes plane
curves of degree d with multiplicity >= m at each point.
Virtual dimension: vdim = C(d+2,2) - 1 - 10*C(m+1,2).
Here d = 136, m = 43: h^0(P^2,O(136)) = C(138,2) = 9453,
conditions per point C(44,2) = 946, total 9460, vdim = 9452 - 9460 = -8.
D = 136H - 43(E_1+...+E_10); D^2 = 6, D.K_X = 22,
chi(O_X(D)) = (6-22)/2 + 1 = -7 = vdim + 1.

## Result

The homogeneous system L(136;43^10) on the blowup of P^2 at 10 general
points has virtual dimension -8 and is empty (non-special), as predicted
by SHGH/Nagata. No (-1)-curve obstructs it: for every (-1)-curve class
C = eH - sum c_i E_i, D.C = 136e - 43*S with S = 3e-1 by adjunction, so
D.C = 7e + 43 > 0 (43 on each Ei, >= 50 for e >= 1).

## Proof / evidence

Exact specialization-rank certificate. Let Z be 10 fat points of
multiplicity 43 at explicit distinct rational coordinates and M the
9460 x 9453 integer interpolation matrix (columns monomials x^i y^j,
i+j <= 136; rows vanishing of d^a_x d^b_y at each point for
a+b <= 42). Then ker_Q(M) = H^0(P^2, I_Z(136)).

Exact Gaussian elimination modulo the prime p = 251 (251 > 136, so no
falling factorial vanishes mod p) gives full column rank 9453.
Any nonzero minor mod p is a nonzero integer minor, so rank_Q(M) = 9453
and h^0 = 0 at this rational 10-tuple. A second disjoint specialization
(all points shifted mod 251) independently gives PIVOTS = 9453.

Since h^0 is upper semicontinuous over the flat family of 10-tuples of
distinct fat points, vanishing at one closed point implies vanishing at
the general 10-tuple (over C, characteristic zero). Hence the general
system is empty.

The C kernel was cross-validated against exact sympy QQ rank on 6 tiny
systems and an independent numpy F_251 implementation on 210- and
861-pivot systems. The auditor independently recompiled both C kernels
and reran both full degree-136/multiplicity-43 eliminations, each
returning PIVOTS=9453 FULL COLUMN RANK.

## Limitations

Decides the single canonical cell (136;43^10) only; the rest of the
sqrt(10) < d/m < 174/55 strip stays open. The proof is
specialization-rank plus semicontinuity, not a Ciliberto-Miranda
degeneration; no degeneration lemma is claimed. Rank logs certify the
two stated specializations; generality transfer uses the classical
h^0-semicontinuity theorem.

## Reproducibility

- `gcc -O3 -march=native -fopenmp -o cm_rank output/artifacts/cm_rank.c`
- `./cm_rank 136 43 10` -> `PIVOTS=9453 C=9453 R=9460 => FULL COLUMN RANK`
  (log: `output/artifacts/target_rank_log.txt`)
- `gcc -O3 -march=native -fopenmp -o cm_rank_shift output/artifacts/cm_rank_shift.c`
- `./cm_rank_shift 136 43 10 100` -> identical `PIVOTS=9453` verdict
  (log: `output/artifacts/target_rank_log_shift100.txt`)
- `python3 output/artifacts/verify_cross.py` (stdlib+numpy+sympy):
  tiny exact-rational and medium independent-F_251 cross-checks.

## References

- Ciliberto-Miranda, Homogeneous interpolation on ten points, arXiv:0812.0032.
- Dumnicki, Reduction method for linear systems of plane curves with base fat points, arXiv:math/0606716.
- Dumnicki-Jarnicki, New effective bounds on the dimension of a linear system in P^2, arXiv:math/0505183.
- Dumnicki, Quasi-homogeneous linear systems on P2 with base points of multiplicity 7,8,9,10, arXiv:0804.1213.
- Petrakiev, Homogeneous Interpolation and Some Continued Fractions, arXiv:1211.6380.
- Eckl, Ciliberto-Miranda degenerations of CP^2 blown up in 10 points, arXiv:0907.4425.
- Ciliberto-Miranda-Roe, Boundedness Results for Planar Linear Systems Assuming SHGH, arXiv:2508.01462.
