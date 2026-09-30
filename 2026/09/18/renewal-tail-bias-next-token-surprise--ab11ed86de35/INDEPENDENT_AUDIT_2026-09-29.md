# Independent audit — 2026-09-29

Record: `2026/09/18/renewal-tail-bias-next-token-surprise--ab11ed86de35`  
Assigned and audited source tree: `c91616c55d1821794f22e1c9ce8eba83a0379c3e`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `1ac79724c6429f84f91d04f67f6a6d27ce61423d`  
Disposition: **passed**

## Correctness

**independently_supported**. The stationary-renewal calculation is correct. With atomless iid block marks, the next-token count is controlled only by the age A of the current block, and the equilibrium-age law gives P(A<=zeta)=E[min(L,zeta+1)]/E[L]. For a complete block of length ell and a rank-r proxy point, deleting the forward window leaves exactly max(r-1,ell-tau) same-mark observations; exhaustive rank algebra therefore gives block reward min(ell,zeta+1) 1{ell<=tau+zeta}. Renewal reward then yields the fixed-window limit and the exact downward bias ((zeta+1)/mu) P(L>tau+zeta). The growing-window result is also consistent: the discarded reward is (zeta+1)1{L>tau_n+zeta}, its centered cycle contribution vanishes in L2 when q_n->0, and finite E[L^2] gives the usual regenerative CLT variance. The deterministic one-sided sample-end loss is O(tau_n/n), hence negligible at root-n scale under tau_n=o(sqrt n). This produces the stated normal shift when sqrt(n)q_n converges and divergence when it tends to infinity.

## Originality

**supported_after_primary_prior_check**. Nakul-Muthukumar-Pananjady introduce the one-sided leave-a-window-out next-token framework, and the 2024 Windowed Good-Turing paper already establishes windowing as a remedy for Markov dependence. Duplication models are also prior art. For this audit, the previously residual Chandra-Thangaraj 2024 ISIT paper 'Missing Mass Under Random Duplications' was retrieved in full through authorized Oxford access after open-access attempts failed. It studies finite-alphabet iid inputs passed through an elementary Bernoulli duplication channel and proves minimax missing-mass results for a different estimator; it does not state the stationary atomless-renewal next-token identity, the exact one-sided bias formula, or the root-n tail phase. Targeted searches likewise found no prior statement of those formulas. Originality is therefore supported narrowly for the exact renewal benchmark, not for Good-Turing windowing or sticky/duplication models themselves.

## Scientific value

**meaningful_exact_dependence_benchmark**. The result turns a generic bias-under-dependence phenomenon into an exact law controlled solely by the renewal tail at tau+zeta. It cleanly distinguishes fixed-window bias from root-n centering and shows why appropriate window growth can be logarithmic or polynomial depending on the block tail, making it a useful benchmark for the broader next-token estimation theory.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/renewal-tail-bias-next-token-surprise--ab11ed86de35
- https://arxiv.org/abs/2609.19529
- https://jmlr.org/papers/v25/24-0511.html
- https://arxiv.org/abs/2503.12808
- https://arxiv.org/abs/2202.02772
- https://doi.org/10.1109/ISIT57864.2024.10619664
## Access note

Open-access searches did not expose the full text of Chandra--Thangaraj, *Missing Mass Under Random Duplications* (ISIT 2024). Authorized Oxford institutional retrieval was therefore used, and all five pages were inspected. It studies an elementary Bernoulli duplication channel and does not contain the exact renewal-tail next-token formulas audited here.

## Limitations

- Exact formulas use atomless block marks, excluding cross-block symbol collisions.
- The root-n theorem assumes E[L^2]<infinity and tau_n=o(sqrt n) and treats the one-sided forward-window estimator only.
- The Chandra-Thangaraj ISIT paper was read through authorized institutional access; no claim is made about unrelated inaccessible duplication literature.
- The result is a solvable regenerative benchmark, not a minimax theorem over arbitrary stationary dependent processes.
