# Independent mathematical audit

## correctness

PASS

At each modulus m=22 or 27, primitive residue pairs modulo unit scaling form exactly 36 free orbits. L(a,b)=(a,a+b) and R(a,b)=(a+b,b) are well-defined on orbits and realize the exact two-child Stern recursion on the shell [2^k,2^(k+1)). An independently written exact-integer BFS enumerated all primitive orbits for both moduli and their transition systems. It reproduced matching shell counts for the first 72 k, independently matched direct raw Stern values through k=13, and checked the 36 consecutive k=12..47 residuals for both moduli for c=(1,-3,4,-6,9,-13,14,-18,12,-16,0,32,-64). The residual sequence itself is a linear output of the 36-dimensional transfer matrix and satisfies its characteristic recurrence, hence 36 consecutive zeros force all zeros by Cayley–Hamilton. The first 12 equal coefficients plus the shared order-12 recurrence imply equal shell counts for all k. Equivalently 72 initial zeros for a block-diagonal 72-dimensional difference output imply equality for all k. Numerator terms (0,...,0,4,-4,8,-16,32) and claimed rational denominator independently recomputed. With s(0)=0, T(2^r;m)=1+sum_{k<r}Z_m(k), including r=0. The finite computation is combined with valid finite-to-infinite linear algebra, not mistaken for an infinite experiment.

## originality

PASS

Best-of-knowledge PASS for the all-r 22-versus-27 dyadic divisibility identity plus its explicit common order-12 generating function. Reznick 2006/2008 expressly labels this exact equality conjectural and checks only r<=19. Accessible general transfer/Markov results give individual rational generating functions and equal limiting density but do not force equality for two different moduli; this distinction is explicit in Reznick. Independent searches of published mathematics and Resultary found no statement that supplies this exact all-level equality. A plausible 2012 Reznick course-note treatment was not readable; its possible coverage and unindexed later work remain real priority risks rather than automatic FAIL.

## value

PASS

Resolves the specific universal Stern divisibility conjecture explicitly posed by Reznick in 2006/2008, not just its small-r empirical verification. The common exact rational shell series/order-12 recurrence is an additional reusable structural description of modular Stern distribution. This natural pair 22/27 is singled out by earlier modular distribution theory and appears as an open case rather than an arbitrary parameter slice. Exact computational certification is mathematically meaningful because the states and recurrence derive from the Stern recursion and Cayley–Hamilton. Scope limited to this pair, not a general modulus-pair classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
