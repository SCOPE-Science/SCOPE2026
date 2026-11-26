# Independent mathematical audit

## correctness

PASS

The constant-drift ODE with absorbing value 1 at zero and Neumann data at L gives the stated two-exponential resolvent. On bounded drift sets, sqrt(a²+4Dr)−2sqrt(Dr) tends uniformly to zero and the reflected term after normalization has an extra factor at most exp[−2(L−x₀)sqrt(r/D)] times a bounded drift factor. The ratio of the ODE exponents is bounded by exp(|a|/sqrt(D)) for r≥1, yielding the needed whole-line exponential envelope. On [0,r^(-1/3)], sandwich the integrated drift between constant drifts V₀±sup|V−V₀| using the same independent spatial Brownian motion. The path differences are nonnegative AND nondecreasing, so their upper regulators differ by at most the final path difference; the absorbed hitting times are ordered when truncated to the horizon. The missing discounted tail is at most exp(−r^(2/3)), even after comparison. Continuity and the OU representation as a scaled time-changed Brownian motion on a bounded clock provide convergence of the drift bounds and finite exponential moments of the maximum for either allowed initial law. Dominated convergence then works for the unbounded Gaussian. The regenerative cycle mean is (1−pᵣ)/r and each cycle succeeds with probability pᵣ, so the mean is (1−pᵣ)/(rpᵣ). The Gaussian Laplace moment is exp[x₀² Var(V₀)/(8D²)]; the ratio of Gaussian-redraw to zero-redraw means is its reciprocal.

## originality

PASS

The same model, renewal identity, and generic frequent-restart asymptotics are known. A distinct catalogue result gives the exact same factor for bounded velocity laws, including deterministic velocity. The scope supporting this assessment is the nonperturbative protocol-dependent prefactor including arbitrary fixed-variance centered Gaussian redraw, not an originality claim for deterministic redraw by itself or for renewal.

## value

PASS

The exact factor discriminates reset protocols whose logarithmically leading cost is identical. The reciprocal Gaussian-to-zero limit quantifies a genuine relative improvement at a fixed activity and persistence, beyond merely transporting a known renewal formula. The Gaussian is the natural stationary velocity law and its unbounded tail makes the averaging step substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
