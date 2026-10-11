# Independent mathematical audit

## correctness

PASS

The one-impulse recurrence solves exactly: m_t=(1-beta_1)beta_1^{t-1}G and v_t=beta_2(1+beta_2)^{t-1}G^2. Substitution into the displayed bias correction gives the stated decreasing v-hat and the increasing kernel F_t from 1 to sqrt((1+beta_2)/beta_2). The gain is an expectation of F_N under a geometric N; stochastic ordering of geometric laws proves strict increase in beta_1 and bounded convergence gives the sharp beta_1-to-1 ceiling. At beta_1=0 the gain is 1. The source-default numerical value and ceiling were independently checked. Under the stated Adam convention, the impulse tail is asymptotic to a positive constant times (beta_1/sqrt(beta_2))^{t-1}, so summability is exactly beta_1<sqrt(beta_2).

## originality

PASS

Best-of-knowledge originality passes. AdaX's source contribution is exponential long-term second-moment memory, and the checked source record/implementation material supplies the recurrence and defaults. The audited theorem isolates the exact response to one sparse gradient, deriving the nonzero asymptotic second-moment weight, finite cumulative gain, strict beta_1 monotonicity, and sharp gain ceiling. The Adam summability condition is prior/contextual and is not treated as the novel component.

## value

PASS

Sparse or intermittent gradients are part of AdaX's stated motivation, so the isolated impulse is a natural diagnostic rather than an arbitrary adversarial input. The exact finite gain quantifies how long-term second-moment retention interacts with first-moment momentum, revealing both guaranteed summability and potentially large amplification when beta_2 is small. This precise transfer fact is useful for interpreting and tuning the method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
