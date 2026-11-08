# Independent mathematical audit

## correctness

PASS

Backward-generator recurrences yield H_1n=sum_i M_i/c_i and H_n1=sum_i(1-M_i)/c_i, each other oriented hitting time being a nonnegative subinterval sum. For every lambda, Cauchy–Schwarz plus the linear budget bounds max(H_1n,H_n1) below by S(lambda)^2/B. Strict concavity of S on [0,1] for n>=3 selects unique lambda*: its derivative sets equal endpoint times in the interior and the appropriate worst direction at a boundary. The Cauchy–Schwarz equality conductances attain the bound and use the full budget, giving uniqueness by strict convexity. For uniform masses with surcharge at k>n/2, the exact derivative S’(1) has a unique sign change at Q_c=(1-A_n sqrt(k)/(2k-n))^2; Riemann-sum A_n/n^(3/2)->-2/3 and midpoint scaling yield the quadratic theta and quartic s constants. Independent generator solves for n=3,5,8 and explicit three-state active-set checks corroborated the proof; source verify.py was inspected rather than used as an infinite proof.

## originality

PASS

Existing Markov hitting-time recurrences and electrical network resource allocation are acknowledged. The final claim concerns worst *directed* endpoint hitting times with fixed stationary masses and explicit asymmetric one-edge price frontier, not total symmetric effective resistance. No dominant prior theorem materially read implied the two exact transition exponents.

## value

PASS

The maximum of directional hitting times is a natural worst-case Markov performance criterion, different from the classical symmetric commute objective. The unique budget-optimal conductance vector and sharp transition from balanced to one-sided travel determine an exact physical-resource phase boundary. The n^2 versus n^4 surcharge scales reveal a nontrivial midpoint spatial dependence that a generic convex optimizer does not display.

The dated certificate retains the supplied scientific assessment, sources and limitations.
