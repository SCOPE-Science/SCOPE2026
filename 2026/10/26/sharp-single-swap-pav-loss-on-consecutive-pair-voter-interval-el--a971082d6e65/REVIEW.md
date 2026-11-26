# Independent mathematical audit

## correctness

PASS

With k selected candidates there are 2k incidences; each adjacent selected pair corresponds to one twice-represented voter and subtracts 1/2 from that incidence total. Thus swaps strictly improve the score precisely when they reduce the selected adjacency count a (equivalently increase the number of one-runs). Removing the middle of a triple removes two adjacencies; if it cannot be swapped profitably, all zeros must have two selected neighbors, which with the specified counts forces alternation. At a nonoptimal local maximum only singleton and double-one runs remain. A zero with no selected neighbors gives an improvement by swapping out one member of a double. The patterns 1100, 0011, and boundary 011 or 110 also give explicit improving moves by moving the one beside the relevant gap into the adjacent zero. It follows that the a extra zeros, after paying one zero per interior gap, are either second zeros between two singleton runs or a boundary zero next to a singleton. A block of t singleton runs can pay for at most t extra zeros, because at least one double-one run exists and the block cannot touch both ends. Therefore a≤s where k=2a+s, yielding a≤floor(k/3). The displayed sharp word has exactly floor(k/3) doubles and only singleton-supported extra zeros. Deleting a singleton loses one run; deleting from a double leaves the run count unchanged but leaves every originally zero position adjacent to some remaining one. No swap can increase the number of runs. Alternation gives the global value and is forced at a=0. The k=3 word is a witness, not a uniqueness statement (its reflection also works). The package's finite checker was inspected rather than run; the all-k proof does not rely on it.

## originality

PASS

The inspected work establishes graph-based score encodings, global tractability, or different swap/greedy claims, not the exact worst stable obstruction on the specified path. The leading analogue shares both the score identity and 11/12 but concerns sequential construction on a cycle, rather than arbitrary one-swap local maxima on a path.

## value

PASS

Even the canonical path of two-person supports has suboptimal local maxima, although its global optimum is immediate. The exact floor correction gives the first obstruction and a sharp quantitative guarantee for every size; the singleton-run charging proof identifies why the loss is limited. This separates the performance of fixed-size local exchange from tractability of global optimization on a natural restricted election domain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
