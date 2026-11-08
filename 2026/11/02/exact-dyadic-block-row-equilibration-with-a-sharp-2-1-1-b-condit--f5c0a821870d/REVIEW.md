# Independent mathematical audit

## correctness

PASS

For D constant on each block, ||DM||∞=max_q d_q alpha_q and ||(DM)^-1||∞=max_l sum_q C_lq/d_q. For any positive scales, set T=max d_q alpha_q, giving objective >=max_l sum_q alpha_q C_lq; equality at d_q=1/alpha_q proves K*. For dyadic d_q=2^{k_q}, normalize a maximizing block s to k_s=0. Replacing each other k_q by floor(log2(alpha_s/alpha_q)) cannot increase maximum forward norm and lowers inverse sum, hence one of exactly b candidates attains global unbounded-integer minimum. Largest circular gap of b fractional log2 alpha_q phases has length >=1/b, so integer shifts make all scaled log norms lie within width <=1-1/b; this yields K2/K*<=2^{1-1/b}. Diagonal block coefficients 2^{(q-1)/b} have equally spaced phases, forcing the opposite bound; works for arbitrary positive block sizes and b=1. Independent exact rational inversion/condition calculations on 56 small nonsingular examples agreed with complete bounded normalized exponent searches; finite checks corroborate, not prove, arbitrary n.

## originality

PASS

The standard continuous one-sided normalization is acknowledged classical. The b-candidate exact optimization and sharp dyadic/continuous factor for blockwise infinity condition numbers are not obtained from the inspected mixed-precision block-scaling premise or from general equilibration practice.

## value

PASS

Exact reduction from infinitely many dyadic exponent vectors to b explicit candidates is a useful global algorithmic structural fact, and the sharp universal loss 2^{1-1/b} quantifies the cost of radix quantization in a common numerical-linear-algebra setting. The b=1 boundary and arbitrary block size extremizers make the statement complete in its natural class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
