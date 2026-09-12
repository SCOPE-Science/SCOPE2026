# Wild mod-3 DW gluing boundary at Q(sqrt(-3)): disproof (1 vs 1/3)

## Context

Arithmetic Dijkgraaf–Witten theory (Kim; Hirano–Kim–Morishita arXiv:2106.02308, hereafter HKM) constructs Chern–Simons functionals and DW partition functions for a number field k and a finite set S of finite primes where the level n is invertible. The decomposition (Theorem 5.2.x) and gluing formulas express the invariant of a glued spectrum through unramified local weights on the boundary tori ∂V_S. The admitted target asks whether formally applying that gluing recipe to reinsert the primes above 3 still predicts the full-ring invariant when 3 is not invertible — the wild-ramification boundary — for the smallest natural test case.

## Definitions and normalizations

Let K = Q(sqrt(-3)) = Q(zeta_3), O_K = Z[omega] the Eisenstein integers, omega = e^{2πi/3}, X_full = Spec O_K, n = 3, G = Z/3, zeta = e^{2πi/3} in C. Let c be the normalized generator of H^3(G, mu_3) ≅ Z/3. Since zeta_3 ∈ O_K^*, the fppf sheaves Z/3 and mu_3 are (noncanonically) identified over X_full. Both sides use DW(Z) = (1/|G|) Σ_{[P] ∈ H^1} zeta^{CS([P])}.

Let p0 = (1−omega) = (sqrt(-3)), S_0 = {p0} the unique prime above 3, N(p0) = 3, (3) = p0^2, residue field F_3, X' = Spec O_K ∖ S_0. Let Z_pred be the value obtained by formally applying the HKM decomposition/gluing formula to reinsert S_0 with unramified local weights depending only on (N(p), Frobenius class). Let Z_full be the flat-cohomology full-ring DW sum where 3 is not invertible, granted by the topic with the same (G,c) normalizations.

## Result (headline claim)

For K = Q(sqrt(-3)), n = 3, G = Z/3 with normalized c: Z_full = 1 (three flat torsor classes, all Chern–Simons invariants zero by Bockstein vanishing) while the formal HKM gluing reinsertion gives Z_pred = 1/3 (one everywhere-unramified class). Hence as complex numbers 1 ≠ 1/3: Z_full ≠ Z_pred. The equality is disproved, delimiting the HKM gluing scope beyond its invertible hypothesis. The two extra flat mu_3-torsors contribute 2/3 of mass invisible to any unramified-weight gluing rule.

## Proof / evidence

1. Class number and units. Minkowski bound (2/π)√3 ≈ 1.10 < 2 gives Cl(O_K) = 0; O_K is a PID. O_K^* = mu_6 of order 6; cubes = {±1}; hence H^1_fppf(X_full, mu_3) = O_K^*/cubes has 3 classes {1, zeta_3, zeta_3^2}.

2. Nine étale classes on X'. O_{K,S_0} is a PID localization so Pic = 0; H^1_ét(X', mu_3) = O_{K,S_0}^*/cubes. S-unit rank r_1+r_2−1+|S_0| = 1 gives mu_6 × ⟨pi⟩, pi = sqrt(-3), so H^1(X', Z/3) ≅ (Z/3)^2 with 9 Kummer representatives a_{i,j} = zeta_3^i pi^j, pairwise distinct mod cubes.

3. Ramification at p0. For j = 1,2, v_{p0}(a) = j is prime to 3, forcing 3 | e: ramified. For j = 0, i = 1,2, v_{p0}(1−a) = 1 certified by N(1−zeta_3^i) = 3; the shifted polynomial Y^3+3Y^2+3Y+(1−a) has Newton valuations (0,1),(1,2),(2,2),(3,0), one segment of slope −1/3: irreducible, totally wildly ramified of degree 3. Only (0,0) is unramified (Frobenius 0). Restriction H^1(X') → H^1(K_{p0}, Z/3) is injective since everywhere-unramified Z/3-extensions are classified by the Hilbert class field, trivial here. Tate local Euler gives dim H^1(K_{p0}, Z/3) = 4 (81 local representations, unramified quotient Z/3). Cubic Artin symbols (a/P)_3 = a^2 mod P at P = (3+omega) of norm 7 tabulated for all nine classes in ledger_output.txt.

4. Z_pred = 1/3. HKM Theorem 5.2.4 with S_1 = ∅, S_2 = S_0 applies formally (mu_3 ∈ K; all primes dividing 3 in S_2); the reinsertion value equals the HKM full-ring invariant Z(X̄_k) = (1/3)zeta^0 = 1/3 since Hom(Gal(H_K/K), Z/3) is a singleton (class number 1, no real places), CS = 0. The V^* weight is supported on unramified representations, depending only on Frobenius class and N(p0) = 3.

5. Z_full = 1. Write c = u·(x ∪ y) with y the tautological H^1 class, x = Bock(y). For flat rho, c∘rho = u·(Bock(rho) ∪ rho) in H^3_fppf(X_full, mu_3). From the fppf Kummer sequence, H^1(G_m) = Pic = 0 and H^2(G_m) = Br(O_K) = 0 (Brauer classes over O_K have vanishing finite invariants and K has no real places, so zero by global reciprocity); hence H^2_fppf(X_full, mu_3) = 0, Bock(rho) = 0, all flat CS invariants vanish under any linear trace. So Z_full = (1/3)(1+1+1) = 1.

6. Disagreement 1 ≠ 1/3 completes the disproof.

## Limitations

Grants the topic premise that the flat full-ring DW invariant exists with the stated normalization; only linearity of its trace is used since all inputs vanish. HKM theorems, fppf Kummer theory, Tate duality, and cubic reciprocity are cited as tools. Individual étale CS phases on X' are bypassed via the HKM gluing theorem rather than computed term by term.

## Reproducibility

Run `python3 output/artifacts/ledger.py` (no dependencies): checks Eisenstein arithmetic, unit cubes, Minkowski bound, N(1−zeta^i) = 3, cubic symbols at the norm-7 prime for all nine classes, local dimension, and prints Z_full = 1.0 vs Z_pred = 0.333…. Artifacts: ledger.py, ledger_output.txt.

## References

Hirano–Kim–Morishita, On arithmetic Dijkgraaf–Witten theory, arXiv:2106.02308; Kim, Arithmetic Chern–Simons Theory I, arXiv:1510.05818; Eichler, Duality for arithmetic DW theory, arXiv:2508.19214 / doi:10.21248/gups.93799; Deng–Kurimaru–Matsusaka, DW invariants for real quadratic fields; Hirano, mod-2 DW invariants.
