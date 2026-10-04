# Review

## Correctness

PASS. The proof uses the randomized probability integral transform to obtain
the exact tie-corrected identity
\[
\operatorname{Var}(F_{\rm mid}(X))
=
\frac{1-\sum_i p_i^3}{12}.
\]
A direct iid-sign calculation gives
\[
\mathbb E|X-X'|
=
4\operatorname{Cov}(X,F_{\rm mid}(X)).
\]
Cauchy--Schwarz therefore yields the claimed constant. Its equality condition
is fully reconstructed: \(X\) must be affine in its mid-distribution value,
which is equivalent to adjacent support gaps proportional to adjacent mass
sums. Jensen's inequality supplies the support-cardinality corollary and its
unique equality profile.

The order-statistic corollary follows from exact identities for the iid
minimum and maximum and uses reflection symmetry only to equalize their
variances.

## Originality

PASS, with a residual older midrank/L-moment risk. The complete 2014
Čiginas--Pumputis preprint was inspected at its definitions and its exact
finite-population gap formulas. It compares Gini and variance but does not
give the cubic atom-profile correction or the fixed-mass equality geometry.

The complete La Haye--Zizler paper was inspected. It proves the classical
continuous-constant Gini--variance inequality by Cauchy--Schwarz and
characterizes continuous uniform equality. It does not state the
\(1-\sum p_i^3\) sharpening or optimize atom locations for prescribed masses.

Papadatos's full discrete order-statistic paper was also inspected. Its
equal-weight min--max theorem gives the same cardinality constant in the
uniform-probability case and is credited explicitly; it does not state the
arbitrary mass-profile Gini theorem or the nonuniform symmetric-profile
corollary.

Targeted semantic and web searches for the exact cubic atom term, fixed
probability profiles, mid-distribution covariance, and arithmetic-progression
equality did not return an equivalent theorem.

## Value

PASS. The classical Gini--variance inequality loses all information about
ties. The result replaces its universal constant by an exact probability-
profile constant and completely classifies the support geometry attaining it.
This is a natural finite-distribution extremal problem, not a recomputation of
a table. Its symmetric order-statistic consequence also supplies a
profile-specific extension of a discrete min--max correlation direction.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK identity_checks=72000 inequality_checks=24000 equality_checks=119600 cardinality_checks=48000 symmetry_checks=9000 uniform_checks=198`.
