# Independent mathematical audit

## correctness

PASS

For the revised theorem set d=max S≥2. gcd(S)=1 leaves only the simple unit-circle pole 1; strict monotonicity of the probability polynomial on the positive axis rules out other positive poles. There are nonunit poles because the polynomial has degree d, and the top partial-fraction coefficients there do not vanish. After exponential and polynomial normalization the dominant error is a bounded real sum of distinct nonconstant unit frequencies, so its Cesàro mean is zero and its mean square strictly positive. An eventually one-signed error would make the opposite part of the sum tend to zero and force its mean square to vanish. Coupled with the exact nonnegative-coefficient recurrence for e_n at n≥d, this excludes a one-signed block of d terms anywhere from n=0. For curvature, let R_i=u_i/u_{i−1}. A block of d curvatures starting at s≥1 on which all u_{s−1},…,u_{s+d} are positive has curvature signs given by the d consecutive ratio differences. At t=s+d the ratio obeys R_t=Σ_j (p_j u_{t−j−1}/u_{t−1})R_{t−j}, from the renewal recurrences at t and t−1. The coefficients are nonnegative, sum to one, and that of R_s is strictly positive because p_d>0. If the d differences have only one weak sign, this last-step convex average forces R_s=R_t, hence every ratio in the block equals some x>0. The recurrence then gives f(1/x)=1, hence x=1, and propagates the constant masses forever, a contradiction. Convergence to L ensures eventual positivity, even when p₁=0. Disjoint d-blocks give the four lower bounds 1/d. The truncated-geometric example has a raised first mass in each block and all other masses equal to its increasing baseline A_m. Its error is positive and its curvature negative exactly at multiples of d on the appropriate domains; this includes d=2 and proves sharpness of the common bounds. The analytic proof establishes the universal quantifiers. Independently authored Python exact checks reproduced the frozen sign counts (`python3 reproductions/frozen_math_checks.py`) and the repaired sharpness examples for d=2..9 with three ratios (`python3 repairs/3/verify_sharp_blocks.py`, 24 examples); neither constitutes a general proof.

## originality

PASS

Pass the repaired, sharp maximum-step block bound for curvature and the resulting sharp common 1/d lower density, not the original unquantified signs. The strongest inspected general sign theorem proves the original claim but supplies no d-block guarantee. The closest renewal envelope argument overlaps the error-block portion; it does not give the local ratio recurrence with time-varying weights, the curvature-block conclusion, or sharpness. This is limited to the inspected evidence.

## value

PASS

A sharp bound of d on the window needed to witness both signs is a useful local obstruction to curvature stability in finite-support renewal models and entails a law-independent quantitative density floor at fixed maximum support. It resolves a natural question not answered by density positivity, includes missing unit interarrivals after masses become positive, and the extremizers explain why no shorter common window can work. The repaired claim does not promise individual sign densities or universal onset without its stated positivity condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
