# Independent mathematical audit

## correctness

PASS

Lebesgue marginal gives equal inverse-branch weights. Writing c=cos(2πx) and P for their averaging operator, the first conditional moment solves m₁=c+αPm₁, hence is c; P kills c and I−αP is invertible. The conditional variance solves v=α²P(c²+v), yielding α²[(1−α²)⁻¹+c]/2. To check the cubic directly rather than subtracting raw polynomials, condition on the previous base point U. The new forcing is c(x) on both branches; after subtracting c(x), the ordinate is α times the old ordinate. Thus κ₃=α³P(κ₃+3cv+c³), with Pc³=0 and P(cv)=α²(1+c)/4. Resolving this equation gives the claimed κ₃, as P kills c on the next iteration. These recursions work in L∞ or L¹ under the stated moment assumptions. The variance has a positive lower bound when α≠0 and vanishes at zero. For negative α the prefactor reverses the inequality; the two zeros pertain to the continuous representative. Arc length gives the increasing proportion with limiting values 0 and 1/3. Integrating the raw profiles yields the stated global moments: the variance gives |α|, the cubic separates its two signs, and α=0 is handled separately. Independent replay, python3 /workspace/frozen_math_replay.py 2, compares direct dyadic-history cubics for ten parameter/base pairs at truncation depth 17, allowing for the discarded tail. This corroborates, but does not prove, the functional identity.

## originality

PASS

The established map, transfer operator and exact conditional variance are not the distinct contribution. The inspected prior results leave the conditional cubic unevaluated, including its sign-region measure and the signed identifiability it yields. No stronger evaluated law has been identified in the accessible comparisons.

## value

PASS

The first conditional moment that distinguishes the contraction sign gives a sharp qualitative distinction: all fibers have positive skewness for positive contraction, but a negative contraction has a varying positive minority despite a positive global third moment. The explicit proportion and a minimal pair of global moments recovering the signed parameter make the cubic identity useful as an exact benchmark rather than another unevaluated moment recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
