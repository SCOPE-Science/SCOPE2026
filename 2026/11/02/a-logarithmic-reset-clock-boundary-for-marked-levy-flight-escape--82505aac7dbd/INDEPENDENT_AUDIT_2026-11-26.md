# Independent mathematical audit

## correctness

PASS

Stable self-similarity scales the exit time by K=L^α and preserves the side. Integrating the stated symmetric Lévy density gives k_± with the two distances 1∓Λ. The marked short-time rate can be verified directly: truncate jumps at b below the two boundary distances, and bound the compensated small-jump supremum exceeding ε over [0,u] by C u b^{2−α}/ε² using its second moment. At most one larger jump occurs except on an O(u²) event for fixed b. On the good small-jump event, a jump beyond the corresponding distance plus ε forces that exit, while exit to that side requires a jump at least the distance minus ε. Let u↓0, b↓0, then ε↓0. This also gives F(u)≤Cu; jumps of absolute size larger than two give an exponential tail for T. For every fixed t>0 there is no fixed-time jump, so T=t would require the stable position to be an endpoint (which has probability zero by its density). This justifies the strict tie-free cycle identities even for atomic R. Independence across cycles gives a_±/(1−b_K) and E[min(KT,R)]/P(KT<R). For finite ER, the scaled success numerator tends to k_± ER under the bound CR; the failure-duration term is dominated by sR and tends to s ER. At critical shape one, the success Stieltjes integral can be written ∫F_±(u)K/(1+Ku)² du: replacing F_±(u) by k_±u below a small fixed cutoff gives k_±log K/K, with the tail O(1/K) and arbitrarily small relative error at zero. Inserting e^(−sT) changes it by at most s/K. In the failure term the same kernel multiplies (1−e^(−su))P(T>u)~su, giving s log K/K. The mean-cycle term is E log(1+KT)~log K by logarithmic integrability. For 0<δ<1 the scaled success converges by dominance by T^(−δ); the failure integral is dominated by min(su,1)u^(−1−δ). The sum of the limiting marked transforms is continuous at zero and equals one there, so it defines the joint weak limit. Integration of the Lomax survival yields the stated limiting mean; differentiating the summed transform at zero gives the same mean for the limiting law. The endpoint limits in δ follow by moment domination at zero and (1−δ)E[T^(−δ)]→k from the linear rate at one. For centered Cauchy flight, the usual Dirichlet mean is √(1−x²)/σ inside the interval, giving 1/σ at the centre; k=2σ/π, so the example detects a genuinely different subcritical limit for small δ. There is no packaged numerical proof and none is needed.

## originality

PASS

The Poisson side-and-time specialization is demonstrably covered, even by an earlier catalogue result with a stronger position mark, and the Poisson mean and restart machinery are prior. The supported distinct claim is the crossover for fixed renewal clocks, especially the exponent-one logarithmic cancellation and the evaluated subcritical marked transform with its inverse-moment weighting. None of the inspected stronger or adjacent results covers that tail comparison.

## value

PASS

The distinction matters in interpreting heavy-tailed reset data: an infinite-mean clock at the exact unit exponent still erases the detailed excursion law, whereas the subcritical clock reweights it, including the side mark. The matching logarithms and the explicit Cauchy comparison explain why a universal exponential based only on near-zero escape hazards cannot be extrapolated across the boundary. This is a fixed-clock, fixed-interior-site result, not a claim about arbitrary correlated clocks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
