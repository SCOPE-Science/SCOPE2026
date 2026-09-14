# Dihedral Case-2 verdict for the symmetric 1/3 Heun operator at t = -1

## Context

The Heun equation is the general second-order Fuchsian equation on P1 with four
regular singularities. Its Picard-Vessiot (differential) Galois group over C(z)
is classified by Kovacic's algorithm into four cases: reducible (Borel, Case 1),
imprimitive irreducible (infinite dihedral, Case 2), finite primitive (Case 3),
or the full SL(2,C). Case 2 holds exactly when the second symmetric power of the
operator admits a nonzero exponential solution with rational logarithmic
derivative. The admitted target asks for a proof deciding this dihedral
inclusion for one natural symmetric parameter point, with separation from the
Borel and finite cases.

## Definitions

Let H be the Heun operator

y'' + (gamma/z + delta/(z-1) + epsilon/(z-t)) y'
  + (alpha*beta*z - q)/(z(z-1)(z-t)) y = 0

with parameters t = -1, gamma = delta = epsilon = 2/3, alpha = 1/3,
beta = 2/3, q = 0. These satisfy the Fuchsian relation
gamma+delta+epsilon = alpha+beta+1 = 2. Put
P = (2/3)(1/z + 1/(z-1) + 1/(z+1)) and Q = (2/9)/(z^2-1).
The standard normalized (SL-form) reduction xi'' = r xi with
xi = y*exp(int P/2) uses r = P^2/4 + P'/2 - Q in C(z).

## Result

For H as above: H does not have Picard-Vessiot Galois group contained in the
infinite dihedral group. Its second symmetric power admits no nonzero
exponential solution with rational logarithmic derivative. In fact all three
Kovacic cases fail, so H has no Liouvillian solution at all and its
Picard-Vessiot Galois group is the full SL(2,C): irreducible (Case 1 fails),
non-dihedral (Case 2 fails), and infinite (Case 3 fails).

## Proof / evidence

Exact rational computation (sympy, no floating point). The normalized
coefficient is

r = -2(z^2+1)^2 / (9 z^2 (z^2-1)^2).

Poles: z in {0, 1, -1} are poles of exact order 2 with
lim (z-c)^2 r = -2/9 and lim (z-c)^3 r = 0; at infinity
deg(den)-deg(num) = 6-4 = 2 with lim z^2 r = -2/9. Hence in Kovacic notation
b_c = -2/9 at each c in {0,1,-1,infinity} and sqrt(1+4 b_c) = 1/3 everywhere;
exponent differences are all 1/3 (non-integral), so no logarithmic cases arise.

Case 1: alpha_c^+- = (1 +- 1/3)/2 = {1/3, 2/3} at every singular point. All 16
sums d = alpha_infinity - alpha_0 - alpha_1 - alpha_{-1} are at most
2/3 - 3(1/3) = -1/3 < 0, so no admissible nonneg-integer degree exists.

Case 2: E_c = {2 + k/3 : k in {0,+-2}} cap Z = {2} at each point, since
2 +- 2/3 are non-integral. The unique tuple gives
d = (2-2-2-2)/2 = -2 < 0, so no monic theta of degree d and no Case-2
polynomial exist: the symmetric square has no rational-logarithmic-derivative
exponential solution.

Case 3: with sqrt(1+4b) = 1/3, the admissible sets are {4,5,6,7,8} (n=4),
{4,6,8} (n=6), {4,5,6,7,8} (n=12); every tuple satisfies
e_infinity - sum e_c <= 8 - 12 = -4 < 0, so
d = (n/12)(e_infinity - sum e_c) <= -n/3 < 0. No finite-primitive solution.

All three failures together give Galois group SL(2,C). The script
output/artifacts/kovacic_verdict.py asserts each identity over Q(z) and prints
the extremal degrees (-1/3, -2, -n/3).

## Limitations

The verdict is specific to the single admitted point
(t=-1, gamma=delta=epsilon=2/3, alpha=1/3, beta=2/3, q=0). It does not classify
nearby accessory-parameter values or other Heun families. The Galois group is
over the constants C via Kovacic's algorithm over C(z); arithmetic monodromy
or fields of definition are not addressed.

## Reproducibility

Run `python3 output/artifacts/kovacic_verdict.py` (exact Q-arithmetic via
sympy). It asserts the closed form of r, each b_c = -2/9 with exact pole
orders, and emptiness of admissible degree sets in all three Kovacic cases.

## References

- DLMF Ch. 31 Heun Functions, esp. 31.8 Solutions via Quadratures and 31.14
  General Fuchsian Equation (Kovacic's algorithm).
- Kovacic, J. An algorithm for solving second order linear homogeneous
  differential equations. J. Symbolic Comput. 2 (1986), 3-43.
- van der Put, M. and Singer, M. F. Galois Theory of Linear Differential
  Equations. Springer, 2003.
- Ronveaux, A. (Ed.). Heun's Differential Equations. Oxford Univ. Press, 1995.
- MathWorld, Heun's Differential Equation (general form reference).
