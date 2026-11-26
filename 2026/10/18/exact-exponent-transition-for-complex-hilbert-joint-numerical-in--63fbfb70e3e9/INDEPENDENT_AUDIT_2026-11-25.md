# Independent mathematical audit

## correctness

PASS

With inner product linear in the first slot, multiplying the four quadratic evaluations at x+i^r y by i^r selects 4⟨Sx,y⟩; the sum of squared argument norms is 8 for unit vectors. Thus ||S||≤2w(S). For signs ε_j, Hölder duality bounds w(sum ε_jT_j) by k^(1/q) w_p with 1/q=1−1/p, also at p=1 using ℓ∞. On every unit input x, expansion and cancellation over all signs gives the exact mean ||sum ε_j T_jx||²=sum ||T_jx||². The largest signed operator norm therefore dominates the joint 2-norm; no attainment of an operator-norm supremum is needed in infinite dimension. For p≤2 the factor k^(1/p−1/2) relating joint p- to 2-norms combines with k^(1/q) to give sqrt(k). For p≥2, the largest individual norm gives k^(1/p) instead. The common-source tuple has all products zero, joint norm k^(1/p), and numerical radius max |a| ||b||_p over |a|²+||b||₂²≤1. The coordinate norm inequality is attained by uniform magnitudes below 2, an arbitrary Euclidean output direction at 2, and a single coordinate above 2, in each case with |a|=||b||₂=1/sqrt(2). The dimension assumption gives the orthogonal input and k outputs, k=1 agrees with the scalar value, and the proof covers all tuples in the lower bound. Inspected the supplied finite checker without executing it. Independent exact small-vector sign moment and four witness-ratio checks agreed; replay python3 /workspace/branches/independent_finite_checks.py (check 4). These samples are not an all-operator verification.

## originality

PASS

Credit Mal's exact p=2 and p>2,k=2 cases, the known rank-one witness idea, and the known general lower bound. The high-p all-k equality is a direct extension by using Mal's lower bound and evaluating the same p=2 witness with the ℓ_p≤ℓ_2 inequality, not the case for substantive novelty. The supported distinct result is the sharp unrestricted 1≤p<2 plateau for k>1 and hence its place in the phase diagram. The known signed Hölder estimate is a component, not the precise universal joint-index lower bound; the proof needs the additional second-moment control on joint operator norms. The result is not presented as new for p=2, k=1, or the already covered and mechanically implied high-p cases.

## value

PASS

Below the Euclidean exponent, settling the sharp comparison simultaneously for every k>1 resolves a natural missing quantitative invariant: the earlier generic bound is worse by k^(1/p−1/2), not a negligible special-case gain. The exact plateau and attaining vectors explain how joint geometry compensates for changing p, including the endpoint p=1. The known high-exponent branch and witness origin do not independently supply novelty or value. No smaller-dimension assertion or classification of all extremizing tuples is needed or claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
