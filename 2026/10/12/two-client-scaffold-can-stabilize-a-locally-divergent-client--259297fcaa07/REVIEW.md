# Independent mathematical audit

## correctness

PASS

Under deterministic full-participation two-client scalar quadratic Option II, write z_i=1-eta a_i, p_i=z_i^K,s_i=(1/K)sum_{j=0}^{K-1}z_i^j and d=(c1-c2)/2. Summing exactly the client local steps and applying the Option-II control update yields A11=(p1+p2)/2, A12=K eta(s1-s2)/2, A21=(p2-p1)/(2K eta), A22=1-(s1+s2)/2. For |z_i|<1 all K>=2 give 0<s_i<1 and |p_i|<1; the three expanded Jury expressions are positive. At K=1 the source writes 0<s_i<1 incorrectly (s_i=1 exactly), but the exact round matrix is triangular with eigenvalues 0 and (z1+z2)/2, still strictly Schur stable. This closes a minor strict-inequality oversight WITHOUT changing the final mathematical claim. Independent exact fractions reproduce K=3, z=(-6/5,9/10), A=[[-999/2000,-147/200],[819/2000,41/120]], det=1629/12500 and negative discriminant, so its spectral radius sqrt(det)<1 though first local factor |-6/5|>1. Tested all three Jury inequalities on 175 sampled exact rational pairs and K=1,2,3,4,7,11,25.

## originality

PASS

The original full SCAFFOLD primary text was inspected through Algorithm 1, the quadratic similarity theory and Appendix F; its rate bounds and modified illustrative quadratic update do not state the exact two-state Option-II matrix with the all-K local-contractive Jury domain or its explicit stable round with an individually divergent client. Later multi-rate or similarity convergence theory concerns different guarantees. A published same-object dominating stability criterion was not identified. The original algorithm, control variates, and quadratic rate bounds are prior art.

## value

PASS

Federated optimization theory often measures local step instability and step restrictions. Showing analytically that feedback through SCAFFOLD Option-II controls stabilizes an otherwise divergent client challenges a natural but false necessity intuition. The exact two-client round state and all-K Jury sufficient region offer a reproducible stability benchmark usable when evaluating distributed optimization step-size claims; it does not purport to solve the general stochastic optimization problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
