# Independent Audit — 2026/09/11/019

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `e9e5393ac304073271499b007132b34138fe3cc4`  
**Disposition:** **PASSED**

## Correctness

**Verdict:** PASS

The signing certificate checks out independently. From the archived edge list and eight negative edges, exact symbolic computation gives characteristic polynomial x^12-24x^10+226x^8-1056x^6+2549x^4-2976x^2+1280, which factors as (x-1)(x+1)(x^2-5)(x^2-x-4)^2(x^2+x-4)^2. Hence the spectral radius is (1+sqrt(17))/2 approximately 2.5615528128, below sqrt(33/5) approximately 2.56905 and well below 2sqrt(3). Independently, all leading principal minors of 33I-5A_sigma^2 are positive, certifying positive definiteness by Sylvester's criterion. The base Chvatal graph's nontrivial old eigenvalues also lie within the 4-regular Ramanujan bound, so the signed new spectrum gives the claimed two-sided Ramanujan 2-lift certificate.

## Originality

**Verdict:** PASS

Bilu–Linial, Marcus–Spielman–Srivastava, and Hall–Puder–Sawin provide the general signing/covering framework, but the inspected literature does not supply this explicit Chvatal-graph signing or its exact polynomial. The contribution is instance-level rather than a general theorem, but the concrete exact certificate appears original in the targeted comparison.

## Scientific value

**Verdict:** PASS

An explicit exact two-sided signing on a canonical small non-bipartite 4-regular graph is a reusable benchmark for signing algorithms and for the gap between one-sided general existence results and two-sided fixed-instance behavior. The mathematical depth is modest because the switching space is finite and small, but the certificate is exact and scientifically meaningful.

## Limitations

- This is a single fixed-graph existence certificate, not a general signing theorem.
- The claimed search optimum over switching classes is not needed for the result and was not used in this audit.
- Priority checking was targeted; it cannot exclude every unpublished enumeration.

## Independent checks

- Independently reconstructed the 12x12 signed adjacency matrix and exactly reproduced the characteristic polynomial.
- Factored the polynomial exactly and obtained rho=(1+sqrt(17))/2.
- Verified positive definiteness of 33I-5A_sigma^2 using exact positive leading principal minors.

## Literature and comparison

- [Bilu–Linial, Ramanujan signing of regular graphs](https://doi.org/10.1017/S0963548304006509): Introduces the signing framework motivating Ramanujan lifts; does not provide the audited Chvatal signing.
- [Hall–Puder–Sawin, Ramanujan coverings of graphs](https://arxiv.org/abs/1506.02335): Provides general covering results and context, not this explicit non-bipartite Chvatal certificate.
- [Chvátal, The smallest triangle-free 4-chromatic 4-regular graph](https://doi.org/10.1016/S0021-9800(70)80057-6): Primary source for the named base graph; the signing result is separate from the classical graph construction.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at the assigned tree. Git history comparison found no changes to this record between the assignment inventory, the dispatcher checked commit, and current `main`. No repository writes were made by this audit.
