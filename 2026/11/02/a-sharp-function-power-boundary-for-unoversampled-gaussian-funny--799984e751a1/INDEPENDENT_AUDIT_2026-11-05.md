# Independent mathematical audit

## correctness

PASS

For B=A_L^(q-1/2)g, Ahat=A_L^(1/2)P_B A_L^(1/2) is PSD<=A_L; Loewner-Heinz gives Ahat^beta<=A_L^beta, so nuclear error equals m+L^beta-mu_L^beta, mu_L=(L^(2q)G²+R)/(L^(2q-1)G²+R). G²/R beta-prime density yields an exact scalar integral. Scaling y=L^(q-1/2)sqrt(G²/R) gives prefactor L^(beta-q+1/2); bracket dominated by integrable 1-(y²/(1+y²))^beta, asymptotic constant equals 2 Gamma((m+1)/2)Gamma(beta+1/2)/(Gamma(m/2)Gamma(beta)). For fixed almost-sure sample with G!=0, L-mu_L=O(1) and L^beta-mu_L^beta->0 for beta<1, including beta=1/2, despite persistent expected excess. Independently reassembled small matrices and 8 numerical Gamma-integral comparisons (216 matrix cases) with consistent results.

## originality

PASS

Prior funNyström papers develop the same algorithm and operator-monotone function-transfer bounds but impose Gaussian oversampling for their expected error corollaries; the rank-one p=0 critical expected error constant and lack of uniform integrability are not given by those bounds.

## value

PASS

Identifies the exact zero-oversampling failure boundary and explicit leading constant in a standard operator-monotone approximation algorithm, including striking almost-sure/expectation contrast. The one-spike family is a natural diagnostic for randomized spectral methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
