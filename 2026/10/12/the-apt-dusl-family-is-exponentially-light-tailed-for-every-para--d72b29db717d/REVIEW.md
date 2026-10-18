# Independent mathematical audit

## correctness

PASS

For every fixed alpha>0 and xi>0, direct expansion of S_L(x)=(1+xi*x/(1+xi))exp(-xi*x) yields S_L~xi/(1+xi)*x*exp(-xi*x). The exact DUS tail 1-H=e(1-exp(-S_L))/(e-1) has derivative e/(e-1) at S_L=0, and the APT map has derivative alpha*log(alpha)/(alpha-1)>0 at H=1 (equal to one when alpha=1). Their product proves the stated K(alpha,xi)>0; differentiating the exact CDF yields f~xi*K*x*exp(-xi*x), so the hazard limit is xi. Tail integration for positive t proves the MGF converges precisely t<xi; for t<=0 finiteness follows from X>=0, and divergence at t=xi gives radius xi of the nonnegative-coefficient moment series. Explicit alpha=1 and alpha<1 parameter boundaries were checked analytically. The exact proof, not a finite numerical plot, supports all-parameter statements.

## originality

PASS

Best-of-knowledge originality judged against exact antecedent model, broader results, tables and mathematical implication. The new complete statement is not covered by the inspected sources; the named residual risks and incomplete full-text material prevent any claim of exhaustive priority or external certification.

## value

PASS

The source treats parametric tail control and apparent ability to handle heavy-tailed lifetime data as material reasons to adopt the model. The analysis proves that alpha never changes the exponential rate, asymptotic hazard, or positive-MGF boundary, ruling out genuine heavy tails under the standard exponential-moment definition. This is a targeted correction of a consequential model interpretation, not merely a routine renaming of a distribution; asymptotic and finite-sample flexibility are carefully distinguished.

The dated certificate retains the supplied scientific assessment, sources and limitations.
