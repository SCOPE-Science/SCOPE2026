# Independent mathematical audit

## correctness

PASS

Using the normalized weighted Bergman moments w_k(gamma)=Gamma(gamma+2) Gamma(k+1)/Gamma(k+gamma+2), the exact matrix is B_nk=(n+1)sqrt(w_n(beta))/[(n+k+1)sqrt(w_k(alpha))]. The infinite k-sum after splitting at k=n is O((n+1)^alpha) for -1<alpha<0, hence squared row tail sum_{n>=N} O(N^{-delta}) where delta=beta-alpha-2>0. For each of J dyadic row blocks, center c_i=3*2^(i-1) makes |(c_i-n)/(k+c_i+1)|<=1/3, so the J-term exact Cauchy geometric expansion has rank <=J per block and HS remainder <=3^-J; row zero adds one. With rows >=2^J removed, rank <=1+J^2 and operator error <=C(3^-J+2^(-delta J/2)), yielding exp(-c sqrt(rank)) and S_p for all p>0. For delta->0+, uniform gamma-ratio expansion and integral k-sum with B(alpha+2,-alpha)/Gamma(alpha+2) yield delta||H2||_HS^2 -> (alpha+2)(alpha+3)B(alpha+2,-alpha); finite rows vanish after multiplication by delta. Noncompact boundary and boundedness limits follow the accurately matched Li-Zhou theorem. A finite checker cannot substitute for these infinite estimates.

## originality

PASS

Best-of-knowledge PASS: Li-Zhou already established compactness and p>=1 Schatten membership, not the separated infinite row-tail approximation, all 0<p<1, or residue coefficient. Beckermann-Townsend provide finite Cauchy matrix compression, not this uniform infinite Bergman family with delta boundary. This is originality of the combined specific additions, not priority for geometric expansions generally.

## value

PASS

The concrete rank-vs-accuracy complexity O(log^2(1/epsilon)) for a nontrivial infinite weighted integral operator, access to genuinely quasi-Banach S_p (0<p<1) and an exact singular coefficient approaching the sharp compactness boundary are independently useful operator-theoretic information; they are not automatic relabelings of p>=1 membership. Optimal singular asymptotics are not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
