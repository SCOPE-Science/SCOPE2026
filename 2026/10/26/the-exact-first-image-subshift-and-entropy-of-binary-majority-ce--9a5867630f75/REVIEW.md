# Independent mathematical audit

## correctness

PASS

A four-state input-pair nondeterministic automaton records the eight majority triples. Subset determinization from full state 15 reaches exactly twelve masks including sink 0. Independently rebuilding transitions from the local truth table yields exactly 110,40,24,12,8,4,0 ordered pairs of distinct surviving states after successive common labels. Thus any nonempty output word of length six synchronizes all nonempty states. This finite *exhaustive* synchronization lemma propagates every accepted length-7 window to the full arbitrary word, proving the exact six minimal forbidden words (four of length 5, two of length 7); no other minimal forbidden patterns can occur. For the eleven nonempty deterministic states, the independently reconstructed integer adjacency matrix obeys (M^5-2M^4+M²-I)1=-e_15, with no transition to 15, giving the full recurrence. Independent exact characteristic polynomial factorization gives t(t^5+t²-1)(t^5-2t^4+t²-1); Perron growth gives the asserted entropy and its unique real root >1. Independent direct block languages through n=13 match 1,2,4,8,16,28,50,88,156,278,496,886,1582,2824. The infinite SFT/recurrent conclusion follows from exact DFA and matrix identities, not finite extrapolation.

## originality

PASS

Kůrka's full relevant Example 7 computes blocking words, attractors, signal/column subshifts and temporal zero entropy for the same rule, but not the one-update *spatial image* language or positive spatial image entropy; he explicitly gives first-image graphs for other elementary rules. Kari–Taati studies general preinjective/surjective maps and Gibbs entropy, not an evaluated Rule 232 one-step SFT. A forgotten automata catalogue may already encode this exact six-word image, so priority is qualified.

## value

PASS

The first spatial image of the elementary majority rule is a canonical dynamical object distinct from the temporal action and long-time attractor. A complete six-word minimal SFT presentation, exact rational all-length word enumerator and explicit spatial entropy are substantive intrinsic invariants; the sharp forbidden-window length 7 has structural significance for recognition and further symbolic-dynamics calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
