# Independent mathematical audit

## correctness

PASS

Ultrahomogeneity of the countable universal r-uniform hypergraph for integer r>=2 makes each injective labeled n-tuple orbit an arbitrary r-edge incidence pattern, exactly I_r(n)=2^{C(n,r)}. Every ordered tuple has a unique equality partition into k blocks, followed by one injective k-tuple orbit, so T_r(n)=sum_k S(n,k)2^{C(k,r)}. Reindexing j=n-k yields exact positive collision layers S(n,n-j)2^{-D_{r,j}}, D=C(n,r)-C(n-j,r)=sum_{t=0}^{j-1}C(n-t-1,r-1). To bound remainder after fixed m, near-diagonal Stirling coefficients satisfy S(n,n-j)<=n^{2j}; for j in [m+1,n/2] the extra successive D increments are Omega(n^{r-1}), giving geometric tail; for j>n/2 the n^n partition bound is negligible against 2^{-Theta(n^r)} when r>=2. Thus remainder O(n^{2m+2}2^{-D_{r,m+1}}). At m=1 the first correction binom(n,2)2^{-C(n-1,r-1)} and next-layer error follow. The inverse expansion uses delta^2=O(error). The n=0 conventional counts are 1; the result states the fixed-n formulas naturally. Independent computations for r=2..5,n<=10 verify Stirling identities, and the actual artifacts/verify.py independently enumerates equality patterns; finite checks cannot prove the asymptotic.

## originality

PASS

The r=2 exact sequence and leading asymptotic are ALREADY OEIS A335390, and labeled simple graph counts are OEIS A006125. Standard Fraisse ultrahomogeneity proves injective orbit count. The potentially new result is the uniform fixed-depth collision-deficit expansion and sharp non-injective first-order correction for every r>=2. Targeted semantic published result searches for automorphism tuple orbits, random hypergraphs, Stirling and correction did not identify a dominating statement; a different oligomorphic tuple profile is not an alias. Because the correction is a short deduction from the existing transform, unindexed folklore is an explicit residual originality risk.

## value

PASS

The ratio T_r/I_r is a natural orbit-growth invariant of canonical oligomorphic automorphism groups, and its defect measures the price of repeated tuple coordinates. The formula resolves all fixed collision depths and reveals arity in the deficit scale n^2 2^{-Theta(n^{r-1})}; it sharpens known asymptotic equivalence and is useful independently of a new general structural theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
