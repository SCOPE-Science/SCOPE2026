# Independent mathematical audit

## correctness

PASS

Rechecked the corrected summable-spectrum claim and proof in repairs/2/RESULT.md. Full-support one-coordinate laws have the stated weak isotropy; sketch magnitude and sign do not affect the coordinate range. Independence and Tonelli give sum_j j^(-rho)(1-pi_j)^L. For L>=2 the cutoff equation has a unique root because its sum is continuous, strictly increasing above 1, and unbounded. Supporting-line slopes at the cutoff law are -L t^(-rho) on the support and at least this slope off it. Derivative sums are absolutely convergent by the probability l1 bounds. Strict coordinate convexity gives the unique closed-simplex optimizer, with finite support; full-support mixtures approach it by dominated convergence and cannot attain it. Substituting yields (m-1)t^(-rho) plus the squared-singular-value tail. The root diverges but is O(1/delta); a decreasing-function integral comparison bounds the discretization error by delta(1+log t), so t delta tends to 1. Thus the contributions inside and outside support have leading coefficients 1 and 1/(rho-1) in units of t^(1-rho). The best rank-L residual is the tail after L, giving the required ratio rho^rho. The original two-draw identity also checks: t^rho=1+2^rho lies strictly between 2^rho and 3^rho. The original checker and notes were inspected, not executed; finite coupon and floating-point checks are corroboration only.

## originality

PASS

Pass applies only to the repaired sharp Hilbert–Schmidt ratio for a fixed summable infinite spectrum. The original framing of the exact finite-budget allocation as part of the novelty does not survive: it is the deterministic-coverage, one-slot specialization of Błaszczyszyn–Giovanidis and is displayed in equivalent truncated form by Ji–Caire–Molisch. The repaired text cites this exact overlap and uses the allocation as a proof ingredient. In the strongest inspected asymptotic comparisons, the explicit gamma^gamma hit constant is for 0<gamma<1 with a growing finite catalogue; the gamma>1 bounds are order estimates for throughput–outage with an exponential miss objective. Neither result provides the sharp error relative to the rank-L tail in the summable regime. The countably infinite, full-support formulation is necessary for the question but by itself is not the novelty.

## value

PASS

The distinct sharp constant quantifies the price of repeated iid coordinate selection relative to the best rank-L approximation on the same summable spectrum. Even after per-budget optimization the factor can be large; it gives a calibration that a mere decay order, cutoff rule, or coupon-collector example cannot supply. The retained and unretained parts both contribute at leading order, so this benchmark is not obtained by identifying effective support alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
