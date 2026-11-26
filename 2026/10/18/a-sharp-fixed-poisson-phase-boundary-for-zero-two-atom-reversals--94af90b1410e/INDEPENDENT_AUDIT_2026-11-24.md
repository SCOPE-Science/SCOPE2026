# Independent mathematical audit

## correctness

PASS

At Bernoulli mean alpha<1, the normalized quadratic coefficient is lambda^2/2 + lambda sum(t_i) + sum_{i<j}t_i t_j, with t_i=p_i/(1-p_i). For x,y>0 and s=x+y, the odds increment under merging is t_x t_y(2-s)/(1-s), so the ratio increment has sign lambda+T-g(s), where T is the other odds sum. Since T>=alpha-s and g(s)-g(alpha)=(alpha-s)/((2-s)(2-alpha)), a merge is strictly increasing for lambda>=g(alpha) if s<alpha; for s=alpha its sign is that of lambda-g(alpha). This proves the uniform bound, all ties, and the two-coin failure below the line. At a_lambda the single-coin ratio equals one and g(a_lambda)=lambda/(1+2lambda-lambda^2/2)<lambda for 0<lambda<sqrt(2). Adding a coin strictly increases the ratio at lower mass up to a_lambda; masses >=1 are already too large to compete, and single coins just above a_lambda give sharpness. At sqrt(2) pure Poisson ties, and positive arbitrarily small coins give strict reversal; above it pure Poisson attains the infimum. Ratios were used only for positive zero mass. Read the frozen script and evidence without executing it. Fresh exact truncated-convolution checks for four rational masses around g(alpha) and four rates around their reversal thresholds passed (review reproduction: /tmp/opencode/frozen-review-replay.py, section 3). These are finite corroboration; the merge proof handles all finite profiles. The supplied counter labels cases as assertions even though it also increments on some cases with no assertion; it is not a formal proof or a literal assertion count.

## originality

PASS

The supported increment is the prescribed-rate, fixed-Bernoulli-mean phase line with strict optimizer/tie determination and the consequent sharp prescribed-rate threshold. Neither the found free-rate threshold nor the adjacent-mode optimization gives this inequality and equality set. Standard coefficient extraction and fixed-sum pair variation are prior ingredients, not the originality claim.

## value

PASS

A fixed independent background intensity is a natural constraint and the free-rate threshold cannot predict how much Bernoulli mass is needed then. The phase line distinguishes exactly when concentrating the signal in a single coin is globally optimal, a tie regime, and when even an arbitrary two-way split improves it, uniformly over finite profiles. The result is useful beyond a numerical crossover or a standard Poisson coefficient calculation, but does not furnish a complete envelope below the line or for alpha>=1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
