# Independent mathematical audit

## correctness

PASS

Uniform-permutation root split K is uniform on 0..n-1, and conditional subtree independence implies the exact mixed-moment recursion. The leaf mean ℓ_m=(m+1)/3+δ_m with δ0=-1/3,δ1=1/3 concentrates conditional-leaf regression on the four boundary splits. Using t_m=2(m+1)H_m-4m gives B_n=-4(H_{n-1}-1)/(3n); the total covariance recurrence and telescoping (n+1)c_{n+1}=(n+2)c_n-4/(3n) yield c_n=-(n+3)(n-2)/(9n) for all n>=2. Initial c0=c1=c2=0 and n2 boundary are correct. Independent new exact-rational joint-moment recurrences checked every n<=65; repository verify.py source was read (it specifies n<=100 and 46,233 permutation checks, but the source assertion is not reported as an independently rerun program). Exact recurrence, not finite checking, proves the infinite statement.

## originality

PASS

Best-of-knowledge original exact finite-size covariance and boundary-local mechanism. Chern et al. Thm5.4 explicitly covers the same d=1 statistic at leading asymptotic order, so that order alone is prior art. Source-level mathematical comparison did not find the all-n rational covariance or boundary decomposition; distinguish this limited novelty and accept with a serious residual older-literature risk.

## value

PASS

A natural finite-n dependence measure for terminal stored vertices and total search cost, with a sharp negative sign for every n>=3, explicit O(n) anticovariance and exact zero boundary. Boundary-support explanation reveals why conditional leaf count varies only at extreme split sizes. This is more than marginal means, a table recomputation, or a bare sign check, even though the leading asymptotic was known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
