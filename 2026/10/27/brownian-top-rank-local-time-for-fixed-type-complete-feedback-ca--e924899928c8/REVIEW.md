# Scientific assessment

**Correctness — PASS.** The proof has two independent finite identities (telescoping maximum and predictable compensator) and a joint hypergeometric martingale functional CLT. The smooth-argmax approximation is needed because the greedy selector is discontinuous at ties; quadratic-variation estimates allow smoothing errors to be removed and control bridge endpoints. Brownian rank Tanaka with the explicitly normalized symmetric local time then gives the claim. Finite enumeration and seeded simulation check identities and constants, not the limiting theorem.

**Originality — PASS, qualified.** Dey and Manthripragada (arXiv:2610.17479v1) explicitly leave the fixed-type actual-score limit open for three or more types, although they prove the compensator limit. Kuba and Panholzer (arXiv:2303.04609v1) cover two types. Classical ranked semimartingale results such as arXiv:0807.5001 provide a rank local-time identity but not this model-specific score convergence. Targeted literature and mathematical-research-record searches found no directly covering fixed-\(n\ge3\) statement. Broader invariance-principle or unindexed coverage remains possible.

**Mathematical value — PASS.** This closes the precise gap between the fixed-type score and compensator: the martingale remainder is retained at leading order and the non-Gaussian actual score is characterized by the collision local time of the two largest Brownian bridge coordinates. The model appears in sequential prediction with feedback and biased treatment allocation; the limit quantifies fluctuations beyond the mean.

**Scientific limitations.** Fixed number of types only, no distributional closed form for more than two types, no convergence rate, independent technical/priority audit outstanding. A standard stochastic-integral convergence theorem and rank-diffusion local-time representation are used; their hypotheses are stated in the proof.

Self-review: passed. Independent audit: not yet performed.
