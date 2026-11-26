# Independent mathematical audit

## correctness

PASS

Under the independent Gaussian noise specified in the Finding and the standardized observations in the assumptions, Gaussian regression yields E[X_i|Z_i]=√ρ Z_i. The variance of the posterior mean is the risk reduction. Fixed pair {1,2} gives ρ²; each pair containing 3 gives a²ρ. For adaptive policies, condition on both the first reading and any independent decision random seed. If a product coordinate is read first at z, the two remaining gains are the conditional squared-norm increments of the posterior mean, ρ²z² and a²ρ. The second label is a function of the first observation and seed, so introduces no additional state information under that conditioning. Revealing the seed cannot lower the optimal expected reduction, and deterministic thresholding attains the conditional upper bound. When coordinate 3 is first, every second choice leaves the posterior mean unchanged. This exhausts all policies. With c=a²/ρ, the optimum ratio is E[max(Z²,c)]/max(1,c), strictly above one since the χ²₁ law has positive mass on both sides of c. Below one use the derivative Pr(Z²<c); above one use −E[Z² 1{Z²>c}]/c². Gaussian tail integration gives 1+2φ(1) at c=1, a unique positive a for each σ²>0; independently evaluated the decimal. Myopic sensing buys only the linear term. This is a ratio of reductions, not of posterior risks or realized losses. Analytic replay: condition on the first reading as above, then use ∫_r^∞ z²φ(z)dz=rφ(r)+Φ̄(r) at r=√c; decimal replay in the section labelled 3 of review_evidence/finite_checks.py. No parameter sampling is needed.

## originality

PASS

The distinct contribution is the exact two-stage Gaussian policy and sharp adaptive-to-fixed ratio, not Gaussian regression, general sequential planning or fixed quadratic design. Inspected primary adaptive and fixed-design comparators and indexed sensing findings do not state or imply that distinct claim. This is a bounded assessment, not a general priority certification.

## value

PASS

This gives a natural small benchmark where Gaussian measurements alone do not make posterior uncertainty reduction nonadaptive: nonlinear prediction makes the conditional second-step gain depend on values. The optimal first experiment has strictly less immediate information about the goal than the myopic choice, yet improves the two-step Bayes risk for every allowed parameter. The pointwise policy, unique balancing condition and sharp ratio quantify that structural contrast, without suggesting a bound for general designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
