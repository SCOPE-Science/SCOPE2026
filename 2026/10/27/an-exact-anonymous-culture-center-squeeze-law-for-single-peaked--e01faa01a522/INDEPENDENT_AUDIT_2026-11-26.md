# Independent mathematical audit

## correctness

PASS

On the four fixed-axis orders, C beats L iff a≤r and beats R iff d≤r; if either extreme instead has a>r or d>r it is both the Condorcet and first-round majority winner. Thus a unique Condorcet winner always exists. In the center-winner region, failure under every tie-break is exactly m=b+c<min(a,d): when C ties for last an extreme can be eliminated, and when an extreme is eliminated C wins the final pairwise comparison. Both a,d≤r force m≥1. For fixed m the integer interval for a is [max(m+1,r+1−m),min(r,2r−2m)]; its cardinality is m up to floor(r/2), then 2r−3m up to floor((2r−1)/3), then zero. Each choice has m+1 splits of m and the uniform denominator is binom(n+3,3). The range convention gives zero for n=1,3. Dividing the numerator by n³ and scaling m by n gives the two integrals of t² on [0,1/4] and t(1−3t) on [1/4,1/3], totaling 7/864. Piecewise polynomial Riemann sums with order-one rounded endpoints and O(n²) errors in the original count justify the stated O(1/n) convergence after normalizing by the denominator, which has leading coefficient 1/6. Hence the limit is 7/144. Independent check: python3 /workspace/branches/independent_checks.py 1; output /workspace/branches/independent-1.txt. It enumerates 12,740 histograms through n=25 using all pairwise margins and all legal first eliminations, e.g. 2 failures at n=5 and 46 at n=17. The frozen script was inspected, not executed. The computation does not prove the limit or extrapolate the result to different cultures.

## originality

PASS

The supported distinct result is the exact finite odd-n count and rational limiting probability of the robust Hare/Condorcet failure event under fixed-axis uniform anonymous histograms. The four ballots, center-elimination possibility and general IAC counting approach are not original. Same-rule and same-culture primary work was examined, but measures different events. No stronger or equivalent count was identified in the bounded comparisons below; historical priority is not certified.

## value

PASS

This is a motivated rule-efficiency benchmark on the smallest single-peaked domain with an IRV center squeeze. The absence of majority cycles does not ensure Condorcet consistency: under uniform anonymous histograms the robust failure rate has a nonzero limit, in contrast to independent uniform ballots under which the center first-choice share approaches 1/2 and the extremes approach 1/4 each. The exact finite calibration, including elimination ties and the first nonzero cases, and the limiting constant answer a specified probability question rather than recasting the deterministic center-squeeze observation. No empirical prevalence is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
