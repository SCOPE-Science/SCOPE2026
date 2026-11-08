# Independent mathematical audit

## correctness

PASS

For prime powers q≡3 (mod4), q≥7, reconstruct Paley edge orientation via quadratic character and 16-witness sum for each 4-point sign pattern. Expanding products gives 16N≥q−38−11√q>0 for every q≥191 by the degree-3/4 Weil bounds and exact sums for one/two factors; this establishes ALL high-order cases. The actual C++17 source enumerates every admissible order 7≤q<191 including F_27 via the irreducible cubic X³+2X+1, every four-subset containing zero (translation is a tournament automorphism) and all 16 orientation masks. Its source has explicit classification checks, and independent direct finite-character calculations for q=7,59,67,71,103,107 recover the pass/fail and q103=(0,1,16,47) all-positive obstruction. P4 iff rank-five EF equivalence with countable random tournament: rank-five extension axioms and 5-round back-and-forth (including padding of shorter patterns). Thus P4 iff S4 within this Paley family and iff q∈{67,71,79,83} or q≥107. The finite enumeration is not extended past its proven cutoff and not used as an infinite proof.

## originality

PASS

Best-of-knowledge PASS for the exact prime-power q-membership classification of Paley P4 / rank-five random theory, and exact Paley-only S4⇔P4. Classical Paley character-sum sufficient bounds, q=67 P4 and weak domination tables predate this claim. Directly relevant 2026 paper poses S4 versus P4 for all vertex-transitive doubly regular tournaments; the specific Paley threshold is not supplied in inspected sections. This is no priority certification.

## value

PASS

A sharp eventual threshold with a nonmonotone q=103 exception and a complete finite-field parameter classification answers a natural logical genericity/dominator question in a canonical tournament family. It also settles a motivated restricted instance of a published S4/P4 comparison; it is not an arbitrary finite sample or a textbook renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
