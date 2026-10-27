# Scientific review: A sharp logarithmic validation-budget frontier

## Correctness — PASS

The proof conditions on the exact training sign and the independent validation count. At the optimum it gives the strict \(3/4\)-majority binomial tail; beyond the optimum the state space closes on the two endpoints. Independence yields a finite survival product, while the \(B^{-1/2}\) binomial prefactor and an infinite-product test jointly prove the sharp thresholds at \(c=1/I\) and at the additional \(a=1/2\) correction. The two-state return impossibility establishes the permanent objective gap. The embedded standard-library verifier reproduced all transition probabilities by exact arithmetic for batches \(1\) through \(11\), covering \(24,564\) complete sign cases and four mixed-batch schedules. The infinite assertions are proved analytically rather than extrapolated from finite checks.

## Originality — PASS, with stated residual risks

The primary 2026 source's independent hypergradient validation/null step is a direct antecedent, but its comparison sits inside an adaptive recurrence and its convergence theorem requires relative gradient and function-value noise. The present noninterpolating example violates the gradient-relative condition at zero (the function-value condition alone may still hold on the discrete reachable states), and the inspected relevant sections do not give the exact all-time binary false-acceptance law, KL validation-budget threshold or half-log-log critical correction. The 2015 probabilistic Wolfe paper has a different GP acceptance criterion; the 2011/2013 variable sample-size and 2017 adaptive-sampling sources address related questions but their accessible descriptions do not show these exact statements. The latter two were not fully inspected, leaving real priority risk. Comparisons were also made with published searchable mathematical results on scalar stochastic preconditioning, finite-time absorption and optimizer stability; those do not imply this claim. See the structured comparisons and inspection limits in `AUDIT.json`. Classical binomial asymptotics and product criteria are explicitly credited as standard ingredients.

## Mathematical value — PASS

A finite validation batch may falsely certify a step away from an exact minimizer. The finding gives an exact, natural worst-horizon event law and a quantitative design threshold for protecting the optimum, including the boundary missed by Chernoff-rate-only estimates. It separates conditional finite-iteration accuracy from infinite-horizon sample-path integrity and shows the offset needed for high-confidence long-time retention. Both the failure and its batch-budget cure are useful interpretations of a common independently sampled descent check.

## Sources, limitations and risks

Primary source: Zhang--Gao--Ye--Udell (2026), dated May 28 at Optimization Online, Algorithm 2, Section 3 and Theorem 3.3. Related: Mahsereci--Hennig (2015), Krejić--Krklec Jerinkić (2011/2013), and Bollapragada--Byrd--Nocedal (2017). The theorem concerns only the precisely specified fixed-unit-step, two-loss, noninterpolating model with independent validation and strict rejection of ties. It does not claim nonconvergence of the complete adaptive algorithm or contradict its conditional theorem. Equivalent earlier reformulations and fuller comparison with inaccessible texts remain unresolved. No external independent mathematical audit has been completed.

Self-review: passed. Independent audit: not yet performed.
