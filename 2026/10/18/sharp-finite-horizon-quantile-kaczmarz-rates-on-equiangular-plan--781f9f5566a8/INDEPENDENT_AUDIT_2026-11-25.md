# Independent mathematical audit

## correctness

PASS

This PASS is for repairs/5/RESULT.md and SLOGAN.txt, not the frozen unrestricted retained-row statement. At x_0=x_star, m=4 and r=1, all residuals are zero after every projection, so all four rows are retained, not one as the frozen Finding states. The replacement gives the parity count only for nonzero post-projection errors, gives the count m for zero, and preserves arbitrary initialization for the moment identities. Independently, normalized squared residual is sin² of projective distance to the error-perpendicular line. The r nearest admit a consecutive r-block, and its doubled-angle geometric sum gives average removal at least 1−Q; additional cutoff ties can only increase this average. The block midpoint makes the bound exact (strict gap to the complement if r<m). A nonzero post-projection error has its perpendicular line on the grid: after the zero residual come equal pairs, with a possible singleton at projective distance pi/2 ranked last. This gives exactly the stated parity change for r<m and all m for r=m. The centered block then gives multiplier B, while at zero the same conditional equality holds because both sides vanish. The tower property gives every finite-horizon identity. At r=1 a least-residual row cannot erase a nonzero error and all later updates vanish; at r≥2 the multiplier is strictly below one, and nonincrease of squared norm plus bounded convergence gives almost-sure convergence. Direct Taylor expansion and the doubled-angle frame Gram sum give the stated rates and normalization. The supplied numerical checker and recorded 39,420 checks were treated as finite supplementary evidence, without executing the script.

## originality

PASS

The tie-inclusive algorithm and the uniform-sampling full-rank cutoff case are covered by prior work. The verified distinctive contribution, retained in the repair, is the sharp all-horizon law for adaptive rank r<m on this frame, particularly the change after the first step and the resulting even/odd factor. The at-zero correction itself is not claimed as new.

## value

PASS

The repaired theorem quantifies a concrete consequence of adaptive low-residual sampling even for a perfectly conditioned tight frame: sharp worst-case loss over any number of steps and a change at even ranks caused solely by inclusion of ties. The orientation reduction, parity, and m^(−2) contraction gap calibrate behavior not predicted by frame conditioning or uniform sampling. Correct handling of the absorbing zero state preserves that quantitative result for every deterministic initialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
