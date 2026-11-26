# Independent mathematical audit

## correctness

PASS

Reconstruct the sort from the first failure of alternation: for offset t in parent block i it is at zero-based comparison position D=2h d_i−t, which lies inside the full rotation because the parent is mixed. At this position the shorter alternating prefix repeats the previous bit, while any longer one alternates. Thus for zero-starting rows odd D precedes all even D and even D sorts in descending order; for one-starting rows even D precedes all odd D and sorts in ascending order. The odd offsets have a constant predecessor in each half, so their internal order need not be resolved. For even offsets the D ranges of successive d_i layers are disjoint, and t=0 is the largest D in each layer. Aligned tied-D rows compare in parent rotation order by the first letter of the code blocks. Equal finite rotations have equal last letters, so neither parent nor child periodicity creates ambiguity. The preceding bit at t=0 is the complement of the parent predecessor, and at t>0 it is the complement of the starting bit. This gives each term of the claimed concatenation. Every indicated layer exists, and the separator lengths stay positive at h>=2, so repeating their letters does not change the number of transitions. Independent direct cyclic sorting for 001 gave 101100 and 110111010000, with four and six runs at h=1 and h=2. The supplied verifier was inspected, not run; its finite tests are not the proof.

## originality

PASS

The supported distinct result is the complete cyclic BWT transport identity for this even alternating expansion and the resulting cross-factor plateau for h>=2, not a claim about preservation relative to the unexpanded word or about the familiar h=1 substitution.

## value

PASS

The exact transform identifies which parts of the rotation order are retained and which are inflated by the alternating block length. It explains a uniform plateau across the whole morphism family despite lack of general preservation relative to the input. The mixed-word proof, including arbitrary periods, and the genuinely different h=1 boundary make this more than a run-count check on a named sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
