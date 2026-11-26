# Independent mathematical audit

## correctness

PASS

For a fixed primitive root and over C, the revised primary Theorem 4.13 gives the additive Chow groups with multiplicity n! r^s/((n−s)!∏j_i!), with the j_i≥2 in their chain order; the shifts are 1 through j_i−1. Odd cohomology vanishes by the blow-up decomposition along products and their corresponding arrangement strata, so these Chow ranks are the rational even Betti numbers. The empty jump tuple supplies (1+t)^n. Ordered jumps give a geometric series of exponential jump terms, yielding the displayed F. To check the PDE directly, put a=1−(r−1)t, E=exp(r(1−t)z) and D=1−tE. Then ∂_z log F=a+rt(1−t)E/D and ∂_t log F=−1/(1−t)−(r−1)z+(1−rtz)E/D. The fractions with denominator D cancel in (1−rtz)∂_z log F−rt(1−t)∂_t log F, leaving 1+t+r(r−2)tz. Coefficients give the stated recurrence, which preserves constant term 1 and makes its top coefficient (rn+1)−rn=1. At each negative zero of P_n the derivative and P_{n−1} both have sign (−1)^(n−i); r−2≥0 including zero at r=2. Hence the next polynomial changes sign in every gap, at the left exterior gap by monicity and at the right by its constant term. The n+1 open intervals exhaust its degree and give simple negative zeros strictly interlacing the preceding row. Base rows 1 and 1+t cover n=0,1. Strict normalized Newton follows because the positive reciprocal-root elementary symmetric means have strict inequalities unless all roots coincide; multiplying by the component count does not change the conclusions for zeros or the inequalities. Independent integer evaluations via the EGF denominator at t=2 reproduce 147, 6075 and 465843 at (r,n)=(2,3),(3,4),(4,5), matching the coefficient table; replay with node /workspace/review-evidence/bounded-checks.js. These evaluations corroborate but cannot establish the recurrence or the all-n root conclusion.

## originality

PASS

The underlying additive ranks and the r=2 type-B case are prior; the supported distinct claim is the uniform simple negative zeros and strict consecutive interlacing for r≥3, giving the stated strengthened resolution of Conjecture 4.15. The closest colored-binomial symmetric component and the Eulerian and derangement transformations were compared by generating functions or low-degree polynomial identities, not titles. The inspected results do not give a specialization covering the claimed family. This is a best-of-knowledge assessment, not proof of priority.

## value

PASS

For r≥3 this resolves a specific geometric conjecture beyond the type-B regime and strengthens it to negative simple roots, strict interlacing across dimensions, and strict binomially normalized log-concavity. Those properties are not supplied by known Betti counts and are meaningful additional structure of this sequence of moduli spaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
