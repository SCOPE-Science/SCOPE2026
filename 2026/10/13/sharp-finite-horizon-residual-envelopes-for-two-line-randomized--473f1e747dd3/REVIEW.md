# Independent mathematical audit

## correctness

PASS

Let T(X)=(P₁XP₁+P₂XP₂)/2 for the two orthogonal row-complement projections and let a=(1−c²)/2. The restriction of H to either complement line has quadratic form a times the squared norm, so T(H)=a(I−H), and T(I−H)=(1−a)(I−H) since T(I)=I−H. This proves the exact law for all t≥1. The eigenvalues (1±c)/2 of H give G_t and the maximum first-step quotient (1+c)²/2; at c=0 every initial direction maximizes. The logarithmic derivative of G_t has positive denominator and numerator h_t=1+(2t−5)c+c²−(2t+1)c³. Its signs at 0 and 1 are opposite; uniqueness follows by factorization at t=1, strict monotonicity of h₂, and one sign change for t≥3. The positive increment 2c(1−c²) forces the root rightward. The root identity 2(t−1)c_t(1+c_t)(1−c_t)=(3c_t−1)(1+c_t²) excludes a limit below 1 and gives t(1−c_t)→1. Then the geometric factor tends to e⁻¹ and t times the prefactor tends to 1. The first-step quotient crosses one at √2−1, whereas each later expected residual is multiplied by (1+c²)/2<1. The boundary c=1 is used only by continuity, not admitted as a row geometry.

## originality

PASS

The fixed-geometry dynamics follow by evaluating a standard moment recursion, the 1/t rate is known generally, and the first-step scalar factor and numerical coherence threshold coincide exactly with earlier greedy Kaczmarz values. The supported distinct contribution is the all-start, all-coherence finite-horizon envelope for the IID residual observable, including its unique moving optimizer and sharp asymptotic constant. Neither the greedy theorem nor the inspected generalized rates or alternative two-row models give that result.

## value

PASS

The worst system varies with the horizon even though each fixed two-row system converges geometrically. The unique angle and 1/e coefficient give a concrete sharp benchmark for general last-iterate residual guarantees. The exact law also explains why an expected initial residual increase can coexist with strictly contracting later residuals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
