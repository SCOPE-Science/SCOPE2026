# Independent mathematical audit

## correctness

PASS

Algorithm 1 has the two cross-control terms with the same sign and applies its controls additively to descent in x and ascent in y. The leading-coordinate prescription is I in the equal-dimensional case. Independent block calculation: for symmetric K and eigenvalue s, the squared modal factor is 1+2ηβs+η²(β²+δ²)s². With β≠0 select a same-sign eigenvalue in the indefinite case; with β=0 the factor is at least one (exactly one when δ=0). In the positive definite case with β>0 every block expands by a factor bounded below by a fixed number greater than one, proving exponential growth of every nonzero state. For I and β<0 sufficiently small η contracts; changing y by diag(1,−1) makes the game indefinite if the coupling is reset to I. With A_c=K, independent left/right SVD coordinates give normal blocks with squared radius f(z)=1−2bηz+η²z(T+b²z), z=s²>0. This proves the strict L-controlled stability interval, including the unit-modulus boundary, and equality of the spectral radius with the Euclidean operator norm. Convexity in z reduces the envelope to μ² and L². For μ<L the crossing is η_e=2b/[T+b²(μ²+L²)]; the stationary point of the L-mode is at or below η_e, so the right branch is increasing beyond the crossing. The μ-mode stationary point lies on the left branch iff T≥b²(L²−μ²); otherwise the crossing minimizes. Substitution yields both stated squared factors; equality and μ=L reduce to the common or single-quadratic formula, respectively. The positive curvatures ensure uniqueness. This exact calculation is the proof; the uploaded NumPy/SymPy test was inspected, not executed. Its finite tests are not needed for the universal claim (and one odd-dimensional signed test includes a zero eigenvalue). No assertion about distinct gains, nonlinear or stochastic updates, or the continuous velocity controller is validated.

## originality

PASS

The assessed novelty is the obstruction for the printed leading-coordinate discrete update and the exact fixed-gain optimal-step transition for its aligned variant. Neither the consensus correction itself nor the spectral-shape framework is new. Actual algorithm and closest compared results support this distinction, with no exact equivalent found in the material checked.

## value

PASS

The indefinite sign witness rules out tuning the advertised identity-like coupling even in elementary bilinear games and isolates the dependence on how the coordinates choose that coupling. The aligned analysis then answers a practical mathematical question about exactly when improving the slow mode is capped by the fast one. It gives a sharp step and factor rather than a bound or a new name for consensus optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
