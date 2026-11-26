# Independent mathematical audit

## correctness

PASS

Centering and independence give conditional risk (1-α)²s+α²v/b; the one-step oracle minimizes this at bs/(v+bs), including α=0 at s=0. The minimized risk f_b(s)=vs/(v+bs) is strictly increasing and strictly concave, with 1/f_b(s)=1/s+b/v for s>0 and f_b(0)=0. The additive reciprocals and Jensen give pooled versus sequential dominance for all prescribed partitions; the squared norm after the first step is nonconstant for positive initial error and nondegenerate Gaussian noise, making the step-two inequality strict and propagating it. The stated dispersion identity follows by subtracting f_b from its tangent at the mean. At fixed d,b1,b2 and increasing initial norm, the first oracle update converges in L2 to minus its Gaussian block mean, so bounded continuous second-stage risk and the pooled limit give R_d(t) with Q_d=χ²_d/d. R_d<1 at all t>0 by strict concavity in Q, and the endpoint limits follow by dominated convergence (at infinity use (1+t)Q/(Q+t)<=2Q for t>=1). The derivative sign is that of the reweighted mean minus one. Weight ratios for increasing t are strictly increasing in q, hence that mean is strictly increasing by covariance. Its small-t numerator converges to 1 while its denominator tends to E[1/Q], infinite for d<=2, and at large t the rescaled moments give E[Q²]/E[Q]=1+2/d. The resulting unique minimum moves strictly upward in value with dimension by strict Jensen on the leave-one-out means at the minimizer for d+1. Gaussian quadrature of the derivative and risk, independent of the frozen erfc root algorithm, gave t=0.604867542154887602248340196450407322274728952 and R=0.68041531003775229177944465141633806949972205. Rational ratios are dense, justifying the infimum without asserting an integer optimizer. Three other split cases confirmed strict finite-signal improvement numerically (python /workspace/branches/independent_replay.py 3). The uploaded verifier was inspected, not run; the bounded replay is not the theorem's proof.

## originality

PASS

Pass for the exact same-budget ordering and the dimension-sharp two-block high-signal split theorem. The oracle step is an exact known specialization, and neither general minibatch tuning nor Jensen's inequality is new. The compared prior results do not supply the remaining sequential-risk ordering together with the optimizing Gaussian split.

## value

PASS

This is a fixed-gradient-query benchmark for the benefit of observing one intermediate state before reoptimizing the next step. It gives universal non-strict dominance within the additive-noise model and a strict, exactly optimized Gaussian benchmark rather than a rate bound or tuned single example. The dimension-monotone loss of benefit and the nontrivial asymmetric optimal split are useful distinctions. The 31.958…% gain is high-signal and two-block only, with exact population information; it neither optimizes finite-signal multi-block methods nor predicts runtime or practical training performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
