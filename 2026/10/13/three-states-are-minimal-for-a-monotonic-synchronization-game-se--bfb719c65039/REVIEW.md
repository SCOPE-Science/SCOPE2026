# Independent mathematical audit

## correctness

PASS

One- and two-state nondecreasing complete binary automata are elementary: any synchronizing two-state pair has a constant letter, allowing Alice immediate victory. For fixed ordered three-state chain there are C(5,3)=10 nondecreasing maps and 100 ordered pairs. Independent complete-subset reachability and game attractor computation reproduced 77 synchronizing Alice-winning, four synchronizing Bob-winning, 19 nonsynchronizing, with exactly pairs (001,022),(002,122) and their swaps. Representative a=(0,0,1), b=(0,2,2) has reset word aa but Bob always plays b, returning the image to {0,2} after each alternating pair; a rigorous explicit strategy. The four form a letter-swap/chain-reversal orbit. This is an exhaustive finite classification, not a sample.

## originality

PASS

Fernau–Haase–Hoffmann (FUN 2022) already develop the game and monotone endpoint reduction and exhibit a four-state monotone Bob-winning example, not a sharp n=3 theorem. Fernau et al. (2024) explicitly exhibit a three-state unrestricted Bob-winning game, but one letter has a nontrivial two-cycle so no common order is preserved. Thus neither paper implies the three-state *monotone* boundary or four complete presentations. Other general reachability-game algorithms can decide specific cases but do not supply the exact census without running and proving the finite enumeration.

## value

PASS

The minimum number of states at which synchronizability and Alice-winning diverge within monotonic binary automata is a natural structural threshold, and the complete four-presentation first-layer classification closes a concrete gap left by published four-state monotone examples. It distinguishes ordinary reset words from adversarial alternating reachability. This is a motivated first boundary, not an arbitrary automaton slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
