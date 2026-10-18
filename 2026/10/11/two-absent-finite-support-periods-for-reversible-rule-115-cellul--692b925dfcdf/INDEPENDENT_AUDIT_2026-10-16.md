# Independent mathematical audit

## correctness

PASS

The exact Wolfram-115 truth table is f(a,b,c)=1+b+ab(1+c) over F2. A time-p-periodic orbit gives temporal spatial columns satisfying b_{t−1}+b_{t+1}=1+b_t+a_t b_t(1+c_t). For any zero entry b_t this forces b_{t−1}≠b_{t+1}, defining an exhaustive finite temporal alphabet. As both initial layers have finite spatial support, all distant sites follow the homogeneous period-three background, so every spatial path begins and ends at the graph vertex (B_p,B_p) and is confined to its forward/reverse root-reachable intersection; conversely any such finite path produces a finite-support trajectory. Independently reimplemented temporal words, rule comparisons and rooted reachability without using saved output or source execution. Exact (eligible words, forward vertices/edges, backward vertices/edges, root vertices) for p=3: (4,4/7,9/21,3), p=6: (10,46/121,45/159,27), p=9: (31,40/52,63/102,3), p=18: (973,5500/8590,8235/17484,27). Direct equality of full labelled rooted sets gives C9=threefold C3, C18=threefold C6, not just matching cardinalities. Thus any finite-support p=9 or p=18 trajectory already repeats after 3 or 6. This is exhaustive over temporal graph and unbounded in spatial support, not a small finite-window scan or timeout inference.

## originality

PASS

Formenti–Kamilya’s 2026 primary paper proves finite-support periods are multiples of 3 and identifies period 9 as attained only for infinite-support examples, while explicitly leaving finite-support period 18 computationally unresolved. These are motivations, not impossibility theorems, and do not imply either fixed-set equality. The exact root-component enumeration is new compared with that full primary paper in the inspected text. Other published cellular automata records found by Resultary concern unrelated rules or finite-volume reversibility; no stronger period-spectrum theorem covering this rule and both exclusions located. An unindexed later computation remains a risk.

## value

PASS

Periods 9 and 18 are exactly the concrete unresolved gaps identified by the 2026 motivating paper, not arbitrary cutoff numbers. Proving equal fixed sets excludes entire families of finite-support orbits with no arbitrary spatial bound, gives a reproducible compact temporal-state certificate (973 admissible words/27 root-component vertices for p=18), and distinguishes infinite-support period-nine phenomena from finite configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
