# Degree-ten Delsarte impossibility for the unconditional 48-dimensional T1-avoiding kissing bound

## Context
The 48-dimensional kissing configurations given by the minimal vectors of the even unimodular extremal lattices (P48p, P48q, P48m, P48n) have cardinality N*=52416000. Boyvalenkov–Cherkashin (arXiv:2312.05121, Theorem 5.1) proved |C|<=52416000 for T1-avoiding 1/2-codes under the extra hypothesis that C is antipodal or a 3-design, using the degree-11 polynomial h(t)=(t+1)P(t) whose only negative Gegenbauer coefficient is h3. The unconditional bound (no antipodality or design assumption) remains open. This record establishes the exact structural obstruction at degree 10.

## Definitions
Let d=48, S^47 the unit sphere, T1=(-1/3,-1/6) cup (1/6,1/3). A code C subset S^47 is T1-avoiding if I(C) cap T1=empty, where I(C) is the set of inner products of distinct points; assume s(C)<=1/2. Let P_k be the Gegenbauer polynomials for d=48 with P_k(1)=1 and f=sum f_k P_k. Delsarte conditions: (A1) f(t)<=0 on the admissible set; (A2) f_0>0, f_k>=0 for all k>=1; then |C|<=f(1)/f_0. Equality forces f(t)=0 for all t in I(C).

## Result
Theorem: There is no polynomial of degree at most 10 satisfying the unconditional Delsarte conditions (A1)+(A2) that proves |C|<=52416000 with equality for 48-dimensional T1-avoiding 1/2-codes. The unique (up to positive scale) degree<=10 polynomial vanishing on the extremal support S={-1,+-1/2,+-1/3,+-1/6,0} with admissible signs is P(t)=(t+1)(t+1/2)^2(t+1/3)(t+1/6)t^2(t-1/6)(t-1/3)(t-1/2); it satisfies P(1)/P_0=52416000 exactly but has normalized coefficients f3=-8507/67651200<0 and f4=-25333/60134400<0.

## Proof / evidence
P has degree 10 with P(1)=35/18 and P_0=E[P]=1/26956800 in exact rational arithmetic, so P(1)/P_0=52416000 exactly. Writing g(t)=(t+1)(t+1/3)(t+1/6)(t-1/6)(t-1/3)(t-1/2) so P=g(t)(t+1/2)^2 t^2, sign analysis gives g<=0 hence P<=0 on J1=[-1,-1/3], J2=[-1/6,1/6], J3=[1/3,1/2], i.e. (A1). Exact ultraspherical expansion gives f0=1/26956800, f1=1/561600, f2=235/21648384, f3=-8507/67651200, f4=-25333/60134400 with f5..f10>0, so (A2) fails at k=3,4 and no positive rescaling repairs it. Uniqueness: for any degree<=10 f attaining equality on full support S, complementary slackness forces zeros at all eight nodes; interior zeros -1/2 in (-1,-1/3) and 0 in (-1/6,1/6) need even multiplicity, forcing pattern (1,2,1,1,2,1,1,1) and f=cP, c>0. Supporting computed evidence (not proof): discretized Delsarte LP is infeasible at K=10,11 and plateaus at 56835894 (8.4% above N*) for K=16,20,24. The claimed distance distribution sums to 52416000 and matches sphere moments through degree 11, confirming the equality case is an antipodal spherical 11-design.

## Limitations
Impossibility covers only single-polynomial Delsarte linear programming at degree<=10. It does not rule out higher-degree LP proofs, three-point semidefinite programming, or Cohn-Elkies modular-form arguments, and does not prove the unconditional target bound itself. The LP plateau is numerical evidence only.

## Reproducibility
Run `python3 output/artifacts/exact_certificate.py` (stdlib only): rebuilds P from its roots, certifies P(1), P_0, the ratio, the negative f3/f4 fractions, and the 0..11 moment identities of the 11-design distribution.

## References
Boyvalenkov–Cherkashin arXiv:2312.05121 (restricted sharp bound via degree-11 h); Boyvalenkov–Dragnev arXiv:2412.07577 (T1/T2 energy bounds); Boyvalenkov–Cherkashin–Dragnev arXiv:2501.13906 (T-avoiding universal optimality); Delsarte–Goethals–Seidel 1977 (LP bounds); Conway–Sloane (extremal lattices); Nebe 2014 (P48n); Venkov (11-design property).
