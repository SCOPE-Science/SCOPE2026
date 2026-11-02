# Independent mathematical audit

## correctness

PASS

The recurrence telescopes to a_n=n!S_n/2^n. The 2-adic logarithm at z=2 gives L1=sum 2^j/j=0, and the formal dilogarithm transformation Li2(z)+Li2(z/(z-1))=-1/2 log²(1-z) gives L2=0 at z=2. For L3=sum2^j/j³ the j=4 term uniquely minimizes j-3 nu2(j) at -2, so nu2(L3)=-2. Let N=2^m; sum expansion gives S_N=-2^N N²(L3-N T_N). For j<N the denominator estimates j-4 nu2(j)>=-4, for j>=N>=16 the term valuation is >=-1, so nu2(T_N)>=-4. With m>=4 the correction N T_N has valuation>=0, strictly above -2, establishing nu2(S_N)=N+2m-2. Legendre nu2(N!)=N-1 gives second formula. Independent exact integer recurrence verified m=4..10. Valid two-adic series converge; no finite truncation is treated as infinite proof.

## originality

PASS

Farhi 2022 defines this exact recurrence and Dubickas 2024 proves a stronger general lower bound with equality precisely n=2^k-1. That theorem does not give equality at n=2^m; the assessed exact power-of-two subsequence and its p-adic third-order term are not stated by these inspected papers.

## value

PASS

A natural exact two-adic valuation law on an infinite distinguished subsequence, complementing the known one-below-dyadic equality indices, is a meaningful arithmetic refinement not obtainable by plugging into the prior lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
