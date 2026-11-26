# Independent mathematical audit

## correctness

PASS

Count the unchanged word once, then assign each nonidentity outcome to its earliest producing window. Outcomes from disjoint windows cannot coincide because their nonempty change sets lie in disjoint positions. A new window therefore needs comparison only with four previous windows, so the last eight input bits are a sufficient state. The exact initial vector at length eight and the suffix transition recurrence follow directly. The independent replay /workspace/replays/5.py used integer XOR change masks, direct whole-word unions for initialization, and the two predecessor states of each target suffix. It checked all 512 weights, all 256 components of V_(n+6)−V_n=19 at each n=12,…,17, and the maximum profile for lengths 5–23 (including whole-word exhaustive enumeration at 5–12). One statewise equality at n=12 already propagates to all n≥12 because the update commutes with a common shift; the finite base maxima plus that algebraic step prove the upper bound for all lengths. For the explicit periodic word the replay checked starts 0–9, covering all four truncated boundary cases and one full period of nine-bit windows, with gains 4,4,3,3,3,4,3,3,3,3. Thus for m=n−4≥2 the gain sum is 3m+2+floor(m/6), and the ball includes one further unchanged word. At n=5 the single block has at most five rotations, attained because a nonconstant five-bit word has period five. The proof is exact and computer-assisted; the optional periodic-word checks through length 60 are not the induction.

## originality

PASS

The closest indexed results give exact size laws for different operators or parameters. The cited primary source defines the identical fixed-window cyclic operator in general, but its inspected theorems address coding redundancy or use coarser ball bounds. Neither the all-length binary fixed-five maximum nor the exact six-step and extremizer statements are given or directly implied by those comparisons.

## value

PASS

The result gives the exact worst-case number of distinct received words in a previously defined channel, measuring how much overlap between nearby windows cuts down the naive sum of their outputs. It gives both the six-length correction and explicit words attaining it, data one can use directly to benchmark bounds on the local output sets. That is a motivated exact invariant, not a sampled table or a claim about code cardinality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
