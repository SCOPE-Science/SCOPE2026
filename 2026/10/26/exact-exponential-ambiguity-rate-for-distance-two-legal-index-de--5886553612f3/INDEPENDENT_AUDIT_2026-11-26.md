# Independent mathematical audit

## correctness

PASS

Moura et al., Proposition 2.3, gives the needed recurrence and initials. It implies increasing positive terms and a_{j+3}−a_{j+2}=a_j for j≥1, hence the sum through n−3 equals a_n−4, including the endpoint n=4. Distinct legal index subsets are independent sets in two disjoint paths on the odd and even indices. Their Fibonacci counts, with empty-path count F_2=1, multiply to D_j. All legal subsets through n−3 qualify, and positivity forbids indices n or later in a representation below a_n. This squeezes the numerator, counting collisions with full multiplicity and the empty sum once. The cubic has no nonpositive root and strictly increases from −1 to a positive value between 1 and 2; its positive root satisfies ρ⁻¹+ρ⁻³=1. Dividing the recurrence by ρ^{j+1} traps a_j/ρ^j between the positive minimum and maximum of its first three values by convexity. Binet's formula yields D_j=Θ(φ^j), proving the claimed Θ estimate and root limit. Testing the cubic at φ proves ρ<φ; the pointwise maximum is at least the mean. Independently, review_evidence/reproduce.py 4 builds a weighted sum histogram from the greedy mex rule with a two-bit legality state through n=18 and checks the prefix sum, D_j and numerator bounds. The exact growth base is about 1.104029578062806; the frozen approximate decimal differs by under 1.5×10⁻¹³ and should not be read as correctly rounded to all printed digits. The exact expression is correct.

## originality

PASS

The recurrence and the method of comparing counts and thresholds are prior. No inspected source supplied the cutoff-sensitive Fibonacci-product bounds or the resulting S={2} mean multiplicity exponent. This is a best-of-knowledge determination of the stated singleton result, not of absolute priority or a general S theorem.

## value

PASS

This resolves the exponential-rate part of a published mean-multiplicity question at a structurally natural boundary case. The finite shift comparison explains why legality entropy dominates numerical term growth, a fact the sequence recurrence alone does not quantify. The contribution is limited to the stated mean rate and useful finite bounds; it does not give a limiting prefactor or a typical-point multiplicity law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
