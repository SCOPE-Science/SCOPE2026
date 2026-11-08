# Independent mathematical audit

## correctness

PASS

Let X>=kappa satisfy both families and Y=X-kappa. The j=2 upper bound gives E[Y]<=1. Summation of moment inequalities through monotone convergence gives (1-u)^{-kappa}<=E[e^{uX}]<=(1-u)^{-kappa-1} for 0<=u<1. With lambda=3/(4sqrt(kappa))<=1/16, the centered MGF satisfies M_Y(lambda)>=exp(9/32), M_Y(2lambda)<=(8/7)exp(9/7). Pointwise [(e^{lambda y}-1)^2]<=lambda*y*(e^{2lambda y}-1)/2 and Cauchy-Schwarz imply (M_Y(lambda)-1)^2 <=lambda E[Y](M_Y(2lambda)-1)/2<= (1/32)*((8/7)e^{9/7}-1). Rational bounds yield the strict contradiction (431649/4194304)>(23/224), with difference 6887/29360128. All steps hold for every real kappa>=144; the finite verifier checks only the terminal rational inequalities. I independently recomputed the exact rational bounds and analytic inequalities.

## originality

PASS

The relevant September 2026 Wikström work introduces the certificate and, according to the assigned source discussion, has a finite polynomial dual obstruction at a single shape kappa=50 and certain discrete verified shapes; a uniform real high-shape infeasibility theorem is a strictly stronger shape-quantified statement. The full Wikström preprint was inaccessible in this run, including authorized institutional access, so that assertion about the specific Proposition 7.3 is based on the source discussion and indexed material rather than independent full-paper reading. Best-of-knowledge originality survives with prominent risk and does not claim the radius fails.

## value

PASS

Uniform infeasibility of a natural sufficient moment-measure criterion for an entire real tail is a structural limitation of a recognized analytic method. It identifies a genuine boundary of applicability, not merely a one-shape numerical dual certificate or a cheap normalization check. It may guide future searches for alternative Fock-radius techniques.

The dated certificate retains the supplied scientific assessment, sources and limitations.
