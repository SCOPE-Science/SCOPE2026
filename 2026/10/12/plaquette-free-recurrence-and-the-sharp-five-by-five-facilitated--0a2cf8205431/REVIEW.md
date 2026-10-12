# Scientific review: finite facilitated exclusion

## Correctness — PASS

The precise state space and transition rule agree with equation (2.2) in Kim–Lee–Seo [1]. The geometric closed-set lemma follows directly from the collinear facilitator constraint. The finite certificate enumerates every one of the \(\binom{25}{h}\) configurations for each \(1\le h\le8\), constructs its forward and reverse transition edges by explicit Boolean tests, and uses two-pass exact strongly connected components to determine all closed communicating classes. It tests terminal membership against absence of empty periodic \(2\times2\) plaquettes for every state, not only counts. The largest enumerated sector has 1,081,575 vertices and 17,054,400 transitions. A second integer transfer-matrix algorithm independently counts the plaquette-free configurations; all eight counts agree. The published low-density theorem supplies the sharpness comparison for \(K\le16\). These are exact finite computations, not evidence about infinitely many lattice sizes.

## Originality — PASS, with residual uncertainty

The closest work [1, Theorem 2.1] gives on the five-by-five torus only uniqueness for \(K\ge22\) and multiplicity for \(K\le16\), not the five intermediate sectors or a complete recurrent-state membership criterion. Its Section 3 uses fully occupied boxes to establish reachability, which does not imply the asserted empty-plaquette exclusion or the specific SCC census. Material comparison of the source model, main theorem, and Section 3 found no corresponding claim. The one-dimensional model [2] and its alternative higher-dimensional facilitation convention do not imply this finite directional result. Targeted published mathematical searches found no equivalent, broader, or tabulated 25-site result; unindexed independent finite enumerations remain a genuine residual uncertainty.

## Value — PASS

This resolves the exact finite-size transition where the best cited general theorem leaves five particle-number sectors open. It gives a new simple invariant description of the recurrent class, not only its size, and an exact finite counting sequence useful for microscopic study of the directional kinetic constraint. The 25-site odd torus is a natural first detailed finite test of the odd-size gap; its sharply closed interval and geometric classification motivate the computation. It does not by itself yield a thermodynamic-limit theorem.

## Closest literature and limitations

[1] S. Kim, S. Lee, I. Seo, *Facilitated Exclusion Process in Higher Dimensions: Recurrent Structure and Transient Dynamics*, arXiv:2609.18885v1, Theorem 2.1 and Sections 2–3, https://arxiv.org/html/2609.18885v1.

[2] S. Goldstein, J. L. Lebowitz, E. R. Speer, *Approach to Hyperuniformity in the One-Dimensional Facilitated Exclusion Process*, arXiv:2407.02652v2, Sections 1–2, https://arxiv.org/html/2407.02652v2.

Finite-only proof and possible unindexed equivalent computations are explicit limits; scientific novelty must not be inferred solely from failure to retrieve an identical title. A separate independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
