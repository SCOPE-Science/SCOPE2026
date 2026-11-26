# Independent mathematical audit

## correctness

PASS

The two-person coalition is represented by every nonempty committee because each candidate has an approver. For each voter the singleton demand exists precisely when some approved candidate has quality ≥2/k (an empty approval set has no demand). A top-k committee that violates rJR misses exactly one eligible voter i, and every selected candidate is approved by the other voter. Let t be the least selected quality and choose a qualifying unselected c for i, of quality s∈[2/k,t]. Replacing a quality-t candidate represents i and leaves the other voter represented because k≥2. With Q*≥kt, the resulting ratio is 1+(t−s)/(Q*−t+s)≤kt/((k−1)t+s)≤k/(k−1+2/k), since t≤1. Replacing the denominator by the optimal feasible quality only improves the bound. With k exclusive quality-one candidates for voter 1 and one exclusive quality-2/k candidate for voter 2, rJR forces that last candidate; the feasible optimum is exactly k−1+2/k. This also covers k=2, where s=t=1 and any repair costs zero. The difference 8/7−k²/(k²−k+2)=(k−4)²/[7(k²−k+2)] proves the unique four-seat maximum. The constructive scan and one replacement have the stated sorting or selection complexity with two explicit approval bits. A bounded independent replay, /workspace/branches/replay_1.js, checks all three coalitions in size-(k+1) profiles on two quality levels in twelfths for k=2 through 7 (56, 126, 252, 462, 792, 1287 multiset-index cases). It corroborates the inequality but is not a universal proof or an equality check when 2/k falls off the twelfths grid. The frozen verification code was inspected but not run.

## originality

PASS

The inspected sources supply the reciprocal axiom and unrestricted price, and indexed two-seat results overlap the trivial k=2 boundary. They do not supply the exact two-voter price as a function of arbitrary seat count or its unique four-seat maximum. The bounded comparison supports that specific contribution, not a claim to the reciprocal rule or publication priority.

## value

PASS

The smallest nontrivial electorate isolates the effect of seat count on the cost of reciprocal representation. The exact bound and matching examples quantify that effect, showing that the worst loss is neither at two seats, as in an unrestricted construction, nor asymptotically, but exactly at four. The one-swap structural reduction also gives a usable repair with a sharp quality guarantee. This is an exact structural result over all seat counts rather than a numerical check at a few chosen k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
