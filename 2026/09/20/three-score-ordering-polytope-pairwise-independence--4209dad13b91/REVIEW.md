# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.  The result was rederived in three independent algebraic pieces.

First, for a fixed label \(i\), conditioning on \(X_i=x\) leaves the two
events \(\{X_j<x\}\) and \(\{X_k<x\}\) with the same marginal probability
\(F(x)\), because each of \(X_j,X_k\) is independent of \(X_i\).  The
two-event Fréchet bounds therefore give
\[
\max(0,2F(x)-1)\le
\Pr(X_j<x,X_k<x\mid X_i=x)\le F(x).
\]
Integrating over \(F(X_i)\sim U(0,1)\) gives the sharp numerical interval
\(1/4\le q_i\le1/2\).

Second, pairwise comparison probabilities are all \(1/2\).  Solving the
resulting four linear equations for the six strict ordering probabilities
gives the reversal form
\[
(a,b,c,b,c,a),\qquad a+b+c=1/2.
\]
The three lower bounds on labeled maximum probabilities are equivalent to
\(a,b,c\le1/4\).

Third, sharpness is explicit.  For independent \(U,V\sim U(0,1)\),
\((U,V,(U+V)\bmod1)\) is pairwise independent and uniform.  The third
coordinate is always the maximum when \(U+V<1\) and always the minimum when
\(U+V>1\), producing one vertex of the ordering triangle.  Coordinate
permutations give the other vertices.  Mixtures preserve every bivariate
product marginal, so barycentric weights \(\lambda_i=4q_i-1\) attain every
admissible point.

The conformal/rank formulas then follow by identifying the three possible
ranks of the test score.  The independently jittered formula is linear in
the single rank parameter \(q\), so its sharp CDF is obtained at
\(q=1/4\) or \(q=1/2\) on each interval.

The verification artifact checks the polytope formulas and barycentric
weights with exact rational arithmetic.  Its finite cyclic-torus
enumerations verify exact pairwise-uniform two-coordinate tables and
convergence of strict ordering frequencies to the claimed continuous
vertex.

## Originality

PASS, to the best of our knowledge.

The older literature used to select the question is the
limited-independence order-statistic line initiated by Kemperman (1997).
Its accessible abstract states that it derives often sharp bounds for
distribution functions and moments of associated order statistics when
each \(k\)-tuple is independent.  Okolewski (2017) extends that framework
to specified \(k\)-tuple copulas and linear combinations of order-statistic
distribution functions.  Okolewski and Błażejczyk-Okolewska (2025) gives
pointwise sharp bounds for linear combinations of joint distribution and
reliability functions of selected order statistics under \(k\)-independence;
its published remark explicitly recovers Kemperman's single-order-statistic
bounds in the pairwise-independent case.

Those sources concern symmetric functions of the sorted sample.  The
present theorem instead characterizes the probabilities of all six
*labelled* strict order patterns and the resulting rank distribution of a
designated observation.  Searches combining pairwise independence with
rank distributions, ordering probabilities, labelled maxima, and conformal
rank calibration did not identify an exact three-variable ordering
polytope or the displayed calibration envelope.

Conformal prediction sources inspected state the standard exchangeability
basis for finite-sample validity.  Barber--Candès--Ramdas--Tibshirani
(2023) treats nonexchangeability through weighted/robust procedures, a
different assumption and guarantee.  No inspected conformal source supplied
the exact pairwise-independence three-score law.

The principal residual originality risk is terminology.  The full text of
Kemperman (1997) and Okolewski (2017) was not inspected, and older copula,
precedence-probability, or order-pattern literature could encode the same
label-sensitive result differently.  This is a concrete residual risk, not
evidence of coverage.  The Fréchet step, torus construction, and the fact
that pairwise independence need not imply mutual independence are standard
ingredients and are not claimed as original.

## Value

PASS.  The theorem gives a complete feasible set, not merely a counterexample
or one-sided inequality.  It shows exactly what pairwise independence does
and does not retain from uniform rank calibration: every label is equally
likely to be its own extreme in the sense that minimum and maximum
probabilities coincide, but each such probability can range from \(1/4\) to
\(1/2\), with the three labels coupled by one sharp triangle.

The statistical consequence is direct.  With two calibration scores, the
standard discrete rank p-value can reject with probability \(1/2\) at its
first attainable nominal level \(1/3\), and an independently jittered rank
transform can have rejection probability \(3\alpha/2\) for every
\(\alpha\le1/3\).  This quantitatively separates pairwise independence from
the exchangeability assumption used by conformal rank arguments.

## Scientific limitations

The exact characterization is for three observations only.  The analogous
labelled ordering polytope for four or more pairwise-independent
observations is not determined here.

The sharp constructions have continuous one-dimensional marginals and
independent bivariate marginals, but their three-dimensional joint laws are
singular.  No claim is made that the same boundary is attained inside a
class restricted to absolutely continuous joint densities.

The conformal corollary concerns exactly two calibration scores and one test
score.  It is not a replacement for general conformal theory under
dependence.

The continuously randomized p-value is an independent rank jitter used to
turn a discrete uniform rank into an exact \(U(0,1)\) variable under
exchangeability.  It is not tie-randomization, since ties already have
probability zero.
