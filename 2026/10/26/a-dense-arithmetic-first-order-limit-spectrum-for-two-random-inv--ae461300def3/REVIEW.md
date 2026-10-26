# Self-review: arithmetic and density of random-involution first-order limits

## Correctness — PASS

Independently uniform involutions yield bicoloured path or even-cycle components. For specified component types, the exact joint factorial-moment identity follows by assigning the labelled copies and independently extending both involutions on the complement; the involution-number ratio gives independent Poisson component limits. All Gaifman degrees are at most two. A closed rooted ball is an entire finite component, and its count is a finite linear combination of counts for bounded-size components. Any nonclosed rooted neighbourhood can be realized in infinitely many odd-order alternating path types, which each have limiting Poisson intensity one, so its count exceeds any fixed Hanf cutoff with probability tending to one. Effective bounded-degree Hanf locality then reduces any first-order sentence to finitely many truncated independent rational-intensity Poisson component counts. Their event probabilities are rational polynomials in a common exponential \(e^{-1/D}\). Distinct odd-path existence sentences give arbitrarily many independent asymptotic Bernoulli events, whose largest atom tends to zero; their Boolean combinations yield a dense set of limits. The exhaustive finite checker verifies the exact component identities but is not used to infer infinity.

## Originality — PASS (qualified historical priority)

Lugo, *The cycle structure of compositions of random involutions*, arXiv:0911.3604 (Theorems 4.1 and 5.1), establishes the alternating component decomposition and associated Poisson asymptotics. Those are input results, not asserted novelties. Mirabi and Shelah, arXiv:2607.11033, prove limit laws for different pruned sparse graphs and percolated tori; their model and formulae do not directly determine this two-involution probability spectrum. Classical Hanf locality is likewise acknowledged. Actual searches for random-involution logical limit laws, exact arithmetic spectra, monounary composition logic, and general bounded-degree convergence did not locate the full conjunction of the first-order arithmetic statement and density. Compton's 1987 general first-order combinatorial framework may imply an abstract convergence result; its full text was not accessible. No absolute historical-priority assertion is made.

## Value — PASS

The model is a natural symmetric pair of constrained random unary functions, with components of all lengths and nonzero limiting probabilities for any fixed component count. Determining the exact arithmetic class of probabilities and proving that logical probabilities are dense despite convergence gives substantive global expressive information, not a single component count or finite enumeration. The result displays a convergence-but-not-zero–one phenomenon with explicit syntactic events approaching any target limiting probability.

## Verification and limitations

The standard-library program `check_involutions.py` enumerates pairs of involutions through size seven and checks 11 exact mixed factorial-moment identities at each size. It does not enumerate all logical sentences, establish the infinite limit, or rule out stronger inaccessible older results. The argument applies to a fixed language with two involution functions, and the derived effective computation is not claimed efficient.

Self-review: passed. Independent audit: not yet performed.
