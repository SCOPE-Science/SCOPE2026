# Rank-0 phi/hat-phi certificate for the cube-sum curve of D1 = 30207

## Context

An integer D is a sum of two rational cubes iff the Mordell curve
E_D: y^2 = x^3 - 432 D^2 (model of x^3 + y^3 = D) has positive
Mordell-Weil rank over Q (D cubefree, D > 2). When the global root
number w(D) = +1 the parity conjecture does not force positive rank,
so exact rank-0 certificates (non-cube-sum proofs) require descent.
Das-Jha (arXiv:2508.05361v2) give, for n = 3l with l prime = 7 mod 9,
a phi-Selmer criterion: if 3l is a cube sum then (3/l)_3 = 1
(Proposition 2.7). The present record instantiates the contrapositive
at a new l = 10069 in the untabulated strip 30000 < D < 30500.

## Definitions

- D1 = 30207 = 3 x 10069, cubefree; l = 10069 prime, l = 7 mod 9.
- E = E_{D1}: y^2 = x^3 - 432 D1^2 = x^3 - 394183950768.
- K = Q(zeta_3), O_K = Z[zeta_3], p = 1 - zeta_3.
- E_t: y^2 = x^3 + t, t = (12 l)^2 = 14599405584, with 3-isogeny
  phi: E_t -> E over K.
- S_phi(E_t/K): phi-Selmer group; S_3(E/Q): full 3-Selmer group.
- w(D1): global root number via Birch-Stephens formula (0.1).
- (a/b)_3: cubic residue symbol.

## Result

Let D1 = 30207 = 3 x 10069. Then:

1. D1 is cubefree with 30000 < D1 < 30500.
2. The global root number w(D1) = +1.
3. The phi/hat-phi 3-isogeny Selmer bound is 0: S_3(E/Q) = 0.
4. Hence E(Q) has exact Mordell-Weil rank 0.
5. So D1 is not a sum of two rational cubes.

## Proof / evidence

Scope and model: 10069 prime by trial division to sqrt < 101;
10069 = 7 mod 9; D1 = 3 mod 9, cubefree (factorization {3:1,
10069:1}); k = -432 D1^2 = -394183950768 with
|k| = 2^4 x 3^5 x 10069^2; discriminant Delta = -432 k^2 < 0;
E(Q)[3] = 0 (k < 0 not a square; D1 not a cube since
31^3 = 29791 < 30207 < 32768 = 32^3; -4k = 1728 D1^2 not a cube by
exact integer-cbrt check, so psi_3 = 3x(x^3 + 4k) has no rational root).

Root number: Birch-Stephens (0.1) gives w_3 = -1 (D1 = 3 mod 9);
no p | D1 has p = 2 mod 3 (10069 = 1 mod 3); hence
w(D1) = -(-1) = +1. Recomputed in script.

Selmer input: l splits in O_K as l = pi pi' with explicit
pi0 = -92 + 15 rho of norm 10069 (verified: 92^2 - 92x15 + 15^2
= 8464 - 1380 + 225 = 10069). S_t = {p, pi, pi'}.
Selmer container S_phi(E_t/K) subset <zeta^2-bar, 9-bar, pi^2-bar,
9l^2-bar>, dim <= 4 (Jha-Majumdar-Shingavekar Thms 3.15/4.14).
Cassels Kummer formula: 9l^2-bar is IN, image of (0, 12l) =
(0, 120828). JMSh Prop 4.6(b) at pi: zeta^2-bar is OUT
(uses l = 7 mod 9).

Key symbol: (3/10069)_3 = zeta_3^2 != 1, computed two independent
ways: Euler 3^((l-1)/3) = 5363 != 1 mod 10069 (with 5363^3 = 1),
and Eisenstein 3^((N pi - 1)/3) mod pi in Z[rho]. Controls: same
engine gives (3/61)_3 = 1 (3 x 61 is a cube sum) and
(3/43)_3 = zeta^2 (3 x 43 proven non-sum). Also verified
(zeta/pi)_3 = zeta^2, (pi/pi')_3 = 1 (Lemma-7/Evans inputs).

Elimination + parity (quoted Das-Jha Prop 2.7 proof, inspected):
under (3/l)_3 != 1 the 13-subgroup elimination gives
dim_{F3} S_phi(E_t/K) <= 2 ((2.12)); since w = +1, the 3-parity
theorem (Nekovar/Kim/Dokchitser-Dokchitser) plus Lemma 2.1 forces
dim S_phi odd, hence 1; then (2.11) gives S_3(E/Q) = 0 (R has even
dimension by BES Prop 49; torsion quotient contributes 1), and
(1.6) gives rank 0.

Quoted vs proved: Cassels Kummer-image formulae, JMSh S-unit
container and local description at pi, the 13-case elimination
pattern, 3-parity theorem, (2.11)/(1.6) dimension algebra are
quoted from [Ca2 Secs 14-15], [JMSh Props 4.6(b), Thms 3.15/4.14],
[Das-Jha v2 Prop 2.7, Lemma 2.1, Thm 1.4], [BES Prop 49]. Every
D1-specific number (primality, mod-9 class, root number, pi, all
symbol values, t, (0,12l), discriminant sign, torsion vanishing)
is recomputed in the artifact.

## Limitations

- Rank 0 is via the 3-isogeny Selmer bound 0 plus the known
  3-parity theorem, not via independent 2-descent or analytic rank;
  no generators/saturation needed at rank 0.
- The 13-subgroup elimination pattern and Kummer/local formulae
  are quoted from Cassels/JMSh/Das-Jha; only the D1-specific
  inputs and symbol values are recomputed.
- The target's s >= r+2 Sha[3] gap is NOT claimed (target route
  blocked: no CAS obtainable; see target_exit.json).

## Reproducibility

- `python3 output/artifacts/selmer_phi.py` prints VERIFY_OK
  (log: `output/artifacts/selmer_phi.log`); exit 0.
- Only dependency: Python 3 stdlib.
- Cross-checks: Euler criterion and independent norm-equation
  solution for pi logged; wplus1.txt gives the Birch-Stephens
  w = +1 sieve of the (30000, 30500) strip.

## References

- Das-Jha, On certain root number 1 cases of the cube sum problem,
  arXiv:2508.05361v2 (J. Pure Appl. Algebra 2025).
- Jha-Majumdar-Shingavekar, 3-Selmer groups, ideal class groups and
  the cube sum problem, arXiv:2207.12487.
- Chan, The 3-isogeny Selmer groups of y^2 = x^3 + n^2.
- Bhargava-Elkies-Shnidman, average size of 3-isogeny Selmer groups.
- Cassels [Ca2]; Birch-Stephens root-number formula.
