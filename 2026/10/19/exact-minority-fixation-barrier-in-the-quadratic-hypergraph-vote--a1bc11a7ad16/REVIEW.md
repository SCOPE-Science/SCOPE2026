# Mathematical assessment

## Correctness — PASS

For each integer \(N\ge3\) and \(2\le d\le N-1\), hypergeometric factorial moments give exact up/down transitions with ratio \((N+c-i)/(c+i)\). Their positive interior rates justify the absorbing birth–death first-step recursion; its gamma-product solution establishes the complete finite fixation formula and strict group-size ordering without approximation. At fixed \(d\), Stirling expansion of that exact product has a smooth strictly concave action with a unique saddle at half density. The denominator's Gaussian saddle and fixed-count numerator produce the stated exponential rate and prefactor. The strict correction to the *diffusion extrapolation* follows from \(\operatorname{artanh}(u)>u\), not from a numerical fit. Independent enumeration in `verify.py` tests exact rates and harmonic identities for 440 cases. No part of the all-size proof relies on those finite tests.

## Originality — PASS, with explicit residual risks

The complete-hypergraph 2026 social-impact source derives microscopic transition laws and macroscopic drift, but not this finite-size absorption sum or sharp one-minority boundary asymptotic. The 2025 group-driven voter study derives the Gaussian central exit curve through a diffusion approximation; the present non-Gaussian barrier shows why extrapolation to a fixed initial minority is exponentially wrong. A 2026 follow-up treats consensus times; earlier nonlinear complete-graph and 2025 biased unanimity q-voter studies use different stochastic structures or approximate/Markov-chain exit analyses. Direct comparisons concern mathematical implications, not just titles. A broader WKB/special-function treatment of birth–death chains might already imply the derived rate and prefactor after specialization; this remains a genuine literature risk. No uniqueness claim beyond the inspected sources is made.

## Mathematical value — PASS

In a current higher-order opinion-formation model, whether an initially tiny minority can reach unanimity is a natural and practically distinct observable from the central transition curve or mean consensus time. The theorem determines this probability at every finite population size and, at fixed group degree, the exact exponentially small large-population behavior including a prefactor. The strict gap from a plausible published Gaussian extrapolation is a substantive scaling boundary rather than a minor parameter substitution. The same analysis yields a complete finite-parameter monotonicity law. It does not forecast empirical persuasion outcomes or arbitrary network dynamics.

## Literature and limits

Closest sources: Llabrés et al. (2026), arXiv:2601.05169, microscopic update law, Eqs. (24),(33); Kim et al. (2025), Phys. Rev. E 111 L052301, Gaussian Appendix B/S20; Kim et al. (2026), arXiv:2604.17689, consensus-time analysis; Castellano et al. (2009), arXiv:0907.1775, complete-graph backward diffusion; Doniec et al. (2025), arXiv:2502.10172, biased unanimity model. The present expansion is fixed-group-size and fixed-minority-size, not uniform when either grows with population size.

Self-review: passed. Independent audit: not yet performed.
