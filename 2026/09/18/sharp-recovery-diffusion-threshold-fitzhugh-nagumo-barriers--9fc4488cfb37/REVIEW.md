# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

For a fixed positive piecewise-C2 profile V and a proportional recovery profile W=cV, the symmetric activator inequalities reduce exactly to

\[
\frac{b_0}{a}V''\le h_V-cV,
\]

so c is admissible for the activator equations exactly when c<=c_*. The recovery inequalities reduce exactly to

\[
\delta cV''\le(\gamma c-1)V.
\]

Because the profile has positive curvature somewhere and delta is positive, this forces c>1/gamma. Negative-curvature points are then automatic, while positive-curvature points are equivalent to kappa_delta<=gamma-1/c. Since gamma-1/c is strictly increasing in c, existence of any c in (1/gamma,c_*] is equivalent to the stated criterion, and c=c_* is optimal. The interface inequalities agree because b0 and c are positive constants.

For the source paper's exponentially decaying D=0 profile constructed with auxiliary tilde_gamma, the initial tail satisfies the scalar barrier equation with equality. Hence its pointwise activator budget equals 1/tilde_gamma on the whole tail, while the global D=0 inequality gives c_*>=1/tilde_gamma. Therefore c_*=1/tilde_gamma exactly. The constant-D threshold and the left-tail upper bound then follow algebraically.

The explicit piecewise profile V=e^x for x<0 and V=1 for x>=0 was checked directly. The compact verification artifact confirms the activator inequality, verifies the recovery inequality below the predicted threshold, detects its failure above threshold, and reproduces the unbounded exact/sufficient ratio family.

## Adversarial checks

The result is intentionally restricted to constant-proportional recovery profiles W=cV for a fixed V. It does not prove that no nonproportional stationary barrier exists above D_sharp, and it does not identify the dynamical propagation/blocking transition. Calling D_sharp a global critical recovery diffusivity would therefore be incorrect.

The positive-curvature assumption matters. Without any point of positive curvature, the recovery inequality need not force c>1/gamma and the stated equivalence would require modification.

The saturation c_*=1/tilde_gamma uses the exponentially decaying source construction, where the far-left tail solves the scalar barrier ODE with equality. It is not asserted for the alternative source construction with a positive constant far-left tail.

The variable-diffusion statement uses the source paper's nondivergence recovery operator delta(x) W'' and its interface condition [W']<=0. It should not be transferred unchanged to a divergence-form recovery operator.

The explicit linear-reaction example is an example under the hypotheses of the source persistence theorem once a D=0 barrier is supplied; it is not presented as satisfying every bistable hypothesis used elsewhere in the source paper's separate constructive theorem.

## Originality

PASS, to the best of our knowledge.

The full arXiv:2609.14944v1 text was inspected, including its symmetric D=0 barrier lemma, the constructive stationary-barrier theorem, the exponential-tail equation, and the proof of persistence for small recovery diffusion. The source proves a sufficient condition based on a global Lipschitz constant, but does not state an exact fixed-profile threshold, optimize over all constant proportional recovery factors, identify the positive normalized curvature as the complete diffusion budget, or give the unbounded conservatism example.

Searches using the exact title and arXiv identifier together with `recovery diffusion`, `stationary barrier`, `proportional`, `threshold`, `curvature`, `supersolution`, `correction`, and synonymous FitzHugh--Nagumo terminology did not locate a public source-specific derivation or correction.

The closest prior source found was Kajiwara (2018), which studies heterogeneous FitzHugh--Nagumo systems by a sub/supersolution method and introduces a Rayleigh quotient sigma(d,gamma) for a related linearized stationary problem. Its bibliographic record and abstract were inspected. The complete paper was not independently inspected here, so it remains the most plausible source that could contain a more general theorem subsuming part of the present criterion. Klaasen--Troy (1984) studies stationary waves in a double-diffusive FitzHugh--Nagumo system, but no evidence of the present source-specific fixed-profile criterion was found.

General sub/supersolution methods, comparison principles, stationary FitzHugh--Nagumo barriers, and diffusion-dependent stationary-wave theory are excluded from the originality claim. The source preprint is recent, so an unindexed author revision or discussion is an additional residual risk.

## Value

PASS.

The source theorem guarantees persistence only for a uniform small-diffusion regime. The present criterion converts that qualitative statement, for the natural proportional family used by the source, into a computable necessary-and-sufficient profile condition. It separates harmless concave regions from the positive-curvature bottleneck, shows that the exponential tail fixes the optimal proportional recovery coefficient, gives an unavoidable tail ceiling, and quantifies how conservative the source's global Lipschitz estimate can be.

This distinction is useful both analytically and for barrier design: improving the profile's maximum positive normalized curvature directly enlarges the certified recovery-diffusion range, whereas changing the proportional recovery factor alone cannot beat the tail-saturated source profile.

## Scope and limitations

The theorem concerns the one-dimensional stationary barrier mechanism of arXiv:2609.14944v1 with constant activator conductivity b0, a fixed positive piecewise-C2 activator profile, positive recovery diffusivity, and constant-proportional recovery components. It does not cover arbitrary W, divergence-form recovery diffusion, higher-dimensional barriers, the full nonlinear dynamical threshold for propagation failure, or the source construction with a positive constant far-left tail. Originality is qualified to the best of our knowledge.
