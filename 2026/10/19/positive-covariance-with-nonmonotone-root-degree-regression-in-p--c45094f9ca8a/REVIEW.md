# Scientific review

## Correctness — PASS

The theorem fixes the initial edge, degree-proportional attachment, inclusion of the original root among possible leaves, and exact finite ranges. The identities are reconstructed directly from the attachment rule. The root-degree survival and degree-two recurrences give their identical probabilities. The conditional first-moment recurrences, initialized at three vertices, give the strict degree-one versus degree-two regression drop. The mixed-moment increment gives the nonnegative exact covariance sum and its strict positivity from four vertices onward. Standard central-binomial asymptotics and separately derived variance recurrences establish the limiting covariance and correlation coefficients. The packaged Python verifier enumerates all weighted attachment histories through nine vertices and checks 397 assertions; finite checks are corroboration, not the basis of the universal proofs. At \(n=2,3\), covariance is zero, and the conditional degree-two claim does not apply at \(n=2\).

## Originality — PASS, subject to historical-priority risk

The 2002 Krapivsky–Redner primary text supplies the exact finite global leaf-count process and selected global degree-count correlations; its scope does not evaluate the covariance of a *distinguished initial root degree* and global leaves. Brightwell–Luczak's degree-evolution/concentration theorem similarly does not provide the requested mixed moments. Peköz–Röllin–Ross treat finite collections of old vertex degrees, not the aggregate leaf count. Hartle–Krapivsky's later full text contains leaf-number fluctuation and local leafdegree statistics but not the present conditional root regression. A publicly reported identity for uniform recursive trees has the same variables but a different, uniform attachment kernel; its covariance converges to a constant, rather than growing on the square-root scale here. Existing moment frameworks could imply the exact formula after specialization, so absolute priority is not certified. The 1993 Mahmoud–Smythe–Szymański paper discusses leaves in branches in a closely related model, but its primary full text was inaccessible and is a residual risk.

## Mathematical value — PASS

The two statistics connect an age-specific hub mechanism to a global measure of tree shape. The nonmonotonic conditional expectation contrasts with positive total covariance, so the sign of aggregate dependence cannot be read as monotone regression. The two lowest degrees have identical positive probability at all finite sizes, making the contrast a natural rather than arbitrarily selected low-probability slice. The exact all-size sign and distinct square-root covariance versus vanishing correlation quantify finite-size dependence not resolved by classical marginal degree and leaf counts.

## Limitations and next checks

The result is limited to the two-vertex seed, one-edge degree-proportional attachment rule. Existing general generating functions and the inaccessible historical branch-leaf article leave residual priority risk. No corresponding claim is made for other preferential-attachment initializations or the complete bivariate distribution. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
