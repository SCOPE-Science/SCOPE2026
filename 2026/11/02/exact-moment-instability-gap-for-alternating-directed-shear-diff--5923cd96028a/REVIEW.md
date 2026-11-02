# Scientific review: Exact moment-instability gap for alternating directed shear diffusion

## Correctness — PASS
The conditional Itô generator and symmetric/antisymmetric sector decomposition yield two explicit first-moment blocks and two cubic second-moment blocks. The Routh–Hurwitz positivity tests show that the first-moment threshold is \(q_1=a^2/(b-2a)\), the second-moment threshold is \(q_2=4a^3/(b^2-4a^2)\) for \(b>2a\), and the critical second-moment forcing projects nontrivially onto the simple positive Perron mode. This proves the specified stable/linear-growth/exponential-growth trichotomy and the exact stationary covariance and critical correlation ratio \(2a/b\). Independent rational identities and finite ODE diagnostics are available in `artifacts/verify.py`; they corroborate but do not establish the universal theorem.

## Originality — PASS (qualified)
Ferraro et al., arXiv:2405.05183v1, already find a mean-finite/variance-divergent phase in a many-coordinate Gaussian colored annealed-interaction model (Figure 6); that qualitative separation is explicitly prior, not new. They do not treat the two-state alternating directed-shear mechanism. Ogura and Preciado, arXiv:1501.03474, give general induced-matrix spectral tests; the present explicit thresholds and covariance require nontrivial specialization and exact sector algebra and are not stated there. Sturman and Thiffeault, doi:10.1007/s00332-018-9497-3, give bounds for independent discrete shear products, not this Markov-modulated diffusion. Primary source and adjacent results were inspected at the material level noted in AUDIT.json. Remaining risk: the same exact specialization might be present elsewhere under another notation; no independent publication-priority check is claimed.

## Mathematical value — PASS
The natural two-coordinate system displays a sharp qualitative design failure: each fixed directed interaction is stable, and ensemble mean stability remains intact, while switching faster than \(q_2\) makes the covariance diverge. The complete classification has a strict and exact interval of width \(a^2/(b+2a)\). Its closed stationary covariance supports an exact instability diagnosis rather than numerical trial and error.

## Scope and limitations
The result concerns equal positive damping, equal positive directional shear strengths, symmetric two-state Poisson switching and additive isotropic independent Brownian noise. It does not prove almost-sure instability or rule out stationary laws with infinite variance. General moment-stability theory is credited, and precise publication priority remains subject to independent examination.

Self-review: passed. Independent audit: not yet performed.
