# Scientific review

## Correctness: PASS
The generator identity \(K=L^{\mathrm{Ex}}-\operatorname{diag}(\kappa)\), component Perron eigenvectors, projection to the connected token graph, and the full-subset-sum argument establish the necessity and sufficiency under precisely the stated finite graph and positive bidirectional rate assumptions. A fixed strictly positive horizon with identical survival across *all* starts forces a constant hazard by Perron simplicity of each labeled component's matrix exponential. The exponential-killing representation follows from commuting scalar subtraction. Exact-arithmetic finite tests in `verify.py` passed 117816 classification assertions; these are reproducibility checks, not the proof for every graph size.

## Originality: PASS, with residual risk
The closest motivating source is Shiatis (arXiv:2610.00741v1), whose full accessible text gives a general density/change-of-measure relation but not the complete graph/weighted-degree iff classification with one-time survival rigidity. Johnston and Shiatis (arXiv:2501.15483v4) provide the ring ASEP predecessor; that ring specialization is acknowledged and not separately asserted to be new. Searches for equivalent Q-process, constant-killing, and particle exclusion formulations did not identify a source explicitly covering the all-connected-graph and all-occupancy dichotomy. A hidden broader token-graph or quasi-stationary formulation remains a meaningful originality risk.

## Mathematical value: PASS
The result addresses a natural exact-equivalence question for two stochastic dynamics normally related by a nontrivial path density, and gives a complete structural classification with a sharp maximal-density exception. It tells precisely when conditional survival introduces no bias in the entire path law and provides a rate and an independent-killing construction useful for simulation. The sparse nonreversible cyclic family demonstrates that this is not merely uniform complete-graph symmetry.

## Scientific boundaries
Only finite connected undirected underlying graphs, strictly positive jump rates in each edge orientation, and \(2\le k\le n-1\) are covered. The proof does not settle directed one-way graphs, infinite particle systems, or non-Markov waiting times. Existing ring results and classical Doob-transform ingredients are credited as prior art. No external independent audit or validation has been carried out.

Self-review: passed. Independent audit: not yet performed.
