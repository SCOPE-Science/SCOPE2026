# Independent mathematical audit

## correctness

PASS

The published MSD interval construction partitions irrational-circle endpoints from negative indices -(c+1),-(c+2). At c=F_k-2, their right-shift chains share all indices -F_(k-1),...,-F_2, yielding k distinct endpoints and <=k states. The lower bound uses the rotation identity F_t phi-F_(t+1)=(-1)^(t+1)phi^-t and the Fibonacci-word coding interval (gamma,2gamma). The k valid prefixes 0,F_2,...,F_(k-1), plus q=4 when k odd or q=6 when k even, have pairwise inequivalent residual functions under suffices of zeroes: F_i prefixes have different last disagreements with baseline at depths k-1-i; q matches F_2 after positive depths but disagrees at zero depth. This proves >=k by Myhill–Nerode on allowed inputs, hence exact k. A newly written Zeckendorf/rotation integer checker verified 31 individual shifts k=5..35 and all k residual distinctions; they corroborate the all-k inequalities.

## originality

PASS

Moradi–Popoli–Shallit–Vukusic prove only logarithmic-size MSD upper construction (their Theorem 4.1/3) and separately an exact LSD-first minimum; their MSD result does not state or imply the matching k lower bound for c=F_k-2. The other linear-subsequence paper studies different operations. The new result is an infinite family of exact MSD MINIMA, not a generic bound or relabeling of an LSD formula.

## value

PASS

For a canonical sequence of Fibonacci-numeration shifts, it converts the recently published O(log c) construction into a sharp minimal DFAO state count, giving explicit infinitely many distinguishing residuals. An exact natural automata complexity invariant without solving every possible shift is useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
