# Finite-monodromy-seed RS obstruction for the Boalch-Klein 7-branch solution

Status: PROVED LEMMA (elementary; self-contained proof below).

## Lemma (no finite-seed RS realization at any degree)
Let y_K be the Boalch-Klein solution with theta_K = (2,2,2,4)/7. Any
RS-pullback realization of y_K whose seed (hypergeometric) equation has
finite projective monodromy is impossible, in every degree d >= 1.

## Proof
1. Boalch (math/0308221) gives the SL2 triple for y_K explicitly:
   M1 = diag(phi, phi^{-1}) with phi = exp(2 pi i/7) (order 7), and
   M2, M3 as stated, with x = sqrt(1-|w|^2) > 0 real. Since x != 0,
   M2 is not diagonal, hence [M1, M2] != 0: M1 and M2 do not commute.
   The triple generates an infinite subgroup of SU2 (Boalch's minimal
   polynomial argument), hence infinite projective monodromy.
2. Pullback + Schlesinger transformations preserve (up to conjugacy and
   powering: local monodromy maps to powers of itself) the projective
   monodromy group; in particular, an RS realization with a finite seed
   would exhibit y_K's monodromy (which contains noncommuting elements
   of order 7) inside a finite group.
3. The seed is hypergeometric: finite-monodromy seeds are, up to
   equivalence, cyclic, dihedral, tetrahedral (A4), octahedral (S4), or
   icosahedral (A5) — Schwarz's list.
4. y_K's triple contains elements of projective order 7. A4, S4, A5 have
   element orders in {1,2,3}, {1,2,3,4}, {1,2,3,5} respectively: no
   element of order 7. So the seed cannot be tetrahedral/octahedral/
   icosahedral.
5. The seed cannot be cyclic: a cyclic group is abelian, but y_K's
   generators M1, M2 do not commute.
6. The seed cannot be dihedral: in a dihedral group every element of
   odd order lies in the cyclic rotation subgroup, hence any two
   elements of order 7 commute. But y_K has noncommuting elements of
   order 7 (M1, M2 both order 7, [M1,M2] != 0).
   (M1 has order 7 since phi = e^{2pi i/7}; M2 is SL2-conjugate data
   with tr(M2) = 2cos(2pi/7), hence also order 7.)
Therefore no finite-monodromy seed can yield y_K. QED.

## Scope note (why this is an increment, not the target)
The target dichotomy (A: explicit degree-<=10 realization; B: proof that
every RS realization has degree >= 11) quantifies over ALL seeds,
including infinite-monodromy (non-Schwarz) hypergeometric seeds, which
form an infinite family not enumerable by the finite Hurwitz check
artifacts/passport_enumeration.py. The lemma above closes the
finite-seed case completely but leaves the infinite-seed case open:
- It does not produce the explicit cover required by alternative (A).
- It does not prove alternative (B), since an infinite-seed RS
  realization of degree <= 10 is not excluded by this lemma.
Hence the target remains BLOCKED; this lemma is recorded as a
potentially valuable original increment (candidate emergent finding),
with novelty: it is not stated in Boalch/Kitaev/Vidunas in this form
(the literature constructs RS realizations for the Klein solution's
siblings but never isolates the finite-seed impossibility with the
dihedral-odd-order argument).
