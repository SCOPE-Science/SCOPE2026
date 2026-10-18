# Independent mathematical audit

## correctness

PASS

Substitute Delta_1=s(x-b), Delta_2=s(x+b), barDelta=sx into Algorithm 1 with M=2, giving T(x)=x-sx*max(1,(x^2+b^2)/(2(x^2+epsilon/s^2))). On the active branch with r=epsilon/(s^2b^2), T'(0)=1-s/(2r), thus |T'(0)|<1 iff r>s/4, with the inactive branch derivative 1-s. Solving T(x)=-x gives x_c^2=b^2(s-4r)/(4-s), positive iff r<s/4; at this cycle the branch ratio equals 2/s>1. Independent exact symbolic differentiation at x_c gives D=-(5rs-16r-s^2+3s)/(s(r-1)); solving |D|<1 gives s(2-s)/(2(8-3s))<r<s/4. At s=b=1,r=1/8, origin multiplier -3, x_c^2=1/6, D=5/7 and two-step multiplier 25/49. Only local stability and attraction claimed; algebra not inferred from simulated trajectories.

## originality

PASS

The FedExP originators analyzed denominator regularization and oscillatory behavior, but their inspected full-text oscillation illustration uses intersecting projection fixed sets and does not establish the underparameterized positive-epsilon 2-cycle or exact sharp epsilon threshold. The later FedExProx interpolation analysis does not imply the disjoint-minima cancellation example; Resultary same-claim search did not identify stronger matching coverage. Best-of-knowledge original in this narrow natural model.

## value

PASS

FedExP explicitly uses epsilon to safeguard cancellation of heterogeneous local updates. Demonstrating an exact sharp positive-epsilon period-doubling, a locally attracting nontrivial cycle, and FedAvg one-round convergence in the same client problem is a motivated algorithmic counterexample rather than a routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
