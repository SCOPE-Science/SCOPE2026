# Independent mathematical audit

## correctness

PASS

For n=2, K_2=2-I with I=1{X1=X2}. Exact conditioning yields E[I]=s_2, E[M_2]=1-2s_2+s_3, E[I M_2]=s_2-s_3; hence Cov(K_2,M_2)=(1+s_2)s_3-2s_2^2. For fixed feasible s_2, compactness allows maximizing s_3 over nonnegative m-tuples; active-support Lagrange equations yield at most two positive masses. If two coordinates share the larger mass a>b, tangent vector e_i-e_j annihilates both first constraints while the constrained Hessian is strictly positive 6(a-b) in each coordinate, contradicting maximality. Thus each nonuniform maximizer has one large mass, equal smaller ones; zero entries mean smaller active support. For r=2,3,4 the exact covariance factors are -2b^2(1-b)^2, -2b^2(18b^3-12b^2+1), -6b^3(48b^2-30b+5), respectively, all strictly negative on 0<b<=1/r (r=3 bracket >=1/3, r=4 discriminant -60). Uniform support r>=2 gives -(r-1)/r^3. One atom gives zero. The positive five-atom rational vector (4/5,1/20,1/20,1/20,1/20) yields exactly 1/1600; epsilon continuity gives any larger full finite support, while uniform laws give negative covariance. Independent direct sample-space enumeration of 9,948 all-positive integer-composition laws (d<=6, denominator <=15), symbolic one-heavy polynomial factorization and full tree SHA reconstruction corroborate the stated proof; finite cases alone are not its unrestricted justification.

## originality

PASS

Best-of-knowledge originality survives for the sharp support-size possibility classification, not for the elementary covariance identity. ICLR 2025 Appendix D.3 encompasses raw component covariances, but its inspected results do not contain or imply the constrained-power-sum cutoff. The relevant infinite-urn CLT has asymptotic scaling, and the closest published related covariance theorems use different random variables or assume uniform p. An unseen classical symmetric power-sum equivalent remains a substantive priority risk.

## value

PASS

For fixed-sample species discovery, observed richness and total unseen population probability are basic nonredundant statistics. The theorem resolves a natural exact minimal-alphabet sign question at n=2, the first sample size with nonconstant K_n: support<=4 forces negative covariance but heterogeneity from five atoms onward allows positive covariance. It is a complete possibility classification over all finite support sizes, and clarifies why independent Poissonization masks the sign reversal. The witness and proof are not arbitrary parameter slices or known-table recomputations. The precise cutoff could be useful when analyzing the dependence of sample coverage and diversity at short horizons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
