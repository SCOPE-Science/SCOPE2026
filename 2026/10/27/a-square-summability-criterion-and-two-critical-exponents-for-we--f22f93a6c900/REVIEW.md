# Independent mathematical audit

## correctness

PASS

Write μ_j and S_j for the attachment-weighted empirical depth mean and variance. The update μ_j−μ_{j−1}=p_j(1+ξ_j) gives the stated coefficient 1+(n−j)p_j in the centered path length. The empirical variance updates to (1−p_j)S_{j−1}+p_j(1−p_j)(D_j−μ_{j−1})², giving the stated recurrence on taking expectations, since the squared term conditionally has mean 1+S_{j−1}. Orthogonality and fixed-prefix lower bounds give scaled variance divergence when Q=∞. When Q is finite, the recurrence gives bounded v_j if the summed inputs p_j(1−p_j) are finite; otherwise v_j eventually exceeds 1, so ∑p_j² is finite and v_j=O(sqrt(j)). Thus ∑v_j/j² is finite; the two martingale series and Kronecker's lemma dispose of the two remainders almost surely, and orthogonality/dominated convergence dispose of them in L². The recurrence barriers give the subcritical local constant 1/c and the balanced one c/(c²+1/2); beyond 1/2 the summed drift loss is lower order than the accumulated input. Multiplying each v_j by p_j² and summing with (1−j/n)² yields the three beta constants, the logarithmic coefficient at 2/3, and Q beyond it. No assertion of necessity for almost-sure convergence alone is made. /workspace/review_checks/check_1.py independently compares exact seven-vertex moments for three schedules; it does not prove the limits.

## originality

PASS

Pass for the arbitrary-weight necessary-and-sufficient criterion and the additional local transition through a=1/2 under mere asymptotic equivalence. Credit substantial earlier Resultary coverage of the 2/3 transition and all three constants for exact powers in 1/2<a<1; that portion alone is not an original contribution. The later exact-power record also overlaps all five regimes, but date alone is not used to adjudicate equivalence or credit.

## value

PASS

The innovation-energy criterion resolves a mathematically motivated question for all positive deterministic weights, including irregular schedules outside simple power regimes. The low-a analysis identifies a separate local mechanism and a critical leading coefficient, rather than only reproducing the known 2/3 transition for exact powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
