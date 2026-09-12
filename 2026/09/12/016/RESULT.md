# CFN Triangle-versus-Sunlet: the Ideals Differ — an Explicit Certified CFN Cycle-Length Separator

## Context

Deciding whether binary Cavender–Farris–Neyman (CFN) data retains reticulation-cycle-length information is a recognized methodological gap. For the Jukes–Cantor (JC), Kimura 2-parameter (K2P), and Kimura 3-parameter (K3P) models, split polynomials such as Q_{12|34} separate quarnets with different splits. No analogous exact CFN statement was recorded for the canonical cross-skeleton pair: the single-triangle quarnet against the 4-sunlet. The admitted target asked whether their CFN Fourier vanishing ideals coincide.

## Definitions

Let the CFN Fourier ring on four taxa be R = C[q_g : g in {0,1}^4, g_1+g_2+g_3+g_4 = 0] (8 even-weight variables; odd-weight coordinates are identically zero). Let D be the semi-directed single-triangle quarnet with split 12|34 and hybrid leaf-child 1 (3-cycle with pendant branches to leaves 1, 2 and to the cherry (3,4)). Let S be the 4-sunlet with circular order (1,2,3,4) and hybrid leaf-child 1. Both are binary semi-directed level-1 quarnets with one reticulation, parametrized as mixtures of their two displayed trees in CFN Z/2 Fourier coordinates with all a^e_0 = 1. Let I(D), I(S) subset R be their CFN Fourier vanishing ideals (vanishing ideals of the Zariski closures of the parametrized images). Let f0 := q_0000 q_1111 − q_0011 q_1100 in R.

Triangle D parametrization (Brits Lemma 4.6 formula carried from split 13|24 to 12|34 by leaf transposition (2 3), fixing hybrid leaf 1):
q^D_g = A_{g1} B_{g2} C_{g3} D_{g4} E_{g1+g2} (L F_{g1} H_{g1+g2} + (1−L) K_{g1} H_{g2}), even-weight g.

4-sunlet S parametrization (Cummings–Hollering–Manon Example 2.8, mixing parameter made explicit):
q^S_g = A_{g1} B_{g2} C_{g3} D_{g4} [L R_{g1} S_{g1+g2} T_{g4} + (1−L) S_{g3} T_{g1+g4} U_{g1}], even-weight g.

## Result

Theorem (disproof of I(D) = I(S)). With f0 as above: (a) f0 vanishes identically on the D variety, so f0 in I(D); (b) f0 does not vanish identically on the S variety: at an explicit stochastic (CFN Theta0) parameter point, f0 evaluates to exactly 1/2400, so f0 is not in I(S). Hence I(D) != I(S): the CFN model algebraically separates the 3-cycle history from the 4-cycle history on these taxa. CFN quartet data can in principle distinguish the single-triangle history from the 4-sunlet history; f0 is a deployable cycle-length diagnostic (zero on every D point, nonzero on an open subset of S).

## Proof / Evidence

(a) Write M(g1,g2) := L F_{g1} H_{g1+g2} + (1−L) K_{g1} H_{g2}. Then q^D_0000 = A0B0C0D0E0M(0,0), q^D_1111 = A1B1C1D1E0M(1,1) (since 1+1=0 in Z/2), q^D_0011 = A0B0C1D1E0M(0,0), q^D_1100 = A1B1C0D0E0M(1,1). Hence q^D_0000 q^D_1111 − q^D_0011 q^D_1100 = A0A1B0B1C0C1D0D1E0^2 M(0,0)M(1,1) − (same) = 0 as a polynomial identity in all parameters. So f0 vanishes on the D image and hence on its Zariski closure; f0 in I(D). Verified by exact symbolic expansion (sympy, general symbols), Part A of the replay script.

(b) Evaluate the S parametrization at the stochastic point: all Fourier 0-parameters = 1, 1-parameters A1=1/2, B1=1/3, C1=1/4, D1=1/5, R1=1/2, S1=1/3, T1=1/4, U1=1/5, L=1/2 (all edge 1-eigenvalues in (0,1), mixing parameter in (0,1): a valid CFN Theta0 point). Exact rational arithmetic gives q^S_0000 = 1, q^S_1111 = 23/28800, q^S_0011 = 1/120, q^S_1100 = 11/240, so f0 = 1·(23/28800) − (1/120)(11/240) = 23/28800 − 22/28800 = 1/2400 ≠ 0. Since this is a point of the S variety, f0 does not vanish on S; f0 not in I(S). Verified in exact Fraction arithmetic, Part B of the replay script. A numeric D sanity check (Part C) confirms f0 = 0 on D.

f0 uses only even-weight binary (CFN, Z/2) labels; it lies in the CFN Fourier ring R, not in any JC/K2P/K3P ring. It is the formal CFN analogue of the JC polynomial Q_{12|34} but a different polynomial in a different ring.

## Limitations

Only the set-theoretic/ideal inequality I(D) != I(S) via one separator is proved; no generating set of either ideal, no dimension or primality claim, and no statement about other taxon orders, hybrid placements, or models (JC/K2P/K3P) is made. The D formula is carried to split 12|34 by the explicit leaf transposition above; the S formula is Cummings Example 2.8 with explicit mixing parameter.

## Reproducibility

Run `python3 output/artifacts/verify_separator.py` (stdlib + sympy only). Expected output ends with `VERIFY_OK`: Part A (symbolic D vanishing), Part B (exact witness f0 = 1/2400), Part C (numeric D sanity).

## References

- J. Cummings, B. Hollering, C. Manon, Invariants for level-1 phylogenetic networks under the Cavendar-Farris-Neyman Model, arXiv:2102.03431.
- J. Brits, N. Holtgrefe, L. van Iersel, S. Martin, On Tree-Network Distinguishability and Full Identifiability of Phylogenetic Networks, arXiv:2607.12919.
- J. Cummings, E. Gross, B. Hollering, S. Martin, I. Nometa, The Pfaffian Structure of CFN Phylogenetic Networks, arXiv:2312.07450.
- E. Gross, R. Krone, S. Martin, Dimensions of Level-1 Group-Based Phylogenetic Networks.
