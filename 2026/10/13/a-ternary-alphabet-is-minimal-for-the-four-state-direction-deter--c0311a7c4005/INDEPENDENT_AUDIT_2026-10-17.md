# Independent mathematical audit

## correctness

PASS

The unrestricted published four-state direction-determinate shortest-accepted-word maximum is binomial(4,2)-1=5. Direct independent simulation of the specified binary witness verifies its first accepted word is abba, length four; the ternary witness first accepts abbac, length five. For the binary upper bound, independently coded exhaustive C++ enumeration treats each of the four direction splits, all 625^2 two-letter transition-map pairs, all independently chosen left/right endmarker return maps (superset of actual machines), and both symmetry-inequivalent singleton accepting states when available; 101,562,500 configurations yielded exact split maxima 0,3,4,3. Singleton final state reduction is safe because any accepted shortest word remains accepted while no new shorter word appears. Initial state normalization and end-marker independent returns only enlarge the checked class. Hence no binary four-state machine reaches five. The published unrestricted upper bound and ternary construction finish the exact minimum alphabet proof.

## originality

PASS

Martynova–Okhotin prove the unrestricted 5 and construct it with a distinct letter for each of five consecutive input symbols; five-symbol construction does not imply a ternary one nor exclude binary. The general fixed-alphabet papers address asymptotic lower bounds and do not establish the exact four-state threshold in inspected material. Resultary query returned related reset automata but no direct result. Best-of-knowledge PASS; potential unpublished small-state census remains.

## value

PASS

Fixed-alphabet restrictions are a recognized distinct regime of 2DFA shortest-string complexity. The new exact smallest alphabet attaining the established 4-state extreme is a natural finite cutoff, with a nontrivial all-model exhaustive upper certificate and explicit sharp witnesses; this is not simply re-running the unrestricted formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
