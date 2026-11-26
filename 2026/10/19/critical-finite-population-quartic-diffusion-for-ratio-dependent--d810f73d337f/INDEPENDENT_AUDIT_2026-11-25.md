# Independent mathematical audit

## correctness

PASS

Uniform repartition is equivalent to a permutation divided into consecutive triples. The one- and two-triple falling factorial laws follow by sampling the first three or six positions. Conditional on compositions the outgoing bits are independent. Dividing the joint law by the two one-triple marginals leaves the first-order cross term -(k-3p)(l-3p)/(N*p*(1-p)), with uniform O(N^-2) remainder on interior compact p-sets. This gives the stated negative covariance correction to the limiting noise. Independently, on the lower boundary the probability in a triple with input spins S_i in {-1,1} is q=1/2+(S_1+S_2+S_3)/6-a*S_1*S_2*S_3. This yields the cubic mean y-8ay^3. For independent balanced spins, the linear and cubic terms are orthogonal: Var(q)=1/12+a^2, E[q(1-q)]=1/6-a^2 and Cov(q,K)=+1/4. In the partition the linear sum is fixed by the input count; the composition contribution is 3a^2, so total variance at balance is 1/6+2a^2. Swapping two permuted labels affects at most six bits, and changing one output uniform affects one; coupling the remaining permutation after a different exposure by a transposition gives the conditional variance O(N) and centered fourth moment O(N^2) for the outgoing count. At h=N^-1/2 and z=N^(1/4)y, the finite-sampling error in the scaled drift divided by h is O(N^-1/4); the scaled variance per h tends to the claimed constant and the compact-state fourth increment moment is O(h^2). Thus Taylor generator convergence and negligible jumps hold on compact sets. The global deterministic contraction in squared distance, with bounded finite-N mean error and variance, gives a stopped second-moment bound and compact containment; on compacts the drift and martingale variance estimates give tightness. Local uniqueness and the dissipative Lyapunov bound give the nonexplosive limiting martingale problem. Its positive integrable speed density is proportional to exp(-4a*z^4/sigma^2) and is the unique invariant probability. Complementing the two probabilities complements the entire output law, and simultaneous spin complementation commutes with the lower kernel, proving the parity identity for every allowed N. These checks apply also at b=0 downstairs and b=1 upstairs; they imply no finite-chain stationary convergence. The frozen script was inspected, not executed.

## originality

PASS

The deterministic cubic map and both critical parameter lines are already covered. The supported distinct contribution is the finite-time diffusion theorem for simultaneous uniform repartition with independent per-agent outputs, particularly its exact partition-corrected noise amplitude. The simple complement identity supports the transfer to the flip line but is not, alone, the original contribution.

## value

PASS

The deterministic phase boundary does not quantify finite-population fluctuations. The theorem determines the fluctuation window, observation time and partition-sensitive amplitude for that specific process, and the flip conjugacy transfers the quantitative law without pretending the uncorrected sign-alternating chain has the same trajectory limit. The quartic invariant density is a meaningful property of the limit, not a claim about equilibrium at finite N.

The dated certificate retains the supplied scientific assessment, sources and limitations.
