# Independent mathematical audit

## correctness

PASS

A labeled square specifies four pairs and leaves a uniform bijection on L-4 stubs per side. The expected number of parallel pairs using a specified edge is 4(d-2)(e-2)/(L-4); using only residual edges it is A_d A_e/[2(L-4)(L-5)] with A_d=L(d-1)-8d+12 and similarly for e. Any occurrence has the same conditional moment, so multiply the shift from the unconditioned mean by B=E[Y]. With a=d-2 and b=e-2, clearing denominator 2(L-4)(L-5)(L-1) gives coefficients 4(L-4), -4(L-4)(L-2) on each linear term, and 12(L-2) on ab, i.e. -4P. When only one excess degree is positive, P=(L-4)[(a+b)(L-2)-1]>0. When both are positive, L-4>=2max(a,b) gives (a+b)(L-4)-3ab>=ab and P>=2. Both zero give P=4-L. At L=4 there are 16 simple-square bijections and 8 doubled-diagonal bijections, giving -4/9; a degree-one side forces both statistics to vanish. The fixed-degree limit of B is (d-1)^2(e-1)^2/4, giving both asserted asymptotics. Independent exact enumeration of all nine degree-at-least-two models with L<=8 agreed, including +4/25 for (3,3,2,2), -36/25 for (2,3,3,2), and -288/49 for (2,2,4,4), in (n,m,d,e) order.

## originality

PASS

Credit the all-biregular exact covariance, specifically the extension to both degrees at least three. The entire degree-two-side subfamily, including the positive coefficient, exceptional -4/9, and the negative higher-degree cases within that subfamily, is already covered by a one-part pairing identity after contraction. The pass does not credit that boundary family, the existence of a degree-two sign/rate reversal in pairing models, or the marginal parallel-pair expectation as new.

## value

PASS

The exact covariance is a finite correction to independent short-cycle heuristics for a standard pairing ensemble. It quantifies the dependence of the simplest defect and the first distinct-vertex cycle even when both sides have multiple available stubs per square vertex. The sign and explicit coefficient in that interior regime remain useful beyond the known contracted boundary; a marginal Poisson approximation gives neither.

The dated certificate retains the supplied scientific assessment, sources and limitations.
