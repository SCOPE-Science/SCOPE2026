# Independent mathematical audit

## correctness

PASS

The count is for normalized positive solutions of Bogachev–Rozikov (2.31), for a homogeneous reduced field (α,0,0), not for arbitrary multi-component fields or all Gibbs measures. In the k=3 normalization write the coordinates (u,v,1), w=θ^α and D=w u³+v³+θ. The equations give u−1=(θ−1)(w u³−1)/D and v−1=(θ−1)(v³−1)/D. The v=1 branch gives w u⁴−θw u³+(θ+1)u−2=0; there are at most three positive roots by the signs, independently confirming the applicable source bound. At θ=1 the normalized solution is unique. For v≠1, division gives D=(θ−1)(1+v+v²), so w u³=L=(v+1)(θv−v²−1) and u=(p+L)/(1+p) for p=v+v². Necessarily L>0, so this branch is empty for θ≤2. For θ>2 put x=v+v⁻¹. Direct reduction gives K_1=(θ−x)(x+1)³/[(x+2)(θ+1−x)³] on 2<x<θ. Logarithmic differentiation has sign given by (θ+2)R_θ(x), confirming the bundled identity by a different route; its denominator is strictly positive. The endpoint values 3(3θ−7) and −(θ+1) and the vertex (θ−3)/2 give no interior zero for θ≤7/3 and one otherwise. Thus at most two x roots per positive level, each with two possible reciprocal v, each fixing u. Any further mixed-branch restrictions only reduce the count. The zero-field equality follows from source Theorem 2.11(b); it can also be checked directly for θ>5/2, when the single-colour polynomial at w=1 has the root 1 and a cubic quotient positive at zero and infinity and negative at 1. The two distinct non-unit roots give six distinct permutations of one distinguished colour after normalization, in addition to the all-ones solution. The packaged verify.py was inspected, not run; an independent exact algebraic expansion corroborated the derivative identity, and the global sign-shape proof is analytic.

## originality

PASS

The no-field sharpness is prior, as are the branch reduction and reciprocal symmetry. The distinct claim is the uniform seven-solution upper bound for the single-distinguished-colour field in the q=3, k=3 case left by Conjecture 2.2. The inspected primary results and closest indexed records do not supply or imply that count.

## value

PASS

This handles a natural case of a stated counting conjecture, not an arbitrary slice: the smallest nontrivial Potts state count at the first tree order beyond the known arbitrary-field result. Bounding each mixed level uniformly, rather than merely locating existence or nonuniqueness, gives the strongest possible numerical cap for this parameter family. This neither classifies all Gibbs measures nor resolves the universal conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
