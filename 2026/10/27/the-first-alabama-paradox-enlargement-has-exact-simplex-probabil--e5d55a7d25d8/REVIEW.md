# Independent mathematical audit

## correctness

PASS

With strict remainders Hamilton is represented by floor(h p_i+α_h) with a common α_h in (0,1). If a party loses a seat, its adjusted quota decreases by less than one, and parties with no larger share cannot gain. Each of the other parties can gain at most one, so both must gain and the loser is the smallest. The smallest cannot hold a seat at h≤2, since the ordered allocations are monotone in share. At h=3 a loss must start from (1,1,1), ending at (2,2,0). The h=4 middle-party remainder comparison gives v−u>1/4 and hence u<1/6. The h=3 largest party must then have w<1/2 (otherwise it already has at least two floors or its remainder exceeds 3u). Thus v>1/3, the three- and four-seat floor vectors both equal (1,1,0), and the h=3 comparison is w−u<1/3. Conversely these strict comparisons give both claimed allocations. The ordered triangle has area 1/864: its u-limits are 1/9 and 1/6 with split at 5/36 into two triangles of area 1/1728 each. Density 2 and six labeled chambers give 1/72. Exact quota/remainder boundaries are a null set. A separate arrangement calculation (python3 /workspace/audit_evidence/apportionment.py) partitioned one chamber into 44 open cells, directly tested each of the three enlargements by exact quota-error minimization, and checked the inequalities and summed loss areas 0,0,1/864. No finite population grid is used to prove the continuum claim.

## originality

PASS

Pass for the complete strict first-enlargement region and its exact simplex measure, not for the existence of a 3→4 paradox. The known equal-larger-share example and long-run averaged probability are different. The numerical worked examples actually checked in Janson–Linusson are at 10→11 and at 4→5 or 5→6 in the rational/tie discussion, so the frozen prose attributing a 3→4 worked example to that paper is not substantiated by those passages. The earlier equal-pair Resultary record supplies an explicit valid 3→4 example. This citation caveat does not affect the mathematical claim or novelty of the chamber/measure.

## value

PASS

The earliest possible expansion is an intrinsic cutoff of the apportionment rule, not an arbitrary house size. A complete iff chamber and exact normalized probability quantify how exceptional the first loss is, and distinguish this finite experiment from an otherwise easily confused classical asymptotic average. This contributes more than an isolated paradox witness or a grid count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
