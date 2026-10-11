# Scientific review: sharp quadratic convexity of a hybrid \(\ell_1\)–Hilbert norm

## Correctness — PASS
The theorem concerns the specified real norm \(N_t=(\|\cdot\|_1^2+t\|\cdot\|_2^2)^{1/2}\), all integers \(n\ge2\), and every \(t>0\). The signed-functional inequality (4), Cauchy–Schwarz step (5), one-variable optimization (6), and balanced-support minimization (7) reconstruct the global sharp midpoint constant. A sign-balanced vector attaining equality is given explicitly; its orthogonality relation (8) makes both normalized endpoints unit vectors and proves the Day modulus formula for the entire claimed initial interval. The strict part follows from equality conditions, coordinatewise domination, and compactness, not numerical sampling. The supplied reproducibility code passed 12 exact rational and 67,536 seeded numeric tests. Finite tests do not prove the universal formula; the analytic argument does.

## Originality — PASS, subject to residual literature risk
García-Lirola–Raja, *Uniformly convex renormings and generalized cotypes* (arXiv:1911.05657), addresses optimized equivalent renormings, not the exact coefficient for a fixed quadratic-mixed norm. Banaś–Ochab–Zając, *On the smoothness of normed spaces* (DOI:10.1007/s43034-023-00310-z), surveys geometry and moduli without the specified finite-dimensional computation. De Bernardi–Veselý, *Moduli of uniform convexity for convex sets* (DOI:10.1007/s00013-024-02031-8), proves equivalence of general modulus definitions, not a value for this norm. An indexed record on Euclidean Banach–Mazur distance of mixed \(\ell_p\)–\(\ell_q\) planes deals with a different invariant and does not imply the Day modulus, even in dimension two. Direct searches under exact quadratic convexity, mixed norms, and modulus aliases found no statement dominating the theorem. An unindexed equivalent calculation remains possible; the search is not a proof of worldwide novelty.

## Mathematical value — PASS
The statement solves a natural exact quantitative invariant for an infinite family of finite-dimensional norms, rather than just proving qualitative uniform convexity. It gives the optimal constant in an inequality for every vector pair and determines precisely the maximal interval on which the induced classical modulus envelope is sharp. The support-balance optimization explains the even/odd dependence and the complementary-support geometry at the transition. Values beyond the transition are intentionally not claimed.

## Scientific limitations
The classical modulus above \(\varepsilon_*=2/\sqrt{1+c}\) is not evaluated; only its strict separation from the quadratic envelope is established. This does not extend to complex spaces or to dimension one. Reproducibility calculations are supporting checks, and an equivalent unindexed prior result cannot be excluded.

Same-model review: passed. Independent audit: not yet performed.
