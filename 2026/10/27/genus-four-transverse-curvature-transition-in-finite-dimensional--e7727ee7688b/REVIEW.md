# Independent mathematical audit

## correctness

PASS

Yuan's Theorem 10, §3.2 and Remark 12 give a nowhere-vanishing factor generator, product isometry and differential basis, including d=1. Rotation gives orthogonality. The two sheets and the m-to-one power substitution give the prefactor 2/m in the complex beta integral (m=2d+1), and the beta evaluation gives the stated positive inverse norms. In a local trivialization the common factor is nonvanishing: dx/y extends nonvanishing at each finite branch point by the defining relation, and the other factor is base-point free. Taking the log removes the common factor. The variance of j with weights proportional to c_j t^j gives t g_d(t)>0 for t>0 when d>=2, and g_d(0)=c_1/c_0>0. Pullback by x causes precisely the branch rank drops; d=1 is constant. The curvature calculation at x=0 uses g_d'(0)=4c_2/c_0-2(c_1/c_0)^2 and agrees with the stated metric convention. The odd gamma-log series has strictly positive defect coefficients, with cubic coefficient 48 zeta(3). The rational truncation at d=3 exceeds 5/12>log(3/2), while the uniform odd-tail estimate for d>=4 gives 1148/6075<2/5<log(3/2). These signs do not rely on decimal gamma values. The supplied verify_curvature.py was inspected, not executed. Independent radial norm integrals and exact fractions in python /workspace/reproductions/reproduce.py reproduce the bounds and give normalized curvatures 2, .236342731544, -.606646810907 for d=2,3,4 respectively.

## originality

PASS

Credit is for the explicit log-Bergman curvature and exact all-genus sign cutoff in Yuan's family. The pseudoconvex construction, basis, and canonical-map mechanism behind the rank observation are not original here.

## value

PASS

The sign of a natural transverse invariant at the distinguished nonbranch points changes at a sharp, finite genus cutoff. This records where a specific kernel-induced metric has positive curvature even though the canonical metric does not, and the exact coefficients make the comparison reproducible. It neither classifies all curvature on these domains nor gives examples of globally positive definite Bergman metrics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
