# Independent mathematical audit

## correctness

PASS

I reconstructed the joint law from the minimum norm problem: let u be the normalized all-ones vector and z the projection of u onto ker Xᵀ. Then <u,z>=||z||²=T, so w=z/(√M T) is the unique minimum norm feasible vector. Haar invariance gives T=U/(U+V) in law with degrees M−d,d. The stabilizer of u forces the conditional direction of z−Tu to be uniform on the sphere in u⊥, independently of T, including the two-point sphere for M=2. A centered Gaussian represents that direction. Hence positivity is R_M²<U/V, where R_M is the maximum of the negated centered standardized Gaussians and is positive almost surely; strictness causes no issue because the independent ratio has a density. Independently checking the asymptotics, centering and rescaling perturb the squared maximum by O_P(log M/√M), and Mills' ratio at √(B_M+2t) gives exactly e^(−t)/M to first order. In the critical window both chi-squares concentrate and the scale of ratio fluctuations is O_P((log M)^(3/2)/√M)=o_P(1), small in the additive window; continuity of the extreme-value law gives exp(−exp(−t)). On either side, comparison after division by 2 log M yields the zero-one statement. At d/M→δ∈(0,1/2) the ratio stays finite and the Gaussian maximum diverges. Wendel's binomial tail gives feasibility with probability tending to one (the general-position hull has no boundary inclusion of 0 almost surely); assigning small positive masses to every node and using the shifted interior target gives strict positivity on all the nodes.

## originality

PASS

The Haar beta radius, independent sphere direction, Gaussian extreme-value theorem and Wendel hull formula are standard ingredients and not claimed independently. The supported distinct statement is their exact identification with the selected affine weights and the resulting sharply centered growing-dimension Gumbel law and linear-vs-logarithmic separation for that particular estimator. Once the weight representation is in hand the asymptotic does follow by standard concentration and extreme-value theory; the relevant prior cubature guarantees and closest catalogue special cases do not supply that representation and event at growing dimension.

## value

PASS

For random Gaussian affine integration the exact formula predicts when the cheap minimum-norm rule loses positivity even though positive moment matching remains feasible. The log–log correction and limiting probability distinguish sampling sequences having the same leading ratio, which a mere sufficient scale or the usual hull test cannot do.

The dated certificate retains the supplied scientific assessment, sources and limitations.
