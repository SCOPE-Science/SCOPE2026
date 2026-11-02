# Independent mathematical audit

## correctness

PASS

Used affine coordinates for any simplex S=conv(0,e_1,...,e_n). Every hyperplane projected simplex admits its scaled negative at factor 1/(n-1) by simplex Minkowski asymmetry; convexity then proves projection shadow-covering for all t. The difference body t*S + ((1-t)/(n-1))*(-S) decomposes disjointly by orthant (up to boundaries), giving exact volume polynomial sum_{j=0}^n binom(n,j)^2 t^(n-j)((1-t)/(n-1))^j, not a finite sample. The classical binomial-Legendre real-root identity makes the volume polynomial a product of positive real affine factors, so log-volume is strictly concave on t in (0,1); endpoint derivative signs give a unique maximizer. For t=1-z/n^2, the binomial coefficient series and its derivatives converge uniformly on bounded z to 1+(z-z^2/4)/n^2 at leading order, giving z->2 and gain 1/n^2. Independent exact SymPy reconstruction for n=2,3,4,5 confirms endpoint signs and dimension-four derivative factor -4(74t^3+57t^2-93t-11)/81 and ratio. Packaged verify.py inspected; limited samples are corroboration only.

## originality

PASS

Best-of-knowledge statement-and-implication comparison against actual primary mathematical results and indexed records. Prior premises/special cases credited; no decisive prior coverage found, with non-zero priority risks.

## value

PASS

The family is the classical universal-dimensional shadow-hiding example. Determining its unique parameter, sharp four-dimensional benchmark and precise decay of optimal volume excess addresses a canonical geometric quantity in the previously open projection-volume comparison program. The optimization is intentionally within the family, not a claim to solve the unrestricted supremum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
