# Independent mathematical audit

## correctness

PASS

Distinct nonzero columns encode a spanning S⊂F_2^5\{0}, whose coordinate automorphisms are exactly GL(5,2) set stabilizers. Below length 9, |GL(5,2)|=9,999,360 exceeds binomial(31,8)=7,888,725; rank-deficient sets admit pointwise-fixing nonidentity elements. For n=9,10,11 every spanning S is equivalent to one containing the five standard basis columns: 14,950, 65,780 and 230,230 choices, exhaustively tested by compiled verify_lower.cpp and an independent review of its sound pruning; each has nontrivial stabilizer. Independent all-basis-image witness checking gives stabilizer one for nested sets of sizes 12–15; complements among 31 nonzero columns give sizes 16–19 and prove nonexistence for n≥20. Direct code paths verify_lower.cpp and verify_spectrum.py were inspected; lower checker recompiled and rerun: 0 rigid cases at n=9,10,11. No timeouts or random sampling.

## originality

PASS

The known smallest trivial-automorphism construction at length twelve does not imply all existence/nonexistence lengths for dimension five, especially the 19-column upper cutoff. Fixed-dimension full-support spectrum is distinguished from random-code asymptotics and from code enumerations without rigidity tabulations.

## value

PASS

For first useful binary dimension with rigid full-support codes, a complete attainable length interval is a natural code-structure invariant, with matching absolute lower and upper endpoints; the upper endpoint follows a nontrivial finite-projective complement obstruction. A researcher testing automorphism-free codes in fixed dimension can use exact feasibility, not merely a small instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
