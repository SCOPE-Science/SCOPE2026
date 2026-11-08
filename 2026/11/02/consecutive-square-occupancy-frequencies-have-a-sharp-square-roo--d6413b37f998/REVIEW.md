# Independent mathematical audit

## correctness

PASS

For distinct frequencies r,s and N>=r+s, the mixed binomial-multinomial moment gives Cov(C_r,C_s)=B²p_rp_s(R_B-1). Direct algebra gives the adjacent-N ratio B(B-2)/(B-1)² times [1+rs/((N+1-r-s)(N+1))], strictly decreasing in N; therefore R_B is log-concave and its positive superlevel set is an interval. In the fixed-loading N/B=λ regime, the 1/B logarithmic term equals -[λ²-(r+s-1)λ+rs]/(λ B). A double root occurs precisely when (s-r-1)²=4r, i.e. r=k²,s=(k+1)². The next term at λ=a=k(k+1) is +1/B². Uniform local expansion yields B² log R→1-u²/a and endpoints aB±sqrt(aB)+O_k(1); p_r,p_s→Poisson(a) masses, yielding the displayed finite nonzero limiting covariance. Independent rational checks for k=1, B=50,100,200 found intervals [91,110],[187,214],[381,420], consistent with the sharp sqrt(2B) window. The proof, not these samples, covers unbounded B.

## originality

PASS

Fixed-sample multinomial mixed moments and generic frequency covariance expressions are classical and not novel. The assessed result is the arithmetic classification of double-root pairs, strict one-interval sign geometry, the critical second-order covariance profile and O(1)-localized sqrt(B) sign window. Gnedin–Hansen–Pitman (2007) explicitly allows straightforward covariance derivation, while its main survey uses a different infinite-frequency asymptotic regime. Nearby Resultary records about occupied-box richness covariance and precision matrices use aggregate/different observables; they do not imply this individual pair-criticality statement.

## value

PASS

Covariance of sample frequency counts is natural for occupancy inference, and at the consecutive-square degeneracy the first asymptotic order loses the sign entirely. A provable positive dependence window of only square-root width, with a closed local limit, fills this precise asymptotic gap and identifies all distinct integer pairs for which it arises. The fact is not a known covariance table entry or an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
