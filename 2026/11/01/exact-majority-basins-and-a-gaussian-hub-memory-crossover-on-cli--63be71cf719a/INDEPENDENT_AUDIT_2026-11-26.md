# Independent mathematical audit

## correctness

PASS

With m=2r and initial hub c, a zero in a clique turns to one iff k+c>=r+1, and a one stays one iff k-1+c>=r. Thus the whole clique updates to the same bit, and the m-1 agreeing internal neighbors then preserve it. At round two the hub takes the strict majority of the n permanent bits, with no tie since n is odd. This describes exactly all 2^n fixed states and rules out other recurrence. For sharpness take c=0, (n+1)/2 cliques with r+1 ones and the rest empty: (n+1)(r+1)/2<=nr since n(r-1)>=r+1, so the hub cannot change at round one but must change at round two. For each prescribed set P of one-cliques, binomial reflection gives the local multiplicities u_m,v_m, interchanged by c, and independence of choices gives the two products. The resulting dependence on p is proportional to cosh((p-n/2)log(v_m/u_m)), giving exactly the stated extrema. Given the initial hub, the number of matching final cliques is Bin(n,(1+q_m)/2). Stirling gives q_m~sqrt(2/(pi m)); the binomial CLT standardizes the cutoff at -q_m sqrt(n)/sqrt(1-q_m^2) up to O(n^(-1/2)), and Chebyshev gives the high-ratio limit. The low-ratio limit follows in the joint growing regime (and for bounded n by continuity of the finite binomial tail). The two saved checkers and output files were inspected, not executed: they check finite graphs with (n,m)=(3,4),(3,6),(5,4), not the all-parameter result.

## originality

PASS

The earlier October 26 Resultary finding is an exact antecedent for two-vertex petals, which are excluded here; the extension in clique order yields an independent second scale and hence a limiting hub-memory law unavailable in the antecedent. No inspected statement or stronger theorem gives the present labelled basin census and growing-even-clique crossover. This is a best-of-knowledge comparison, not a claim that two-round triangle-windmill fixation, general module arguments, or the binomial CLT are new.

## value

PASS

The odd number of even cliques gives a natural separation of local voting and hub feedback. The individual labelled basin law recovers the full terminal-state distribution, rather than only a stabilization bound. Growing clique order changes the local influence of the hub, and the exact tie count identifies the n/m balance that separates memory loss from almost certain retention. This two-scale prediction has no counterpart at fixed triangle size and concerns retention of an initial bit, not unanimity or recovery of external truth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
