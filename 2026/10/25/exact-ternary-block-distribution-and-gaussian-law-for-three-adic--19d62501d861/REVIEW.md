# Independent mathematical audit

## correctness

PASS

By Kummer ν3(C_n)=number of ternary carries in n+n−ν3(n+1). Split length-L ternary strings at the first non-2 digit and account for cancellation of trailing-two carries; subsequent positions use transition matrix T(u)=[[2,u],[1,2u]]. The inverse (I−zT)^{-1} gives Σ_{L≥0}P_L(u)z^L=[1+(1−2u)z]/[1−2(1+u)z+3uz²] with P0=1,P1=3, and recurrence P_L=2(1+u)P_{L−1}−3uP_{L−2}. Differentiation at u=1 gives exact mean L/2−3/4+3/(4·3^L) and variance [8L−15+24·3^{−L}−9·3^{−2L}]/16. Dominant root λ+(u)=1+u+sqrt(1−u+u²), with log(λ+(e^s)/3)=s/2+s²/4+O(s³), proves normal limit centered L/2 and scaled sqrt(L/2). At u=0 gives zero count 3·2^{L−1}; support 0..L−1 realized with explicit ternary digits; fixed-r singular root expansion gives claimed polynomial asymptotics. Independent Legendre-factorial enumeration for every n<3^L up to L=9, exact rational moments and polynomial histograms all matched. Finite cases not used as proof for unbounded L.

## originality

PASS

Existing prime-power divisibility, individual 3-adic valuation recurrences and Catalan congruence sources do not state or obviously imply the exact all-valuation distribution over the complete aligned ternary blocks, with rational bivariate GF, exact moments and a Gaussian law. The work organizes carry statistics via a nontrivial weighted transfer and spectral asymptotics. Historical priority qualified because the 1973 primary Alter–Kubota full text could not be obtained.

## value

PASS

The full distribution of a natural p-adic valuation over canonical complete digital blocks, not just divisibility at individual indices, is a meaningful exact enumerative invariant. The bivariate rational generating function gives every finite-scale histogram; the exact mean/variance and CLT describe typical fluctuations, while fixed-r asymptotics treat rare tails. These nontrivial aggregate conclusions add information beyond a digitwise lookup and have natural future use for Catalan divisibility statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
