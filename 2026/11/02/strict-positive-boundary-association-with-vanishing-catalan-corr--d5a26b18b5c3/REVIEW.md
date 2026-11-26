# Independent mathematical audit

## correctness

PASS

Fixed identity boundaries leave a freely chosen middle 231-avoider because 231 has no proper direct-sum cut; when the boundaries overlap only the identity is possible. For 1<=a,b and a+b<=n, dividing the Catalan ratio products compares factors C_t/C_(t-1) with strictly smaller-index factors, proving strictness; for overlap the direct-sum injection gives C_(n-a)C_(n-b)<=C_(2n-a-b)<C_n (including n=2). Increment expansions prove the transform statement, and fixed-threshold tail differences give convergence to independent geometrics. For t>=2 the ratio of successive Catalan ratios is exactly 1+3/((t+1)(2t-3)). Thus on a,b<=ceil(10 log_4 n) the log joint-to-product ratio is 3ab/(2n^2)+O(ab(a+b+1)/n^3); expansion and the uniform marginal estimate give a summable error after multiplication by 4^(-a-b). The rest of the covariance tail sum is bounded by O(n(n+1)^(3/2)4^(-ceil(10 log_4 n))) using 0<=Delta_(a,b)<=min(p_a,p_b), so the limit is (3/2)(4/9)^2=8/27. This is a covariance limit, not a claimed total-variation upper bound in the proof. The frozen checker was inspected, not executed; its finite enumeration and rational evaluations are not needed for the all-size proof. Replay: use RESULT.md lines 18–49 and the exact ratio above.

## originality

PASS

The count is an elementary Catalan consequence and does not by itself warrant distinct credit. The inspected fixed-point, direct-sum and logical-limit results do not cover the all-threshold strict association or the first nonzero boundary covariance term. Bounded comparison supports that combined claim, not historical priority.

## value

PASS

For two canonical endpoints of a Catalan family, strict association at every admissible nonconstant threshold and the first nonzero covariance term quantify what is lost in the independent limit. The overlap treatment and sharp constant make this useful as a finite-to-limit comparison beyond merely reproducing a Catalan count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
