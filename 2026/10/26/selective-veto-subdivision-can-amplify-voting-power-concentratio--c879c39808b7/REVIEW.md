# Independent mathematical audit

## correctness

PASS

The m minimal winners are exactly the veto bloc united with each respective committee. Each veto seat has normalized DP weight 1/(a+t); each committee seat has weight 1/[m(a+t)], yielding C(t)=(mt+a)/[m(a+t)^2]. Clearing the positive denominators in C(t)-C(1) leaves (t-1)[m(a^2-t)-a(2a+t+1)]. The ratio is the product of (t+a/m)/(1+a/m)<t and ((a+1)/(a+t))^2<1; along m=a^2 both factors approach their bounds. For the one-to-two comparison, m<=2 or a=1 cannot work, a=2 needs m>=8, a=3 needs m>=4, and a>=4 needs m>=3. At the only other a>=4 borderline with a*m=12 and m>=3, (4,3) fails. Thus 13 is sharp within the family; the gain is 1/1600 at (3,4). The adjacent comparison numerator is m[a^2-t(t+1)]-a(2a+2t+1), strictly decreasing in t; C(t) tends to zero. An independent full Boolean-coalition scan, testing winning status and all immediate predecessors for both t=1 and t=2 up through 13 pre-subdivision seats, found only (3,4) with a gain. Replay: python3 /workspace/review-checks.py (voting section); the finite scan is not used to justify the all-parameter result.

## originality

PASS

The definition, the squared-index form, and uniform all-player replication are prior. Relevant primary passages and the related indexed result do not provide the selective-veto classification, its sharp fixed-t envelope, or the minimal amplification witness in this family. The originality assessment credits the operation and its consequences, not the direct evaluation of the index by counting memberships.

## value

PASS

The perturbation isolates a natural design question that uniform replication does not answer: whether replacing a veto by several jointly required seats necessarily reduces power concentration. The exact opposite-regime criterion, almost t-fold gain, in-family minimum, and one-turn dependence give reusable benchmarks. The minimum is not a claim about arbitrary voting games, or about normative institutional desirability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
