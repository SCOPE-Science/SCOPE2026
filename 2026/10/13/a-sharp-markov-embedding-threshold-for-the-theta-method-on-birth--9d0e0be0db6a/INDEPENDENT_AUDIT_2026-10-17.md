# Independent mathematical audit

## correctness

PASS

A finite irreducible birth–death generator Q is diagonally similar to a symmetric Jacobi matrix with simple real spectrum 0,-lambda2,...,-lambdan. The theta method maps eigenvalues through strictly decreasing g=(1-(1-theta)h lambda)/(1+theta h lambda), so its spectrum is simple; a zero or simple negative eigenvalue precludes a real logarithm. With all eigenvalues positive the unique real logarithm B=log P has series coefficients c_k=[theta^k+(-1)^(k+1)(1-theta)^k]/k. At any distance-two entry Q^k has the sign (-1)^k, hence every contributing term in B_ij is nonpositive when theta<=1/2 and at least one is strictly negative (k=2 for theta<1/2, k=3 at equality); therefore no CTMC generator can embed P at any h. If theta>1/2, all c_k>0; the first nonzero distance-d term c_d h^d Q^d_ij>0 for small h, giving strictly positive dense generator off-diagonal entries. At theta>=1, B=integral_{theta-1}^theta h Q (I-s hQ)^(-1)ds has strictly positive off-diagonal entries using positive stochastic resolvents for irreducible Q, for all h>0. For n=2, the nontrivial eigenvalue r must be positive and B=[-log r/Lambda]Q is unique. Reconstructed exact 3-state Crank–Nicolson example has positive stochastic P, eigenvalues 1,3/5,1/7 and B13=(1/6)log(125/189)<0. Independent exact rational spectral/c_k and power-parity checks corroborated; general conclusions from analytical path and integral arguments.

## originality

PASS

Classical Markov embedding, principal-log criteria, and the sparse forward-Euler theta=0 nonembedding special case are explicitly prior. The surviving original contribution is principally the all-n sharp theta=1/2 boundary even for positive stochastic dense steps and the complementary theta>1/2 small-step dense-generator existence. The theta>=1 all-step resolvent embedding is a natural general subordination/log-resolvent consequence and is proved here without asserting the resolvent principle itself is new. The birth–death-specific sign threshold does not follow mechanically from the directly inspected general embedding or positivity results.

## value

PASS

Markov embeddability is strictly stronger than stochasticity and ensures a homogeneous CTMC interpretation of a numerical transition step. A universal sharp boundary at theta=1/2, where even positive reversible Crank–Nicolson transitions fail, distinguishes two basic integration choices; the complementary all-step theta>=1 embedding with an explicit dense generator is meaningful structural guidance. The dimension-two exception and exact 3-state counterexample make the threshold sharp and interpretable; this is not merely a routine positivity calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
