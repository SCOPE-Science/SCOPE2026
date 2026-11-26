# Independent mathematical audit

## correctness

PASS

Let c=ε/h, X=x/h and W=sqrt(v)/h. For a two-step return fix a coordinate with gradient magnitudes s,t and memories u,w. The memory equations give (1+β)u²=βs²+t², (1+β)w²=s²+βt²; equal displacement magnitudes give s(u+c)=t(w+c). If s>t the latter forces su<tw, but (1+β)(s²u²−t²w²)=β(s⁴−t⁴)>0; the reverse strict inequality is likewise impossible. This covers zero gradient coordinates as well. Thus memories agree with the gradient magnitudes and signed gradients are opposite; invertibility gives X and −X and the reduced equation (1), which conversely yields a prime-two orbit for nonzero X. Positive b disallows a vanishing spatial coordinate. Modulo overall sign the same-sign equations force equal magnitudes by comparing their opposite-monotone sides, yielding the a+b branch. In the opposite-sign sector equal magnitudes give the a−b branch. For unequal magnitudes x,z, subtracting the equations and the equations divided by x,z gives (1−2x)(1−2z)=2c/(a+b) and b(x+z)=2(a+b)xz. Their unique fixed sum S=(a+b−2c)/(2a) and product bS/(2(a+b)) satisfy the discriminant bound precisely at c<(a−b)²/[2(a+b)], since S>0. Conversely their distinct positive roots lie below 1/2 because S<1 and the product of 1−2x and 1−2z is positive. The relations make the two residuals equal (first subtraction) and equal after division by x,z (second subtraction); x≠z forces both residuals to vanish. At equality they collapse into the already counted antisymmetric orbit. The excluded zero-amplitude cases at the other two thresholds, counting modulo sign, and the limits {x,z}→{1/2,b/(2a)} agree with the claimed counts and representatives. Independent replay: python3 /workspace/review-evidence/check_frozen_math.py 2 eliminates one coordinate directly in each sign sector and uses exact real-root isolation in 16 rational parameter cases, including all three equality cases and on both sides of the merger. This does not assess stability. Frozen numerical substitutions are corroboration, not a proof of exhaustion.

## originality

PASS

The same reduced equation, antipodal bijection, first existence threshold and large-rate corner existence are due to Loh et al. The supported distinct finding is the exhaustive coupled census with its two further thresholds, boundary multiplicities and two explicit noncorner branches/limits. The checked statements do not establish these consequences, and alternative indexed update maps are not equivalent.

## value

PASS

The symmetric coupled quadratic isolates a natural solvable test of whether known corner existence accounts for all large-rate cycles. The answer is no: two additional cycles have explicit noncorner limits and a sharp merger, and the classification handles all rates, not just a perturbative neighborhood. The merger is an exact statement about the cycle equations, not an orbital stability claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
