# Independent mathematical audit

## correctness

PASS

For every finite n>=1, real symmetric commuting A,C share a common orthonormal eigenbasis, and C positive definite gives alpha_i=2c_i-lambda>0 under 0<lambda<2lambda_min(C). Starting from any nonzero x_k, weights p_i=x_{k,i}^2/||x_k||^2 are nonnegative and sum to one. The exact threshold ratio after the pulse/off interval is G(d)=sum_i p_i exp(-alpha_i epsilon+beta_i d), beta_i=2a_i+lambda. G(0)<1. For every d less than d*=epsilon min_{beta_i>0}alpha_i/beta_i every exponential is strictly below 1 (including beta_i<=0); hence no mixture triggers. A state supported on the minimizing eigenmodes reaches G(d*)=1, proving both the sharp minimum and all equality cases; adding any nonminimizing active weight keeps G(d*)<1. If the initial state has a beta_i>0 component, G(d)->infinity so the continuous convex function crosses 1 at finite d. If none, G(d)<1 for all d>=0; its gap is infinite/no next pulse, not 0. For the generic Banno bound set P*=I,Q=2C; lambda*=2c_min, mu=2|a_max|, and d*>=epsilon(2c_min-lambda)/(2a_max+lambda)>=2tau_min as long as beta_max>0. Boundary beta_i=0 has a factor exp(-alpha_i epsilon)<1 forever; tied modal minima allow arbitrary mixtures supported in the tied eigenspaces. Does not claim noncommuting/nonnormal cases, disturbances, uncertain parameters or arbitrary pulse lengths. Direct recomposition of all seven Git blob entries gave exact record-tree SHA 34c2a4904873118bc137b403c95a7a9220cc5fcf; read the full RESULT.md proof and verify_gap.py rather than relying on recorded VERIFY_OK. A separate 500-case test (n=1..9 random alphas/betas positive pulse dissipation) corroborated pre-gap exclusion and later crossing in 471 cases, with 29 no-trigger cases; not used as infinite proof.

## originality

PASS

Best-of-knowledge originality attaches only to the sharp infimum over initial states, its equality-mode classification, and the no-trigger support dichotomy in a commuting symmetric pulse/off system. The 2022 journal paper (Theorem 1, eqs 18–26) introduced the same architecture and gave a conservative uniform positive gap, not this exact modal minimax formula. The paper explicitly says its gap-existence result was added beyond its 2021 preliminary version. The 2018 intermittent-actuation abstract refers to a held piecewise-constant input, and 2019 planar inter-event analysis uses a relative sampling threshold. None of three Resultary queries returned a semantically equivalent exact modal formula; searches do not prove priority. The two inaccessible conference full texts and generic diagonal specialization risk remain explicit.

## value

PASS

The minimum feasible zero-input interval is the natural hard guarantee for intermittent actuators, fixed-duration energy packets and hardware duty-cycle scheduling. The formula isolates the precise worst spectral mode and characterizes all worst-case directions and the genuine never-retrigger subspace, including ties. It turns a qualitative/conservative generic gap guarantee into an exact arbitrary-dimensional answer and quantifies when controller inactivity is indefinitely safe relative to the chosen exponential threshold. Despite the short diagonal argument, the sharp optimand and equality/non-trigger classification are motivated by this precise scheduling question, not an arbitrary numerical slice, parameter substitution or known table. It is not advertised as a novel stability theorem or a robustness guarantee, and the generic literature contains much of the framework.

The dated certificate retains the supplied scientific assessment, sources and limitations.
