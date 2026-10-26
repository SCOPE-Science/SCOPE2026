# Scientific assessment

## Correctness — PASS
The model is fully specified by \(p_j=Z_\beta^{-1}e^{-j^\beta}\) and independent Poisson occupancies. Equation (1) gives the exact variance. In the regime \(0<\beta<1\), the transition-window Riemann sum gives the constant \(\log2/\beta\), and the Lyapunov ratio is at most \(V_\beta(t)^{-1/2}\to0\). At \(\beta=1\), summable phase-indexed Bernoulli deviations yield a discrete limit; for \(\beta>1\), the tuned sequence isolates one nondegenerate Bernoulli urn. These arguments establish both the Gaussian regime and the failure of a full-sequence Gaussian limit outside it.

## Originality — PASS, with a bounded literature risk
The closest primary source is Abebe–Chebunin–Kovalevskii (arXiv:2602.13938v1). Its stated central limit theorem assumes regular-variation index \(\theta\in(0,1)\), and its functional theorem assumes \(\theta\in(0,1]\); the present family has index zero. It cites earlier central-limit work for a subclass of index-zero sequences, so the Gaussian regime alone is not claimed as the sole novelty. The explicit \(\beta=1\) phase-indexed law and the \(\beta>1\) Bernoulli subsequential obstruction are not stated in the inspected theorems. Targeted published-finding corpus and accessible-ledger searches found no exact stretched-exponential phase classification. Residual risk remains from the cited index-zero literature, whose full scope was not inspected.

## Value — PASS
The family \(p_j\propto e^{-j^\beta}\) is a natural stretched-exponential boundary between slowly and rapidly separating urn probabilities. The transition-window width diverges for \(\beta<1\), stays order one at \(\beta=1\), and shrinks for \(\beta>1\). The resulting complete classification gives both the exact variance scale and a concrete criterion for when Gaussian occupancy approximations fail; it is more than a routine CLT application.

Closest literature: Abebe–Chebunin–Kovalevskii (2026), Chebunin–Zuyev (online 2020/print 2022), and Karlin (1968). The exact scope of the index-zero CLT cited as Dutko [6] by Abebe et al. was not inspected; this is the principal remaining priority risk.

Self-review: passed. Independent audit: not yet performed.
