# Review

## Correctness
PASS. The proof reduces the binary radius-one ball size to \(B_n=n(n-1)+2-(n-1)K-Q\), where the equality indicators are independent Bernoulli variables and \(Q\) counts pairs inside zero-runs. The covariance with \(K\) is summed interval-by-interval, and a closed five-moment recurrence gives \(\operatorname{Var}(Q)\). Substitution yields the displayed variance for every \(n\ge1\). The boundary case \(n=1\) gives variance zero. Literal ball enumeration through \(n=10\) and an independent recurrence check through \(m=200\) agree exactly.

## Originality
PASS, with residual literature risk. The closest primary source is Wang--Wang, arXiv:2204.02201: it studies the same random radius-one FLL ball, states the exact mean, and proves Azuma concentration, but the inspected statement does not give an exact variance or second moment. Bar-Lev--Etzion--Yaakobi, arXiv:2206.07995, gives minimum, maximum, and average ball sizes rather than the variance. Targeted searches under variance, second moment, ball-size distribution, and synchronization-channel aliases found no statement that implies the formula. A differently phrased or unindexed derivation remains possible.

## Value
PASS. The exact variance is a natural second-order invariant of the same distribution for which concentration was introduced as the next question after minimum, maximum, and average size. It identifies the precise root-mean-square scale \(\frac12 n^{3/2}\) and leading variance constant \(1/4\), rather than reporting a finite parameter table or a routine recomputation.

## Closest literature and limitations
The result uses a known pointwise radius-one ball formula as input and advances from the known mean/concentration picture to an exact all-length second moment. It is binary and radius-one only and does not establish a limiting distribution or sharp tails.

Same-model review: passed. Independent audit: not yet performed.
