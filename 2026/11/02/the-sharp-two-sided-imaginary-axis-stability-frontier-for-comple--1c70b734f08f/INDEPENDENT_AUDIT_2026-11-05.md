# Independent mathematical audit

## correctness

PASS

For c=a+ib, |1+iy-cy²|²-1=y²[(a²+b²)y²-2by+1-2a]. Convexity means two endpoint checks are necessary and sufficient. Each endpoint gives a closed coefficient disk with squared center distance minus squared radii sum equal ((R+S)²-4)/(R²S²). Thus existence iff R+S<=2; external tangency gives unique c at equality. Independent SymPy verified expansion, distance, and strict-interior factorization, including asymmetry. The corollary correctly restricts operator norm to normal matrices with both extrema present.

## originality

PASS

Mixed positive/negative frontier and unique complex tangent optimizer are more specific than the identified one-sided/real results.

## value

PASS

Natural exact design boundary for complex-coefficient two-stage time integrators facing both imaginary-frequency signs, quantifying improvement over real coefficients and asymmetry while proving uniqueness. This is not a routine substitution of one-sided optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
