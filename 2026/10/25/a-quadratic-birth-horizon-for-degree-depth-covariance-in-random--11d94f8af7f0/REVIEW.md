# Independent mathematical audit

## correctness

PASS

PASS. For independent uniform parents P_t, H_j uses only parent choices t<=j, so D_i is independent of H_j when i>=j. For t<=j the event that j descends from t is independent of P_t and has probability 1 (j=t) or 1/t (j>t). Resampling P_t yields Cov(1{P_t=i},H_j)=q_{t,j}(1+h_(i-1)-h_(t-1))/(t-1). Summing gives C_i(i+1)=(i-1)/i², and direct subtraction telescopes to C_i(j+1)-C_i(j)=-1/j². Thus the exact matrix holds for every n>=2 and 1<=i,j<=n. For i>=2, the reciprocal-square tail Q_(i+1)>1/(i+1)>(i-1)/i² ensures the limit C_i(j)<0; monotonicity gives the single crossing. Euler–Maclaurin gives δ_i=1/(2i²)+1/(6i³)+O(i^-5), and Q_(2i²-(2/3)i+v)-δ_i=(13/72-v/4)i^-4+O(i^-5), uniformly for bounded v; this traps J_i=2i²-(2/3)i+O(1). Direct independent exhaustive parent-sequence enumeration covered all (i,j) for n=2,...,8 (203 matrix entries, 5913 trees in total); exact transition calculations independently recovered J_2=8,J_3=17,J_4=31 and i<=9. No infinite claim rests on the finite enumeration. All seven actual Git blobs were inspected; independently reconstructed Git tree equals the frozen assignment SHA.

## originality

PASS

PASS on checked statements, with bounded priority risk. Eslava (2016/2021) and Lodewijks (2022/2023) give degree/depth limiting distributions, not all fixed-label finite cross-covariances. A published same-model SCOPE root-degree/total-path-length theorem DOES already imply the i=1 root row, and that partial overlap is expressly deducted. Its root-special aggregate does not determine the nonroot i>=2 rows or J_i~2i². Searches of Resultary and primary literature found no stronger all-nonroot formula or table, although a historical bivariate exact-moment identity may exist. Lack of search hits is not a proof of novelty.

## value

PASS

PASS. The source child count and target depth are canonical age-indexed observables of a random recursive tree, where their finite cross-dependence is not resolved by marginal harmonic moments or normalized joint limits. For nonroot sources the covariance starts strictly positive, decreases at a universal label rate 1/j², and crosses zero at a precise quadratic birth horizon J_i=2i²-2i/3+O(1). This quantitative phase of age separation is a motivated, exact all-label dependence law and a natural invariant for analyses of recursive network attachment; it is not merely a restatement of the previously known i=1 root case. The effect is small and no stronger stochastic-order consequence or general growing-tree theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
