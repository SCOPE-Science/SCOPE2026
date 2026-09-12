# Wild Z/4 linking at p2, r7 over Q(zeta_8): disproof of the order-2 value

## Context

Arithmetic topology views Spec O_K as a 3-manifold and the Artin-Verdier trace
of a cup product of Kummer classes as a linking number. For K = Q(zeta_8),
S = {p2, r7} with p2 the unique prime above 2 and r7 a fixed prime above 7,
and Z/4 coefficients, the target asked whether the cup-trace
w = Tr(a2 cup a7) equals the 4th-power norm-residue (Hilbert) symbol value at
this wild pair, concretely the nontrivial element of order 2 in Z/4
(2 mod 4) rather than 0. This is the minimal mu_4-containing cyclotomic
setting with one wild and one tame prime admitting nontrivial 4th-power
symbols.

## Definitions

Let K = Q(zeta_8), O = Z[zeta_8], X = Spec O, p2 = (1 - zeta_8),
r7 a fixed prime above 7, S = {p2, r7}, U = X \ S.
Identify mu_4 ~= Z/4 via zeta_4 = i in K.
Let d2 = 1 - zeta_8 and d7 = pi_7 with (pi_7) = r7 (possible since
h(Q(zeta_8)) = 1). Let a2 = [d2], a7 = [d7] in H^1(U, Z/4) be the
order-4 Kummer classes ramified exactly at p2 and r7 respectively.
Let w = Tr_AV(a2 cup a7) be the Artin-Verdier trace, and let
( , )_v denote the 4th-power Hilbert symbol at v. Let w_link denote the
linking-number normalization given by the single tame local term at r7.

## Result

The stated identity is false. The 4th-power Hilbert symbols at both p2 and
r7 are primitive of exact order 4, never the order-2 element 2 mod 4, while
the literal Artin-Verdier trace Tr(a2 cup a7) equals 0 by global reciprocity;
under the linking-number normalization the trace equals the primitive tame
term. Hence w equals neither the symbol nor the claimed value 2 mod 4, in
every standard normalization.

| quantity | value | equals 2 mod 4? |
|---|---|---|
| Hilbert (tame) symbol at r7 | primitive, order 4 | no |
| Hilbert (wild) symbol at p2 | primitive, order 4 | no |
| literal AV cup-trace w | 0 | no |
| linking normalization w_link | primitive, order 4 | no |

## Proof / evidence

Splitting and Kummer classes: N_{K/Q}(1 - zeta_8) = Phi_8(1) = 2, so
(1 - zeta_8) = p2 is the unique prime above 2 with residue field F2.
Since 7 does not divide 8, 7 is unramified with residue degree equal to the
order of 7 mod 8, namely 2; there are phi(8)/2 = 2 primes above 7, each with
residue field F49. Exactly, O_K/7O_K = F7[x]/(x^4+1) with
x^4+1 = (x^2+3x+1)(x^2+4x+1) mod 7, each quadratic of discriminant 5, a
nonsquare mod 7, hence irreducible. Valuations give v_{p2}(d2) = 1,
v_{r7}(d2) = 0, v_{r7}(d7) = 1, v_{p2}(d7) = 0; a class [d] with valuation 1
has exact order 4 in K^times/K^times4, so both Kummer classes have exact
order 4.

Tame symbol: for v not dividing 2 with residue size q = 1 mod 4, the
4th-power symbol of (unit, uniformizer) is u^{(q-1)/4} up to inversion. At
r7, d7 is a uniformizer, d2 reduces to u = 1 - x in F49, and (q-1)/4 = 12.
Exact integer arithmetic in both F49 fields gives u^12 with (u^12)^2 = -1
and u^12 != +-1 (concretely 1+3x mod (x^2+3x+1) and 1+4x mod (x^2+4x+1),
both squaring to -1 with u^48 = 1). Hence the tame symbol is primitive of
order 4 for both choices of r7; inversion preserves order, so the conclusion
is convention-independent.

Wild symbol: d2, d7 in K^times satisfy the global product formula. All
places outside S union {infinite} see two units with residue characteristic
prime to 4 (trivial symbol), and all infinite places are complex. Hence
(d2,d7)_{p2} * (d2,d7)_{r7} = 1, so the wild symbol at p2 is the inverse of
the primitive tame symbol, again primitive of exact order 4.

Cup-trace: by Artin-Verdier/local duality the global trace is the sum of
local invariants, i.e. the sum of the two Hilbert symbols, which cancel:
w = 0. The linking normalization keeps only the tame term, which is
primitive order 4. Neither 0 nor any primitive root equals the unique
order-2 element, and 2 mod 4 is fixed by inversion while primitive roots
swap, so no identification or inversion convention yields 2 mod 4.

## Limitations

Order-based conclusions are invariant under mu_4 ~= Z/4 identifications and
tame-symbol inversion conventions. Class number 1 of Q(zeta_8), splitting of
7, triviality of unit-unit symbols away from 2, and complex infinite places
are cited to Washington and standard local class field theory. No direct
2-adic expansion is needed since reciprocity determines the wild value from
the certified tame value.

## Reproducibility

Run `python3 output/artifacts/compute_tame_symbol.py` (pure Python, no
dependencies); expected output is stored in
`output/artifacts/tame_symbol_output.txt`. It verifies the mod-7
factorization, irreducibility via discriminant 5, and u^12 of exact order 4
in each F49.

## References

- L. Washington, Introduction to Cyclotomic Fields (class number of Q(zeta_8)).
- C. Deninger, On Artin-Verdier duality for function fields; T. Zink / B. Mazur exposition of Artin-Verdier duality.
- K. McCallum, R. Sharifi, A cup product in the Galois cohomology of number fields.
- M. Morishita, arithmetic-topology / Ihara programme references for linking-number normalization.
- LMFDB Number Fields database (field/splitting/class-group scope).
