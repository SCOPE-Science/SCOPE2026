# Review

## Correctness

PASS. The probabilities that the sample maximum and minimum equal a given atom give the coefficient
\[
c_i=K_n(P_i)-K_n(P_{i-1}).
\]
These coefficients sum to zero, so the expected range is a weighted covariance between the support vector and
\[
z_i=c_i/p_i.
\]
Weighted Cauchy--Schwarz gives the claimed constant.

The equality geometry is valid rather than merely formal: \(z_i\) is the average of the strictly increasing function \(K_n'\) over the \(i\)-th probability cell, so the \(z_i\) are strictly increasing. Equality therefore produces a distinct ordered support and is unique up to positive affine transformation.

The unrestricted constant is the exact squared \(L^2\) norm of \(K_n'\). Subtracting the squared norm of its cell-average projection gives the stated positive atomization deficit.

## Originality

PASS, with explicit access and older-projection-literature residual risks. The complete Han--Wang--Wu arXiv text was inspected through its quantile representation, global expected-range/standard-deviation inequality, equality condition, and estimation section. It optimizes over the unrestricted square-integrable class and does not prescribe atom probabilities.

The complete Kozyra--Rychlik article was inspected through its main theorem, proof, special cases, and discussion of order-statistic differences. It normalizes centered \(L\)-statistics by Gini mean difference and explicitly identifies Plackett's standard-deviation result as prior context; it does not solve the fixed-probability support problem.

Plackett's bibliographic record and later primary description verify the classical global mean-range/standard-deviation scope. Its PDF required publisher-side human verification and was not treated as a full-text noncoverage certificate.

Targeted semantic searches for prescribed probability profiles, expected range, standard deviation, finite support, and support geometry did not return the profile constant, unique support shape, or exact projection-deficit formula.

## Value

PASS. Expected sample range is both a classical order-statistic functional and the modern higher-order Gini deviation. The unrestricted sharp constant does not say how much dispersion is lost when the probabilities of a categorical or empirical distribution are fixed. The theorem solves that finite-profile extremal problem exactly, identifies the unique optimal coding of the categories, and quantifies the entire gap to the global bound by a transparent \(L^2\) projection error.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK formula_checks=18000 monotonicity_checks=71616 bound_checks=18000 equality_checks=54000 deficit_checks=125616 global_norm_checks=18000`.
